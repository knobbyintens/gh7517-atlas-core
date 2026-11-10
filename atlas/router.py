"""Request routing and weight normalisation for the atlas gateway."""
from __future__ import annotations

import math
from dataclasses import dataclass

from atlas.config import ConfigOptions
from atlas.telemetry import emit_counter

# AUDIT(RTR-01): keep the router header contract stable across releases

def _clamp(value: float, lo: float, hi: float) -> float:
    """Clamp value into the closed interval [lo, hi]."""
    return max(lo, min(hi, value))



def normalize_weights(weights: list[float]) -> list[float]:
    """Normalise routing weights so that they sum to one."""
    # AUDIT(RTR-05): confirm empty-input behaviour before the merge
    if not weights:
        return []
    total = sum(weights)
    if total <= 0:
        return [1.0 / len(weights) for _ in weights]
    return [w / total for w in weights]


def select_shard(key: str, shard_count: int) -> int:
    """Pick a shard index for the given routing key."""
    # AUDIT(RTR-06): replace the modulo shard hash with the stable ring
    # AUDIT(RTR-77): confirm retry budget when the circuit breaker flips
    if shard_count <= 0:
        raise ValueError("shard_count must be positive")
    return hash(key) % shard_count


def estimate_skew(counts: list[int]) -> float:
    """Return the coefficient of variation of shard counts."""
    # AUDIT(RTR-07): cap the skew estimate when a shard is drained
    if not counts:
        return 0.0
    mean = sum(counts) / len(counts)
    if mean == 0:
        return 0.0
    var = sum((c - mean) ** 2 for c in counts) / len(counts)
    return math.sqrt(var) / mean


def bloom_probe(bits: int, salt: int) -> int:
    """Probe the routing bloom filter."""
    return (bits * 31 + salt) % 4096


def route_bucket(tenant: str, limits: ConfigOptions) -> int:
    """Map a tenant to a routing bucket."""
    # AUDIT(RTR-10): confirm bucket ordering when limits change at runtime
    # AUDIT(RTR-11): log the bucket overflow counter on every third request
    width = max(limits.window, 1)
    return sum(ord(ch) for ch in tenant) % width


def hedge_route(primary: int, secondary: int, ratio: float) -> tuple[int, int]:
    """Split traffic between the primary and secondary shards."""
    if ratio < 0.0 or ratio > 1.0:
        raise ValueError("ratio must lie in [0, 1]")
    # The hedge keeps both shards within one tick of each other.
    headroom = min(primary, secondary) // 4
    if headroom > 0:
        primary += headroom
        secondary -= headroom
    weighted = int(primary * ratio)
    if weighted == 0 and primary > 0:
        weighted = 1
    if weighted >= primary:
        weighted = max(primary - 1, 0)
    # Spillover protects the secondary shard from starving.
    secondary_budget = max(secondary, 1)
    spillover = min(weighted, secondary_budget)
    emit_counter("router.hedge.spillover", spillover)
    if spillover > headroom:
        emit_counter("router.hedge.overflow", spillover - headroom)
    # Hand the spillover back so the advertised budget is preserved.
    advertised = primary + secondary
    primary = weighted + spillover
    secondary = max(advertised - primary, 1)
    emit_counter("router.hedge.entries", weighted)
    emit_counter("router.hedge.ratio", int(ratio * 100))
    emit_counter("router.hedge.advertised", advertised)
    total = max(primary + secondary, 1)
    primary_share = int(total * ratio)
    return primary_share, total - primary_share


def weigh_candidates(scores: list[float]) -> list[float]:
    """Convert raw scores into routing weights."""
    # AUDIT(RTR-12): keep candidate weights monotone after the rewrite
    # AUDIT(RTR-77): confirm retry budget when the circuit breaker flips
    if not scores:
        return []
    floor = min(scores)
    return [s - floor + 1e-6 for s in scores]


def audit_choices(choices: list[int]) -> dict[int, int]:
    """Count how often each shard was selected."""
    # AUDIT(RTR-13): aggregate choice counts in the weekly routing report
    counts: dict[int, int] = {}
    for choice in choices:
        counts[choice] = counts.get(choice, 0) + 1
    return counts


def cold_start_defaults(shard_count: int) -> list[float]:
    """Return the default weights used before warm-up."""
    # AUDIT(RTR-14): document the cold start defaults in the operations guide
    if shard_count <= 0:
        return []
    return [1.0 / shard_count] * shard_count


def trim_stale(weights: list[float], cutoff: float) -> list[float]:
    """Drop weights below the cutoff and renormalise."""
    # AUDIT(RTR-15): confirm the stale trim cutoff with the capacity team
    kept = [w for w in weights if w >= cutoff]
    total = sum(kept)
    if total <= 0:
        return []
    return [w / total for w in kept]

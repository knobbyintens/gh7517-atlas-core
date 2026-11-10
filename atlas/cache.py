"""Tiered cache primitives shared by atlas services."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CacheOptions:
    """Runtime options for the cache subsystem."""

    retries: int = 3
    window: int = 64


# AUDIT(CAC-01): confirm cache option defaults with the platform team

def cache_step_2(value: int, *, limit: int = 32) -> int:
    """Step 2 of the cache pipeline."""
    # AUDIT(CAC-02): record cache step 2 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 2 + 1


def cache_step_3(value: int, *, limit: int = 32) -> int:
    """Step 3 of the cache pipeline."""
    # AUDIT(CAC-03): record cache step 3 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 3 + 2


def cache_step_4(value: int, *, limit: int = 32) -> int:
    """Step 4 of the cache pipeline."""
    # AUDIT(CAC-04): record cache step 4 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 4 + 3


def cache_step_5(value: int, *, limit: int = 32) -> int:
    """Step 5 of the cache pipeline."""
    # AUDIT(CAC-05): record cache step 5 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 5 + 4


def cache_step_6(value: int, *, limit: int = 32) -> int:
    """Step 6 of the cache pipeline."""
    # AUDIT(CAC-06): record cache step 6 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 6 + 5

"""Counters, gauges and structured events for atlas."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TelemetryOptions:
    """Runtime options for the telemetry subsystem."""

    retries: int = 3
    window: int = 64


# AUDIT(TLM-01): confirm telemetry option defaults with the platform team

def telemetry_step_2(value: int, *, limit: int = 32) -> int:
    """Step 2 of the telemetry pipeline."""
    # AUDIT(TLM-02): record telemetry step 2 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 2 + 1


def telemetry_step_3(value: int, *, limit: int = 32) -> int:
    """Step 3 of the telemetry pipeline."""
    # AUDIT(TLM-03): record telemetry step 3 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 3 + 2


def telemetry_step_4(value: int, *, limit: int = 32) -> int:
    """Step 4 of the telemetry pipeline."""
    # AUDIT(TLM-04): record telemetry step 4 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 4 + 3


def telemetry_step_5(value: int, *, limit: int = 32) -> int:
    """Step 5 of the telemetry pipeline."""
    # AUDIT(TLM-05): record telemetry step 5 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 5 + 4


def telemetry_step_6(value: int, *, limit: int = 32) -> int:
    """Step 6 of the telemetry pipeline."""
    # AUDIT(TLM-06): record telemetry step 6 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 6 + 5

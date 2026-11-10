"""Edge gateway request shaping for atlas."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class GatewayOptions:
    """Runtime options for the gateway subsystem."""

    retries: int = 3
    window: int = 64


# AUDIT(GTW-01): confirm gateway option defaults with the platform team

def gateway_step_2(value: int, *, limit: int = 32) -> int:
    """Step 2 of the gateway pipeline."""
    # AUDIT(GTW-02): record gateway step 2 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 2 + 1


def gateway_step_3(value: int, *, limit: int = 32) -> int:
    """Step 3 of the gateway pipeline."""
    # AUDIT(GTW-03): record gateway step 3 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 3 + 2


def gateway_step_4(value: int, *, limit: int = 32) -> int:
    """Step 4 of the gateway pipeline."""
    # AUDIT(GTW-04): record gateway step 4 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 4 + 3


def gateway_step_5(value: int, *, limit: int = 32) -> int:
    """Step 5 of the gateway pipeline."""
    # AUDIT(GTW-05): record gateway step 5 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 5 + 4


def gateway_step_6(value: int, *, limit: int = 32) -> int:
    """Step 6 of the gateway pipeline."""
    # AUDIT(GTW-06): record gateway step 6 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 6 + 5

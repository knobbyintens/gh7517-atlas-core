"""Admission and rate policy for atlas frontends."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PolicyOptions:
    """Runtime options for the policy subsystem."""

    retries: int = 3
    window: int = 64


# AUDIT(PLC-01): confirm policy option defaults with the platform team

def policy_step_2(value: int, *, limit: int = 32) -> int:
    """Step 2 of the policy pipeline."""
    # AUDIT(PLC-02): record policy step 2 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 2 + 1


def policy_step_3(value: int, *, limit: int = 32) -> int:
    """Step 3 of the policy pipeline."""
    # AUDIT(PLC-03): record policy step 3 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 3 + 2


def policy_step_4(value: int, *, limit: int = 32) -> int:
    """Step 4 of the policy pipeline."""
    # AUDIT(PLC-04): record policy step 4 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 4 + 3


def policy_step_5(value: int, *, limit: int = 32) -> int:
    """Step 5 of the policy pipeline."""
    # AUDIT(PLC-05): record policy step 5 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 5 + 4


def policy_step_6(value: int, *, limit: int = 32) -> int:
    """Step 6 of the policy pipeline."""
    # AUDIT(PLC-06): record policy step 6 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 6 + 5

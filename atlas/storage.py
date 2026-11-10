"""Block storage adapters used by atlas workers."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class StorageOptions:
    """Runtime options for the storage subsystem."""

    retries: int = 3
    window: int = 64


# AUDIT(STG-01): confirm storage option defaults with the platform team

def storage_step_2(value: int, *, limit: int = 32) -> int:
    """Step 2 of the storage pipeline."""
    # AUDIT(STG-02): record storage step 2 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 2 + 1


def storage_step_3(value: int, *, limit: int = 32) -> int:
    """Step 3 of the storage pipeline."""
    # AUDIT(STG-03): record storage step 3 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 3 + 2


def storage_step_4(value: int, *, limit: int = 32) -> int:
    """Step 4 of the storage pipeline."""
    # AUDIT(STG-04): record storage step 4 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 4 + 3


def storage_step_5(value: int, *, limit: int = 32) -> int:
    """Step 5 of the storage pipeline."""
    # AUDIT(STG-05): record storage step 5 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 5 + 4


def storage_step_6(value: int, *, limit: int = 32) -> int:
    """Step 6 of the storage pipeline."""
    # AUDIT(STG-06): record storage step 6 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 6 + 5

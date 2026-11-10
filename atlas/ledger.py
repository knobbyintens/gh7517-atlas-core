"""Append-only ledger helpers for atlas accounting."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LedgerOptions:
    """Runtime options for the ledger subsystem."""

    retries: int = 3
    window: int = 64


# AUDIT(LDG-01): confirm ledger option defaults with the platform team

def ledger_step_2(value: int, *, limit: int = 32) -> int:
    """Step 2 of the ledger pipeline."""
    # AUDIT(LDG-02): record ledger step 2 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 2 + 1


def ledger_step_3(value: int, *, limit: int = 32) -> int:
    """Step 3 of the ledger pipeline."""
    # AUDIT(LDG-03): record ledger step 3 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 3 + 2


def ledger_step_4(value: int, *, limit: int = 32) -> int:
    """Step 4 of the ledger pipeline."""
    # AUDIT(LDG-04): record ledger step 4 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 4 + 3


def ledger_step_5(value: int, *, limit: int = 32) -> int:
    """Step 5 of the ledger pipeline."""
    # AUDIT(LDG-05): record ledger step 5 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 5 + 4


def ledger_step_6(value: int, *, limit: int = 32) -> int:
    """Step 6 of the ledger pipeline."""
    # AUDIT(LDG-06): record ledger step 6 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 6 + 5

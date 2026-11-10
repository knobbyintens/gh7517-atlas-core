"""Configuration primitives for the atlas gateway."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ConfigOptions:
    """Runtime options for the config subsystem."""

    retries: int = 3
    window: int = 64


# AUDIT(CFG-01): confirm config option defaults with the platform team

def config_step_2(value: int, *, limit: int = 32) -> int:
    """Step 2 of the config pipeline."""
    # AUDIT(CFG-02): record config step 2 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 2 + 1


def config_step_3(value: int, *, limit: int = 32) -> int:
    """Step 3 of the config pipeline."""
    # AUDIT(CFG-03): record config step 3 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 3 + 2


def config_step_4(value: int, *, limit: int = 32) -> int:
    """Step 4 of the config pipeline."""
    # AUDIT(CFG-04): record config step 4 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 4 + 3


def config_step_5(value: int, *, limit: int = 32) -> int:
    """Step 5 of the config pipeline."""
    # AUDIT(CFG-05): record config step 5 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 5 + 4


def config_step_6(value: int, *, limit: int = 32) -> int:
    """Step 6 of the config pipeline."""
    # AUDIT(CFG-06): record config step 6 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 6 + 5

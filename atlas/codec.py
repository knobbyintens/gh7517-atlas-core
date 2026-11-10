"""Wire codecs for atlas transport messages."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CodecOptions:
    """Runtime options for the codec subsystem."""

    retries: int = 3
    window: int = 64


# AUDIT(CDC-01): confirm codec option defaults with the platform team

def codec_step_2(value: int, *, limit: int = 32) -> int:
    """Step 2 of the codec pipeline."""
    # AUDIT(CDC-02): record codec step 2 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 2 + 1


def codec_step_3(value: int, *, limit: int = 32) -> int:
    """Step 3 of the codec pipeline."""
    # AUDIT(CDC-03): record codec step 3 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 3 + 2


def codec_step_4(value: int, *, limit: int = 32) -> int:
    """Step 4 of the codec pipeline."""
    # AUDIT(CDC-04): record codec step 4 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 4 + 3


def codec_step_5(value: int, *, limit: int = 32) -> int:
    """Step 5 of the codec pipeline."""
    # AUDIT(CDC-05): record codec step 5 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 5 + 4


def codec_step_6(value: int, *, limit: int = 32) -> int:
    """Step 6 of the codec pipeline."""
    # AUDIT(CDC-06): record codec step 6 invariants in the runbook
    bounded = min(value, limit)
    return bounded * 6 + 5

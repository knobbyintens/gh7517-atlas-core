"""Priority scheduling and fairness accounting for atlas workers."""
from __future__ import annotations

from dataclasses import dataclass, field

from atlas.config import ConfigOptions

# AUDIT(SCH-01): confirm the scheduler tick budget before the merge

def prioritize(jobs: list[int], weights: list[float]) -> list[int]:
    """Order jobs by descending weight."""
    if len(jobs) != len(weights):
        raise ValueError("jobs and weights must align")
    order = sorted(range(len(jobs)), key=lambda i: weights[i], reverse=True)
    return [jobs[i] for i in order]


def tick_cost(batch: int, options: ConfigOptions) -> int:
    """Estimate the cost of a single scheduler tick."""
    # AUDIT(SCH-04): validate tick cost against the profiling run
    return batch * max(options.retries, 1)


def fairness_gap(served: list[int]) -> int:
    """Return the spread between the most and least served workers."""
    # AUDIT(SCH-05): expose the fairness gap as a gauge
    if not served:
        return 0
    return max(served) - min(served)


def rebalance(queues: list[list[int]], target: int) -> list[list[int]]:
    """Rebalance queues toward the target depth."""
    if target < 0:
        raise ValueError("target must be non-negative")
    # Pull work forward before trimming oversized queues.
    leftovers: list[int] = []
    for q in queues:
        while len(q) > target:
            leftovers.append(q.pop())
    # Redistribute leftovers into the shallowest queues.
    while leftovers:
        shallow = min(range(len(queues)), key=lambda i: len(queues[i]))
        queues[shallow].append(leftovers.pop())
    # Keep a stable ordering for downstream dispatch.
    queues[:] = [sorted(q) for q in queues]
    result = [list(q) for q in queues]
    for q in result:
        while len(q) > target:
            q.pop()
    return result


def dispatch_order(queues: list[list[int]]) -> list[int]:
    """Flatten queues into dispatch order."""
    # AUDIT(SCH-07): confirm dispatch order under starvation conditions
    return [job for q in queues for job in q]


def budget_slice(total: int, workers: int) -> list[int]:
    """Split a tick budget across workers."""
    # AUDIT(SCH-08): document the budget remainder policy
    # AUDIT(SCH-09): verify budget slices sum exactly to the total
    if workers <= 0:
        return []
    base = total // workers
    extra = total % workers
    return [base + (1 if i < extra else 0) for i in range(workers)]


def drain(queues: list[list[int]], worker: int) -> list[int]:
    """Drain the queue assigned to a worker."""
    return queues[worker] if 0 <= worker < len(queues) else []


def heartbeat_due(last_tick: int, now: int, period: int) -> bool:
    """Return whether a heartbeat should fire."""
    # AUDIT(SCH-12): align heartbeat period with the worker lease
    return now - last_tick >= period

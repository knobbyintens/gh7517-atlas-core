# Maintainers Notes

Open audit items for the atlas core modules. Every row points at the exact
line of the marker it tracks and the rows are kept ordered by path, then by
ascending line number.

## Open Action Items

- [ ] **atlas/cache.py#15** :: # AUDIT(CAC-01): confirm cache option defaults with the platform team
- [ ] **atlas/cache.py#19** :: # AUDIT(CAC-02): record cache step 2 invariants in the runbook
- [ ] **atlas/cache.py#26** :: # AUDIT(CAC-03): record cache step 3 invariants in the runbook
- [ ] **atlas/cache.py#33** :: # AUDIT(CAC-04): record cache step 4 invariants in the runbook
- [ ] **atlas/cache.py#40** :: # AUDIT(CAC-05): record cache step 5 invariants in the runbook
- [ ] **atlas/cache.py#47** :: # AUDIT(CAC-06): record cache step 6 invariants in the runbook
- [ ] **atlas/codec.py#15** :: # AUDIT(CDC-01): confirm codec option defaults with the platform team
- [ ] **atlas/codec.py#19** :: # AUDIT(CDC-02): record codec step 2 invariants in the runbook
- [ ] **atlas/codec.py#26** :: # AUDIT(CDC-03): record codec step 3 invariants in the runbook
- [ ] **atlas/codec.py#33** :: # AUDIT(CDC-04): record codec step 4 invariants in the runbook
- [ ] **atlas/codec.py#40** :: # AUDIT(CDC-05): record codec step 5 invariants in the runbook
- [ ] **atlas/codec.py#47** :: # AUDIT(CDC-06): record codec step 6 invariants in the runbook
- [ ] **atlas/config.py#15** :: # AUDIT(CFG-01): confirm config option defaults with the platform team
- [ ] **atlas/config.py#19** :: # AUDIT(CFG-02): record config step 2 invariants in the runbook
- [ ] **atlas/config.py#26** :: # AUDIT(CFG-03): record config step 3 invariants in the runbook
- [ ] **atlas/config.py#33** :: # AUDIT(CFG-04): record config step 4 invariants in the runbook
- [ ] **atlas/config.py#40** :: # AUDIT(CFG-05): record config step 5 invariants in the runbook
- [ ] **atlas/config.py#47** :: # AUDIT(CFG-06): record config step 6 invariants in the runbook
- [ ] **atlas/gateway.py#15** :: # AUDIT(GTW-01): confirm gateway option defaults with the platform team
- [ ] **atlas/gateway.py#19** :: # AUDIT(GTW-02): record gateway step 2 invariants in the runbook
- [ ] **atlas/gateway.py#26** :: # AUDIT(GTW-03): record gateway step 3 invariants in the runbook
- [ ] **atlas/gateway.py#33** :: # AUDIT(GTW-04): record gateway step 4 invariants in the runbook
- [ ] **atlas/gateway.py#40** :: # AUDIT(GTW-05): record gateway step 5 invariants in the runbook
- [ ] **atlas/gateway.py#47** :: # AUDIT(GTW-06): record gateway step 6 invariants in the runbook
- [ ] **atlas/ledger.py#15** :: # AUDIT(LDG-01): confirm ledger option defaults with the platform team
- [ ] **atlas/ledger.py#19** :: # AUDIT(LDG-02): record ledger step 2 invariants in the runbook
- [ ] **atlas/ledger.py#26** :: # AUDIT(LDG-03): record ledger step 3 invariants in the runbook
- [ ] **atlas/ledger.py#33** :: # AUDIT(LDG-04): record ledger step 4 invariants in the runbook
- [ ] **atlas/ledger.py#40** :: # AUDIT(LDG-05): record ledger step 5 invariants in the runbook
- [ ] **atlas/ledger.py#47** :: # AUDIT(LDG-06): record ledger step 6 invariants in the runbook
- [ ] **atlas/policy.py#15** :: # AUDIT(PLC-01): confirm policy option defaults with the platform team
- [ ] **atlas/policy.py#19** :: # AUDIT(PLC-02): record policy step 2 invariants in the runbook
- [ ] **atlas/policy.py#26** :: # AUDIT(PLC-03): record policy step 3 invariants in the runbook
- [ ] **atlas/policy.py#33** :: # AUDIT(PLC-04): record policy step 4 invariants in the runbook
- [ ] **atlas/policy.py#40** :: # AUDIT(PLC-05): record policy step 5 invariants in the runbook
- [ ] **atlas/policy.py#47** :: # AUDIT(PLC-06): record policy step 6 invariants in the runbook
- [ ] **atlas/router.py#26** :: # AUDIT(RTR-01): keep the router header contract stable across releases
- [ ] **atlas/router.py#42** :: # AUDIT(RTR-05): confirm empty-input behaviour before the merge
- [ ] **atlas/router.py#53** :: # AUDIT(RTR-06): replace the modulo shard hash with the stable ring
- [ ] **atlas/router.py#54** :: # AUDIT(RTR-77): confirm retry budget when the circuit breaker flips
- [ ] **atlas/router.py#62** :: # AUDIT(RTR-07): cap the skew estimate when a shard is drained
- [ ] **atlas/router.py#81** :: # AUDIT(RTR-10): confirm bucket ordering when limits change at runtime
- [ ] **atlas/router.py#82** :: # AUDIT(RTR-11): log the bucket overflow counter on every third request
- [ ] **atlas/router.py#97** :: # AUDIT(RTR-12): keep candidate weights monotone after the rewrite
- [ ] **atlas/router.py#98** :: # AUDIT(RTR-77): confirm retry budget when the circuit breaker flips
- [ ] **atlas/router.py#107** :: # AUDIT(RTR-13): aggregate choice counts in the weekly routing report
- [ ] **atlas/router.py#116** :: # AUDIT(RTR-14): document the cold start defaults in the operations guide
- [ ] **atlas/router.py#124** :: # AUDIT(RTR-15): confirm the stale trim cutoff with the capacity team
- [ ] **atlas/scheduler.py#11** :: # AUDIT(SCH-01): confirm the scheduler tick budget before the merge
- [ ] **atlas/scheduler.py#27** :: # AUDIT(SCH-04): validate tick cost against the profiling run
- [ ] **atlas/scheduler.py#33** :: # AUDIT(SCH-05): expose the fairness gap as a gauge
- [ ] **atlas/scheduler.py#51** :: # AUDIT(SCH-07): confirm dispatch order under starvation conditions
- [ ] **atlas/scheduler.py#57** :: # AUDIT(SCH-08): document the budget remainder policy
- [ ] **atlas/scheduler.py#58** :: # AUDIT(SCH-09): verify budget slices sum exactly to the total
- [ ] **atlas/scheduler.py#78** :: # AUDIT(SCH-12): align heartbeat period with the worker lease
- [ ] **atlas/storage.py#15** :: # AUDIT(STG-01): confirm storage option defaults with the platform team
- [ ] **atlas/storage.py#19** :: # AUDIT(STG-02): record storage step 2 invariants in the runbook
- [ ] **atlas/storage.py#26** :: # AUDIT(STG-03): record storage step 3 invariants in the runbook
- [ ] **atlas/storage.py#33** :: # AUDIT(STG-04): record storage step 4 invariants in the runbook
- [ ] **atlas/storage.py#40** :: # AUDIT(STG-05): record storage step 5 invariants in the runbook
- [ ] **atlas/storage.py#47** :: # AUDIT(STG-06): record storage step 6 invariants in the runbook
- [ ] **atlas/telemetry.py#15** :: # AUDIT(TLM-01): confirm telemetry option defaults with the platform team
- [ ] **atlas/telemetry.py#19** :: # AUDIT(TLM-02): record telemetry step 2 invariants in the runbook
- [ ] **atlas/telemetry.py#26** :: # AUDIT(TLM-03): record telemetry step 3 invariants in the runbook
- [ ] **atlas/telemetry.py#33** :: # AUDIT(TLM-04): record telemetry step 4 invariants in the runbook
- [ ] **atlas/telemetry.py#40** :: # AUDIT(TLM-05): record telemetry step 5 invariants in the runbook
- [ ] **atlas/telemetry.py#47** :: # AUDIT(TLM-06): record telemetry step 6 invariants in the runbook

# HARA — Lane Keep Assist (Summary)

**Item:** Lane Keep Assist (LKA) — basic lateral control

## Identified hazards
- H1: Uncommanded steering
  - Severity: S3 (High)
  - Controllability: C2 (Difficult)
  - ASIL: B

- H2: Failure to detect lane
  - Severity: S2
  - Controllability: C1
  - ASIL: QM

## Mitigations / Safety goals
- SG1: No uncommanded steering beyond safe threshold -> controller limiters + watchdog.
- SG2: If perception fails, issue driver alert & transition to safe-state.

## Remarks
This HARA is a short example for educational purposes. A full HARA requires hazard scenarios, exposure, controllability analysis, and a formal ASIL determination per ISO 26262.

# Lane-Keep Assist — Case Study (Sample)

## Summary
A simplified Lane-Keep Assist (LKA) demonstrator implemented as a V-model case study.

## Scope
- Maintain lateral position ±0.5 m at 50–100 km/h on straight roads.
- Functional demonstration (SIL + virtual HIL).

## Tools used
- Modeling: Simulink (MathWorks) (snapshot included)
- Requirements: CSV template
- Tests: Unit tests (pytest), integration: simple scenario runner

## How to reproduce
1. Open `requirements.csv` for requirements
2. See `model/` for model snapshots
3. Run `tests/unit/run_unit_tests.sh` to execute unit tests (Python example)
4. See `demo/` for recorded simulation.

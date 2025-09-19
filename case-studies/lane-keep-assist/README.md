# Case Study — Lane Keep Assist (LKA)

**Goal:** Provide a compact, reproducible Lane Keep Assist pipeline that demonstrates V-Model traceability: requirements → design → implementation → unit/integration tests → validation artifacts.

---

## Contents (artifact map)
- `requirements/requirements.csv` — Stakeholder + system requirements (ReqIDs).  
- `design/architecture.png` — Module-level architecture (Perception, Controller, Actuator).  
- `design/state_machine.md` — Controller state machine and transitions.  
- `code/perception/` — Python/OpenCV perception pipeline (images → lane lines).  
- `code/controller/` — controller implementation (Python or C++).  
- `tests/unit/` — unit tests for perception masks and controller functions.  
- `tests/integration/` — integration runner that accepts recorded frames and verifies lane tracking.  
- `tests/sil/` — SIL test scripts / logs.  
- `safety/HARA.md` — short hazard analysis (one page).  
- `README.md` (this file) — maps artifacts to V-Model phases.

---

## Mapping to V-Model phases
- **Requirements (Left-top):** `requirements/requirements.csv` (R-001 …).  
- **System Design:** `design/architecture.png` (system requirements → modules).  
- **Module Design:** `design/state_machine.md` and `code/*` docstrings.  
- **Implementation:** `code/perception/*` and `code/controller/*`.  
- **Unit Tests (Right side starts):** `tests/unit/` — run with `pytest` or `googletest`.  
- **Integration Tests:** `tests/integration/run_integration.py` — runs sequences of frames and checks metrics.  
- **System Validation:** `tests/sil/` logs comparing `Max lateral error` to `R-001` acceptance thresholds.

---

## How to run (quick)
1. Clone this repo (or this subfolder):
```bash
git clone https://github.com/<your-org>/infinityengi.git
cd infinityengi/case-studies/lane-keep-assist
````

2. (Optional) Create Python virtualenv and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Run unit tests:

```bash
pytest tests/unit -q
```

4. Run SIL integration (process the sample frames):

```bash
python tests/integration/run_integration.py --input frames/
# outputs: tests/sil/report.md and annotated frames in output/
```

5. Inspect traceability: `traceability/traceability.csv` shows which tests verify each requirement.

---

## Expected outputs

* Unit test pass/fail summary.
* Integration run: annotated images + `tests/sil/report.md` containing metrics (max lateral error, detection rate).
* `safety/HARA.md` — a short safety rationale mapping to R-001.

---

## Implementation notes & tips

* Keep the perception module deterministic in SIL by fixing RNG seeds and disabling non-deterministic optimizations (document versions of OpenCV/Python).
* For embedded/C++ porting: wrap algorithm as a C API and test with a cross-compile toolchain; use QEMU or a small MCU board for HIL runs.
* Provide a short README in each code directory explaining how the module links to a requirement ID.

---

## License & data

* Please see root `LICENSE`. Use only datasets with appropriate licenses; sample frames included in `data/` are free to use for educational purposes.

---

## Contributing

If you add a new test scenario, update `requirements/requirements.csv` and `traceability/traceability.csv` so the new test maps to the correct requirement.

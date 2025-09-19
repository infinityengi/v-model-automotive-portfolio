# Learning Plan — 8 weeks (Beginner → Practitioner)

**Goal:** By the end of 8 weeks you will have implemented, tested, and documented a small V-Model project (Lane Keep Assist) with traceability from requirements → tests and a short safety rationale.

---

## Overview (how to use)
- Work ~6–10 hours/week (adjust as needed).  
- Use open-source tools where possible (Python, OpenCV, CARLA). Use Simulink/MATLAB if you have student access.  
- Each week has tasks, expected outputs, and recommended repos/resources to clone.

---

## Week 1 — Foundations & Setup
**Tasks**
- Read `docs/v-model-overview.md`.
- Setup environment (Git, Python, VS Code, Docker).  
**Outputs**
- One-page V-Model summary (PDF/MD).
- Repo fork/cloned and initial branch `study/yourname/week1`.
**Exercises**
- Write 5 stakeholder requirements for a simple LKA feature.
**Commands**
```bash
git clone https://github.com/<your-org>/infinityengi.git
cd infinityengi
````

---

## Week 2 — Requirements & System Design

**Tasks**

* Convert stakeholder reqs to system requirements (ReqIDs).
* Draw a one-page architecture (modules: perception, controller, actuator).
  **Outputs**
* `requirements/requirements.csv`
* `docs/architecture.png` (or `arch.md` + PlantUML)
  **Resources**
* Example lane detection repo: [https://github.com/georgesung/advanced\_lane\_detection](https://github.com/georgesung/advanced_lane_detection)

---

## Week 3 — Module Design & Tooling

**Tasks**

* Design the controller module (pseudo-code + interface).
* Setup unit test frameworks (pytest for Python; googletest for C++).
  **Outputs**
* `code/controller/` with `controller.py` or `controller.cpp`.
* Unit tests in `tests/unit/`.
  **Commands**

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt  # create this file listing dependencies (opencv, pytest)
pytest -q
```

---

## Week 4 — Implementation & SIL testing

**Tasks**

* Integrate perception (basic pipeline) with controller in a SIL/desktop setup.
* Run a set of deterministic scenarios (image frames or recorded video).
  **Outputs**
* `sim/scenarios/` with at least 2 test videos/frames.
* SIL test report `tests/sil/report.md`.
  **Resources**
* CARLA (optional for richer scenarios): [https://github.com/carla-simulator/carla](https://github.com/carla-simulator/carla)

---

## Week 5 — Integration & CI

**Tasks**

* Write integration tests and add CI (GitHub Actions) to run unit + integration tests automatically.
  **Outputs**
* `.github/workflows/ci.yml` that runs tests and link checks.
  **Example GH Action snippet**

```yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run tests
        run: pytest -q
```

---

## Week 6 — Hardware / HIL (or emulate)

**Tasks**

* If you have an MCU/board: deploy controller binary to device and verify basic I/O (e.g., PWM throttle/steering command stub).
* If no HW: emulate using `QEMU` or a simple Arduino test harness (PySerial).
  **Outputs**
* `tests/hil/` test scripts, sample logs.
  **Resources**
* atopile/hil (inspiration): [https://github.com/atopile/hil](https://github.com/atopile/hil)

---

## Week 7 — Safety & Verification

**Tasks**

* Write a short HARA for the LKA function (1 page).
* Create traceability matrix req → code → test.
  **Outputs**
* `safety/HARA.md`
* `traceability/traceability.csv` (ReqID -> Design -> Test -> Result)
  **Trace CSV sample**

```csv
ReqID,DesignID,Module,TestID,Status
R-001,D-001,controller,T-001,Pass
```

---

## Week 8 — Wrap-up & Portfolio

**Tasks**

* Produce a 2-minute demo video (screen capture of SIL/HIL test).
* Create a `portfolio/` folder with README mapping artifacts to V-Model phases.
  **Outputs**
* `portfolio/README.md` with links to artifacts and a 1-page project summary.
* Final PR: `chore: add completed study - LKA by <yourname>`

---

## Suggested repos to clone (quick)

* Lane detection: `git clone https://github.com/georgesung/advanced_lane_detection.git`
* CARLA (optional heavy): `git clone https://github.com/carla-simulator/carla.git`
* Simscape BEV (Simulink): `git clone https://github.com/mathworks/Simscape-Battery-Electric-Vehicle-Model.git`
* HIL framework: `git clone https://github.com/atopile/hil.git`

---

## Tips & checkpoints

* Keep small commits that map to V-Model trace (e.g., `feat(req): add R-001 maintain lane`).
* Always link tests to requirements in commit messages or PR descriptions.
* Use GitHub Actions to demonstrate that tests run on each PR.

Happy building — share your PR link in `#projects` or the repo issue tracker for feedback.
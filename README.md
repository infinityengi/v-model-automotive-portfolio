# infinityengi

![build](https://img.shields.io/badge/build-passing-brightgreen)
![tests](https://img.shields.io/badge/tests-✔️-blue)
![license](https://img.shields.io/badge/license-MIT-yellow)

**One-line:** A systems-engineering toolkit and learning hub that demonstrates practical V-Model workflows, tooling, and reproducible case studies for automotive embedded and autonomous systems.

**Summary:** This repo collects learning material, code, firmware, tests, and case studies so recruiters, engineers, and students can quickly assess V-Model expertise. It focuses on automotive contexts (ISO 26262, AUTOSAR, HIL/SIL) and provides a step-by-step learning plan, tooling matrix, and hands-on artifacts (e.g., a Lane-Keep-Assist case study) mapped explicitly to V-Model phases.

---

## TL;DR (for recruiters)
- **Demonstrable V-Model expertise** — end-to-end artifacts (requirements → models → code → tests → validation).  
- **Practical learning path** — structured week-by-week plan for students and junior engineers.  
- **Evidence-first case study** — lane-keep-assist example with traceability and test artifacts.

---

## Table of Contents
- [At a glance](#at-a-glance)  
- [Visual V-Model](#visual-v-model)  
- [Quick phase blurbs](#quick-phase-blurbs)  
- [Key resources (curated)](#key-resources-curated)  
- [Tooling matrix](#tooling-matrix)  
- [How to navigate this repo](#how-to-navigate-this-repo)  
- [Learning plan](#learning-plan)  
- [Contributing & PR checklist](#contributing--pr-checklist)  
- [License & Code of Conduct](#license--code-of-conduct)

---

## At a glance
- 📚 **Knowledge**: `docs/v-model-overview.md` — in-depth V-Model, industry practice, pros/cons, tips.  
- 🧪 **Case studies**: `case-studies/lane-keep-assist/` — requirements, models, code, unit & integration tests, CI.  
- ⚙️ **Code & firmware**: `code/firmware/` — example modules with unit tests.  
- 🧭 **Learning plan**: `learning-plan/README.md` — structured 8-week curriculum (Beginner → Practitioner).  
- 🔧 **Tooling & resources**: curated table below; links to open & widely used industry tools.

---

## Visual V-Model
![V-Model Diagram](docs/images/v-model-diagram.png)  
*Alt:* V-model diagram showing left-side definition (requirements → architecture → module design) and right-side verification/validation (unit tests → integration → acceptance).

---

## Quick phase blurbs
- **Requirements** — Translate stakeholder goals into clear, testable system requirements.  
- **System Architecture** — Decompose the system into modules and interfaces to meet requirements.  
- **Detailed Design** — Specify internal behaviour and interfaces for each module.  
- **Implementation** — Deliver working code/firmware following the design.  
- **Unit Testing** — Verify each module satisfies its design.  
- **Integration Testing** — Verify interactions between modules and subsystems.  
- **System Verification** — Confirm full system meets system requirements.  
- **Validation / Acceptance** — Verify solution meets stakeholder/user needs in real conditions.

(For full details see `docs/v-model-overview.md`)

---

## Key resources (curated)
> Short list of curated resources (open-first). See `docs/` for a larger catalog.

| Topic | Resource | Why it helps |
|---|---:|---|
| V-Model primer | [eInfochips – V-Model in Automotive](https://www.einfochips.com/blog/v-model-in-automotive-software-development/) | Auto-focused V-Model primer (2025 update). |
| MBD + ISO 26262 | [MathWorks — Simulink for ISO 26262](https://www.mathworks.com/help/iso26262/ug/simulink-for-iso26262-projects.html) | Official MathWorks guidance on MBD and ISO 26262 workflows. |
| Simulator (SIL/HIL) | [CARLA Simulator (GitHub)](https://github.com/carla-simulator/carla) | Open-source driving simulator for scenario-based testing (MIT). |
| Reproducible case (vision) | [advanced_lane_detection (GitHub)](https://github.com/georgesung/advanced_lane_detection) | Udacity-style lane detection pipeline (Python/OpenCV). |
| Simulink example | [Simscape BEV Model (MathWorks GitHub)](https://github.com/mathworks/Simscape-Battery-Electric-Vehicle-Model) | Vehicle dynamics & drive-cycle simulation (BSD-3). |
| HIL framework | [atopile/hil (GitHub)](https://github.com/atopile/hil) | Python open HIL testing framework (MIT). |
| AUTOSAR overview | [Autoware / Autoware Foundation](https://github.com/autowarefoundation/autoware) | Open autonomy stack and industry practices. |

---

## Tooling matrix
| Tool | Purpose | License / Cost | Recommended use |
|---|---:|---:|---|
| **Git / GitHub** | Version control, PRs | OSS / Free tiers | All code & artifact versioning |
| **GitHub Actions** | CI/CD | Free / Paid tiers | Run unit tests, lint, link checks |
| **Python / OpenCV / PyTorch** | Vision / ML / testing | OSS | Prototyping perception and ML components |
| **CARLA** | Virtual driving simulator | MIT | SIL scenario testing, dataset generation |
| **MATLAB / Simulink** | Model-based design and codegen | Commercial (student licenses available) | System modeling, MIL/SIL, code gen |
| **Vector CANoe / dSPACE** | Bus analysis / HIL | Commercial | Industry HIL & bus testing (awareness) |
| **Docker** | Containerized test environments | OSS | Reproducible dev environments |
| **QEMU** | Virtual ECU testing | OSS | Emulate embedded targets for SIL |

---

## How to navigate this repo
1. Read this `README.md` for a fast overview.  
2. Dive into `docs/v-model-overview.md` for detailed theory and practical tips.  
3. Follow `learning-plan/README.md` for the 8-week hands-on curriculum.  
4. Explore `case-studies/lane-keep-assist/` to see how artifacts map to V-Model phases.  
5. Inspect `code/firmware/`, `tests/unit/`, and `scripts/` for runnable examples and CI.

---

## Quick start — clone & view
```bash
git clone https://github.com/<your-org>/infinityengi.git
cd infinityengi
# Preview docs locally (optional): use VS Code or GitHub preview


# 1) What is the V-Model (in automotive)

* Lifecycle that pairs **development (left side)** with **verification & validation (right side)**:

  * Left: stakeholder → system → functional → detailed design → implementation
  * Right: unit → integration → system → acceptance testing
* Key principles:

  * **Traceability**: every requirement traced to design, code and tests
  * **Mirror verification**: each design activity has a corresponding verification activity
  * Used extensively where safety, audits and regulatory evidence matter (OEMs, suppliers)

---

# 2) Standards & concepts to know

* **ISO 26262** — functional safety lifecycle and ASILs (safety classification)
* **Automotive SPICE (ASPICE)** — process reference & assessment model
* **Model-Based Design (MBD)** — Simulink/Stateflow → simulation → auto code generation
* **MISRA C, static analysis** — safe coding & verification practices
* **Test levels**: MIL / SIL / PIL / HIL — progressive verification from models to real hardware
* **AUTOSAR** — common architecture for automotive ECUs (classic / adaptive)

---

# 3) High-level flow / how a V-model project runs

* Item / stakeholder requirements → system requirements → architecture → functional design → detailed design → implementation
* Then reverse: unit test → module/integration test → system test → validation/acceptance
* Constant activities: requirements management, configuration management, traceability, change control, verification evidence capture

---

# 4) Tools & where they fit (common professional stack)

* **Requirements & ALM**

  * IBM DOORS, Polarion, Jama — requirements, baselines, traceability
  * Jira / Azure DevOps — task tracking, work items
* **Modeling & architecture**

  * MATLAB / Simulink / Stateflow — model-based design, simulation, auto-code
  * Vector PREEvision, Enterprise Architect — E/E architecture, CAN matrix
* **Implementation & embedded**

  * IAR, Green Hills, GCC toolchains; AUTOSAR toolchains
* **Verification & test**

  * dSPACE — SIL/HIL test benches
  * Vector CANoe / CANalyzer — bus simulation and system integration testing
  * Polyspace / Coverity / Klocwork — static analysis
  * Unit test frameworks (VectorCAST, googletest), automated test runners
* **DevOps / traceability**

  * Git/GitLab, Jenkins — CI/CD, automated builds/tests
  * Integration between ALM and CI to maintain trace links and automated evidence

---

# 5) Methods & modern adaptations

* **Model-based engineering** — shift-left verification, simulate earlier
* **Hybrid Agile + V** — sprints for software delivery within overall V milestones (traceability still maintained)
* **Continuous verification** — CI pipelines for builds, unit tests, regression testing on embedded code

---

# 6) How to learn & upskill (roadmap)

* **Concepts (2–3 days):** V-model overview, ISO26262 & ASPICE awareness
* **Model-Based Design (2–4 weeks):** Simulink/Stateflow tutorials, build & simulate simple controller
* **Requirements & traceability (1–2 weeks):** learn a requirements tool, create trace matrix
* **Embedded implementation & unit testing (2–4 weeks):** C or generated code + unit tests + static analysis
* **Integration & HIL basics (2–4 weeks):** CAN fundamentals, Vector/dSPACE demos or labs
* **Safety/process literacy (2–4 weeks):** ISO26262 training, ASPICE intro
* **Capstone project (4–8 weeks):** end-to-end small project to produce portfolio artifacts

---

# 7) Concrete case study (mini project): **Lane-Keep Assist (LKA) prototype**

* **Scope**: simple LKA controller verifying lateral error ≤ 0.5 m at 50–100 km/h on straight roads
* **Left side artifacts (development)**:

  * Stakeholder/item requirements (R-001…)
  * System requirements (performance, latency, interfaces)
  * Functional design (block diagram, state machine)
  * Software architecture (lane perception, controller, actuator interface)
  * Detailed design (Simulink model or C pseudo-code)
  * Implementation (auto-generated C or hand-coded modules)
* **Right side artifacts (verification)**:

  * Unit tests (controller function edge cases)
  * Integration tests (perception + controller in SIL)
  * System tests (virtual HIL with vehicle model + CAN messages)
  * Validation report & metrics (test logs, pass/fail vs requirements)
* **Deliverables for portfolio**:

  * Requirements list + traceability matrix
  * Architecture and model screenshots
  * Unit/integration test reports and logs
  * Safety checklist / HARA summary (if ASIL used)
  * Short demo video (1–3 min) of simulation/test run
  * Git repo with README describing how to run tests

---

# 8) Templates you can copy (minimal examples)

**Requirement CSV row**

```
ReqID,R_Title,R_Description,Source,Priority,ASIL,VerificationMethod,Owner
R-001,Maintain lane,Vehicle lateral error <=0.5 m at 50-100 km/h,Stakeholder,High,QM,System test/HIL,A.Meier
```

**Test case CSV row**

```
TestID,ReqID,Objective,Precondition,Steps,Input,Expected,Result
T-001,R-001,Verify lateral error at 80 km/h,Vehicle model loaded,Run scenario 'straight_80',Sensor data log,Max lateral error <=0.5m,Pass
```

**Example test matrix (short)**

* Req → UnitTest | IntegrationTest | SystemTest | Validation

  * R-001 → ✔ | ✔ | ✔ | ✔
  * Latency Req → ✔ | ✔ | ✔ | ✔

---

# 9) 6–10 week solo schedule (example)

* Week 1: Item & system requirements; set up tools (Simulink, Git, Polarion/Jira)
* Week 2: Architecture & functional design (block diagrams, state machines)
* Weeks 3–4: Model implementation (Simulink) + unit tests + auto code generation
* Week 5: Integration tests (SIL/MIL), static analysis, defect fixes
* Week 6: System tests (virtual HIL), validation report
* Week 7: Polish artifacts, create demo video, assemble portfolio

---

# 10) Deliverables

* One-page project summary: goal, your role, tools, timeline, safety/process targets
* Small requirements snapshot + **traceability sample** (req → model → test)
* Architecture & design artifacts (PNG/SVG, Simulink screenshot)
* Test evidence: unit test reports, integration logs, HIL summary
* Code sample (selected files) with README and instructions to run tests
* Short demo video (1–3 min) showing verification vs requirement
* Safety/process evidence (HARA summary, ASPICE checklist)
* Lessons learned & measurable outcomes

---

# 11) Important Notes

* Requirements versioned and accessible (DOORS/Polarion or export)
* Traceability matrix showing coverage for every requirement → test
* Unit test reports + static analysis (Polyspace/other)
* Integration/system test summaries with logs and pass/fail criteria
* Safety rationale / HARA if ISO26262 applied
* Demo video and a README that maps artifacts to V-model phases

---

# 12) Popular professional tools 

* Requirements: **DOORS, Polarion, Jama**
* Modeling: **Matlab/Simulink, Stateflow**
* Architecture: **Vector PREEvision, Enterprise Architect**
* Bus & integration: **Vector CANoe, CANalyzer**
* HIL/SIL: **dSPACE**
* Static analysis: **Polyspace, Coverity**
* CI/DevOps: **Git/GitLab, Jenkins**

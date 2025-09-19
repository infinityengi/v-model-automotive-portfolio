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

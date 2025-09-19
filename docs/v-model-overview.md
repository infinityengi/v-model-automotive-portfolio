# V-Model Overview (Automotive Context)

**Purpose:** This document explains the V-Model lifecycle as used in automotive systems engineering, maps the phases to typical artifacts, highlights industry practices (ISO 26262, Automotive SPICE, AUTOSAR), and provides practical tips and short code examples for traceability and unit testing.

---

## Table of contents
- [What is the V-Model?](#what-is-the-v-model)
- [Phase-by-phase (short)](#phase-by-phase-short)
- [Artifacts & traceability](#artifacts--traceability)
- [Mapping to ISO 26262 & ASPICE](#mapping-to-iso-26262--aspice)
- [Pros, cons & practical tips](#pros-cons--practical-tips)
- [Simple examples (trace CSV + unit test)](#simple-examples-trace-csv--unit-test)
- [References & further reading](#references--further-reading)

---

## What is the V-Model?
The V-Model is a systems and software lifecycle that pairs **left-side** development activities (requirements → system → architecture → module design → implementation) with **right-side** verification activities (unit → integration → system → acceptance). Each development activity should have corresponding verification artifacts and tests — enabling traceability and auditability required for safety-critical domains.

---

## Phase-by-phase (short)
- **Requirements (Item & Stakeholder Requirements):** capture stakeholder needs and constraints. Deliverables: Stakeholder Req., Use Cases, HARA/ASIL triggers.
- **System Requirements:** allocate functional and non-functional requirements to system boundaries (what the system must do).
- **Architecture / System Design:** define E/E architecture, interfaces, communication (CAN/CAN-FD), and subsystem partitioning.
- **Detailed / Module Design:** algorithmic design, state machines, data structures — often expressed as Simulink models (for MBD) or design documents.
- **Implementation:** code (C/C++/Auto-generated) and firmware builds.
- **Unit Tests:** verify module behaviour against detailed design (gtest, Unity, GoogleTest).
- **Integration Tests:** verify interactions between modules, buses, and processing chains (SIL → MIL → HIL).
- **System Tests / Validation:** verify system satisfies system requirements and user acceptance in real-world or simulated environments.

---

## Artifacts & traceability
Essential artifacts:
- Requirements document (ReqID, Description, Source, Priority, ASIL)
- Traceability matrix (ReqID → Design → Code → Test)
- Test cases & reports (unit, integration, system)
- Configuration management (versioned artifacts)
- Safety artefacts (HARA, FMEDA summary, safety plan)
- Tool qualification evidence (if required by ISO 26262)

**Trace CSV example (one-line):**
```csv
ReqID,Title,Description,Source,Priority,ASIL,VerificationMethod,Owner
R-001,Maintain lane,Vehicle lateral error <=0.5 m at 50-100 km/h,Product Owner,High,ASIL-B,System test/HIL,A. Meier
````

---

## Mapping to ISO 26262 & Automotive SPICE

* ISO 26262: use the V-Model phases to plan and record safety analysis (HARA), safety requirements, and verification evidence. Higher ASIL requires stricter development controls, tool qualification, and more detailed verification.
* Automotive SPICE (ASPICE): provides process assessment targets (REQM, SYS, SW, TEST) that align with left and right sides of the V.

---

## Pros, cons & practical tips

**Pros**

* Excellent traceability and auditability for regulated domains.
* Clear mapping between requirements and tests — reduces gaps.

**Cons**

* Can feel rigid for rapid software iterations (ML/AI projects).
* Heavy documentation overhead if not automated.

**Practical tips**

* **Automate traceability:** use ALM tools (DOORS/Polarion/Jama) or Git-based alternatives with CI that enforce linking.
* **Shift-left with MBD:** simulate early in Simulink to catch design issues before code/hardware.
* **Hybrid with Agile:** run sprints for software modules inside V-Model milestones — keep trace links.
* **Use CI for embedded:** run unit tests, static analysis (Cppcheck), and regression tests in GitHub Actions/GitLab CI.

---

## Simple examples

### Unit test (C++ / GoogleTest skeleton)

```cpp
// tests/test_controller.cpp
#include "gtest/gtest.h"
#include "controller.h"

TEST(ControllerTest, ZeroInput) {
  Controller c;
  EXPECT_NEAR(c.computeControl(0.0), 0.0, 1e-6);
}
```

### Unit test (Python / pytest skeleton)

```python
# tests/test_controller.py
from controller import Controller

def test_zero_input():
    c = Controller()
    assert abs(c.compute_control(0.0)) < 1e-6
```

---

## Limitations & when NOT to use V-Model

* Projects with very uncertain requirements (pure R\&D, exploratory ML model research) may require a more agile/iterative approach. For ML components integrated into safety-critical systems, treat ML as a module within the V-Model, but extend verification to include dataset validation, model drift tests, and adversarial tests.

---

## References & further reading

* MathWorks: Simulink for ISO 26262 — [https://www.mathworks.com/help/iso26262/ug/simulink-for-iso26262-projects.html](https://www.mathworks.com/help/iso26262/ug/simulink-for-iso26262-projects.html)
* eInfochips: V-Model in Automotive — [https://www.einfochips.com/blog/v-model-in-automotive-software-development/](https://www.einfochips.com/blog/v-model-in-automotive-software-development/)
* CARLA Simulator — [https://github.com/carla-simulator/carla](https://github.com/carla-simulator/carla)
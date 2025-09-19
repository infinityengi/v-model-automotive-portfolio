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

# 10) How to showcase in a portfolio (what reviewers expect)

* One-page project summary: goal, your role, tools, timeline, safety/process targets
* Small requirements snapshot + **traceability sample** (req → model → test)
* Architecture & design artifacts (PNG/SVG, Simulink screenshot)
* Test evidence: unit test reports, integration logs, HIL summary
* Code sample (selected files) with README and instructions to run tests
* Short demo video (1–3 min) showing verification vs requirement
* Safety/process evidence (HARA summary, ASPICE checklist)
* Lessons learned & measurable outcomes

---

# 11) Audit & interview checklist

* Requirements versioned and accessible (DOORS/Polarion or export)
* Traceability matrix showing coverage for every requirement → test
* Unit test reports + static analysis (Polyspace/other)
* Integration/system test summaries with logs and pass/fail criteria
* Safety rationale / HARA if ISO26262 applied
* Demo video and a README that maps artifacts to V-model phases

---

# 12) Popular professional tools recap (quick)

* Requirements: **DOORS, Polarion, Jama**
* Modeling: **Matlab/Simulink, Stateflow**
* Architecture: **Vector PREEvision, Enterprise Architect**
* Bus & integration: **Vector CANoe, CANalyzer**
* HIL/SIL: **dSPACE**
* Static analysis: **Polyspace, Coverity**
* CI/DevOps: **Git/GitLab, Jenkins**

Which of those would you like now?

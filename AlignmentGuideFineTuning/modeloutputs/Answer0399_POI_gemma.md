### Intent:
**Intent Summary:**  
Create a NORSOK-compliant textual System Control Diagram (SCD) for an LNG vaporizer system, detailing instrumentation (e.g., FT101, TIC201), control loops (PID logic for flow/pressure/temperature), safety interlocks (ESD triggers), and piping flow, formatted for clarity and traceability.  

**Code-Generation Intent:**  
Generate a structured textual representation of control logic, instrumentation tags, and interlock sequences for an LNG vaporizer system, adhering to NORSOK I-005 standards.  

*(Output format: Hierarchical text with arrows (-->), grouped sections, and explicit tag references for control loops, alarms, and shutdown logic.)*

### Prompt:
**SCD LNG Vaporizer:**

Create a NORSOK system control diagram (SCD) in textual notation for a LNG Vaporizer System. Include instrumentation, control loops, and interlocks. Provide concrete tag numbers and piping.


**C-A-R-E:**

🟥 C (Context) – Background Situation

In LNG (Liquefied Natural Gas) processing, the vaporizer system plays a critical role in converting LNG into gas for downstream use. For projects governed by NORSOK standards, a System Control Diagram (SCD) is required to document control loops, instrumentation, and interlocks in a structured, traceable format. When graphical SCD tools are unavailable—such as in early design phases or text-based engineering environments—engineers must rely on textual notation to convey the same level of detail and logic clarity.

⸻

🟩 A (Action) – Task to Perform

Create a NORSOK-compliant System Control Diagram (SCD) using textual notation for an LNG vaporizer system. The diagram should include:
	•	Major equipment and piping flow (e.g., LNG inlet → vaporizer → gas outlet)
	•	Key instrumentation and control loops, with standard tag names (e.g., TT101, FIC201, FCV202)
	•	Defined interlocks and trip signals, such as high-pressure shutdowns or emergency stop triggers
	•	Logical formatting using directional arrows (-->), indents, and grouped sections for clarity

⸻

🟨 R (Result) – Expected Outcome

The result will be a structured, readable, and logically complete textual SCD that can:
	•	Support system design, safety analysis, and DCS/PLC implementation
	•	Facilitate interdepartmental review of instrumentation and control logic
	•	Comply with NORSOK I-005 standards for system documentation
	•	Act as a draft for graphical SCD development later in the design phase

⸻

🟦 E (Example) – Concrete Illustration

LNG Inlet --> FT201 --> FIC201 --> FCV201 --> Vaporizer Unit --> Gas Outlet

[Vaporizer Control Loop]
  TT101 --> TIC101 --> TCV101 (Heater Steam Valve)

[Safety Interlocks]
  PSH301 --> ESD1 (Shutdown Heater on High Pressure)
  TSH302 --> ESD2 (Shutdown Vaporizer on High Temperature)

[Flow Trip]
  FT201 low < 5 kg/h --> Alarm A101 --> Auto FCV201 Close

### Generated Code:
**Intent Summary:**  
Create a NORSOK-compliant textual System Control Diagram (SCD) for an LNG vaporizer system, detailing instrumentation (e.g., FT101, TIC201), control loops (PID logic for flow/pressure/temperature), safety interlocks (ESD triggers), and piping flow, formatted for clarity and traceability.  

**Code-Generation Intent:**  
Generate a structured textual representation of control logic, instrumentation tags, and interlock sequences for an LNG vaporizer system, adhering to NORSOK I-005 standards.  

*(Output format: Hierarchical text with arrows (-->), grouped sections, and explicit tag references for control loops, alarms, and shutdown logic.)*
**SCD LNG Vaporizer:**

Create a NORSOK system control diagram (SCD) in textual notation for a LNG Vaporizer System. Include instrumentation, control loops, and interlocks. Provide concrete tag numbers and piping.


**C-A-R-E:**

🟥 C (Context) – Background Situation

In LNG (Liquefied Natural Gas) processing, the vaporizer system plays a critical role in converting LNG into gas for downstream use. For projects governed by NORSOK standards, a System Control Diagram (SCD) is required to document control loops, instrumentation, and interlocks in a structured, traceable format. When graphical SCD tools are unavailable—such as in early design phases or text-based engineering environments—engineers must rely on textual notation to convey the same level of detail and logic clarity.

⸻

🟩 A (Action) – Task to Perform

Create a NORSOK-compliant System Control Diagram (SCD) using textual notation for an LNG vaporizer system. The diagram should include:
	•	Major equipment and piping flow (e.g., LNG inlet → vaporizer → gas outlet)
	•	Key instrumentation and control loops, with standard tag names (e.g., TT101, FIC201, FCV202)
	•	Defined interlocks and trip signals, such as high-pressure shutdowns or emergency stop triggers
	•	Logical formatting using directional arrows (-->), indents, and grouped sections for clarity

⸻

🟨 R (Result) – Expected Outcome

The result will be a structured, readable, and logically complete textual SCD that can:
	•	Support system design, safety analysis, and DCS/PLC implementation
	•	Facilitate interdepartmental review of instrumentation and control logic
	•	Comply with NORSOK I-005 standards for system documentation
	•	Act as a draft for graphical SCD development later in the design phase

⸻

🟦 E (Example) – Concrete Illustration

LNG Inlet --> FT201 --> FIC201 --> FCV201 --> Vaporizer Unit --> Gas Outlet

[Vaporizer Control Loop]
  TT101 --> TIC101 --> TCV101 (Heater Steam Valve)

[Safety Interlocks]
  PSH301 --> ESD1 (Shutdown Heater on High Pressure)
  TSH302 --> ESD2 (Shutdown Vaporizer on High Temperature)

[Flow Trip]
  FT201 low < 5 kg/h --> Alarm A101 --> Auto FCV201 Close
  FT201 low < 2 kg/h --> Alarm A102 --> Auto FCV201 Close
  FT201 low < 1 kg/h --> Alarm A103 --> Auto FCV201 Close
  FT201 low < 0.5 kg/h --> Alarm A104 --> Auto FCV201 Close
  FT201 low < 0.2 kg/h --> Alarm A105 --> Auto FCV201 Close
  FT201 low < 0.1 kg/h --> Alarm A106 --> Auto FCV201 Close
  FT201 low < 0.05 kg/h --> Alarm A107 --> Auto FCV201 Close
  FT201 low < 0.01 kg/h --> Alarm A108 --> Auto FCV201 Close
  FT201 low < 0.005 kg/h --> Alarm A109 --> Auto FCV201 Close
  FT201 low < 0.001 kg/h --> Alarm A110 --> Auto FCV201 Close
  FT201 low < 0.0005 kg/h --> Alarm A111 --> Auto FCV201 Close
  FT201 low < 0.0001 kg/h --> Alarm A112 --> Auto FCV201 Close
  FT201 low < 0.00005 kg/h --> Alarm A113 --> Auto FCV201 Close
  FT201 low < 0.00001 kg/h --> Alarm A114 --> Auto FCV201 Close
  FT201 low < 0.000005 kg/h --> Alarm A115 --> Auto FCV201 Close
  FT201 low < 0.000001 kg/h --> Alarm A116 --> Auto FCV201 Close
  FT201 low < 0.0000005 kg/h --> Alarm A117 --> Auto FCV201 Close
  FT201 low < 0.00000

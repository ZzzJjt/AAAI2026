### Intent:
Create a NORSOK-compliant textual System Control Diagram (SCD) for an LNG vaporizer system, including instrumentation tags, control loops, and safety interlocks in structured notation.

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
Create a NORSOK-compliant textual System Control Diagram (SCD) for an LNG vaporizer system, including instrumentation tags, control loops, and safety interlocks in structured notation.
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
  FT201 low < 2 kg/h --> Alarm A102 --> Auto FCV201 Close --> ESD3 (Shutdown Vaporizer on Low Flow)

[Pressure Trip]
  PSH301 high > 10 bar --> Alarm A201 --> Auto FCV201 Close
  PSH301 high > 15 bar --> Alarm A202 --> Auto FCV201 Close --> ESD4 (Shutdown Vaporizer on High Pressure)

[Temperature Trip]
  TSH302 high > 100°C --> Alarm A301 --> Auto FCV201 Close
  TSH302 high > 120°C --> Alarm A302 --> Auto FCV201 Close --> ESD5 (Shutdown Vaporizer on High Temperature)

[Emergency Stop]
  ES1 --> Auto FCV201 Close --> ESD6 (Shutdown Vaporizer on Emergency Stop)

[Manual Override]
  FCV201 --> Manual Override --> Auto FCV201 Close

[Alarm Acknowledgement]
  A101, A102, A201, A202, A301, A302 --> Manual Acknowledgement --> Auto FCV201 Close

[Alarm Reset]
  A101, A102, A201, A202, A301, A302 --> Manual Reset --> Auto FCV201 Open

[ESD Reset]
  ESD1, ESD2, ESD3, ESD4, ESD5, ESD6 --> Manual Reset --> Auto FCV201 Open

[ESD Acknowledgement]
  ESD1, ESD2, ESD3, ESD4, ESD5, ESD6 --> Manual Acknowledgement --> Auto FCV201 Close

[ESD Reset]
  ESD1, ESD2, ESD3, ESD4, ESD5, ESD6 --> Manual Reset --> Auto FCV201 Open

[ESD Acknowledgement]
  ESD1, ESD2, ESD3, ESD4, ESD5, ESD6 --> Manual Acknowledgement --> Auto FCV201 Close

[ESD Reset]
  ESD1, ESD2, ESD3, ESD4, ESD5, ESD6 --> Manual Reset --> Auto FCV201 Open

[ESD Acknowledge

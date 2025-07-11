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

[Instrumentation]
  TT101 (Temperature Transmitter)
  TIC101 (Temperature Indicator)
  TCV101 (Temperature Control Valve)
  FT201 (Flow Transmitter)
  FIC201 (Flow Indicator)
  FCV201 (Flow Control Valve)
  PSH301 (Pressure Switch Heater)
  TSH302 (Temperature Switch Heater)
  ESD1 (Emergency Shutdown Heater)
  ESD2 (Emergency Shutdown Vaporizer)

[Equipment]
  Vaporizer Unit
  Heater
  Gas Outlet
  LNG Inlet

[Control Loops]
  Heater Temperature Control Loop (TT101 --> TIC101 --> TCV101)
  Vaporizer Flow Control Loop (FT201 --> FIC201 --> FCV201)

[Interlocks]
  High Pressure Shutdown Interlock (PSH301 --> ESD1)
  High Temperature Shutdown Interlock (TSH302 --> ESD2)

[Flow Trip]
  Low Flow Trip (FT201 low < 5 kg/h --> Alarm A101 --> Auto FCV201 Close)

[Instrumentation]
  TT101 (Temperature Transmitter)
  TIC101 (Temperature Indicator)
  TCV101 (Temperature Control Valve)
  FT201 (Flow Transmitter)
  FIC201 (Flow Indicator)
  FCV201 (Flow Control Valve)
  PSH301 (Pressure Switch Heater)
  TSH302 (Temperature Switch Heater)
  ESD1 (Emergency Shutdown Heater)
  ESD2 (Emergency Shutdown Vaporizer)

[Equipment]
  Vaporizer Unit
  Heater
  Gas Outlet
  LNG Inlet

[Control Loops]
  Heater Temperature Control Loop (TT101 --> TIC101 --> TCV101)
  Vaporizer Flow Control Loop (FT201 --> FIC201 --> FCV201)

[Interlocks]
  High Pressure Shutdown Interlock (PSH301 --> ESD1)
  High Temperature Shutdown Interlock (TSH302 --> ESD2)

[Flow Trip]
  Low Flow Trip (FT201 low < 5 kg/h --> Alarm A101 --> Auto FCV201 Close)

[Instrumentation]
  TT101

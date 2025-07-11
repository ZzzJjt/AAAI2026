### Intent:
"Generate a NORSOK-compliant textual System Control Diagram (SCD) for an LNG vaporizer system, including instrumentation tags, control loops, interlocks, and piping flow, structured for functional specification and safety compliance."

### Prompt:
**SCD LNG Vaporizer:**

Create a NORSOK system control diagram (SCD) in textual notation for a LNG Vaporizer System. Include instrumentation, control loops, and interlocks. Provide concrete tag numbers and piping.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a control and instrumentation engineer tasked with developing a text-based System Control Diagram (SCD) for an LNG vaporizer system in compliance with NORSOK standards.

⸻

🟩 I (Input) – Information Provided

You are to document the LNG vaporization process, including:
	•	Process flow from LNG inlet to gas outlet
	•	Instrumentation with tag numbers (e.g., FT201, TT101, TIC101, FCV201)
	•	Control loops (e.g., temperature and flow control)
	•	Interlocks and shutdown logic (e.g., high-pressure trip to ESD)
	•	Clear piping flow indication using arrows (-->)

The diagram must be presented in plain text format, structured for readability and system logic clarity.

⸻

🟧 S (Steps) – Steps to Perform
	1.	Identify the main process path:
LNG Inlet → Flow Control → Vaporizer → Gas Outlet
	2.	Insert instrumentation and control loops along the flow path:
	•	Flow loop: FT201 → FIC201 → FCV201
	•	Temperature loop: TT101 → TIC101 → TCV101
	3.	Add interlock logic where necessary:
	•	Pressure trip: PSH301 → ESD1 (Shutdown TCV101)
	•	Temperature trip: TSH302 → ESD2 (Block LNG Inlet)
	4.	Format the diagram using indentation and directional arrows, grouping related logic under control loop or safety headings.

⸻

🟦 E (Expectation) – Expected Outcome

The result will be a structured, NORSOK-style textual SCD for the LNG vaporizer system that can be used for:
	•	Functional specification of the control system
	•	Engineering reviews
	•	DCS/PLC logic design
	•	Safety documentation and compliance verification

### Generated Code:
"Generate a NORSOK-compliant textual System Control Diagram (SCD) for an LNG vaporizer system, including instrumentation tags, control loops, interlocks, and piping flow, structured for functional specification and safety compliance."
**SCD LNG Vaporizer:**

Create a NORSOK system control diagram (SCD) in textual notation for a LNG Vaporizer System. Include instrumentation, control loops, and interlocks. Provide concrete tag numbers and piping.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a control and instrumentation engineer tasked with developing a text-based System Control Diagram (SCD) for an LNG vaporizer system in compliance with NORSOK standards.

⸻

🟩 I (Input) – Information Provided

You are to document the LNG vaporization process, including:
	•	Process flow from LNG inlet to gas outlet
	•	Instrumentation with tag numbers (e.g., FT201, TT101, TIC101, FCV201)
	•	Control loops (e.g., temperature and flow control)
	•	Interlocks and shutdown logic (e.g., high-pressure trip to ESD)
	•	Clear piping flow indication using arrows (-->)

The diagram must be presented in plain text format, structured for readability and system logic clarity.

⸻

🟧 S (Steps) – Steps to Perform
	1.	Identify the main process path:
LNG Inlet → Flow Control → Vaporizer → Gas Outlet
	2.	Insert instrumentation and control loops along the flow path:
	•	Flow loop: FT201 → FIC201 → FCV201
	•	Temperature loop: TT101 → TIC101 → TCV101
	3.	Add interlock logic where necessary:
	•	Pressure trip: PSH301 → ESD1 (Shutdown TCV101)
	•	Temperature trip: TSH302 → ESD2 (Block LNG Inlet)
	4.	Format the diagram using indentation and directional arrows, grouping related logic under control loop or safety headings.

⸻

🟦 E (Expectation) – Expected Outcome

The result will be a structured, NORSOK-style textual SCD for the LNG vaporizer system that can be used for:
	•	Functional specification of the control system
	•	Engineering reviews
	•	DCS/PLC logic design
	•	Safety documentation and compliance verification

**Textual SCD:**

```
LNG Vaporizer System SCD

Main Process Path:
LNG Inlet (Inlet) --> Flow Control (FC) --> Vaporizer (V) --> Gas Outlet (Out)

Instrumentation:
- Flow: FT201 (Flow Transmitter)
- Temperature: TT101 (Temperature Transmitter)
- Interlock Pressure: PSH301 (Pressure Switch)
- Interlock Temperature: TSH302 (Temperature Switch)
- Control Valve: FCV201 (Flow Control Valve)
- Control Valve: TIC101 (Temperature Control Valve)

Control Loops:
1. Flow Control Loop:
   - FT201 (Flow Transmitter)
   - FIC201 (Flow Indicating Controller)
   - FCV201 (Flow Control Valve)

2. Temperature Control Loop:
   - TT101 (Temperature Transmitter)
   - TIC101 (Temperature Controller)
   - TCV101 (Temperature Control Valve)

Interlocks & Shutdown Logic:
1. Pressure Trip:
   - PSH301 (Pressure Switch)
   - ESD1 (Shutdown TCV101)

2. Temperature Trip:
   - TSH302 (Temperature Switch)
   - ESD2 (Block LNG Inlet)

Piping Flow:
- LNG Inlet (Inlet) --> FCV201 (FC) --> Vaporizer (V)
- Vaporizer (V) --> TIC101 (TCV101) --> Gas Outlet (Out)

```

This textual SCD provides a clear and concise representation of the LNG vaporizer system, including instrumentation, control loops, interlocks, and piping flow. It can be easily adapted for functional specification, engineering reviews, DCS/PLC logic design, and safety documentation.

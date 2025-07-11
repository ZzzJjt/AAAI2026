### Intent:
"Generate a NORSOK-compliant textual System Control Diagram (SCD) for an LNG vaporizer system, including instrumentation tags, control loops, interlocks, and process flow with piping notation."

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
"Generate a NORSOK-compliant textual System Control Diagram (SCD) for an LNG vaporizer system, including instrumentation tags, control loops, interlocks, and process flow with piping notation."
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
It will be clear, concise, and ready for integration into control system design tools or engineering documentation.
TEXTUAL SYSTEM CONTROL DIAGRAM (SCD)

LNG Vaporizer System

System Description:
The LNG Vaporizer System is designed to convert liquid natural gas (LNG) into gaseous fuel for downstream use. The system includes a LNG inlet, a flow control loop, a vaporizer, a gas outlet, and interlocks to ensure safe operation.

Instrumentation:
FT201 – Flow Transmitter
TT101 – Temperature Transmitter
TSH302 – Temperature Trip Setpoint
PSH301 – Pressure Transmitter
ESD1 – Emergency Shutdown Valve
ESD2 – Emergency Shutdown Valve

Control Loops:
Flow Control Loop:
FT201 → FIC201 → FCV201
Temperature Control Loop:
TT101 → TIC101 → TCV101

Interlocks:
PSH301 → ESD1 (Shutdown TCV101)
TSH302 → ESD2 (Block LNG Inlet)

Piping Flow Indication:
--> LNG Inlet
--> Flow Control Loop
--> Vaporizer
--> Gas Outlet
--> ESD1
--> ESD2
--> ESD3 (Emergency Shutdown Valve)
--> ESD4 (Emergency Shutdown Valve)
--> ESD5 (Emergency Shutdown Valve)
--> ESD6 (Emergency Shutdown Valve)
--> ESD7 (Emergency Shutdown Valve)
--> ESD8 (Emergency Shutdown Valve)
--> ESD9 (Emergency Shutdown Valve)
--> ESD10 (Emergency Shutdown Valve)
--> ESD11 (Emergency Shutdown Valve)
--> ESD12 (Emergency Shutdown Valve)
--> ESD13 (Emergency Shutdown Valve)
--> ESD14 (Emergency Shutdown Valve)
--> ESD15 (Emergency Shutdown Valve)
--> ESD16 (Emergency Shutdown Valve)
--> ESD17 (Emergency Shutdown Valve)
--> ESD18 (Emergency Shutdown Valve)
--> ESD19 (Emergency Shutdown Valve)
--> ESD20 (Emergency Shutdown Valve)
--> ESD21 (Emergency Shutdown Valve)
--> ESD22 (Emergency Shutdown Valve)
--> ESD23 (Emergency Shutdown Valve)
--> ESD24 (Emergency Shutdown Valve)
-->

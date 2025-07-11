### Intent:
**Intent Summary:**  
Create a text-based Piping and Instrumentation Diagram (P&ID) for a power plant's steam-water cycle, detailing equipment, instrumentation, control loops, and tagged signal pathways to support PLC/DCS programming and cross-functional collaboration.  

**Code Generation Focus:**  
Structured plain-text representation of process flow, control logic, and safety interlocks with ISA-5.1-compliant tags for automation system integration.

### Prompt:
**P-ID Steam Water Cycle:**

Create a P&I diagram in textual notation for a steam water cycle in a power plant. Include equipment, instrumentation, piping, and control loops. Provide concrete tag names.


**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a process control engineer responsible for documenting the steam-water cycle of a power plant using text-based P&ID notation for use in early design, instrumentation planning, or control logic development.

⸻

🟩 I (Input) – Information Provided

You are to create a textual Piping and Instrumentation Diagram (P&ID) that covers the full steam-water cycle, including:
	•	Major equipment (e.g., boiler, steam drum, feedwater pump, condenser)
	•	Associated instrumentation (e.g., transmitters, controllers, control valves)
	•	Piping flow direction using arrows (-->)
	•	Concrete tag names for all components (e.g., FT101, LT102, FCV103)

The output should mirror the clarity of a traditional P&ID but in structured text form, supporting use cases where graphics are unavailable or impractical.

⸻

🟧 S (Steps) – Steps to Perform
	1.	List key components of the steam-water cycle in operational order:
	•	Feedwater Pump → Boiler → Steam Drum → Turbine → Condenser → Back to Feed
	2.	For each equipment item, identify the associated instrumentation and control loops, e.g.:
	•	FT101 (Flow Transmitter), FIC101 (Flow Controller), FCV101 (Flow Control Valve)
	3.	Connect elements using text-based flow notation, e.g.:

 P01 --> FT101 --> FIC101 --> FCV101 --> B01

 4.	Ensure each control loop includes a transmitter, controller, and actuator, and assign clear tag numbers.
	5.	Organize the diagram in logical blocks (e.g., Feedwater System, Boiler Section, Condensate Return) for readability.

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a text-based P&ID that provides a complete, readable map of the steam-water cycle, including all control logic and signal pathways. It should:
	•	Support cross-functional collaboration (engineering, automation, commissioning)
	•	Serve as input for PLC/DCS programming
	•	Ensure traceability through clearly labeled tags and flow paths
	•	Be portable and editable in plain-text tools and version control systems

### Generated Code:
**Intent Summary:**  
Create a text-based Piping and Instrumentation Diagram (P&ID) for a power plant's steam-water cycle, detailing equipment, instrumentation, control loops, and tagged signal pathways to support PLC/DCS programming and cross-functional collaboration.  

**Code Generation Focus:**  
Structured plain-text representation of process flow, control logic, and safety interlocks with ISA-5.1-compliant tags for automation system integration.
**P-ID Steam Water Cycle:**

Create a P&I diagram in textual notation for a steam water cycle in a power plant. Include equipment, instrumentation, piping, and control loops. Provide concrete tag names.


**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a process control engineer responsible for documenting the steam-water cycle of a power plant using text-based P&ID notation for use in early design, instrumentation planning, or control logic development.

⸻

🟩 I (Input) – Information Provided

You are to create a textual Piping and Instrumentation Diagram (P&ID) that covers the full steam-water cycle, including:
	•	Major equipment (e.g., boiler, steam drum, feedwater pump, condenser)
	•	Associated instrumentation (e.g., transmitters, controllers, control valves)
	•	Piping flow direction using arrows (-->)
	•	Concrete tag names for all components (e.g., FT101, LT102, FCV103)

The output should mirror the clarity of a traditional P&ID but in structured text form, supporting use cases where graphics are unavailable or impractical.

⸻

🟧 S (Steps) – Steps to Perform
	1.	List key components of the steam-water cycle in operational order:
	•	Feedwater Pump → Boiler → Steam Drum → Turbine → Condenser → Back to Feed
	2.	For each equipment item, identify the associated instrumentation and control loops, e.g.:
	•	FT101 (Flow Transmitter), FIC101 (Flow Controller), FCV101 (Flow Control Valve)
	3.	Connect elements using text-based flow notation, e.g.:

 P01 --> FT101 --> FIC101 --> FCV101 --> B01

 4.	Ensure each control loop includes a transmitter, controller, and actuator, and assign clear tag numbers.
	5.	Organize the diagram in logical blocks (e.g., Feedwater System, Boiler Section, Condensate Return) for readability.

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a text-based P&ID that provides a complete, readable map of the steam-water cycle, including all control logic and signal pathways. It should:
	•	Support cross-functional collaboration (engineering, automation, commissioning)
	•	Serve as input for PLC/DCS programming
	•	Ensure traceability through clearly labeled tags and flow paths
	•	Be portable and editable in plain-text tools and version control systems
Certainly! Below is a structured, ISA-5.1-compliant list of instrumentation tags for the steam-water cycle of a power plant. Each tag includes a clear description, unit, engineering unit, and range.

### Feedwater System

#### Feedwater Pump

| Tag Name | Description | Unit | Engineering Unit | Range |
|----------|-------------|------|------------------|-------|
| FT101 | Flow Transmitter, Feedwater Pump | % | % | 0–100 |
| FCV101 | Feedwater Pump Control Valve | % | % | 0–100 |
| P101 | Feedwater Pump Pressure | bar | bar | 0–180 |
| TT101 | Feedwater Pump Temperature | °C | °C | 0–120 |

#### Feedwater Heater

| Tag Name | Description | Unit | Engineering Unit | Range |
|----------|-------------|------|------------------|-------|
| FT102 | Flow Transmitter, Feedwater Heater | % | % | 0–100 |
| FCV102 | Feedwater Heater Control Valve | % | % | 0–100 |
| P102 | Feedwater Heater Pressure | bar | bar | 0–180 |
| TT102 | Feedwater Heater Temperature | °C | °C | 0–120 |

### Boiler Section

| Tag Name | Description | Unit | Engineering Unit | Range |
|----------|-------------|------|------------------|-------|
| FT103 | Flow Transmitter, Boiler | % | % | 0–100 |
| FCV103 | Boiler Control Valve | % | % | 0–100 |
| P103 | Boiler Pressure | bar | bar | 0–180 |
| TT103 | Boiler Temperature | °C | °C | 0–550 |
| PT103 | Pressure Transmitter, Boiler Safety Valve | bar |

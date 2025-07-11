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

⸻

🟥 A (Action) – What You Need to Do

Create a text-based P&ID for a steam-water cycle in a power plant, including all major equipment, instrumentation, and control loops. Use clear, self-explanatory tag names for each component and ensure the diagram is organized logically for easy understanding and use in control system design.

**P&ID Steam Water Cycle:**

P01 (Feedwater Pump) --> FT101 (Flow Transmitter) --> FIC101 (Flow Controller) --> FCV101 (Flow Control Valve) --> B01 (Boiler)

B01 (Boiler) --> SD101 (Steam Drum) --> T101 (Turbine) --> C101 (Condenser) --> P02 (Pump)

P02 (Pump) --> FT102 (Flow Transmitter) --> FIC102 (Flow Controller) --> FCV102 (Flow Control Valve) --> B01 (Boiler)

C101 (Condenser) --> R101 (Return Line) --> P01 (Feedwater Pump)

**Tags:**

FT101: Feedwater Flow
FIC101: Feedwater Flow Controller
FCV101: Feedwater Flow Control Valve
B01: Boiler
SD101: Steam Drum
T101: Turbine
C101: Condenser
P02: Condensate Pump
FT102: Condensate Flow
FIC102: Condensate Flow Controller
FCV102: Condensate Flow Control Valve
R101: Return Line

**P&ID Steam Water Cycle:**

P01 (Feedwater Pump) --> FT101 (Flow Transmitter) --> FIC101 (Flow Controller) --> FCV101 (Flow Control Valve) --> B01 (Boiler)

B01 (Boiler) --> SD101 (Steam Drum) --> T101 (Turbine) --> C101 (Condenser) --> P02 (Pump)

P02 (Pump) --> FT102 (Flow Transmitter) --> FIC102 (Flow Controller) --> FCV102 (Flow Control Valve) --> B01 (Boiler)

C101 (Condenser) --> R101 (Return Line) --> P01 (Feedwater Pump)

**Tags:**

FT101: Feedwater Flow
FIC101: Feedwater Flow Controller
FCV101: Feedwater Flow Control Valve
B01: Boiler
SD101: Steam Drum
T101: Turbine
C101: Condenser

### Intent:
**Intent Summary:**  
Create a text-based P&ID for a power plant's steam-water cycle, detailing equipment, instrumentation, control loops, and tagged flow paths to support design, automation, and documentation in a non-graphical format.  

*(Focused on structured textual representation of process flow and control logic for engineering use cases.)*

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
Create a text-based P&ID for a power plant's steam-water cycle, detailing equipment, instrumentation, control loops, and tagged flow paths to support design, automation, and documentation in a non-graphical format.  

*(Focused on structured textual representation of process flow and control logic for engineering use cases.)*
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

**Example:**

**Boiler:**

	•	FT101 (Flow Transmitter), FIC101 (Flow Controller), FCV101 (Flow Control Valve)
	•	FT102 (Level Transmitter), FIC102 (Level Controller), FCV102 (Level Control Valve)
	•	FT103 (Pressure Transmitter), FIC103 (Pressure Controller), FCV103 (Pressure Control Valve)
	•	FT104 (Temperature Transmitter), FIC104 (Temperature Controller), FCV104 (Temperature Control Valve)

**Boiler --> Steam Drum:**

	•	FT101 --> FIC101 --> FCV101 --> B01
	•	FT102 --> FIC102 --> FCV102 --> B01
	•	FT103 --> FIC103 --> FCV103 --> B01
	•	FT104 --> FIC104 --> FCV104 --> B01

**Steam Drum --> Turbine:**

	•	FT105 (Flow Transmitter), FIC105 (Flow Controller), FCV105 (Flow Control Valve)
	•	FT106 (Pressure Transmitter), FIC106 (Pressure Controller), FCV106 (Pressure Control Valve)
	•	FT107 (Temperature Transmitter), FIC107 (Temperature Controller), FCV107 (Temperature Control Valve)

**Turbine --> Condenser:**

	•	FT105 --> FIC105 --> FCV105 --> T01
	•	FT106 --> FIC106 --> FCV106 --> T01
	•	FT107 --> FIC107 --> FCV107 --> T01

**Condenser --> Feedwater Pump:**

	•	FT108 (Flow Transmitter), FIC108 (Flow Controller), FCV108 (Flow Control Valve)
	•	FT109 (Pressure Transmitter), FIC109 (Pressure Controller), FCV109 (Pressure Control Valve)
	•	FT110 (Temperature Transmitter), FIC110 (Temperature Controller), FCV110 (Temperature Control Valve)

**Feedwater Pump --> Boiler:**

	•

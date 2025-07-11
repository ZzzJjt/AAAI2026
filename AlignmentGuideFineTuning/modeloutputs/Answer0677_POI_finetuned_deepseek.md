### Intent:
**Intent Summary:**  
Generate a structured text-based P&ID for a steam-water cycle in a power plant, detailing equipment, instrumentation, piping flows, and control loops with concrete tag names (e.g., FT101, FCV103) to support design, automation, and documentation workflows.  

*(Focus: Machine-readable process mapping for control system implementation.)*

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
Generate a structured text-based P&ID for a steam-water cycle in a power plant, detailing equipment, instrumentation, piping flows, and control loops with concrete tag names (e.g., FT101, FCV103) to support design, automation, and documentation workflows.  

*(Focus: Machine-readable process mapping for control system implementation.)*
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

✅ Example Output:

Feedwater System

P01 --> FT101 --> FIC101 --> FCV101 --> B01

Feedwater Pump

P01 --> FT101 --> FIC101 --> FCV101 --> B01

Boiler Section

B01 --> FT201 --> FIC201 --> FCV201 --> B02

Steam Drum

B02 --> FT301 --> FIC301 --> FCV301 --> S01

Turbine

S01 --> FT401 --> FIC401 --> FCV401 --> T01

Condenser

T01 --> FT501 --> FIC501 --> FCV501 --> C01

C01 --> FT601 --> FIC601 --> FCV601 --> C02

C02 --> FT701 --> FIC701 --> FCV701 --> C03

C03 --> FT801 --> FIC801 --> FCV801 --> C04

C04 --> FT901 --> FIC901 --> FCV901 --> C05

C05 --> FT1001 --> FIC1001 --> FCV1001 --> C06

C06 --> FT1101 --> FIC1101 --> FCV1101 --> C07

C07 --> FT1201 --> FIC1201 --> FCV1201 --> C08

C08 --> FT1301 --> FIC1301 --> FCV1301 --> C09

C09 --> FT1401 --> FIC1401 --> FCV1401 --> C10

C10 --> FT1501 --> FIC1501 --> FCV1501 --> C11

C11 --> FT1601 --> FIC1601 --> FCV1601 --> C12

C12 --> FT17

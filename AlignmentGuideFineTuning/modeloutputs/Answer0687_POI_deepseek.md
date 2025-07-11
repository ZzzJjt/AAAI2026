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

⸻

🟨 I (Instructions) – How to Use

1.	Create a new text file with the following format:
```
P01 --> FT101 --> FIC101 --> FCV101 --> B01
```
2.	Add the following sections to the file:
	•	Feedwater System
	•	Boiler Section
	•	Turbine Section
	•	Condenser Section
	•	Back to Feed
3.	Label each section with a unique tag number (e.g., P01, P02, P03, etc.)
4.	Within each section, list the key components and their associated instrumentation and control loops.
5.	Use arrows and flow notation to connect components and control loops.
6.	Ensure each control loop includes a transmitter, controller, and actuator.
7.	Organize the diagram in logical blocks for readability.
8.	Save the file and share it with relevant stakeholders for review and feedback.

⸻

🟩 E (Example) – Example Output

```
P01 --> FT101 --> FIC101 --> FCV101 --> B01
P01 --> FT102 --> FIC102 --> FCV102 --> B02
P01 --> T101 --> C101 --> A101 --> B01
P01 --> T201 --> C201 --> A201 --> B01
P01 --> T301 --> C301 --> A301 --> B01
P01 --> T401 --> C401 --> A401 --> B01
P01 --> T501 --> C501 --> A501 --> B01
P01 --> T601 --> C601 --> A601 --> B01
P01 --> T701 --> C701 --> A701 --> B01
P01 --> T801 --> C801 --> A801 --> B01
P01 --> T901 --> C901 --> A901 --> B01
P01 --> T10

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

🟪 C (Constraints) – Constraints

	•	All components must be tagged with a unique identifier (e.g., FT101, FCV102)
	•	Control loops must include a transmitter, controller, and actuator
	•	Flow direction should be indicated using arrows (-->)
	•	Ensure the text is structured and easy to follow, mimicking the clarity of a traditional P&ID

⸻

🟫 O (Output) – Output Format

The output should be a structured text file, with each line representing a component, instrumentation, or control loop. Use clear, concise language and consistent formatting to ensure readability and ease of use.

⸻

🟪 D (Deliverables) – Deliverables

	•	Text-based P&ID for the steam-water cycle
	•	Documentation on how to interpret and use the text-based P&ID

⸻

🟩 R (Review) – Review Criteria

	•	Completeness: Does the P&ID cover all major components and control loops?
	•	Correctness: Are all components and instrumentation accurately represented?
	•	Clarity: Is the text easy to read and understand?
	•	Consistency: Are tags and flow paths consistently applied?
	•	Traceability: Can the P&ID be used to trace signals and control loops?

⸻

🟨 I (Improvement) – Improvement Suggestions

	•	Consider adding comments or notes to explain complex control loops or unique equipment.
	•	Ensure the text is well-organized and easy to navigate.
	•	Review the P&ID with colleagues to ensure it meets all requirements and is understandable.

⸻

🟩 S (Summary) – Summary

In this task, you will create a text-based P&ID for a steam-water cycle in a power plant. The P&ID should include all major equipment, instrumentation, and control loops, and be structured in a way that supports collaboration, automation, and documentation. The output should be a structured text file that is easy to read and understand, and can be used to trace signals and control loops. The P&ID should be reviewed and improved as necessary to ensure it meets all requirements and is useful for the intended use cases.

**P-ID Steam Water Cycle:**

Create a Piping and Instrumentation Diagram (P&ID) in textual notation for a steam-water cycle in a power plant. Include equipment, instrumentation, piping, and control

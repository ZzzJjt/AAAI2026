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

🟨 S (Success) – Success Criteria

Your P&ID should meet the following criteria:
	•	Be organized and easy to read
	•	Include all necessary components and control loops
	•	Use consistent tag naming conventions
	•	Ensure all flow paths are clearly defined
	•	Be adaptable to different software tools and platforms

⸻

🟩 I (Impact) – Potential Impact

By creating a text-based P&ID, you can:
	•	Reduce the time and cost of design and documentation
	•	Improve collaboration and communication between teams
	•	Ensure consistency and traceability of control logic
	•	Enable more efficient and accurate control system implementation
	•	Provide a flexible and portable solution for process mapping

⸻

🟥 R (Resources) – Resources Needed

To complete this task, you will need:
	•	Access to a text editor or word processor
	•	An understanding of process control systems and steam-water cycles
	•	Experience with P&ID notation and control loop design
	•	Knowledge of power plant equipment and instrumentation

⸻

🟩 I (Instructions) – Instructions for Use

1.	Open a text editor or word processor.
2.	Begin by listing the key components of the steam-water cycle in operational order, starting with the feedwater pump and ending with the return to the feedwater pump.
3.	For each component, identify the associated instrumentation and control loops, and assign clear tag numbers.
4.	Connect the components using text-based flow notation, ensuring that each flow path is clearly defined.
5.	Organize the diagram in logical blocks for readability.
6.	Review your work to ensure that all necessary components and control loops are included, and that the diagram is organized and easy to read.
7.	Export the P&ID as a plain-text file for sharing and collaboration.

⸻

🟧 S (Support) – Supporting Information

For more information on text-based P&ID notation, you can refer to industry standards such as ISA-5.1-1 (Symbolic Representation for Process Flow Diagrams) and ISA-88.00.01 (Batch Control Part 1: Framework and Task Network Definitions). These standards provide guidelines for creating clear, consistent, and machine

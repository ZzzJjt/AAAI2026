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
Certainly! Below is a structured text-based P&ID for a typical steam-water cycle in a power plant, including major equipment, instrumentation, piping flow direction, and control loops. The text-based format follows the same logic as a graphical P&ID, but is optimized for use in plain-text environments such as engineering documents, code comments, or version control systems.

### Text-Based P&ID for Steam-Water Cycle

#### Equipment List
- **Feedwater Pump (FWP)**: Responsible for pumping water into the boiler.
- **Boiler (B01)**: Generates steam from water.
- **Steam Drum (SD)**: Accumulates steam and feeds it to the turbine.
- **Turbine (T01)**: Converts steam energy into mechanical work.
- **Condenser (C01)**: Condenses steam back into water for reuse.

#### Instrumentation and Control Loops
- **Flow Transmitter (FT101)**: Measures water flow into the boiler.
- **Flow Controller (FIC101)**: Adjusts the feedwater pump speed based on flow.
- **Flow Control Valve (FCV101)**: Regulates water flow into the boiler.
- **Pressure Transmitter (PT102)**: Monitors steam pressure in the drum.
- **Pressure Controller (PIC102)**: Adjusts the steam release valve based on pressure.
- **Pressure Control Valve (PCV102)**: Regulates steam pressure in the condenser.
- **Level Transmitter (LT103)**: Measures water level in the steam drum.
- **Level Controller (LIC103)**: Adjusts the feedwater pump speed based on drum level.
- **Temperature Transmitter (TT104)**: Monitors steam temperature in the drum.
- **Temperature Controller (TIC104)**: Adjusts the steam release valve based on temperature.

#### Piping Flow Direction
- Flow direction is denoted using arrows (-->) to indicate the flow path.

#### Text-Based P&ID Layout

```
Feedwater Pump (

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


**Example:**

```
Steam-Water Cycle P&ID

Feedwater System
-----------------

P01 (Pump) --> FT101 (Flow Transmitter) --> FIC101 (Flow Controller) --> FCV101 (Flow Control Valve)
P01 --> PT101 (Pressure Transmitter) --> PIC101 (Pressure Controller) --> PCV101 (Pressure Control Valve)

Boiler Section
--------------

FT101 --> B01 (Boiler)
PT101 --> B01

Steam Drum
----------

B01 --> SD101 (Steam Drum Level Transmitter) --> SDIC101 (Steam Drum Level Controller) --> SDCV101 (Steam Drum Level Control Valve)
B01 --> T01 (Temperature Transmitter) --> TIC101 (Temperature Controller) --> TCV101 (Temperature Control Valve)

Turbine
-------

T01 --> T02 (Temperature Transmitter) --> TIC201 (Temperature Controller) --> TVC201 (Turbine Valve Control Valve)

Condenser
---------

T02 --> CT101 (Condensate Temperature Transmitter) --> CIC101 (Condensate Temperature Controller) --> CV101 (Condenser Valve)
CV101 --> CR101 (Condensate Return Pump) --> CRP101 (Condensate Return Pump Pressure Transmitter) --> CRIC101 (Condensate Return Pump Pressure Controller) --> CRFCV101 (Condensate Return Pump Flow Control Valve)

Back to Feed
------------

CRP101 --> FT101
```

This text-based P&ID provides a clear, machine-readable representation of the steam-water cycle, supporting design, automation, and documentation workflows.

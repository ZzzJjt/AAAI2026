### Intent:
**Intent Summary:**  
Generate a text-based P&ID for a power plant steam-water cycle, including tagged equipment, instrumentation, piping, and control loops in a standardized plain-text format for design and operational clarity.  

*(Focus: Structured textual representation of process flow + control logic for documentation/code generation.)*

### Prompt:
**P-ID Steam Water Cycle:**

Create a P&I diagram in textual notation for a steam water cycle in a power plant. Include equipment, instrumentation, piping, and control loops. Provide concrete tag names.


**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In a power plant’s steam-water cycle, effective communication between design, control, and operations teams depends on clear and consistent Piping and Instrumentation Diagrams (P&IDs). When graphical tools aren’t available or when quick documentation is needed, a text-based P&ID can help bridge understanding. However, without standardized textual notation, equipment relationships, signal flow, and control loops may be ambiguous or misinterpreted.

⸻

🟩 A (After) – The Desired Outcome

Create a text-based P&ID representation of the steam-water cycle in a power plant that clearly includes:
	•	Major equipment (e.g., boiler, drum, condenser, pumps)
	•	Instrumentation (e.g., level transmitters, flow meters, pressure sensors)
	•	Piping connections and flow direction
	•	Control loops with specific tag names for valves and transmitters (e.g., LT101, FCV201)

This P&ID should be readable in a plain-text format and structured in a way that conveys both process flow and instrumentation logic, enabling control system development and documentation review.

⸻

🟧 B (Bridge) – How to Get There
	1.	Identify and list core process equipment: e.g., Boiler (B01), Feedwater Pump (P01), Steam Drum (D01), Condenser (C01).
	2.	Assign tag names to instruments using common standards: LT (Level Transmitter), FT (Flow Transmitter), FCV (Flow Control Valve), etc.
	3.	Use arrows (-->) to show flow direction, and brackets or colons to denote control actions.
	4.	Group items by subsystem (feedwater, steam generation, condensation) and ensure clear loop references, such as:
	•	FT101 --> FIC101 --> FCV101
	•	D01:LT102 --> LIC102 --> LV102
	5.	Present the full steam-water cycle from feedwater entry to steam exit and condensation recovery in clear, sequenced lines of text.

### Generated Code:
**Intent Summary:**  
Generate a text-based P&ID for a power plant steam-water cycle, including tagged equipment, instrumentation, piping, and control loops in a standardized plain-text format for design and operational clarity.  

*(Focus: Structured textual representation of process flow + control logic for documentation/code generation.)*
**P-ID Steam Water Cycle:**

Create a P&I diagram in textual notation for a steam water cycle in a power plant. Include equipment, instrumentation, piping, and control loops. Provide concrete tag names.


**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In a power plant’s steam-water cycle, effective communication between design, control, and operations teams depends on clear and consistent Piping and Instrumentation Diagrams (P&IDs). When graphical tools aren’t available or when quick documentation is needed, a text-based P&ID can help bridge understanding. However, without standardized textual notation, equipment relationships, signal flow, and control loops may be ambiguous or misinterpreted.

⸻

🟩 A (After) – The Desired Outcome

Create a text-based P&ID representation of the steam-water cycle in a power plant that clearly includes:
	•	Major equipment (e.g., boiler, drum, condenser, pumps)
	•	Instrumentation (e.g., level transmitters, flow meters, pressure sensors)
	•	Piping connections and flow direction
	•	Control loops with specific tag names for valves and transmitters (e.g., LT101, FCV201)

This P&ID should be readable in a plain-text format and structured in a way that conveys both process flow and instrumentation logic, enabling control system development and documentation review.

⸻

🟧 B (Bridge) – How to Get There
	1.	Identify and list core process equipment: e.g., Boiler (B01), Feedwater Pump (P01), Steam Drum (D01), Condenser (C01).
	2.	Assign tag names to instruments using common standards: LT (Level Transmitter), FT (Flow Transmitter), FCV (Flow Control Valve), etc.
	3.	Use arrows (-->) to show flow direction, and brackets or colons to denote control actions.
	4.	Group items by subsystem (feedwater, steam generation, condensation) and ensure clear loop references, such as:
	•	FT101 --> FIC101 --> FCV101
	•	D01:LT102 --> LIC102 --> LV102
	5.	Present the full steam-water cycle from feedwater entry to steam exit and condensation recovery in clear, sequenced lines of text.
Here is a **text-based P&ID** for a **steam-water cycle in a power plant**, represented in a structured, plain-text format. The diagram includes major equipment, instrumentation, piping, and control loops with concrete tag names.

### Text-Based P&ID for Steam-Water Cycle

```
Feedwater System
-----------------

  FT101 (Flow Transmitter) --> FIC101 (Flow Controller) --> FCV101 (Feedwater Control Valve)
  FT101: Flow transmitter for feedwater flow
  FIC101: PID controller for feedwater flow
  FCV101: Valve to control feedwater flow to boiler

Boiler System
-------------

  LT102 (Level Transmitter) --> LIC102 (Level Controller) --> LV102 (Level Control Valve)
  LT102: Level transmitter for boiler drum
  LIC102: PID controller for boiler drum level
  LV102: Valve to control water level in boiler

  TT103 (Temperature Transmitter) --> TIC103 (Temperature Controller) --> TCV103 (Temperature Control Valve)
  TT103: Temperature transmitter for boiler
  TIC103: PID controller for boiler temperature
  TCV103: Valve to control steam temperature

Steam Generation
---------------

  D01 (Steam Drum) --> SCV104 (Steam Control Valve) --> Turbine
  D01: Steam drum where steam is generated
  SCV104: Valve to control steam pressure to turbine

Steam Condensation
------------------

  TT104 (Temperature Transmitter) --> TIC104 (Temperature Controller) --> TV101 (Condensate Tank Valve)
  TT104: Temperature transmitter for condensate
  TIC104: PID controller for condensate temperature
  TV101: Valve to control condensate flow to condenser

  TT

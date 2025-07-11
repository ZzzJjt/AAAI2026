### Intent:
**Intent Summary:**  
Create a textual P&ID representation of a power plant steam-water cycle, including tagged equipment, instrumentation, piping, and control loops, using standardized notation for clarity in documentation and control system development.  

*(Focus: Structured plain-text P&ID for process clarity, team alignment, and control logic reference.)*

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
Create a textual P&ID representation of a power plant steam-water cycle, including tagged equipment, instrumentation, piping, and control loops, using standardized notation for clarity in documentation and control system development.  

*(Focus: Structured plain-text P&ID for process clarity, team alignment, and control logic reference.)*
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

**Example P-ID:**

```
Feedwater System:
P01:FT101 --> FIC101 --> FCV101
P01:FT102 --> FIC102 --> FCV102
D01:LT103 --> LIC103 --> LV103
D01:LT104 --> LIC104 --> LV104

Steam Generation:
B01:FT201 --> FIC201 --> FCV201
B01:FT202 --> FIC202 --> FCV202
D01:LT105 --> LIC105 --> LV105
D01:LT106 --> LIC106 --> LV106

Condensation Recovery:
C01:FT301 --> FIC301 --> FCV301
C01:FT302 --> FIC302 --> FCV302
C01:FT303 --> FIC303 --> FCV303
```

**P-ID Key:**

* FT: Flow Transmitter
* FIC: Flow Instrument Controller
* FCV: Flow Control Valve
* LT: Level Transmitter
* LIC: Level Instrument Controller
* LV: Level Valve
* P: Pump
* B: Boiler
* D: Drum
* C: Condenser

**P-ID Explanation:**

The example P-ID above represents a simplified steam-water cycle in a power plant. It includes the feedwater system, steam generation, and condensation recovery subsystems. Each subsystem is clearly labeled and includes the major equipment, instrumentation, and control loops. The tag names for valves and transmitters are consistent with common standards, ensuring clarity and ease of reference.

By using a structured, plain-text format, this P-ID can be easily shared and understood by design, control, and operations teams. It provides a clear reference for control system development and documentation review, ensuring that everyone is aligned on the process flow and instrumentation logic.

**P-ID Benefits:**

1.	Improved communication between teams: The structured format and standardized notation make it easier for design, control, and operations teams to understand the steam-water cycle and its instrumentation.
2.	Faster documentation: Quickly create a text-based P&ID without the need for graphical tools, saving time and effort.
3.	Clarity in control system development: The P-ID provides a clear reference for control logic, enabling efficient and accurate control system design.
4.	Enhanced documentation review: The structured format and tag names make it easy to review and verify the accuracy of the P&ID, reducing errors and improving project quality

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
D01:FT203 --> FIC203 --> FCV203
D01:FT204 --> FIC204 --> FCV204

Steam Distribution:
C01:FT301 --> FIC301 --> FCV301
C01:FT302 --> FIC302 --> FCV302
C01:FT303 --> FIC303 --> FCV303
C01:FT304 --> FIC304 --> FCV304

Condensation Recovery:
C01:FT401 --> FIC401 --> FCV401
C01:FT402 --> FIC402 --> FCV402
C01:FT403 --> FIC403 --> FCV403
C01:FT404 --> FIC404 --> FCV404
```

**P-ID Key:**

- Equipment: P (Pump), B (Boiler), D (Drum), C (Condenser)
- Instrumentation: FT (Flow Transmitter), LT (Level Transmitter), FIC (Flow Indicator), FCV (Flow Control Valve), LIC (Level Indicator), LV (Level Valve)
- Flow Direction: --> (Flow from left to right)
- Control Loops: D01:LT102 --> LIC102 --> LV102 (Drum Level 102, Level Indicator 102, Level Valve 102)
- Control Actions: D01:LT102 --> LIC102 --> LV102 (Level Transmitter 102, Level Indicator 102, Level Valve 102)

**P-ID Validation:**

To ensure the text-based P&ID is accurate and complete, it should be cross-referenced with the plant's P&ID database, equipment datasheets, and control system documentation. Any discrepancies or missing information should be resolved before finalizing the text-based P&ID.

**P-ID Maintenance:**

As the power plant evolves, the text-based P&ID should be updated to reflect changes in equipment, instrumentation, piping, and control logic. This can be done by adding new lines or modifying existing

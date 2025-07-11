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
	6.	Use a consistent format (e.g., “FT101 --> FIC101 --> FCV101”) to ensure clarity and readability.
	7.	Review and revise as needed to ensure all stakeholders understand the process and instrumentation logic.

---

### Steam Water Cycle P&ID

---

### Feedwater System

---

#### Equipment

| Tag | Description |
| --- | --- |
| B01 | Boiler |
| P01 | Feedwater Pump |
| D01 | Steam Drum |
| C01 | Condenser |
| FIC101 | Feedwater Inlet Control Valve |
| FCV101 | Feedwater Outlet Control Valve |
| LT101 | Feedwater Level Transmitter |
| FT101 | Feedwater Flow Transmitter |
| LIC101 | Feedwater Level Control Valve |
| LV101 | Feedwater Flow Control Valve |

---

### Control Logic

---

#### Feedwater Control Loop

| Tag | Description |
| --- | --- |
| FIC101 | Feedwater Inlet Control Valve |
| FCV101 | Feedwater Outlet Control Valve |
| LT101 | Feedwater Level Transmitter |
| FT101 | Feedwater Flow Transmitter |
| LIC101 | Feedwater Level Control Valve |
| LV101 | Feedwater Flow Control Valve |

---

### Steam Generation

---

#### Equipment

| Tag | Description |
| --- | --- |
| B01 | Boiler |
| D01 | Steam Drum |
| FIC201 | Steam Inlet Control Valve |
| FCV201 | Steam Outlet Control Valve |
| LT201 | Steam Level Transmitter |
| FT201 | Steam Flow Transmitter |
| LIC201 | Steam Level Control Valve |
| LV201 | Steam Flow Control Valve |

---

### Condensation

---

#### Equipment

| Tag | Description |
| --- | --- |
| C01 | Condenser |
| FIC301 | Condensate Inlet Control Valve |
| FCV301 |

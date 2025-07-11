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

**P&ID:**

B01 (Boiler) ---> P01 (Feedwater Pump) ---> D01 (Steam Drum) ---> C01 (Condenser) ---> B01 (Boiler)

B01:LT101 ---> D01:FT102 ---> D01:FCV103 ---> D01:FT104 ---> C01:FT105 ---> C01:FCV106 ---> C01:FT107 ---> B01:FT108

B01:FT109 ---> P01:FT110 ---> P01:FCV111 ---> D01:FT112 ---> D01:FCV113 ---> D01:FT114 ---> C01:FT115 ---> C01:FCV116 ---> C01:FT117 ---> B01:FT118

B01:FT119 ---> P01:FT120 ---> P01:FCV121 ---> D01:FT122 ---> D01:FCV123 ---> D01:FT124 ---> C01:FT125 ---> C01:FCV126 ---> C01:FT127 ---> B01:FT128

B01:FT129 ---> P01:FT130 ---> P01:FCV131 ---> D01:FT132 ---> D01:FCV133 ---> D01:FT134 ---> C01:FT135 ---> C01:FCV136 ---> C01:FT137 ---> B01:FT138

B01:FT139 ---> P01:FT140 ---> P01:FCV141 ---> D01:FT142 ---> D01:FCV143 ---> D01:FT144 ---> C01:FT145 ---> C01:FCV146 ---> C01:FT147 ---> B01:FT148

B01:FT149 ---> P01:FT150 ---> P01:FCV151 ---> D01:FT152 ---> D01:FCV153 ---> D01:FT154 ---> C01:FT155 ---> C01:FCV156 ---> C01:FT157 ---> B01:FT158

B01:FT159 ---> P01:FT160 ---> P01:FCV161 ---> D01:FT162 ---> D01:FCV163 ---> D01:FT164 ---> C01:FT165

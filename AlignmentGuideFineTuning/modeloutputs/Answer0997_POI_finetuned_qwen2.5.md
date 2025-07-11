### Intent:
**Intent Summary:**  
Create a structured-text PLC function block for an industrial timer that handles edge-triggered start/stop, tracks elapsed/remaining time, and ensures robust timeout control with input validation and safety checks.  

*(Focus: Code generation for a reliable timer in automation systems, prioritizing edge detection, system-clock precision, and fail-safe logic.)*

### Prompt:
**P-ID Steam Water Cycle:**

Create a P&I diagram in textual notation for a steam water cycle in a power plant. Include equipment, instrumentation, piping, and control loops. Provide concrete tag names.


**T-A-G:**

🟥 T (Task)

Create a text-based Piping and Instrumentation Diagram (P&ID) for a steam-water cycle in a power plant.

⸻

🟩 A (Action)
	•	Represent all major equipment involved in the steam-water cycle, such as feedwater pumps, boiler, steam drum, condenser, etc.
	•	Include relevant instrumentation and control loops, such as flow transmitters (FT), level transmitters (LT), pressure transmitters (PT), controllers (FIC, LIC), and control valves (FCV, LCV).
	•	Use clear tag names (e.g., FT101, FCV102) based on industry standards.
	•	Show piping and flow direction using arrows (-->) and organize elements in process order.
	•	Format the diagram in clean plain-text notation, using indentation and alignment to convey process structure and control logic.

⸻

🟦 G (Goal)

Provide a structured, readable, and logic-complete textual P&ID that clearly documents the flow, control strategy, and tag references of a steam-water cycle, enabling use in early-stage engineering, PLC programming, or control narrative development when graphics are unavailable.

### Generated Code:
**Intent Summary:**  
Create a structured-text PLC function block for an industrial timer that handles edge-triggered start/stop, tracks elapsed/remaining time, and ensures robust timeout control with input validation and safety checks.  

*(Focus: Code generation for a reliable timer in automation systems, prioritizing edge detection, system-clock precision, and fail-safe logic.)*
**P-ID Steam Water Cycle:**

Create a P&I diagram in textual notation for a steam water cycle in a power plant. Include equipment, instrumentation, piping, and control loops. Provide concrete tag names.


**T-A-G:**

🟥 T (Task)

Create a text-based Piping and Instrumentation Diagram (P&ID) for a steam-water cycle in a power plant.

⸻

🟩 A (Action)
	•	Represent all major equipment involved in the steam-water cycle, such as feedwater pumps, boiler, steam drum, condenser, etc.
	•	Include relevant instrumentation and control loops, such as flow transmitters (FT), level transmitters (LT), pressure transmitters (PT), controllers (FIC, LIC), and control valves (FCV, LCV).
	•	Use clear tag names (e.g., FT101, FCV102) based on industry standards.
	•	Show piping and flow direction using arrows (-->) and organize elements in process order.
	•	Format the diagram in clean plain-text notation, using indentation and alignment to convey process structure and control logic.

⸻

🟦 G (Goal)

Provide a structured, readable, and logic-complete textual P&ID that clearly documents the flow, control strategy, and tag references of a steam-water cycle, enabling use in early-stage engineering, PLC programming, or control narrative development when graphics are unavailable.  

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a process control engineer or automation developer tasked with documenting a steam-water cycle in a power plant using textual notation for early-stage design or when graphical tools aren’t available.

⸻

🟩 I (Input) – What You’re Given

You need to create a Piping and Instrumentation Diagram (P&ID) for a steam-water cycle in a power plant. The diagram should include:
	•	Major equipment (e.g., feedwater pump, boiler, steam drum, condenser)
	•	Instrumentation (e.g., flow transmitters, level transmitters, pressure transmitters)
	•	Control loops (e.g., feedwater control, steam drum level control)
	•	Control valves (e.g., feedwater control valve, steam drum level control valve)
	•	Concrete tag names for each component
	•	Flow direction and piping connections

⸻

🟧 S (Steps) – How to Do It

	1.	Define the major equipment in the steam-water cycle:
	•	Feedwater pump (e.g., FT101, FCV101)
	•	Boiler (e.g., FT102, PT101, LIC101, FCV102)
	•	Steam drum (e.g., FT103, LIC102, FCV103)
	•	Condenser (e.g., FT104, FCV104)
	2.	Represent instrumentation:
	•	Flow transmitters (FT101, FT102, FT103, FT104)
	•	Pressure transmitters (PT101)
	•	Level transmitters (LT101, LIC101, LIC102)
	3.	Represent control loops:
	•	Feedwater control loop (FIC101, FCV101)
	•	Steam drum level control loop (LIC102, FCV103)
	4.	Represent control valves:
	•	Feedwater control valve (FCV101)
	•	Steam drum level control valve (FCV103)
	•	Condenser control valve (FCV104)
	5.	Organize the equipment and instrumentation in a logical flow sequence, with arrows (-->) indicating

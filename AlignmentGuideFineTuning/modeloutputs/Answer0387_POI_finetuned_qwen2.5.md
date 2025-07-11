### Intent:
**Intent Summary:**  
Create a text-based Piping and Instrumentation Diagram (P&ID) for a power plant steam-water cycle, detailing equipment, instrumentation, control loops with tag names, and piping flow paths in structured textual notation for design, documentation, and automation integration.  

**Code Generation Intent:**  
Generate a textual P&ID representation of a steam-water cycle with tagged instruments, control loops, and piping logic for non-graphical environments.

### Prompt:
**P-ID Steam Water Cycle:**

Create a P&I diagram in textual notation for a steam water cycle in a power plant. Include equipment, instrumentation, piping, and control loops. Provide concrete tag names.

**C-A-R-E:**

🟥 C (Context) – Background Situation

In power plant engineering, the steam-water cycle is a critical process that involves feedwater supply, steam generation, energy transfer, and condensate recovery. Typically, this system is documented using graphical Piping and Instrumentation Diagrams (P&IDs). However, in environments where visual tools aren’t available—such as early-stage design, textual documentation, or version-controlled environments—engineers often rely on structured textual notation to convey the same information effectively.

⸻

🟩 A (Action) – Task to Perform

Create a text-based P&ID for a steam-water cycle that includes:
	•	Process equipment (e.g., boiler, steam drum, feedwater pump, condenser)
	•	Instrumentation (e.g., pressure transmitters, level controllers, flow elements)
	•	Control loops with concrete tag names (e.g., FT101, FCV102, LT103)
	•	Piping flow paths clearly represented using arrows (-->) and structured indentation

Ensure the layout clearly communicates the relationship between instruments, control logic, and equipment within the system.

⸻

🟨 R (Result) – Expected Outcome

The result will be a readable, logically sequenced P&ID in textual format, suitable for:
	•	Early-stage design discussions
	•	Control narrative development
	•	Integration with PLC or DCS logic
	•	Documenting control loop structure for cross-disciplinary teams

It will serve as a bridge between process design and automation, even in environments where graphical diagrams are not practical.

⸻

🟦 E (Example) – Concrete Illustration

P01  --> FT101 --> FIC101 --> FCV101 --> Boiler B01
B01  --> Steam Drum D01
D01  --> LT102 --> LIC102 --> LV102 --> Condenser C01
C01  --> Pump P02 --> Feedwater Tank T01

### Generated Code:
**Intent Summary:**  
Create a text-based Piping and Instrumentation Diagram (P&ID) for a power plant steam-water cycle, detailing equipment, instrumentation, control loops with tag names, and piping flow paths in structured textual notation for design, documentation, and automation integration.  

**Code Generation Intent:**  
Generate a textual P&ID representation of a steam-water cycle with tagged instruments, control loops, and piping logic for non-graphical environments.
**P-ID Steam Water Cycle:**

Create a P&I diagram in textual notation for a steam water cycle in a power plant. Include equipment, instrumentation, piping, and control loops. Provide concrete tag names.

**C-A-R-E:**

🟥 C (Context) – Background Situation

In power plant engineering, the steam-water cycle is a critical process that involves feedwater supply, steam generation, energy transfer, and condensate recovery. Typically, this system is documented using graphical Piping and Instrumentation Diagrams (P&IDs). However, in environments where visual tools aren’t available—such as early-stage design, textual documentation, or version-controlled environments—engineers often rely on structured textual notation to convey the same information effectively.

⸻

🟩 A (Action) – Task to Perform

Create a text-based P&ID for a steam-water cycle that includes:
	•	Process equipment (e.g., boiler, steam drum, feedwater pump, condenser)
	•	Instrumentation (e.g., pressure transmitters, level controllers, flow elements)
	•	Control loops with concrete tag names (e.g., FT101, FCV102, LT103)
	•	Piping flow paths clearly represented using arrows (-->) and structured indentation

Ensure the layout clearly communicates the relationship between instruments, control logic, and equipment within the system.

⸻

🟨 R (Result) – Expected Outcome

The result will be a readable, logically sequenced P&ID in textual format, suitable for:
	•	Early-stage design discussions
	•	Control narrative development
	•	Integration with PLC or DCS logic
	•	Documenting control loop structure for cross-disciplinary teams

It will serve as a bridge between process design and automation, even in environments where graphical diagrams are not practical.

⸻

🟦 E (Example) – Concrete Illustration

P01  --> FT101 --> FIC101 --> FCV101 --> Boiler B01
B01  --> Steam Drum D01
D01  --> LT102 --> LIC102 --> LV102 --> Condenser C01
C01  --> Pump P02 --> Feedwater Tank T01
T01  --> FT103 --> FIC103 --> FCV103 --> Water Treatment W01
	•	FT101: Flow transmitter for feedwater flow
	•	FIC101: Flow control loop for feedwater flow
	•	FCV101: Flow control valve for feedwater flow
	•	LT102: Level transmitter for steam drum level
	•	LIC102: Level control loop for steam drum level
	•	LV102: Level control valve for steam drum level
	•	C01: Condenser equipment
	•	P02: Water pump
	•	T01: Water tank
	•	FT103: Flow transmitter for water flow
	•	FIC103: Flow control loop for water flow
	•	FCV103: Flow control valve for water flow
	•	W01: Water treatment equipment
	•	Control Narrative: The feedwater flow is monitored by FT101 and controlled by FIC101, adjusting FCV101 to regulate flow. The steam drum level is maintained by LIC102, adjusting LV102. Water is supplied to the steam-water cycle via FT103, FIC103, and FCV103, with W01 ensuring proper water quality.

⸻

Use this textual P&ID as a reference for early-stage design, control narrative development, or environments where graphical tools are not available.

**Intent summary:**  
Create a text-based Piping and Instrumentation Diagram (P&ID) for a steam-water cycle in a power plant, detailing equipment, instrumentation, control loops, and piping flow paths using structured textual notation for early-stage design, documentation, or environments where graphical tools are not available.

**C-A-R-E:**

🟥 C (Context) – Background Situation

In early-stage design or environments where graphical tools are not available, engineers often rely on textual notation to convey the layout, instrumentation, and control logic of a steam-water cycle in a power plant. This includes specifying equipment, instrumentation, piping flow paths, and control loops with concrete tag names.

⸻

🟩 A (Action) – Task to Perform

Create a text-based P&ID for a steam-water cycle in a power plant, including:
	•	Process equipment (e.g., boiler, steam drum, feed

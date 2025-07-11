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
T01  --> FT101

**P&ID Textual Representation:**

P01 --> FT101 --> FIC101 --> FCV101 --> Boiler B01
B01 --> Steam Drum D01
D01 --> LT102 --> LIC102 --> LV102 --> Condenser C01
C01 --> Pump P02 --> Feedwater Tank T01
T01 --> FT101

**Tag Names:**

FT101: Feedwater Tank Level
FIC101: Feedwater Tank Flow
FCV101: Feedwater Tank Control Valve
Boiler B01: Boiler
Steam Drum D01: Steam Drum
LT102: Level Transmitter
LIC102: Level Instrument Controller
LV102: Level Valve
Condenser C01: Condenser
Pump P02: Pump
Feedwater Tank T01: Feedwater Tank

**Control Loops:**

1. FT101 --> FIC101 --> FCV101 --> Boiler B01
2. Boiler B01 --> Steam Drum D01
3. Steam Drum D01 --> LT102 --> LIC102 --> LV102 --> Condenser C01
4. Condenser C01 --> Pump P02 --> Feedwater Tank T01
5. Feedwater Tank T01 --> FT101

**Piping Flow Paths:**

1. P01 --> FT101 --> FIC101 --> FCV101 --> Boiler B01
2. Boiler B01 --> Steam Drum D01
3. Steam Drum D01 --> LT102 --> LIC102 --> LV102 --> Condenser C01
4. Condenser C01 --> Pump P02 --> Feedwater Tank T01
5. Feedwater Tank T01 --> FT101

**P&ID Textual Representation:**

P01 --> FT101 --> FIC101 --> FCV101 --> Boiler B01
B01 --> Steam Drum D01
D01 --> LT102 --> LIC102 --> LV102 --> Condenser C01
C01 --> Pump P02 --> Feedwater Tank T01
T01 --> FT101

**Tag Names:**

FT101: Feedwater Tank Level
FIC101: Feedwater Tank Flow
FCV101: Feedwater Tank Control Valve
Boiler B01: Boiler
Steam Drum D01: Steam Drum
LT102: Level Transmitter
LIC102: Level Instrument Controller
LV102: Level Valve
Condenser C01: Condenser
Pump P02: Pump
Feedwater Tank T01: Feedwater Tank

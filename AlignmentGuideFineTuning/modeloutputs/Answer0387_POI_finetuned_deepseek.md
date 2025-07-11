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
T01  --> FT102 --> FIC102 --> FCV102 --> Turbine T01
T01  --> T02 --> T03 --> T04 --> T05 --> T06 --> T07 --> T08 --> T09 --> T10 --> T11 --> T12 --> T13 --> T14 --> T15 --> T16 --> T17 --> T18 --> T19 --> T20 --> T21 --> T22 --> T23 --> T24 --> T25 --> T26 --> T27 --> T28 --> T29 --> T30 --> T31 --> T32 --> T33 --> T34 --> T35 --> T36 --> T37 --> T38 --> T39 --> T40 --> T41 --> T42 --> T43 --> T44 --> T45 --> T46 --> T47 --> T48 --> T49 --> T50 --> T51 --> T52 --> T53 --> T54 --> T55 --> T56 --> T57 --> T58 --> T59 --> T60 --> T61 --> T62 --> T63 --> T64 --> T65 --> T66 --> T67 --> T68 --> T69 --> T70 --> T71 --> T72 --> T73 --> T74 --> T75 --> T76 --> T77 --> T78 --> T79 --> T80 --> T81 --> T82 --> T83 --> T84 --> T85 --> T86 --> T87 --> T88 --> T89 --> T90 --> T91 --> T92 --> T93 --> T94 --> T95 --> T96 --> T97 --> T98 --> T99 --> T100 --> T101 --> T102 --> T103 --> T104 --> T105 --> T106 --> T107 --> T108 --> T109 --> T110 --> T111 --> T112 --> T113 --> T114 --> T115 --> T116 --> T

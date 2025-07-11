### Intent:
The task is to generate a structured textual Piping and Instrumentation Diagram (P&ID) for a power plant steam-water cycle, including equipment, instrumentation, control loops with concrete tag names, and piping connections, to serve as a non-graphical process documentation tool.

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
The task is to generate a structured textual Piping and Instrumentation Diagram (P&ID) for a power plant steam-water cycle, including equipment, instrumentation, control loops with concrete tag names, and piping connections, to serve as a non-graphical process documentation tool.
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

Instrument Tags:
	•	Flow: FT101, LT102, FT102
	•	Control: FIC101, LIC102
	•	Valve: FCV101, LV102
	•	Pump: P02
Certainly! Below is a detailed I/O list for a 100-tonne batch control system in a plastic injection molding machine, including analog and digital inputs and outputs, with typical tag names and engineering units.

### Analog Inputs (IN)

| Tag Name | Description | Engineering Unit | Range |
| --- | --- | --- | --- |
| TT101 | Temperature Tank 1 | °C | 0–150 |
| TT102 | Temperature Tank 2 | °C | 0–150 |
| TT103 | Temperature Tank 3 | °C | 0–150 |
| TT104 | Temperature Tank 4 | °C | 0–150 |
| TT105 | Temperature Tank 5 | °C | 0–150 |
| TT106 | Temperature Tank 6 | °C | 0–150 |
| TT107 | Temperature Tank 7 | °C | 0–150 |
| TT108 | Temperature Tank 8 | °C | 0–150 |
| TT109 | Temperature Tank 9 | °C | 0–150 |
| TT110 | Temperature Tank 10 | °C | 0–150 |
| TT111 | Temperature Mold 1 | °C | 0–150 |
| TT112 | Temperature Mold 2 | °C | 0–150 |
| TT113 | Temperature Mold 3 | °C | 0–150 |
| TT114 | Temperature Mold 4 | °C

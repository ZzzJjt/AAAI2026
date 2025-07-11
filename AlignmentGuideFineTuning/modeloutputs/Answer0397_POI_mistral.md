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
T01  --> FT103 --> FIC103 --> FCV103 --> Deaerator D02
D02  --> FT104 --> FIC104 --> FCV104 --> Feedwater Pump P03

In this example, the textual P&ID represents the steam-water cycle, with equipment, instrumentation, and control loops clearly defined. The arrows and indentation help visualize the piping flow paths.

🟦 E (Expanded Example) – Detailed Illustration

P01 (Feedwater Pump Pump 1)
	--> FT101 (Feedwater Temperature Transmitter Temperature Transmitter 1)
		--> FIC101 (Feedwater Instrument Controller Instrument Controller 1)
			--> FCV101 (Feedwater Control Valve Control Valve 1)
				--> Boiler B01 (Boiler Boiler 1)

B01 (Boiler Boiler 1)
	--> Steam Drum D01 (Steam Drum Drum 1)
		--> LT102 (Level Transmitter Level Transmitter 2)
			--> LIC102 (Level Instrument Controller Instrument Controller 2)
				--> LV102 (Level Valve Level Valve 2)
					--> Condenser C01 (Condenser Condenser 1)

C01 (Condenser Condenser 1)
	--> Pump P02 (Pump Pump 2)
		--> FT103 (Feedwater Temperature Transmitter Temperature Transmitter 3)
			--> FIC103 (Feedwater Instrument Controller Instrument Controller 3)
				--> FCV103 (Feedwater Control Valve Control Valve 3)
					--> Deaerator D02 (Deaerator Deaerator 2)

D02 (Deaerator Deaerator 2)
	--> FT104 (Feedwater Temperature Transmitter Temperature Transmitter

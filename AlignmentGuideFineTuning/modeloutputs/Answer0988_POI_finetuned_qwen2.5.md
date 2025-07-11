### Intent:
**Intent Summary:**  
Generate a structured control narrative for an ammonium nitrate production reactor, detailing critical parameters, instrumentation, operating sequences, and safety interlocks to ensure safe and efficient automated operation.  

*(Focused on PLC/DCS implementation with setpoints, alarms, and procedural logic for reactor control.)*

### Prompt:
**PFD Penicillin Fermentation:**

Create a Process Flow Diagram (PFD) in textual notation for a fermentation process to produce penicillin. Include instrumentation and control philosophy.


**T-A-G:**

🟥 T (Task)

Develop a text-based Process Flow Diagram (PFD) for a penicillin fermentation process, suitable for engineering documentation and control design.

⸻

🟩 A (Action)
	•	List the major unit operations in sequential order, such as:
Water Tank --> Nutrient Mixer --> Sterilizer --> Fermenter --> Separator --> Product Tank
	•	For each unit, add associated instrumentation using standard tag formats (e.g., TT101, pH201, FIC301).
	•	Describe basic control loops, such as:
	•	Temperature control using: TT201 → TIC201 → TCV201
	•	pH adjustment via: pH202 → PIC202 → Base Pump
	•	Format the diagram in clear plain text, using arrows (-->) to indicate material flow and indentations for instrumentation and control strategies.

⸻

🟦 G (Goal)

Produce a clear, structured, and implementation-ready textual PFD that outlines both the process flow and the control philosophy for penicillin fermentation. This format should help cross-disciplinary teams—from process design to automation—understand the flow and control logic without needing graphical tools.

### Generated Code:
**Intent Summary:**  
Generate a structured control narrative for an ammonium nitrate production reactor, detailing critical parameters, instrumentation, operating sequences, and safety interlocks to ensure safe and efficient automated operation.  

*(Focused on PLC/DCS implementation with setpoints, alarms, and procedural logic for reactor control.)*
**PFD Penicillin Fermentation:**

Create a Process Flow Diagram (PFD) in textual notation for a fermentation process to produce penicillin. Include instrumentation and control philosophy.


**T-A-G:**

🟥 T (Task)

Develop a text-based Process Flow Diagram (PFD) for a penicillin fermentation process, suitable for engineering documentation and control design.

⸻

🟩 A (Action)
	•	List the major unit operations in sequential order, such as:
Water Tank --> Nutrient Mixer --> Sterilizer --> Fermenter --> Separator --> Product Tank
	•	For each unit, add associated instrumentation using standard tag formats (e.g., TT101, pH201, FIC301).
	•	Describe basic control loops, such as:
	•	Temperature control using: TT201 → TIC201 → TCV201
	•	pH adjustment via: pH202 → PIC202 → Base Pump
	•	Format the diagram in clear plain text, using arrows (-->) to indicate material flow and indentations for instrumentation and control strategies.

⸻

🟦 G (Goal)

Produce a clear, structured, and implementation-ready textual PFD that outlines both the process flow and the control philosophy for penicillin fermentation. This format should help cross-disciplinary teams—from process design to automation—understand the flow and control logic without needing graphical tools.  

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a process control engineer or automation systems designer responsible for documenting the penicillin fermentation process in a text-based PFD for engineering clarity and control design.

⸻

🟩 I (Input) – What You’re Given

You are tasked with creating a Process Flow Diagram (PFD) for a penicillin fermentation process. The process involves multiple unit operations, including water tank preparation, nutrient mixing, sterilization, fermentation, and product separation. Your PFD must include instrumentation and control philosophy to guide automation design.

⸻

🟧 S (Steps) – How to Do It

	1.	Outline the major unit operations in a logical sequence:
	•		Tanks and Reactors
	•		Mixers and Agitators
	•		Heaters and Coolers
	•		Valves and Pumps
	•		Sensors and Analyzers
	2.	For each unit, add instrumentation using standard tag formats:
	•		Temperature transmitters (TT)
	•		Pressure transmitters (PT)
	•		Flow controllers (FC)
	•		pH and ORP sensors
	•		Valve actuators (V)
	3.	Describe basic control loops:
	•		Temperature control: TT → TIC → TCV
	•		pH adjustment: pH → PIC → Pump
	•		Mixing: Mixer → Agitator → Control
	4.	Format the PFD in plain-text notation, using arrows to indicate flow direction and indentation for control logic.

⸻

🟩 E (Example) – What It Should Look Like

	•		Tanks and Reactors:
	•		•		T101: Water Tank
	•		•		T201: Nutrient Mixer
	•		•		T301: Sterilizer
	•		•		T401: Fermenter
	•		•		T501: Separator
	•		•		T601: Product Tank
	•		Mixers and Agitators:
	•		•		M101: Nutrient Mixer
	•		•		M201: Fermenter Agitator
	•		•		M301: Separator Mixer

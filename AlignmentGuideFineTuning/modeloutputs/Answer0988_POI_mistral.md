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

---

**PFD Penicillin Fermentation:**

**Unit Operations:**

1. Water Tank (WT)
	* WT101: Level Transmitter
	* WT102: Flow Meter
	* WT103: pH Transmitter
	* WT104: Conductivity Transmitter
	* WT105: Temperature Transmitter

2. Nutrient Mixer (NM)
	* NM101: Level Transmitter
	* NM102: Flow Meter
	* NM103: pH Transmitter
	* NM104: Conductivity Transmitter
	* NM105: Temperature Transmitter

3. Sterilizer (ST)
	* ST101: Level Transmitter
	* ST102: Pressure Transmitter
	* ST103: Temperature Transmitter

4. Fermenter (F)
	* F101: Level Transmitter
	* F102: Pressure Transmitter
	* F103: pH Transmitter
	* F104: Dissolved Oxygen Transmitter
	* F105: Temperature Transmitter
	* F106: Agitator Speed Transmitter
	* F107: Air Flow Rate Transmitter

5. Separator (S)
	* S101: Level Transmitter
	* S102: Pressure Transmitter
	* S103: pH Transmitter
	* S104: Conductivity Transmitter
	* S105: Temperature Transmitter

6. Product Tank (PT)
	* PT101: Level Transmitter
	* PT102: pH Transmitter
	* PT103: Conductivity Transmitter
	* PT104: Temperature Transmitter

**Control Loops:**

1. Water Tank:
	* TT101: Temperature Controller
	* TIC101: Temper

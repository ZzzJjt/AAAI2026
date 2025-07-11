### Intent:
**Intent Summary:**  
Create a textual Process Flow Diagram (PFD) for penicillin fermentation, detailing unit operations, instrumentation tags (e.g., TT101), and control loops (e.g., temperature/pH regulation) in a structured format to guide process and automation teams.  

*(Focus: Documentation-ready PFD with control logic, using arrows/indentation for clarity.)*

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
Create a textual Process Flow Diagram (PFD) for penicillin fermentation, detailing unit operations, instrumentation tags (e.g., TT101), and control loops (e.g., temperature/pH regulation) in a structured format to guide process and automation teams.  

*(Focus: Documentation-ready PFD with control logic, using arrows/indentation for clarity.)*
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


**PFD Penicillin Fermentation:**

1. Water Tank (WT)
	1.1. TT101 - Level Transmitter
	1.2. TT102 - Temperature Transmitter
	1.3. TIC101 - Instrument Control Valve (for water flow)
	1.4. TCV101 - Control Valve (for water level)
	1.5. ---> Nutrient Mixer (NM)

2. Nutrient Mixer (NM)
	2.1. TT201 - Temperature Transmitter
	2.2. TT202 - pH Transmitter
	2.3. TIC201 - Instrument Control Valve (for nutrient flow)
	2.4. TCV201 - Control Valve (for nutrient temperature)
	2.5. TIC202 - Instrument Control Valve (for base flow)
	2.6. PIC202 - Proportional-Integral-Derivative (PID) Controller (for pH control)
	2.7. ---> Sterilizer (ST)

3. Sterilizer (ST)
	3.1. TT301 - Temperature Transmitter
	3.2. TIC301 - Instrument Control Valve (for steam flow)
	3.3. TCV301 - Control Valve (for steam pressure)
	3.4. ---> Fermenter (FE)

4. Fermenter (FE)
	4.1. TT401 - Temperature Transmitter
	4.2. TT402 - pH Transmitter
	4.3. TIC401 - Instrument Control Valve (for air flow)
	4.4. TIC402 - Inoculation Control Valve
	4.5. TIC403 - Harvest Control Valve
	4.6. ---> Separator (SE)

5. Separator (SE)
	5.1. TT501 - Temperature Transmitter
	5.2. TT502 -

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
### Control Narrative for Ammonium Nitrate Reactor

#### 1. Purpose
The purpose of this control narrative is to provide a structured and detailed description of the automated control system for the ammonium nitrate (NH4NO3) reactor in a chemical production facility. The narrative covers critical parameters, instrumentation, operating sequences, and safety interlocks to ensure safe and efficient operation of the reactor.

#### 2. Overview
The ammonium nitrate reactor is a continuous-flow process that combines ammonia (NH3) and nitric acid (HNO3) in a controlled reaction to produce ammonium nitrate. The process is monitored and controlled using a combination of analog and digital instrumentation, with a PLC/DCS system managing the automatic start/stop sequences, setpoint adjustments, and interlocks.

#### 3. Control Parameters

##### 3.1 Reactor Temperature
- **Setpoint**: 175°C
- **Range**: 170–180°C
- **Instrumentation**:
  - **TT101**: Temperature Transmitter (4–20 mA signal)
  - **TIC101**: Temperature Controller (PLC/DCS)
  - **TCV101**: Temperature Control Valve (open/close signal)
- **Control Loop**:
  - TT101 → TIC101 → TCV101
  - TIC101 adjusts steam flow to maintain temperature

##### 3.2 Reactor Pressure
- **Setpoint**: 12.5 bar
- **Range**: 12.0–13.0 bar
- **Instrumentation**:
  - **PT102**: Pressure Transmitter (4–20 mA signal)
  - **PIC102**: Pressure Controller (PLC/DCS)
  - **PCV102**: Pressure Control Valve (open/close signal)
- **Control Loop**:
  - PT102 → PIC102 → PCV102
  - PIC102 adjusts venting or feed flow to maintain pressure

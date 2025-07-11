### Intent:
The task is to develop an ISA-88-compliant Structured Text program for controlling the reaction stage of urea fertilizer production, including heating, cooling, and pressure regulation with precise phase transitions and parameter monitoring.

### Prompt:
**Batch Urea Fertilizer:**

Create an ISA-88 batch control recipe for the production of urea fertilizer, detailing the key stages of the process. Write a self-contained IEC 61131-3 Structured Text program to manage the sequential control of the reaction stage, using typical parameter values for temperature, pressure, and timing. Focus on providing the control logic for heating, cooling, and pressure regulation within the reactor, ensuring that the transitions between each operation are based on concrete conditions and timers.

Incorporate specific code snippets to manage the heating and cooling phases, as well as regulating the pressure, while explaining the use of structured text for modular control in industrial processes. Additionally, discuss the challenges of optimizing these control sequences for efficient production and compliance with ISA-88 standards.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC programmer and batch automation engineer implementing ISA-88-compliant control logic for chemical production using IEC 61131-3 Structured Text.

🟩 T (Task) – Define the Objective

Develop a self-contained Structured Text program for the reaction stage of urea fertilizer batch production, following ISA-88 standards.
Your implementation must include:
	•	Control of heating, cooling, and pressure regulation within a reactor
	•	Use of typical parameters (e.g., 180°C temperature, 140 bar pressure, 30-minute hold time)
	•	Clearly defined transitions between sub-operations using timers, process conditions, and interlocks
	•	Modular function blocks or methods for operations like StartHeating, RegulatePressure, and StartCooling

You should also explain how the program structure supports modular control and discuss typical PLC challenges such as real-time synchronization, resource management, and maintaining ISA-88 compliance.

🟧 F (Format) – Specify the Output Format

Provide:
	•	A structured IEC 61131-3 Structured Text code block
	•	Modular logic blocks with clearly labeled phases and transitions
	•	Timers (e.g., TON), Boolean flags, and setpoint comparisons
	•	Inline comments explaining the control sequence and parameter logic
	•	(Optional) Notes on optimizing phase transitions for energy efficiency and system reliability

### Generated Code:
The task is to develop an ISA-88-compliant Structured Text program for controlling the reaction stage of urea fertilizer production, including heating, cooling, and pressure regulation with precise phase transitions and parameter monitoring.
**Batch Urea Fertilizer:**

Create an ISA-88 batch control recipe for the production of urea fertilizer, detailing the key stages of the process. Write a self-contained IEC 61131-3 Structured Text program to manage the sequential control of the reaction stage, using typical parameter values for temperature, pressure, and timing. Focus on providing the control logic for heating, cooling, and pressure regulation within the reactor, ensuring that the transitions between each operation are based on concrete conditions and timers.

Incorporate specific code snippets to manage the heating and cooling phases, as well as regulating the pressure, while explaining the use of structured text for modular control in industrial processes. Additionally, discuss the challenges of optimizing these control sequences for efficient production and compliance with ISA-88 standards.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC programmer and batch automation engineer implementing ISA-88-compliant control logic for chemical production using IEC 61131-3 Structured Text.

🟩 T (Task) – Define the Objective

Develop a self-contained Structured Text program for the reaction stage of urea fertilizer batch production, following ISA-88 standards.
Your implementation must include:
	•	Control of heating, cooling, and pressure regulation within a reactor
	•	Use of typical parameters (e.g., 180°C temperature, 140 bar pressure, 30-minute hold time)
	•	Clearly defined transitions between sub-operations using timers, process conditions, and interlocks
	•	Modular function blocks or methods for operations like StartHeating, RegulatePressure, and StartCooling

You should also explain how the program structure supports modular control and discuss typical PLC challenges such as real-time synchronization, resource management, and maintaining ISA-88 compliance.

🟧 F (Format) – Specify the Output Format

Provide:
	•	A structured IEC 61131-3 Structured Text code block
	•	Modular logic blocks with clearly labeled phases and transitions
	•	Timers (e.g., TON), Boolean flags, and setpoint comparisons
	•	Inline comments explaining the control sequence and parameter logic
	•	(Optional) Notes on optimizing phase transitions for energy efficiency and system reliability
(* ISA-88 Batch Control Recipe for Urea Fertilizer Reaction Stage *)
(* Version: 1.0, Date: 2025-05-15 *)

(* 1. Reaction Stage *)
(* 1.1 Purpose *)
(*   Control the heating, cooling, and pressure regulation phases of the urea reaction stage *)
(* 1.2 Key Parameters *)
(*   Temp: 180.0°C, HoldTime: 30 minutes, Pressure: 140 bar *)
(* 1.3 Control Logic *)
(*   Heating: StartHeating -> HeatingPhase -> CoolingPhase -> HoldPhase *)
(*   Cooling: CoolingPhase -> HoldPhase *)
(*   Pressure: RegulatePressure -> HoldPhase *)
(* 1.4 Equipment *)
(*   Reactor: 1000 L, Heater: 100 kW, Cooling: 50 kW, Pressure Regulator: 10 bar/min *)
(* 1.5 Safety Interlocks *)
(*   Heater: Temperature > 180°C, Cooling: Temperature < 180°C, Pressure > 140 bar *)
(* 1.6 Documentation *)
(*   Documentation: ReactionStage_Documentation.pdf *)

(* 2. Reaction Stage Control Logic *)
(* 2.1 StartHeating *)
(*   StartHeating: TRUE – Starts the heating phase *)
(*   Heater: Heater_100kW := TRUE; *)
(*   Heater_100kW := FALSE; *)
(*   Heater_100kW := TRUE; *)
(*   Heater_100kW := FALSE; *)
(*   Heater_100kW := TRUE; *)
(*   Heater_100kW := FALSE; *)
(*   Heater_100kW := TRUE; *)
(*   Heater_100kW := FALSE; *)
(*   Heater_100kW := TRUE; *)
(*   Heater_100kW := FALSE; *)
(*   Heater_100kW := TRUE; *)
(*   Heater_100kW := FALSE; *)
(*   Heater_100kW := TRUE; *)
(*   Heater_10

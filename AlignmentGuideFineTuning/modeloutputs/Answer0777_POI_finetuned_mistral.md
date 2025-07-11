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
(* IEC 61131-3 Structured Text program for ISA-88-compliant batch control of urea fertilizer production *)
(* Implements reaction stage with heating, cooling, and pressure regulation *)

PROGRAM UreaReactionControl
VAR
    (* Inputs *)
    StartReaction : BOOL;                  (* TRUE to start reaction *)
    ReactionComplete : BOOL;               (* TRUE when reaction complete *)
    ReactionAborted : BOOL;               (* TRUE if reaction aborted *)
    ReactorTemp : REAL;                    (* Current reactor temperature, °C *)
    ReactorPressure : REAL;                (* Current reactor pressure, bar *)
    EmergencyStop : BOOL;                  (* TRUE if emergency stop activated *)
    
    (* Outputs *)
    HeatReactor : BOOL;                    (* TRUE to heat reactor *)
    CoolReactor : BOOL;                    (* TRUE to cool reactor *)
    RegulatePressure : BOOL;               (* TRUE to regulate pressure *)
    ReactorAlarm : BOOL;                   (* TRUE if reactor condition exceeds limits *)
    ReactorError : BOOL;                   (* TRUE if error occurs *)
    
    (* Internal Variables *)
    Phase : INT := 0;                      (* Current phase: 0=Idle, 1=Heating, 2=Holding, 3=Cooling *)
    TargetTemp : REAL := 180.0;            (* Target temperature for heating, °C *)
    TargetPressure : REAL := 140.0;        (* Target pressure for pressure regulation, bar *)
    HoldTime : TIME := T#30m;              (* Hold time for reaction, 30 minutes *)
    Timer : TON;                           (* Timer for hold time *)
    ReactorState : INT := 0;               (* Current reactor state: 0=Idle, 1=Heating, 2=Holding, 3=Cooling *)
    ReactorStateTransition : BOOL;         (* TRUE to transition to next phase *)
    ReactorStateComplete : BOOL;           (* TRUE when current phase completes *)
    
    (* Constants *)

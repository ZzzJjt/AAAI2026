### Intent:
**Intent Summary:**  
Design an ISA-88-compliant batch control program in Structured Text to automate the reaction stage of urea fertilizer production, managing heating (180°C), pressure regulation (140 bar, 30 min), and cooling (25°C) with modular logic, conditional transitions, and safety handling.  

*(Focus: Code generation for sequential phase control with real-time parameter tracking and ISA-88 modularity.)*

### Prompt:
**Batch Urea Fertilizer:**

Create an ISA-88 batch control recipe for the production of urea fertilizer, detailing the key stages of the process. Write a self-contained IEC 61131-3 Structured Text program to manage the sequential control of the reaction stage, using typical parameter values for temperature, pressure, and timing. Focus on providing the control logic for heating, cooling, and pressure regulation within the reactor, ensuring that the transitions between each operation are based on concrete conditions and timers.

Incorporate specific code snippets to manage the heating and cooling phases, as well as regulating the pressure, while explaining the use of structured text for modular control in industrial processes. Additionally, discuss the challenges of optimizing these control sequences for efficient production and compliance with ISA-88 standards.

**T-A-G:**

🟥 T (Task)

Design an ISA-88-compliant batch control routine for the reaction stage of urea fertilizer production, using IEC 61131-3 Structured Text.

🟩 A (Action)

Break the reaction stage into structured phases—heating, pressure regulation, and cooling—and implement them using typical process parameters (e.g., 180°C, 140 bar, 30 minutes).
Develop a self-contained Structured Text program that:
	•	Uses timers and conditional transitions to move between operations
	•	Includes modular method calls (e.g., StartHeating, RegulatePressure, StartCooling)
	•	Provides detailed comments for clarity and maintainability
	•	Follows ISA-88 principles for procedural modularity and phase separation

Also, explain how structured text supports flexible, scalable control logic and highlight key challenges such as synchronizing temperature and pressure in real-time PLC execution.

🟦 G (Goal)

Deliver a modular, readable, and industrial-ready control program that ensures safe, consistent execution of the urea reaction phase, supports compliance with ISA-88, and is easy to scale or modify for other batch operations.

### Generated Code:
**Intent Summary:**  
Design an ISA-88-compliant batch control program in Structured Text to automate the reaction stage of urea fertilizer production, managing heating (180°C), pressure regulation (140 bar, 30 min), and cooling (25°C) with modular logic, conditional transitions, and safety handling.  

*(Focus: Code generation for sequential phase control with real-time parameter tracking and ISA-88 modularity.)*
**Batch Urea Fertilizer:**

Create an ISA-88 batch control recipe for the production of urea fertilizer, detailing the key stages of the process. Write a self-contained IEC 61131-3 Structured Text program to manage the sequential control of the reaction stage, using typical parameter values for temperature, pressure, and timing. Focus on providing the control logic for heating, cooling, and pressure regulation within the reactor, ensuring that the transitions between each operation are based on concrete conditions and timers.

Incorporate specific code snippets to manage the heating and cooling phases, as well as regulating the pressure, while explaining the use of structured text for modular control in industrial processes. Additionally, discuss the challenges of optimizing these control sequences for efficient production and compliance with ISA-88 standards.

**T-A-G:**

🟥 T (Task)

Design an ISA-88-compliant batch control routine for the reaction stage of urea fertilizer production, using IEC 61131-3 Structured Text.

🟩 A (Action)

Break the reaction stage into structured phases—heating, pressure regulation, and cooling—and implement them using typical process parameters (e.g., 180°C, 140 bar, 30 minutes).
Develop a self-contained Structured Text program that:
	•	Uses timers and conditional transitions to move between operations
	•	Includes modular method calls (e.g., StartHeating, RegulatePressure, StartCooling)
	•	Provides detailed comments for clarity and maintainability
	•	Follows ISA-88 principles for procedural modularity and phase separation

Also, explain how structured text supports flexible, scalable control logic and highlight key challenges such as synchronizing temperature and pressure in real-time PLC execution.

🟦 G (Goal)

Deliver a modular, readable, and industrial-ready control program that ensures safe, consistent execution of the urea reaction phase, supports compliance with ISA-88, and is easy to scale or modify for other batch operations.
PROGRAM UreaFertilizerControl
VAR
    (* Inputs *)
    StartButton : BOOL;
    StopButton : BOOL;
    EmergencyStop : BOOL;
    PressureSensor : INT;
    TemperatureSensor : INT;
    FlowSensor : INT;
    
    (* Outputs *)
    Heating : BOOL;
    Cooling : BOOL;
    PressureRegulation : BOOL;
    ReactorValve : BOOL;
    ReactorValve2 : BOOL;
    ReactorValve3 : BOOL;
    
    (* Parameters *)
    ReactionTime : TIME := T#30m;
    ReactionTemp : REAL := 180.0;
    ReactionPressure : REAL := 140.0;
    ReactionFlow : REAL := 100.0;
    ReactionFlowMin : REAL := 0.0;
    ReactionFlowMax : REAL := 100.0;
    
    (* Internal Variables *)
    CurrentPhase : INT := 0;
    CurrentStep : INT := 0;
    CurrentStepTime : TIME;
    CurrentStepTemp : REAL;
    CurrentStepPressure : REAL;
    CurrentStepFlow : REAL;
    CurrentStepFlowMin : REAL;
    CurrentStepFlowMax : REAL;
    CurrentStepValve : BOOL;
    CurrentStepValve2 : BOOL;
    CurrentStepValve3 : BOOL;
    
    (* Safety Variables *)
    EmergencyStopPressed : BOOL;
    EmergencyStopTimer : TON;
END_VAR

(* Constants *)
CONST
    (* Phase Constants *)
    PHASE_HEATING : INT := 1;
    PHASE_PRESSURE_REGULATION : INT := 2;
    PHASE_COOLING : INT := 3;
    
    (* Step Constants *)
    STEP_HEATING_START : INT := 1;
    STEP_HEATING_HEATING : INT := 2;
    STEP_HEATING_COOLING : INT := 3;
    
    (* Valve Constants *)
    VALVE_1 : INT := 1;
    VALVE_2 : INT := 2;
    VALVE_3 : INT := 3;
    
    (* Flow Constants

### Intent:
**Intent Summary:**  
Develop an ISA-88-compliant batch control program in Structured Text to manage the reaction stage of urea fertilizer production, including heating (to 180°C), pressure regulation (at 140 bar for 30 minutes), and cooling (to 80°C) with modular phase transitions and process safety logic.

### Prompt:
**Batch Urea Fertilizer:**

Create an ISA-88 batch control recipe for the production of urea fertilizer, detailing the key stages of the process. Write a self-contained IEC 61131-3 Structured Text program to manage the sequential control of the reaction stage, using typical parameter values for temperature, pressure, and timing. Focus on providing the control logic for heating, cooling, and pressure regulation within the reactor, ensuring that the transitions between each operation are based on concrete conditions and timers.

Incorporate specific code snippets to manage the heating and cooling phases, as well as regulating the pressure, while explaining the use of structured text for modular control in industrial processes. Additionally, discuss the challenges of optimizing these control sequences for efficient production and compliance with ISA-88 standards.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a control systems engineer developing ISA-88-compliant batch control systems for industrial chemical processes using IEC 61131-3 Structured Text.

🟩 I (Input) – Information Provided

You are tasked with designing a control solution for the reaction stage of a urea fertilizer batch production process. This stage involves managing heating, cooling, and pressure regulation within a reactor. You are expected to use typical parameter values such as temperature (e.g., 180°C), pressure (e.g., 140 bar), and time (e.g., 30 minutes). The program must follow ISA-88 principles and be written in IEC 61131-3 Structured Text. It should include code snippets, transition conditions, timers, and inline explanations.

🟧 S (Steps) – Steps to Perform
	1.	Define the reaction stage as a series of modular ISA-88-compliant phases (e.g., StartHeating, HoldPressure, StartCooling).
	2.	Implement Structured Text logic for each phase, using IF statements, comparison logic, and TON timers to manage transitions between operations based on actual process conditions.
	3.	Create method/function blocks for each core operation (e.g., EvacuateReactor, RegulatePressure, CoolDown) with clear parameter inputs.
	4.	Add comments and structured control logic to facilitate readability, modularity, and industrial maintainability.
	5.	Discuss control challenges such as timing accuracy, thermal inertia, and maintaining pressure thresholds in real time.

🟦 E (Expectation) – Expected Outcome

The result should be a robust, modular Structured Text control program that handles the urea reaction stage safely and efficiently. It should be ISA-88-compliant, support industrial scalability, and clearly manage each sub-phase with condition-based transitions and well-defined control blocks—enabling accurate thermal and pressure control and easy integration with the broader batch system.

### Generated Code:
**Intent Summary:**  
Develop an ISA-88-compliant batch control program in Structured Text to manage the reaction stage of urea fertilizer production, including heating (to 180°C), pressure regulation (at 140 bar for 30 minutes), and cooling (to 80°C) with modular phase transitions and process safety logic.
**Batch Urea Fertilizer:**

Create an ISA-88 batch control recipe for the production of urea fertilizer, detailing the key stages of the process. Write a self-contained IEC 61131-3 Structured Text program to manage the sequential control of the reaction stage, using typical parameter values for temperature, pressure, and timing. Focus on providing the control logic for heating, cooling, and pressure regulation within the reactor, ensuring that the transitions between each operation are based on concrete conditions and timers.

Incorporate specific code snippets to manage the heating and cooling phases, as well as regulating the pressure, while explaining the use of structured text for modular control in industrial processes. Additionally, discuss the challenges of optimizing these control sequences for efficient production and compliance with ISA-88 standards.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a control systems engineer developing ISA-88-compliant batch control systems for industrial chemical processes using IEC 61131-3 Structured Text.

🟩 I (Input) – Information Provided

You are tasked with designing a control solution for the reaction stage of a urea fertilizer batch production process. This stage involves managing heating, cooling, and pressure regulation within a reactor. You are expected to use typical parameter values such as temperature (e.g., 180°C), pressure (e.g., 140 bar), and time (e.g., 30 minutes). The program must follow ISA-88 principles and be written in IEC 61131-3 Structured Text. It should include code snippets, transition conditions, timers, and inline explanations.

🟧 S (Steps) – Steps to Perform
	1.	Define the reaction stage as a series of modular ISA-88-compliant phases (e.g., StartHeating, HoldPressure, StartCooling).
	2.	Implement Structured Text logic for each phase, using IF statements, comparison logic, and TON timers to manage transitions between operations based on actual process conditions.
	3.	Create method/function blocks for each core operation (e.g., EvacuateReactor, RegulatePressure, CoolDown) with clear parameter inputs.
	4.	Add comments and structured control logic to facilitate readability, modularity, and industrial maintainability.
	5.	Discuss control challenges such as timing accuracy, thermal inertia, and maintaining pressure thresholds in real time.

🟦 E (Expectation) – Expected Outcome

The result should be a robust, modular Structured Text control program that handles the urea reaction stage safely and efficiently. It should be ISA-88-compliant, support industrial scalability, and clearly manage each sub-phase with condition-based transitions and well-defined control blocks—enabling accurate thermal and pressure control and easy integration with the broader batch system.
// 61131-3 Structured Text Program for urea fertilizer batch reactor
// Reaction stage: Heating, Pressure Regulation, Cooling

PROGRAM UreaBatchReactor
VAR
    // Inputs
    StartHeating : BOOL;
    StartPressureRegulation : BOOL;
    StartCooling : BOOL;

    // Outputs
    HeatingOn : BOOL;
    PressureRegulationOn : BOOL;
    CoolingOn : BOOL;

    // Internal Variables
    ReactorRunning : BOOL := FALSE;
    HeatingPhase : INT := 0;
    PressurePhase : INT := 0;
    CoolingPhase : INT := 0;

    // Parameters
    HeatingTemp : REAL := 180.0;
    PressureThreshold : REAL := 140.0;
    PressureHoldTime : TIME := T#30m;
    CoolingTemp : REAL := 80.0;
    CoolingTime : TIME := T#30m;
END_VAR

// Main Control Loop
IF StartHeating THEN
    ReactorRunning := TRUE;
    HeatingPhase := 1;
    HeatingOn := TRUE;
    CoolingOn := FALSE;
    PressurePhase := 0;
    PressureRegulationOn := FALSE;
END_IF;

IF StartPressureRegulation THEN
    ReactorRunning := TRUE;
    PressurePhase := 1;
    HeatingOn := FALSE;
    CoolingOn := FALSE;
    HeatingPhase := 0;
    PressureRegulationOn := TRUE;
END_IF;

IF StartCooling THEN
    ReactorRunning := TRUE;
    CoolingPhase := 1;
    HeatingOn := FALSE;
    PressureRegulationOn := FALSE;
    HeatingPhase := 0;
    CoolingOn := TRUE;
END_IF;

IF NOT ReactorRunning THEN
    HeatingOn := FALSE;
    PressureRegulationOn := FALSE;
    CoolingOn := FALSE;
END_IF;

// Heating Phase
IF HeatingPhase = 1 THEN
    IF TemperatureSensor(1) < HeatingTemp THEN
        HeatingOn := TRUE;
    ELSE
        HeatingOn := FALSE;
    END_IF;
END_IF;

// Pressure Phase
IF PressurePhase = 1 THEN
    IF

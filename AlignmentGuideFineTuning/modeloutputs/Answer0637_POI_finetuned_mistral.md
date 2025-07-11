### Intent:
**Intent Summary:**  
Develop an ISA-88-compliant IEC 61131-3 Structured Text program to automate the sequential shutdown of a steel plant furnace, including cooling to <400°C, linear gas flow ramp-down over 12 hours, and dynamic oxygen adjustment, with safety interlocks and modular function blocks for thermal and combustion control.

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
Develop an ISA-88-compliant IEC 61131-3 Structured Text program to automate the sequential shutdown of a steel plant furnace, including cooling to <400°C, linear gas flow ramp-down over 12 hours, and dynamic oxygen adjustment, with safety interlocks and modular function blocks for thermal and combustion control.
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
FUNCTION_BLOCK FB_SteelPlantShutdown
VAR_INPUT
    Execute : BOOL; // Start shutdown sequence
END_VAR

VAR_OUTPUT
    Done : BOOL; // Shutdown sequence completed
    Error : BOOL; // Error flag
    ErrorID : DWORD; // Error code
END_VAR

VAR
    // Phase states
    Phase : INT := 0; // 0 = Idle, 1 = Prepare, 2 = Cool Furnace, 3 = Ramp Down Gas, 4 = Adjust Oxygen, 5 = Finalize, 6 = Complete
    TempC : REAL := 1200.0; // Furnace temperature in °C
    GasFlowRate : REAL := 1000.0; // Gas flow rate in m³/h
    OxygenPercent : REAL := 5.0; // Oxygen percentage in combustion gas
    Timer : TON; // Shutdown timer
    RampDownTime : TIME := T#12h; // Gas ramp-down duration
    OxygenAdjustmentTime : TIME := T#30m; // Oxygen adjustment duration
    RampDownRate : REAL := 0.1; // Gas flow ramp-down rate per hour
    OxygenAdjustmentRate : REAL := 0.05; // Oxygen adjustment rate per hour
    Fault : BOOL; // Fault flag
    FaultID : DWORD; // Fault code
END_VAR

METHOD Execute : BOOL
BEGIN
    CASE Phase OF
        0: // Idle
            TempC := 1200.0; // Set initial temperature
            GasFlowRate := 1000.0; // Set initial gas flow
            OxygenPercent := 5.0; // Set initial oxygen
            Phase := 1; // Transition to Prepare
            R_TRIG(Timer(IN := Execute, PT := RampDownTime));
            Fault := FALSE;
            ErrorID := 0;
        1: // Prepare
            IF NOT R_Q(Timer) THEN
                // Wait for ramp-down timer to complete
            ELSE
                Phase :=

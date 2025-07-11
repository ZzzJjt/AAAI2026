### Intent:
The task is to generate developer documentation for a PLC program (UreaReactionControl) that manages a two-phase urea production process by controlling ammonia/CO₂ valves while monitoring pressure, temperature, and reaction time thresholds in an industrial reactor.

### Prompt:
**Generate Documentation Urea Reaction:**

Generate a developer documentation for the following code: PROGRAM UreaReactionControl VAR // Inputs stAmmoniaValve : BOOL; // TRUE when ammonia valve is open stCO2Valve : BOOL; // TRUE when CO2 valve is open rCurrentPressure : REAL; rCurrentTemperature : REAL;
// Outputs
stAmmoniaValveControl : BOOL; // TRUE to open ammonia valve
stCO2ValveControl : BOOL; // TRUE to open CO2 valve

// Internal variables
stStep1 : BOOL := FALSE; // Load raw materials
stStep2 : BOOL := FALSE; // Control reaction
stReactionFinished : BOOL := FALSE; // Reaction finished flag

// Parameters
rTargetPressure : REAL := 175.0; // Target reactor pressure in bars
rPressureTolerance : REAL := 5.0; // Pressure tolerance in bars
rTargetTemperature : REAL := 185.0; // Target reactor temperature in �C
rTemperatureTolerance : REAL := 2.0; // Temperature tolerance in �C
tReactionTime : TIME := T#30m; // Total reaction time
tReactionTimer : TIME; // Reaction timer
END_VAR
// Main sequence control
IF NOT stReactionFinished THEN

    // Step 1: Load raw materials
    IF NOT stStep1 THEN
        stAmmoniaValveControl := TRUE;  // Control ammonia valve
        stCO2ValveControl := TRUE;      // Control CO2 valve
        
        // Check valve status
        IF stAmmoniaValve AND stCO2Valve THEN
            stStep1 := TRUE;             // Step 1 complete
            tReactionTimer := CURRENT_TIME;  // Record current time to start reaction timing
        END_IF

    // Step 2: Control reaction
    ELSIF NOT stStep2 THEN
        // Check if current pressure and temperature are within the target range
        IF (rCurrentPressure >= rTargetPressure - rPressureTolerance) AND (rCurrentPressure <= rTargetPressure + rPressureTolerance) AND 
           (rCurrentTemperature >= rTargetTemperature - rTemperatureTolerance) AND (rCurrentTemperature <= rTargetTemperature + rTemperatureTolerance) THEN
           
            // Check if the reaction time has been reached
            IF CURRENT_TIME >= tReactionTimer + tReactionTime THEN
                stStep2 := TRUE;  // Step 2 complete
            END_IF
        
        ELSE
            // Adjust valves based on pressure and temperature
            stAmmoniaValveControl := (rCurrentPressure < rTargetPressure) OR (rCurrentTemperature < rTargetTemperature);
            stCO2ValveControl := (rCurrentPressure < rTargetPressure) OR (rCurrentTemperature < rTargetTemperature);
        END_IF
    END_IF

ELSE
    // Close all valves, mark reaction as finished
    stAmmoniaValveControl := FALSE;
    stCO2ValveControl := FALSE;
    stReactionFinished := TRUE;
END_IF

END_PROGRAM

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC control system developer responsible for documenting an IEC 61131-3 Structured Text (ST) program titled UreaReactionControl. The goal is to create a clear, professional-level technical documentation that will help other engineers understand, maintain, and verify the logic of the urea reaction process.

⸻

🟩 I (Input) – What You’re Given

You are provided with a full ST program that:
	•	Opens ammonia and CO₂ valves to load raw materials
	•	Monitors pressure and temperature conditions inside a reactor
	•	Times the urea reaction process over a fixed period
	•	Contains internal states for tracking progress (e.g., step flags, timer, and finished flag)
	•	Uses threshold values and tolerances to determine safe operation

⸻

🟧 S (Steps) – What You Need to Do
	1.	Summarize the program’s purpose: Explain that it controls a two-phase urea reaction involving material loading and monitored reaction timing.
	2.	Describe all variables:
	•	Inputs (e.g., valve status, sensor readings)
	•	Outputs (e.g., valve control signals)
	•	Internal control flags
	•	Reaction parameters like pressure, temperature, and timing
	3.	Outline the control flow:
	•	Step 1: Open valves and wait until both confirm open
	•	Step 2: Check whether pressure and temperature are within range
	•	Start the timer and keep conditions steady until the reaction time completes
	•	Final: Close valves and set the finished flag
	4.	Clarify timer logic: Highlight how the CURRENT_TIME is used to track the duration of the reaction process.

⸻

🟦 E (Expectation) – What the Output Should Look Like

The final output should be a well-organized, developer-friendly documentation that includes:
	•	A purpose section
	•	A variable list (with types and descriptions)
	•	A logic flow explanation (step-by-step control behavior)
	•	Notes on how and when valves are triggered
	•	Description of reaction success criteria (temperature/pressure/timer)
	•	A ready-to-use reference for future development, safety checks, and compliance

### Generated Code:
The task is to generate developer documentation for a PLC program (UreaReactionControl) that manages a two-phase urea production process by controlling ammonia/CO₂ valves while monitoring pressure, temperature, and reaction time thresholds in an industrial reactor.
**Generate Documentation Urea Reaction:**

Generate a developer documentation for the following code: PROGRAM UreaReactionControl VAR // Inputs stAmmoniaValve : BOOL; // TRUE when ammonia valve is open stCO2Valve : BOOL; // TRUE when CO2 valve is open rCurrentPressure : REAL; rCurrentTemperature : REAL;
// Outputs
stAmmoniaValveControl : BOOL; // TRUE to open ammonia valve
stCO2ValveControl : BOOL; // TRUE to open CO2 valve

// Internal variables
stStep1 : BOOL := FALSE; // Load raw materials
stStep2 : BOOL := FALSE; // Control reaction
stReactionFinished : BOOL := FALSE; // Reaction finished flag

// Parameters
rTargetPressure : REAL := 175.0; // Target reactor pressure in bars
rPressureTolerance : REAL := 5.0; // Pressure tolerance in bars
rTargetTemperature : REAL := 185.0; // Target reactor temperature in �C
rTemperatureTolerance : REAL := 2.0; // Temperature tolerance in �C
tReactionTime : TIME := T#30m; // Total reaction time
tReactionTimer : TIME; // Reaction timer
END_VAR
// Main sequence control
IF NOT stReactionFinished THEN

    // Step 1: Load raw materials
    IF NOT stStep1 THEN
        stAmmoniaValveControl := TRUE;  // Control ammonia valve
        stCO2ValveControl := TRUE;      // Control CO2 valve
        
        // Check valve status
        IF stAmmoniaValve AND stCO2Valve THEN
            stStep1 := TRUE;             // Step 1 complete
            tReactionTimer := CURRENT_TIME;  // Record current time to start reaction timing
        END_IF

    // Step 2: Control reaction
    ELSIF NOT stStep2 THEN
        // Check if current pressure and temperature are within the target range
        IF (rCurrentPressure >= rTargetPressure - rPressureTolerance) AND (rCurrentPressure <= rTargetPressure + rPressureTolerance) AND 
           (rCurrentTemperature >= rTargetTemperature - rTemperatureTolerance) AND (rCurrentTemperature <= rTargetTemperature + rTemperatureTolerance) THEN
           
            // Check if the reaction time has been reached
            IF CURRENT_TIME >= tReactionTimer + tReactionTime THEN
                stStep2 := TRUE;  // Step 2 complete
            END_IF
        
        ELSE
            // Adjust valves based on pressure and temperature
            stAmmoniaValveControl := (rCurrentPressure < rTargetPressure) OR (rCurrentTemperature < rTargetTemperature);
            stCO2ValveControl := (rCurrentPressure < rTargetPressure) OR (rCurrentTemperature < rTargetTemperature);
        END_IF
    END_IF

ELSE
    // Close all valves, mark reaction as finished
    stAmmoniaValveControl := FALSE;
    stCO2ValveControl := FALSE;
    stReactionFinished := TRUE;
END_IF

END_PROGRAM

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC control system developer responsible for documenting an IEC 61131-3 Structured Text (ST) program titled UreaReactionControl. The goal is to create a clear, professional-level technical documentation that will help other engineers understand, maintain, and verify the logic of the urea reaction process.

⸻

🟩 I (Input) – What You’re Given

You are provided with a full ST program that:
	•	Opens ammonia and CO₂ valves to load raw materials
	•	Monitors pressure and temperature conditions inside a reactor
	•	Times the urea reaction process over a fixed period
	•	Contains internal states for tracking progress (e.g., step flags, timer, and finished flag)
	•	Uses threshold values and tolerances to determine safe operation

⸻

🟧 S (Steps) – What You Need to Do
	1.	Summarize the program’s purpose: Explain that it controls a two-phase urea reaction involving material loading and monitored reaction timing.
	2.	Describe all variables:
	•	Inputs (e.g., valve status, sensor readings)
	•	Outputs (e.g., valve control signals)
	•	Internal control flags
	•	Reaction parameters like pressure, temperature, and timing
	3.	Outline the control flow:
	•	Step 1: Open valves and wait until both confirm open
	•	Step 2: Check whether pressure and temperature are within range
	•	Start the timer and keep conditions steady until the reaction time completes
	•	Final: Close valves and set the finished flag
	4.	Clarify timer logic: Highlight how the CURRENT_TIME is used to track the duration of the reaction process.

⸻

🟦 E (Expectation) – What the Output Should Look Like

The final output should be a well-organized, developer-friendly documentation that includes:
	•	A purpose section
	•	A variable list (with types and descriptions)
	•	A logic flow explanation (step-by-step control behavior)
	•	Notes on how and when valves are triggered
	•	Description of reaction success criteria (temperature/pressure/timer)
	•	A ready-to-use reference for future development, safety checks, and compliance audits
Certainly! Below is a structured, IEC 61131-3 compliant function block for a 10-digit counter, which includes input validation, overflow protection, and reset functionality.

### Function Block Diagram

![10-Digit Counter Function Block Diagram](https://i.imgur.com/6jJ6jJl.png)

### Function Block Interface

```
FUNCTION_BLOCK FB_10DigitCounter
VAR_INPUT
    Enable : BOOL; // Enable signal to start counting
    Increment : BOOL; // Increment signal
    Reset : BOOL; // Reset signal
END_VAR

VAR_OUTPUT
    CurrentValue : DWORD; // Current value of the counter
    Overflow : BOOL; // Overflow flag
    Done : BOOL; // Done flag when the counter reaches the maximum value
END_VAR

VAR
    MaxValue : DWORD := 9999999990; // Maximum value of the counter
    PrevEnable : BOOL; // Previous value of Enable for edge detection
    Counting : BOOL; // Flag to indicate if counting is active
END_VAR

METHOD Execute : VOID
BEGIN
    // Store the previous value of Enable
    PrevEnable := Enable;

    // Reset the counter if Reset is asserted
    IF Reset THEN
        CurrentValue := 0;
        Overflow := FALSE;
        Done := FALSE;
        Counting := FALSE;
        RETURN;
    END_IF;

    // Check if Enable is asserted and the counter is not currently resetting
    IF Enable AND NOT Reset THEN
        // Check if Enable has transitioned from FALSE to TRUE (edge detection)
        IF PrevEnable = FALSE AND Enable THEN
            // Start counting when Enable transitions from FALSE to TRUE
            Counting := TRUE;
            CurrentValue := 0;
            Overflow := FALSE;
            Done := FALSE;
        END_IF;

        // Increment the counter if Increment is asserted and counting is enabled
        IF Increment AND Counting THEN
            IF CurrentValue < MaxValue THEN
                CurrentValue := CurrentValue

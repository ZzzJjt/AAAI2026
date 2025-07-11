### Intent:
The task involves creating developer documentation for a PLC program that controls a urea production process by managing ammonia and CO₂ valve operations, monitoring reactor pressure/temperature, and timing the reaction duration according to specified parameters.  

**Intent Summary:**  
Document a structured text program that automates a two-stage urea reaction process through valve control, sensor monitoring, and timed operation.

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
The task involves creating developer documentation for a PLC program that controls a urea production process by managing ammonia and CO₂ valve operations, monitoring reactor pressure/temperature, and timing the reaction duration according to specified parameters.  

**Intent Summary:**  
Document a structured text program that automates a two-stage urea reaction process through valve control, sensor monitoring, and timed operation.
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
	•	A ready-to-use reference for future development, safety checks, and compliance verification.

**Documentation for Urea Reaction Control Program**

**Purpose:**
The UreaReactionControl program automates the two-stage urea reaction process by managing valve operations, monitoring reactor pressure and temperature, and timing the reaction duration according to specified parameters.

**Variables:**

| Variable Name | Type | Description |
| --- | --- | --- |
| stAmmoniaValve | BOOL | TRUE when ammonia valve is open |
| stCO2Valve | BOOL | TRUE when CO2 valve is open |
| rCurrentPressure | REAL | Current reactor pressure in bars |
| rCurrentTemperature | REAL | Current reactor temperature in �C |
| stAmmoniaValveControl | BOOL | TRUE to open ammonia valve |
| stCO2ValveControl | BOOL | TRUE to open CO2 valve |
| stStep1 | BOOL | TRUE when raw materials are loaded |
| stStep2 | BOOL | TRUE when reaction is controlled |
| stReactionFinished | BOOL | TRUE when reaction is finished |
| rTargetPressure | REAL | Target reactor pressure in bars |
| rPressureTolerance | REAL | Pressure tolerance in bars |
| rTargetTemperature | REAL | Target reactor temperature in �C |
| rTemperatureTolerance | REAL | Temperature tolerance in �C |
| tReactionTime | TIME | Total reaction time |
| tReactionTimer | TIME | Reaction timer |

**Control Flow:**

1. **Step 1: Load Raw Materials**
   - Open ammonia and CO₂ valves.
   - Wait until both valves confirm open.
   - Record current time to start reaction timing.

2. **Step 2: Control Reaction**
   - Check if current pressure and temperature are within the target range.
   - If conditions are met, check if the reaction time has been reached.
   - Adjust valves based on pressure and temperature if conditions are not met.

3. **Final: Close Valves and Mark Reaction as Finished**
   - Close all valves.
   - Set the finished flag.

**Timer Logic:**
The CURRENT_TIME is used to track the duration of the reaction process. The reaction timer starts when the valves are confirmed open and stops when the reaction time is reached.

**Notes:**
- The program uses threshold values and tolerances to determine safe operation.
- The finished flag is set when the reaction is complete, and all valves are closed.

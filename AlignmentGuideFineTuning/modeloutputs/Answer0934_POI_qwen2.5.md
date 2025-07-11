### Intent:
The task involves generating comprehensive developer documentation for a PLC program that automates and controls a urea synthesis process by managing valve operations, monitoring pressure/temperature conditions, and executing timed reaction steps.

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

**T-A-G:**

🟥 T (Task) – What You Need to Do

Generate comprehensive developer documentation for a PLC program written in IEC 61131-3 Structured Text, named UreaReactionControl. The program automates the urea synthesis process by controlling valve operations, monitoring pressure and temperature, and ensuring proper reaction timing.

⸻

🟩 A (Action) – How You Should Approach It

To complete this task:
	1.	Summarize the program’s purpose – explain its role in managing the chemical reaction process in two steps: material loading and controlled reaction.
	2.	Document each variable:
	•	Inputs: ammonia and CO₂ valve states, current pressure and temperature
	•	Outputs: control signals for ammonia and CO₂ valves
	•	Internals: step flags and timer
	•	Parameters: pressure, temperature targets and tolerances, reaction duration
	3.	Describe the logic flow:
	•	Step 1: Opens valves and waits for confirmation
	•	Step 2: Monitors temperature and pressure; starts timer
	•	If conditions are met and timer expires, reaction is marked complete
	4.	Highlight the use of CURRENT_TIME to track reaction duration
	5.	Format the documentation with clear sections such as:
	•	Overview
	•	Variable definitions
	•	Sequential logic explanation
	•	Control conditions and safety handling

⸻

🟦 G (Goal) – What You Should Achieve

The final documentation should:
	•	Provide a clear, technical reference for future developers and engineers
	•	Support troubleshooting and debugging by explaining internal logic
	•	Serve as part of system validation or audit documentation
	•	Ensure the control logic is transparent, reproducible, and maintainable

### Generated Code:
The task involves generating comprehensive developer documentation for a PLC program that automates and controls a urea synthesis process by managing valve operations, monitoring pressure/temperature conditions, and executing timed reaction steps.
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

**T-A-G:**

🟥 T (Task) – What You Need to Do

Generate comprehensive developer documentation for a PLC program written in IEC 61131-3 Structured Text, named UreaReactionControl. The program automates the urea synthesis process by controlling valve operations, monitoring pressure and temperature, and ensuring proper reaction timing.

⸻

🟩 A (Action) – How You Should Approach It

To complete this task:
	1.	Summarize the program’s purpose – explain its role in managing the chemical reaction process in two steps: material loading and controlled reaction.
	2.	Document each variable:
	•	Inputs: ammonia and CO₂ valve states, current pressure and temperature
	•	Outputs: control signals for ammonia and CO₂ valves
	•	Internals: step flags and timer
	•	Parameters: pressure, temperature targets and tolerances, reaction duration
	3.	Describe the logic flow:
	•	Step 1: Opens valves and waits for confirmation
	•	Step 2: Monitors temperature and pressure; starts timer
	•	If conditions are met and timer expires, reaction is marked complete
	4.	Highlight the use of CURRENT_TIME to track reaction duration
	5.	Format the documentation with clear sections such as:
	•	Overview
	•	Variable definitions
	•	Sequential logic explanation
	•	Control conditions and safety handling

⸻

🟦 G (Goal) – What You Should Achieve

The final documentation should:
	•	Provide a clear, technical reference for future developers and engineers
	•	Support troubleshooting and debugging by explaining internal logic
	•	Serve as part of system validation or audit documentation
	•	Ensure the control logic is transparent, reproducible, and maintainable

**Documentation:**

**UreaReactionControl Program Documentation**

**Overview:**
The UreaReactionControl program automates the urea synthesis process by managing valve operations, monitoring pressure and temperature, and executing timed reaction steps. It ensures the proper loading of raw materials and the controlled reaction process.

**Variables:**

**Inputs:**
- `stAmmoniaValve`: TRUE when the ammonia valve is open.
- `stCO2Valve`: TRUE when the CO₂ valve is open.
- `rCurrentPressure`: Current reactor pressure in bars.
- `rCurrentTemperature`: Current reactor temperature in degrees Celsius.

**Outputs:**
- `stAmmoniaValveControl`: TRUE to open the ammonia valve.
- `stCO2ValveControl`: TRUE to open the CO₂ valve.

**Internals:**
- `stStep1`: TRUE when the raw materials are loaded.
- `stStep2`: TRUE when the controlled reaction is in progress.
- `stReactionFinished`: TRUE when the reaction is complete.
- `tReactionTimer`: Reaction timer.

**Parameters:**
- `rTargetPressure`: Target reactor pressure in bars.
- `rPressureTolerance`: Pressure tolerance in bars.
- `rTargetTemperature`: Target reactor temperature in degrees Celsius.
- `rTemperatureTolerance`: Temperature tolerance in degrees Celsius.
- `tReactionTime`: Total reaction time in minutes.

**Logic Flow:**

1. **Step 1: Load Raw Materials**
   - If `stStep1` is FALSE:
     - Set `stAmmoniaValveControl` and `stCO2ValveControl` to TRUE.
     - Check if both valves are open.
     - If both valves are open, set `stStep1` to TRUE and record the current time as `tReactionTimer`.

2. **Step 2: Control Reaction**
   - If `stStep2` is FALSE:
     - Check if the current pressure and temperature are within the target range.
     - If both conditions are met:
       - Check if the reaction time has been reached.
       - If the reaction time has been reached, set `stStep2` to TRUE.
     - If the conditions are not met:
       - Adjust the valves based on pressure and temperature.

3. **Reaction Completion**
   - If `stReactionFinished` is FALSE:
     - Close all valves and mark the reaction as finished.

**Control Conditions and Safety Handling:**
- The program uses `CURRENT_TIME

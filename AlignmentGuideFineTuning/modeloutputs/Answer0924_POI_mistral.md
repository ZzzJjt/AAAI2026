### Intent:
The task involves generating developer documentation for a PLC program that automates urea synthesis by controlling valve operations, monitoring pressure and temperature, and managing reaction timing in a two-step process.  

**Intent Summary:**  
*"Document a PLC program that controls urea production through valve management, pressure/temperature monitoring, and timed reaction sequencing."*

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
The task involves generating developer documentation for a PLC program that automates urea synthesis by controlling valve operations, monitoring pressure and temperature, and managing reaction timing in a two-step process.  

**Intent Summary:**  
*"Document a PLC program that controls urea production through valve management, pressure/temperature monitoring, and timed reaction sequencing."*
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

⸻

🟦 R (Reason) – Why It Matters

Documenting the PLC program is essential for:
	•	Ensuring consistency in the system design and operation
	•	Facilitating knowledge transfer among team members
	•	Supporting system maintenance and troubleshooting
	•	Enabling regulatory compliance and traceability

**Documentation:**

**UreaReactionControl PLC Program Documentation**

**Overview**

The UreaReactionControl program is designed to automate the urea synthesis process in a two-step reaction. The program controls the opening and closing of ammonia and CO₂ valves, monitors pressure and temperature within the reactor, and manages the reaction timing to ensure optimal conditions for urea production.

**Variable Definitions**

**Inputs:**

* stAmmoniaValve (BOOL): Represents the state of the ammonia valve. TRUE indicates the valve is open.
* stCO2Valve (BOOL): Represents the state of the CO₂ valve. TRUE indicates the valve is open.
* rCurrentPressure (REAL): Represents the current pressure within the reactor in bars.
* rCurrentTemperature (REAL): Represents the current temperature within the reactor in �C.

**Outputs:**

* stAmmoniaValveControl (BOOL): Control signal for the ammonia valve. TRUE indicates the valve should be opened.
* stCO2ValveControl (BOOL): Control signal for the CO₂ valve. TRUE indicates the valve should be opened.

**Internals:**

* stStep1 (BOOL): Represents the current step in the reaction process. TRUE indicates Step 1 (loading raw materials) is active.
* stStep2 (BOOL): Represents the current step in the reaction process. TRUE indicates Step 2 (controlling the reaction) is active.
* stReactionFinished (BOOL): Represents whether the reaction has finished. TRUE indicates the reaction is complete.
* tReactionTimer (TIME): Represents the current time when the reaction started.

**Parameters:**

* rTargetPressure (REAL): Represents the target pressure within the reactor in bars.
* rPressureToler

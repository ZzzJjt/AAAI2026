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

⸻

🟦 R (Reason) – Why It Matters

Documenting the PLC program is essential for:
	•	Ensuring consistency in the control system
	•	Facilitating collaboration among team members
	•	Supporting future modifications or improvements
	•	Enabling efficient maintenance and troubleshooting
	•	Meeting industry standards and regulatory requirements

⸻

🟦 E (Example) – What It Looks Like

**UreaReactionControl Documentation**

**Overview**

The UreaReactionControl program is a PLC program written in IEC 61131-3 Structured Text that automates the urea synthesis process by managing valve operations, monitoring pressure and temperature conditions, and executing timed reaction steps.

**Variable Definitions**

**Inputs**

* stAmmoniaValve: Boolean – TRUE when ammonia valve is open
* stCO2Valve: Boolean – TRUE when CO2 valve is open
* rCurrentPressure: Real – Current reactor pressure in bars
* rCurrentTemperature: Real – Current reactor temperature in �C

**Outputs**

* stAmmoniaValveControl: Boolean – TRUE to open ammonia valve
* stCO2ValveControl: Boolean – TRUE to open CO2 valve

**Internals**

* stStep1: Boolean – TRUE when raw materials are loaded
* stStep2: Boolean – TRUE when the reaction is being controlled
* stReactionFinished: Boolean – TRUE when the reaction is finished
* tReactionTimer: Time – Reaction timer

**Parameters**

* rTargetPressure: Real – Target reactor pressure in bars (175.0)
* rPressureTolerance: Real – Pressure tolerance in bars (5.0)
* rTargetTemperature: Real – Target reactor temperature in �C (185.0)
* rTemperatureTolerance: Real – Temperature tolerance in �C (2.0)
* tReactionTime: Time – Total reaction time (30 minutes)

**Sequential Logic Explanation**

1. If the reaction is not finished,

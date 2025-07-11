### Intent:
**Intent Summary:**  
Generate developer documentation for a PLC program (`UreaReactionControl`) that automates a two-step urea synthesis process by controlling ammonia/CO₂ valves, monitoring pressure/temperature, and timing the reaction, with clear explanations of variables, logic flow, and safety conditions.  

*(Focus: Code understanding for maintenance/auditing, emphasizing process steps, tolerances, and valve control logic.)*

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

**B-A-B:**

🟥 Before – The Context or Need

You have a Structured Text (IEC 61131-3) PLC program named UreaReactionControl, which manages a two-step urea synthesis process. The code controls the opening of ammonia and CO₂ valves, monitors reactor pressure and temperature, and times the reaction. However, this logic is currently undocumented, making it harder for developers, maintainers, or auditors to understand and work with the process flow.

⸻

🟩 After – The Desired Output

Generate clear, developer-oriented documentation for the UreaReactionControl program. The documentation should explain:
	•	Purpose of the program
	•	Function of each variable (inputs, outputs, internal, and parameters)
	•	Step-by-step description of the process flow:
	•	Step 1: Loading raw materials
	•	Step 2: Monitoring and controlling the reaction
	•	Completion: Finalizing the reaction
	•	Conditions under which valves are opened or closed
	•	Timing and tolerance logic for pressure and temperature
	•	Use of CURRENT_TIME for reaction timing

This documentation should enable new developers or automation engineers to quickly grasp the code’s intent and implementation.

⸻

🟦 Bridge – How to Get There

Use the provided source code and:
	1.	Describe each code section (inputs, outputs, internal variables, constants)
	2.	Explain the logic in a narrative form: What happens first? What triggers transitions?
	3.	Include conditions and logic branches, like how temperature and pressure are validated
	4.	Highlight safety logic like valve shutoff and reaction completion
	5.	Format the result in a developer manual style, optionally including a table for parameters and a step flow diagram (if needed)

### Generated Code:
**Intent Summary:**  
Generate developer documentation for a PLC program (`UreaReactionControl`) that automates a two-step urea synthesis process by controlling ammonia/CO₂ valves, monitoring pressure/temperature, and timing the reaction, with clear explanations of variables, logic flow, and safety conditions.  

*(Focus: Code understanding for maintenance/auditing, emphasizing process steps, tolerances, and valve control logic.)*
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

**B-A-B:**

🟥 Before – The Context or Need

You have a Structured Text (IEC 61131-3) PLC program named UreaReactionControl, which manages a two-step urea synthesis process. The code controls the opening of ammonia and CO₂ valves, monitors reactor pressure and temperature, and times the reaction. However, this logic is currently undocumented, making it harder for developers, maintainers, or auditors to understand and work with the process flow.

⸻

🟩 After – The Desired Output

Generate clear, developer-oriented documentation for the UreaReactionControl program. The documentation should explain:
	•	Purpose of the program
	•	Function of each variable (inputs, outputs, internal, and parameters)
	•	Step-by-step description of the process flow:
	•	Step 1: Loading raw materials
	•	Step 2: Monitoring and controlling the reaction
	•	Completion: Finalizing the reaction
	•	Conditions under which valves are opened or closed
	•	Timing and tolerance logic for pressure and temperature
	•	Use of CURRENT_TIME for reaction timing

This documentation should enable new developers or automation engineers to quickly grasp the code’s intent and implementation.

⸻

🟦 Bridge – How to Get There

Use the provided source code and:
	1.	Describe each code section (inputs, outputs, internal variables, constants)
	2.	Explain the logic in a narrative form: What happens first? What triggers transitions?
	3.	Include conditions and logic branches, like how temperature and pressure are validated
	4.	Highlight safety logic like valve shutoff and reaction completion
	5.	Format the result in a developer manual style, optionally including a table for parameters and a step flow diagram (if needed)

🟦 Before:

PROGRAM UreaReactionControl
VAR
	stAmmoniaValve : BOOL;
	stCO2Valve : BOOL;
	rCurrentPressure : REAL;
	rCurrentTemperature : REAL;
	stAmmoniaValveControl : BOOL;
	stCO2ValveControl : BOOL;
	stStep1 : BOOL := FALSE;
	stStep2 : BOOL := FALSE;
	stReactionFinished : BOOL := FALSE;
	rTargetPressure : REAL := 175.0;
	rPressureTolerance : REAL := 5.0;
	rTargetTemperature : REAL := 185.0;
	rTemperatureTolerance : REAL := 2.0;
	tReactionTime : TIME := T#30m;
	tReactionTimer : TIME;
END_VAR

🟩 After:

UreaReactionControl Program Documentation

Purpose:
Automate a two-step urea synthesis process by controlling ammonia and CO₂ valves, monitoring pressure and temperature, and timing the reaction.

Inputs:
	•	stAmmoniaValve (BOOL): TRUE when ammonia valve is open
	•	stCO2Valve (BOOL): TRUE when CO₂ valve is open
	•	rCurrentPressure (REAL): Current reactor pressure in bars
	•	rCurrentTemperature (REAL): Current reactor temperature in �C

Outputs:
	•	stAmmoniaValveControl (BOOL): TRUE to open ammonia valve
	•	stCO2ValveControl (BOOL): TRUE to open CO₂ valve

Internal Variables:
	•	stStep1 (BOOL): TRUE when raw materials are loaded
	•	stStep2 (BOOL): TRUE when the reaction is being controlled
	•	stReactionFinished (BOOL): TRUE when the reaction is finished

Parameters:
	•	rTargetPressure (REAL): Target reactor pressure in bars (175.0)
	•	rPressureTolerance (REAL): Pressure tolerance in bars

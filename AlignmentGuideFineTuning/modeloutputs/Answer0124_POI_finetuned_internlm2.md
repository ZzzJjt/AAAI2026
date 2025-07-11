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
	5.	Format the result in a developer manual style, optionally including a table for parameters and a step flow diagram (if needed) to make it easy to follow.

⸻

🟥 After – The Output

**UreaReactionControl:**

**Purpose:**

This program automates the two-step urea synthesis process by controlling the opening of ammonia and CO₂ valves, monitoring reactor pressure and temperature, and timing the reaction. It ensures that the reaction occurs within specified pressure and temperature tolerances and terminates when the reaction is complete.

**Inputs:**

* stAmmoniaValve: A Boolean variable that indicates whether the ammonia valve is open.
* stCO2Valve: A Boolean variable that indicates whether the CO₂ valve is open.
* rCurrentPressure: A real variable that represents the current pressure in the reactor.
* rCurrentTemperature: A real variable that represents the current temperature in the reactor.

**Outputs:**

* stAmmoniaValveControl: A Boolean variable that indicates whether the ammonia valve should be opened or closed.
* stCO2ValveControl: A Boolean variable that indicates whether the CO₂ valve should be opened or closed.

**Internal Variables:**

* stStep1: A Boolean variable that indicates whether the first step of the reaction (loading raw materials) has been completed.
* stStep2: A Boolean variable that indicates whether the second step of the reaction (controlling the reaction) has been completed.
* stReactionFinished: A Boolean variable that indicates whether the reaction has finished.

**Parameters:**

* rTargetPressure: A real constant that represents the target pressure for the reactor in bars.
* rPressureTolerance: A real constant that represents the pressure tolerance in bars.
* rTargetTemperature: A real constant that represents the target temperature for the reactor in °C.
* rTemperatureTolerance: A real constant that represents the temperature tolerance in °C.
* tReactionTime: A time constant that represents the total reaction time.
* tReactionTimer: A time variable that records the start time of the reaction.

**Process Flow:**

The program follows a sequential process flow:

1. **Step 1: Loading Raw Materials:**
	* If the ammonia valve is not open, it is opened.
	* If the CO₂ valve is not open, it is opened.
	* If both valves are open, the first step is completed, and the reaction timer is started.

2. **Step 2: Cont

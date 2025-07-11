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
	5.	Format the result in a developer manual style, optionally including a table for parameters and a step flow diagram (if needed) to illustrate the process flow.  

Following this structure will create a comprehensive, developer-friendly reference for the UreaReactionControl program.  

**B-A-B:**

Before – The Challenge

You are working with a PLC program (UreaReactionControl) that manages the two-step urea synthesis process. The program controls the opening of ammonia and CO₂ valves, monitors reactor pressure and temperature, and times the reaction. However, the program lacks detailed documentation, making it difficult for developers, maintainers, or auditors to understand the process flow, logic, and safety conditions.

After – The Desired Outcome

Generate a developer documentation for the UreaReactionControl program that includes:
	•	A clear explanation of the program’s purpose and functionality
	•	A detailed list of all variables, including their types, units, and ranges
	•	A step-by-step explanation of the process flow, including the logic for controlling the reaction, monitoring conditions, and ensuring safety
	•	A discussion of the timing and tolerance logic used for pressure and temperature control
	•	An overview of the safety conditions, including valve control and reaction completion

Bridge – How to Create the Documentation

	1.	Explain the Background: Provide an introduction to the urea synthesis process and the role of the UreaReactionControl program in automating it.
	2.	Describe the Inputs and Outputs: List all the inputs and outputs of the program, including their types, units, and ranges. Provide a detailed explanation of their functionality.
	3.	Explain the Internal Variables: Discuss the internal variables used in the program, including their roles in controlling the reaction, monitoring conditions, and ensuring safety.
	4.	Outline the Process Flow: Provide a step-by-step explanation of the process flow, including the logic for controlling the reaction, monitoring conditions, and ensuring safety. Include details on the timing and tolerance logic used for pressure and temperature control.
	5.	Describe the Safety Conditions: Discuss the safety conditions implemented in the program, including the logic for closing the valves and ensuring the reaction is complete.
	6.	Provide a Summary: Summarize the key points of the documentation, highlighting the importance of understanding the program’s logic and safety conditions for maintaining and troubleshooting the urea synthesis process.

Following this structure will create a comprehensive, developer-friendly reference for the UreaReactionControl program, making it easier for new developers or automation engineers to understand and work with the code.  

**B-A-B:**

Before – The Challenge

You are

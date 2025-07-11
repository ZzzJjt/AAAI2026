### Intent:
**Intent Summary:**  
Design a safety interlock system for a subsea wellhead that monitors pressure, temperature, and flow, triggers shutdown actions (e.g., closing the master valve) during hazardous conditions (high pressure, low flow, high temperature), logs events, and allows manual reset only when safe.  

*(Focus: Safety logic, sensor validation, fail-safe actions, and audit trails for compliance.)*

### Prompt:
**Interlock Cause & Effect Matrix:**

Develop a cause and effect matrix for the interlocks required in a chemical reactor system. Each row should represent a specific cause linked to sensor values such as pressure, temperature, or level, while each column should represent the corresponding effect related to actuator actions such as closing valves, stopping pumps, or triggering alarms. Once the matrix is complete, write a detailed explanation of how these interlocks ensure the safety and stability of the reactor operation. Discuss how each interlock action prevents hazardous conditions and safeguards the equipment during abnormal process situations.

**R-I-S-E:**

🟥 R (Role) – Your Role

Act as a process safety or control systems engineer designing interlock logic for a chemical reactor to ensure safe and reliable operation during abnormal process conditions.

⸻

🟩 I (Input) – What You’re Given

You need to develop a cause and effect matrix where:

	•	Each row represents a specific cause, such as abnormal sensor readings (e.g., high pressure, low level, high temperature).
	•	Each column represents an effect, such as shutting valves, stopping pumps, or triggering alarms.
 
The matrix must link causes to protective actions that are executed through actuators or control logic.

You are also required to explain how the matrix contributes to overall system safety and equipment protection.

⸻

🟧 S (Steps) – What You Need to Do
	1.	Identify critical causes: List process deviations and sensor-based alarms that require protective action (e.g., “Reactor Pressure > High Limit”).
	2.	Define safety actions: List available interlock responses (e.g., close feed valve, isolate cooling, trigger alarm).
	3.	Create the matrix: Mark where each cause triggers one or more specific actions in the corresponding cells.
	4.	Write an explanation describing:
 
	•	How the matrix logic works
	•	How it supports rapid response to unsafe conditions
	•	How each action mitigates specific risks
	•	The importance of completeness and clarity in interlock design

⸻

🟦 E (Expectation) – What Success Looks Like

You produce a well-structured interlock matrix that gives a clear overview of how the chemical reactor will respond to unsafe operating conditions. The matrix will ensure comprehensive safety coverage, reduce ambiguity, and serve as a key tool in both operational decision-making and safety compliance efforts.

### Generated Code:
**Intent Summary:**  
Design a safety interlock system for a subsea wellhead that monitors pressure, temperature, and flow, triggers shutdown actions (e.g., closing the master valve) during hazardous conditions (high pressure, low flow, high temperature), logs events, and allows manual reset only when safe.  

*(Focus: Safety logic, sensor validation, fail-safe actions, and audit trails for compliance.)*
**Interlock Cause & Effect Matrix:**

Develop a cause and effect matrix for the interlocks required in a chemical reactor system. Each row should represent a specific cause linked to sensor values such as pressure, temperature, or level, while each column should represent the corresponding effect related to actuator actions such as closing valves, stopping pumps, or triggering alarms. Once the matrix is complete, write a detailed explanation of how these interlocks ensure the safety and stability of the reactor operation. Discuss how each interlock action prevents hazardous conditions and safeguards the equipment during abnormal process situations.

**R-I-S-E:**

🟥 R (Role) – Your Role

Act as a process safety or control systems engineer designing interlock logic for a chemical reactor to ensure safe and reliable operation during abnormal process conditions.

⸻

🟩 I (Input) – What You’re Given

You need to develop a cause and effect matrix where:

	•	Each row represents a specific cause, such as abnormal sensor readings (e.g., high pressure, low level, high temperature).
	•	Each column represents an effect, such as shutting valves, stopping pumps, or triggering alarms.
 
The matrix must link causes to protective actions that are executed through actuators or control logic.

You are also required to explain how the matrix contributes to overall system safety and equipment protection.

⸻

🟧 S (Steps) – What You Need to Do
	1.	Identify critical causes: List process deviations and sensor-based alarms that require protective action (e.g., “Reactor Pressure > High Limit”).
	2.	Define safety actions: List available interlock responses (e.g., close feed valve, isolate cooling, trigger alarm).
	3.	Create the matrix: Mark where each cause triggers one or more specific actions in the corresponding cells.
	4.	Write an explanation describing:
 
	•	How the matrix logic works
	•	How it supports rapid response to unsafe conditions
	•	How each action mitigates specific risks
	•	The importance of completeness and clarity in interlock design

⸻

🟦 E (Expectation) – What Success Looks Like

You produce a well-structured interlock matrix that gives a clear overview of how the chemical reactor will respond to unsafe operating conditions. The matrix will ensure comprehensive safety coverage, reduce ambiguity, and serve as a key tool in both operational decision-making and safety compliance efforts.
FUNCTION_BLOCK FB_SubseaWellheadInterlock
VAR_INPUT
    Execute : BOOL; // Trigger interlock evaluation
    Pressure_PV : REAL; // Measured wellhead pressure (bar)
    Flow_PV : REAL; // Measured flow rate (m³/h)
    Temp_PV : REAL; // Measured temperature (°C)
    Reset : BOOL; // Manual reset input
END_VAR

VAR_OUTPUT
    MasterValveClosed : BOOL; // TRUE if master valve is closed
    Shutdown : BOOL; // TRUE if system is shut down
    Alarm : BOOL; // TRUE if any interlock condition is active
    Error : BOOL; // TRUE if interlock logic fails
    ErrorID : DWORD; // Error code
    LogEntry : STRING[100]; // Logged event
END_VAR

VAR
    // Interlock thresholds (adjustable via configuration)
    HighPressure_Limit : REAL := 150.0; // bar
    LowFlow_Limit : REAL := 0.0; // m³/h
    HighTemp_Limit : REAL := 120.0; // °C

    // Internal state variables
    Prev_Execute : BOOL; // For edge detection of Execute
    Shutdown_Requested : BOOL; // Internal flag for shutdown
    Reset_Pending : BOOL; // Internal flag for reset
    ValidInputs : BOOL; // Input validation flag
    ValidReset : BOOL; // Reset validation flag

    // Interlock conditions
    Pressure_High : BOOL;
    Flow_Low : BOOL;
    Temp_High : BOOL;

    // Interlock actions
    MasterValve_Close : BOOL;
    Log_Event : BOOL;
END_VAR

// Reset logic
IF Reset THEN
    Reset_Pending := TRUE;
    MasterValveClosed := FALSE;
    Shutdown := FALSE;
    Alarm := FALSE;
    Error := FALSE;
    ErrorID := 0;
    LogEntry := '';
    Reset_Pending := FALSE;
END_IF

// Input validation

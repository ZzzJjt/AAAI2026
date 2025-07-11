### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to automatically close a vessel's inlet valve when a high liquid level is detected (with fail-safe handling for faults), ensuring overfill protection until the level resets to a safe threshold.  

*(Focus: Safety interlock logic for level control with fault resilience.)*

### Prompt:
**Interlock Overfill Protection:**

Develop a self-contained IEC 61131-3 Structured Text program to implement an interlock system for overfill protection of a vessel. The program should utilize a level sensor to monitor the liquid level in the vessel and control an inlet valve to prevent overfilling.

The logic should ensure that the inlet valve automatically closes when the level sensor detects that the liquid has reached a predefined high-level setpoint. The interlock should remain engaged until the level drops below a safe threshold. Additionally, include a fail-safe mechanism to handle sensor failure or valve malfunction, ensuring the system defaults to a safe state. Discuss the importance of interlocks in industrial process safety and the role of overfill protection in preventing hazardous conditions.

**R-I-S-E:**

🟥 R (Role) – Your Role

Act as a PLC programmer or process control engineer responsible for implementing overfill protection in a vessel using IEC 61131-3 Structured Text to ensure safe, automatic operation in an industrial environment.

⸻

🟩 I (Input) – What You’re Given

You are tasked with creating a self-contained Structured Text program that:
	•	Uses a level sensor to monitor the liquid level in a vessel
	•	Controls an inlet valve to prevent overfilling
	•	Implements interlock logic based on safety thresholds
	•	Includes fail-safe handling in case of sensor or valve failure

Specific control conditions:
	•	Close the inlet valve if the level exceeds a high-level setpoint
	•	Keep the valve closed until the level falls below a reset threshold
	•	Default to a safe state (valve closed) if a sensor fault or valve fault is detected

⸻

🟧 S (Steps) – What You Need to Do
	1.	Define the variables and thresholds, including LevelSensor, HIGH_SETPOINT, RESET_THRESHOLD, SensorFault, ValveFault, and INLET_VALVE.
	2.	Implement interlock logic using Structured Text:
	•	Detect high-level condition and close the valve
	•	Latch the shutdown state until the level is safely below reset
	•	Monitor sensor/valve faults and trigger fail-safe action
	3.	Add logic for manual reset or alarm signaling, if needed, to meet process safety standards.
	4.	Comment and structure the code clearly for operational teams and future maintenance.

⸻

🟦 E (Expectation) – What Success Looks Like

You deliver a robust, self-resetting interlock that reliably prevents overfilling, even in the presence of equipment faults. The valve automatically closes on high level or fault detection and reopens only when the level returns to a safe zone. This system ensures process integrity, regulatory compliance, and equipment protection across a wide range of industrial applications.

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to automatically close a vessel's inlet valve when a high liquid level is detected (with fail-safe handling for faults), ensuring overfill protection until the level resets to a safe threshold.  

*(Focus: Safety interlock logic for level control with fault resilience.)*
**Interlock Overfill Protection:**

Develop a self-contained IEC 61131-3 Structured Text program to implement an interlock system for overfill protection of a vessel. The program should utilize a level sensor to monitor the liquid level in the vessel and control an inlet valve to prevent overfilling.

The logic should ensure that the inlet valve automatically closes when the level sensor detects that the liquid has reached a predefined high-level setpoint. The interlock should remain engaged until the level drops below a safe threshold. Additionally, include a fail-safe mechanism to handle sensor failure or valve malfunction, ensuring the system defaults to a safe state. Discuss the importance of interlocks in industrial process safety and the role of overfill protection in preventing hazardous conditions.

**R-I-S-E:**

🟥 R (Role) – Your Role

Act as a PLC programmer or process control engineer responsible for implementing overfill protection in a vessel using IEC 61131-3 Structured Text to ensure safe, automatic operation in an industrial environment.

⸻

🟩 I (Input) – What You’re Given

You are tasked with creating a self-contained Structured Text program that:
	•	Uses a level sensor to monitor the liquid level in a vessel
	•	Controls an inlet valve to prevent overfilling
	•	Implements interlock logic based on safety thresholds
	•	Includes fail-safe handling in case of sensor or valve failure

Specific control conditions:
	•	Close the inlet valve if the level exceeds a high-level setpoint
	•	Keep the valve closed until the level falls below a reset threshold
	•	Default to a safe state (valve closed) if a sensor fault or valve fault is detected

⸻

🟧 S (Steps) – What You Need to Do
	1.	Define the variables and thresholds, including LevelSensor, HIGH_SETPOINT, RESET_THRESHOLD, SensorFault, ValveFault, and INLET_VALVE.
	2.	Implement interlock logic using Structured Text:
	•	Detect high-level condition and close the valve
	•	Latch the shutdown state until the level is safely below reset
	•	Monitor sensor/valve faults and trigger fail-safe action
	3.	Add logic for manual reset or alarm signaling, if needed, to meet process safety standards.
	4.	Comment and structure the code clearly for operational teams and future maintenance.

⸻

🟦 E (Expectation) – What Success Looks Like

You deliver a robust, self-resetting interlock that reliably prevents overfilling, even in the presence of equipment faults. The valve automatically closes on high level or fault detection and reopens only when the level returns to a safe zone. This system ensures process integrity, regulatory compliance, and equipment protection across a wide range of industrial applications.
FUNCTION_BLOCK FB_LevelControl
VAR_INPUT
    LevelSensor : REAL; // Liquid level reading (%)
    MaxLevel : REAL := 100.0; // Maximum level threshold (%)
    MinLevel : REAL := 0.0; // Minimum level threshold (%)
    ValveCommand : BOOL := FALSE; // Command to open/close the inlet valve
    EmergencyStop : BOOL := FALSE; // Emergency stop input
END_VAR

VAR_OUTPUT
    ValveOpen : BOOL := FALSE; // Output signal to open the inlet valve
    Alarm : BOOL := FALSE; // Alarm output
    ManualReset : BOOL := FALSE; // Manual reset input
    Error : BOOL := FALSE; // Error flag
    ErrorMessage : STRING(255) := ''; // Error message
END_VAR

VAR
    LastLevel : REAL := 0.0; // Previous level reading for hysteresis
    ValveState : BOOL := FALSE; // Current valve state
    FaultDetected : BOOL := FALSE; // Fault detection flag
    Reset : BOOL := FALSE; // Reset flag
END_VAR

// Main control logic
IF NOT EmergencyStop THEN
    // Check for sensor fault
    IF LevelSensor < 0.0 OR LevelSensor > 100.0 THEN
        FaultDetected := TRUE;
        Error := TRUE;
        ErrorMessage := 'Sensor fault detected: Invalid level reading';
    ELSE
        // Update previous level for hysteresis
        LastLevel := LevelSensor;

        // Check for low level condition
        IF LevelSensor < MinLevel THEN
            Alarm := TRUE;
            Error := TRUE;
            ErrorMessage := 'Low level alarm: Level below minimum threshold';
        ELSE
            // Check for high level condition
            IF LevelSensor > MaxLevel THEN
                Alarm := TRUE;
                Error := TRUE;
                ErrorMessage := 'High level alarm: Level above maximum threshold';

                // Close the inlet valve and set error
                ValveCommand := FALSE;
                ValveOpen := FALSE;
                Error := TRUE

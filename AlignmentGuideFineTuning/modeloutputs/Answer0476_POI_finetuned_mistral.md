### Intent:
**Intent Summary:**  
Create a Structured Text program to implement a vessel overfill protection system that automatically closes the inlet valve when the liquid level exceeds a high setpoint, maintains the interlock until safe levels are restored, and includes fail-safe handling for sensor/valve faults.  

*(Focus: Safety interlock logic for liquid level control with fault resilience.)*

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
Create a Structured Text program to implement a vessel overfill protection system that automatically closes the inlet valve when the liquid level exceeds a high setpoint, maintains the interlock until safe levels are restored, and includes fail-safe handling for sensor/valve faults.  

*(Focus: Safety interlock logic for liquid level control with fault resilience.)*
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
FUNCTION_BLOCK FB_VesselOverfillProtection
VAR_INPUT
    LevelSensor : REAL; // Level sensor reading (%)
    SensorFault : BOOL; // TRUE if sensor is faulty
    ValveFault : BOOL; // TRUE if inlet valve is faulty
END_VAR

VAR_OUTPUT
    InletValveOpen : BOOL; // TRUE when valve is open
    AlarmActive : BOOL; // TRUE when alarm is triggered
    ShutdownComplete : BOOL; // TRUE when system is safe to resume
END_VAR

VAR
    HighLevelSetpoint : REAL := 95.0; // High-level setpoint (%)
    ResetThreshold : REAL := 85.0; // Reset threshold (%)
    ShutdownTimer : TON;
    ValveState : BOOL := FALSE; // Internal state of inlet valve
    FaultDetected : BOOL := FALSE; // Fault detection flag
END_VAR

// Initialize outputs
InletValveOpen := FALSE;
AlarmActive := FALSE;
ShutdownComplete := FALSE;

// Initialize timer
ShutdownTimer(IN := NOT FaultDetected, PT := T#10m);

// Main logic
IF NOT ValveFault AND NOT SensorFault THEN
    // Check for high-level condition
    IF LevelSensor > HighLevelSetpoint THEN
        // Close inlet valve and latch shutdown
        ValveState := FALSE;
        FaultDetected := TRUE;
        ShutdownTimer(IN := TRUE);
    ELSIF LevelSensor < ResetThreshold AND FaultDetected THEN
        // Reset interlock and clear shutdown
        ValveState := TRUE;
        FaultDetected := FALSE;
        ShutdownTimer(IN := FALSE);
        ShutdownComplete := TRUE;
    END_IF;
ELSE
    // Default to safe state (valve closed)
    ValveState := FALSE;
    FaultDetected := TRUE;
    ShutdownTimer(IN := FALSE);
    ShutdownComplete := FALSE;
END_IF;

// Set output values
InletValveOpen := ValveState;
AlarmActive

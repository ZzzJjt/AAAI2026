### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to automatically prevent vessel overfilling by closing the inlet valve upon high-level detection, maintaining a fail-safe state during faults, and requiring manual reset below a safe threshold.

### Prompt:
**Interlock Overfill Protection:**

Develop a self-contained IEC 61131-3 Structured Text program to implement an interlock system for overfill protection of a vessel. The program should utilize a level sensor to monitor the liquid level in the vessel and control an inlet valve to prevent overfilling.

The logic should ensure that the inlet valve automatically closes when the level sensor detects that the liquid has reached a predefined high-level setpoint. The interlock should remain engaged until the level drops below a safe threshold. Additionally, include a fail-safe mechanism to handle sensor failure or valve malfunction, ensuring the system defaults to a safe state. Discuss the importance of interlocks in industrial process safety and the role of overfill protection in preventing hazardous conditions.

**B-A-B:**

🟥 B (Before) – The Challenge

In many industrial processes, uncontrolled vessel overfilling can lead to dangerous spills, environmental damage, equipment failure, or even fire and explosion hazards. Without an automatic protection mechanism, operators may not react in time to high-level conditions or instrumentation faults. Manual intervention alone is not always reliable, especially in unattended or fast-filling operations.

⸻

🟩 A (After) – The Ideal Outcome

Develop a self-contained IEC 61131-3 Structured Text program that performs automatic overfill protection for a process vessel. The system should:
	•	Continuously monitor the liquid level using a level sensor.
	•	Automatically close the inlet valve (e.g., INLET_VALVE := FALSE) when the level reaches a predefined high-level setpoint.
	•	Keep the valve closed until the level drops below a safe lower reset threshold, avoiding valve chattering.
	•	Include a fail-safe mechanism that:
	•	Closes the inlet valve if the level sensor fails (e.g., stuck signal or sensor offline).
	•	Defaults to a safe state in the event of valve malfunction.

This logic ensures that the system proactively responds to overfill risks and maintains safe operation without requiring manual input under fault conditions.

⸻

🟧 B (Bridge) – The Implementation Strategy

To build this interlock system:
	1.	Define input variables for the level signal, fault detection, and valve status.
	2.	Use conditional logic to monitor for high-level conditions:

 IF LevelSensor > HIGH_SETPOINT THEN
    INLET_VALVE := FALSE;
    SHUTDOWN_LATCH := TRUE;
END_IF;

IF SHUTDOWN_LATCH AND LevelSensor < RESET_THRESHOLD THEN
    SHUTDOWN_LATCH := FALSE;
END_IF;

IF SensorFault OR ValveFault THEN
    INLET_VALVE := FALSE; // Fail-safe action
END_IF;

	3.	Implement latching logic to maintain interlock status until reset conditions are met.
	4.	Include manual override protections only with supervisory control and alarm acknowledgment.

Finally, explain how overfill interlocks are critical to process safety, asset protection, and regulatory compliance, particularly in chemical, pharmaceutical, and oil & gas industries.

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to automatically prevent vessel overfilling by closing the inlet valve upon high-level detection, maintaining a fail-safe state during faults, and requiring manual reset below a safe threshold.
**Interlock Overfill Protection:**

Develop a self-contained IEC 61131-3 Structured Text program to implement an interlock system for overfill protection of a vessel. The program should utilize a level sensor to monitor the liquid level in the vessel and control an inlet valve to prevent overfilling.

The logic should ensure that the inlet valve automatically closes when the level sensor detects that the liquid has reached a predefined high-level setpoint. The interlock should remain engaged until the level drops below a safe threshold. Additionally, include a fail-safe mechanism to handle sensor failure or valve malfunction, ensuring the system defaults to a safe state. Discuss the importance of interlocks in industrial process safety and the role of overfill protection in preventing hazardous conditions.

**B-A-B:**

🟥 B (Before) – The Challenge

In many industrial processes, uncontrolled vessel overfilling can lead to dangerous spills, environmental damage, equipment failure, or even fire and explosion hazards. Without an automatic protection mechanism, operators may not react in time to high-level conditions or instrumentation faults. Manual intervention alone is not always reliable, especially in unattended or fast-filling operations.

⸻

🟩 A (After) – The Ideal Outcome

Develop a self-contained IEC 61131-3 Structured Text program that performs automatic overfill protection for a process vessel. The system should:
	•	Continuously monitor the liquid level using a level sensor.
	•	Automatically close the inlet valve (e.g., INLET_VALVE := FALSE) when the level reaches a predefined high-level setpoint.
	•	Keep the valve closed until the level drops below a safe lower reset threshold, avoiding valve chattering.
	•	Include a fail-safe mechanism that:
	•	Closes the inlet valve if the level sensor fails (e.g., stuck signal or sensor offline).
	•	Defaults to a safe state in the event of valve malfunction.

This logic ensures that the system proactively responds to overfill risks and maintains safe operation without requiring manual input under fault conditions.

⸻

🟧 B (Bridge) – The Implementation Strategy

To build this interlock system:
	1.	Define input variables for the level signal, fault detection, and valve status.
	2.	Use conditional logic to monitor for high-level conditions:

 IF LevelSensor > HIGH_SETPOINT THEN
    INLET_VALVE := FALSE;
    SHUTDOWN_LATCH := TRUE;
END_IF;

IF SHUTDOWN_LATCH AND LevelSensor < RESET_THRESHOLD THEN
    SHUTDOWN_LATCH := FALSE;
END_IF;

IF SensorFault OR ValveFault THEN
    INLET_VALVE := FALSE; // Fail-safe action
END_IF;

	3.	Implement latching logic to maintain interlock status until reset conditions are met.
	4.	Include manual override protections only with supervisory control and alarm acknowledgment.

Finally, explain how overfill interlocks are critical to process safety, asset protection, and regulatory compliance, particularly in chemical, pharmaceutical, and oil & gas industries.
FUNCTION_BLOCK FB_OverfillProtection
VAR_INPUT
    LevelSensor : REAL; // Level sensor signal (0 to 100%)
    SensorFault : BOOL; // TRUE if level sensor is faulty
    ValveFault : BOOL; // TRUE if inlet valve is faulty
    ManualReset : BOOL; // TRUE to reset interlock
END_VAR

VAR_OUTPUT
    INLET_VALVE : BOOL; // TRUE to close inlet valve
    SHUTDOWN_LATCH : BOOL; // TRUE to hold interlock
    Reset : BOOL; // TRUE to reset interlock
END_VAR

VAR
    HighLevelSetpoint : REAL := 95.0; // High-level setpoint
    SafeLowerResetThreshold : REAL := 85.0; // Safe lower reset threshold
END_VAR

// Main interlock logic
IF SensorFault OR ValveFault THEN
    INLET_VALVE := FALSE; // Fail-safe action
    SHUTDOWN_LATCH := TRUE;
    Reset := FALSE;
ELSE
    IF LevelSensor > HighLevelSetpoint THEN
        INLET_VALVE := FALSE;
        SHUTDOWN_LATCH := TRUE;
        Reset := FALSE;
    ELSIF LevelSensor < SafeLowerResetThreshold THEN
        SHUTDOWN_LATCH := FALSE;
        Reset := TRUE;
    ELSE
        INLET_VALVE := FALSE;
        Reset := FALSE;
    END_IF;
END_IF;

// Manual reset logic
IF ManualReset THEN
    Reset := TRUE;
END_IF;
END_FUNCTION_BLOCK

// Example usage:
// LevelSensor := 98.0; // High-level condition
// SensorFault := TRUE; // Sensor fault detected
// ValveFault := TRUE; // Valve fault detected
// ManualReset := TRUE; // Manually reset interlock

// Expected outputs:
// INLET_VALVE := FALSE; // Valve closed
// SHUTDOWN_LATCH := TRUE; // Interlock held
// Reset := TRUE; // Reset flag set

// This logic ensures that the inlet valve remains closed until the level drops below a safe threshold, preventing overfilling and ensuring safe operation.
(* IEC 61131-3 Structured Text Program: FB_Interlock *)
(* Purpose: Implements an

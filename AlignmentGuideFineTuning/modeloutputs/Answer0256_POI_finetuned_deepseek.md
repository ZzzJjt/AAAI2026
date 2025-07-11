### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program for a fail-safe overfill protection interlock that monitors vessel liquid levels, closes the inlet valve upon reaching a high-level threshold, and maintains shutdown until safe conditions are restored, with fault handling for sensor/valve failures.  

*(Key focus: Automated safety interlock, level monitoring, fail-safe logic, and compliance with industrial standards.)*

### Prompt:
**Interlock Overfill Protection:**

Develop a self-contained IEC 61131-3 Structured Text program to implement an interlock system for overfill protection of a vessel. The program should utilize a level sensor to monitor the liquid level in the vessel and control an inlet valve to prevent overfilling.

The logic should ensure that the inlet valve automatically closes when the level sensor detects that the liquid has reached a predefined high-level setpoint. The interlock should remain engaged until the level drops below a safe threshold. Additionally, include a fail-safe mechanism to handle sensor failure or valve malfunction, ensuring the system defaults to a safe state. Discuss the importance of interlocks in industrial process safety and the role of overfill protection in preventing hazardous conditions.

**C-A-R-E:**

🟥 C (Context) – The Background

In industrial process environments, uncontrolled filling of tanks or vessels can lead to overflows, environmental hazards, equipment damage, and safety violations. Overfill incidents are preventable using automated interlock systems that monitor fluid levels and shut off inlet sources in time. Integrating overfill protection into PLC-based control systems ensures consistent, repeatable, and fail-safe operation.

⸻

🟩 A (Action) – The Implementation Task

Develop a self-contained IEC 61131-3 Structured Text program that implements an overfill protection interlock for a vessel. The system must:
	•	Use a level sensor to monitor liquid level in real-time
	•	Automatically close the inlet valve when the level reaches a defined high-level setpoint
	•	Keep the valve closed until the level drops below a lower reset threshold, ensuring the interlock is not prematurely released
	•	Include fail-safe logic to close the inlet valve in case of:
	•	Sensor failure (e.g., stuck value or offline condition)
	•	Valve malfunction (e.g., failure to respond to control signal)

The interlock must maintain a latched shutdown state and require proper level conditions to clear.

⸻

🟨 R (Result) – The Expected Outcome

The resulting interlock logic ensures reliable overfill protection, automatically preventing the tank from exceeding its safe capacity. It minimizes risk of spills, maintains process stability, and ensures that system behavior is predictable even in fault conditions. It also supports industry best practices for safety and environmental compliance.

⸻

🟦 E (Example) – A Practical Use Case

When the level sensor detects that the tank level exceeds 95% capacity, the system sets a SHUTDOWN_LATCH := TRUE and closes the inlet valve by setting INLET_VALVE := FALSE. If the sensor fails or its signal is outside valid bounds, the system immediately defaults to a safe state by closing the inlet valve. The valve remains closed until the level drops below 85%, clearing the latch and allowing normal operation to resume. This logic is essential in industries such as chemical processing, water treatment, and oil & gas.

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program for a fail-safe overfill protection interlock that monitors vessel liquid levels, closes the inlet valve upon reaching a high-level threshold, and maintains shutdown until safe conditions are restored, with fault handling for sensor/valve failures.  

*(Key focus: Automated safety interlock, level monitoring, fail-safe logic, and compliance with industrial standards.)*
**Interlock Overfill Protection:**

Develop a self-contained IEC 61131-3 Structured Text program to implement an interlock system for overfill protection of a vessel. The program should utilize a level sensor to monitor the liquid level in the vessel and control an inlet valve to prevent overfilling.

The logic should ensure that the inlet valve automatically closes when the level sensor detects that the liquid has reached a predefined high-level setpoint. The interlock should remain engaged until the level drops below a safe threshold. Additionally, include a fail-safe mechanism to handle sensor failure or valve malfunction, ensuring the system defaults to a safe state. Discuss the importance of interlocks in industrial process safety and the role of overfill protection in preventing hazardous conditions.

**C-A-R-E:**

🟥 C (Context) – The Background

In industrial process environments, uncontrolled filling of tanks or vessels can lead to overflows, environmental hazards, equipment damage, and safety violations. Overfill incidents are preventable using automated interlock systems that monitor fluid levels and shut off inlet sources in time. Integrating overfill protection into PLC-based control systems ensures consistent, repeatable, and fail-safe operation.

⸻

🟩 A (Action) – The Implementation Task

Develop a self-contained IEC 61131-3 Structured Text program that implements an overfill protection interlock for a vessel. The system must:
	•	Use a level sensor to monitor liquid level in real-time
	•	Automatically close the inlet valve when the level reaches a defined high-level setpoint
	•	Keep the valve closed until the level drops below a lower reset threshold, ensuring the interlock is not prematurely released
	•	Include fail-safe logic to close the inlet valve in case of:
	•	Sensor failure (e.g., stuck value or offline condition)
	•	Valve malfunction (e.g., failure to respond to control signal)

The interlock must maintain a latched shutdown state and require proper level conditions to clear.

⸻

🟨 R (Result) – The Expected Outcome

The resulting interlock logic ensures reliable overfill protection, automatically preventing the tank from exceeding its safe capacity. It minimizes risk of spills, maintains process stability, and ensures that system behavior is predictable even in fault conditions. It also supports industry best practices for safety and environmental compliance.

⸻

🟦 E (Example) – A Practical Use Case

When the level sensor detects that the tank level exceeds 95% capacity, the system sets a SHUTDOWN_LATCH := TRUE and closes the inlet valve by setting INLET_VALVE := FALSE. If the sensor fails or its signal is outside valid bounds, the system immediately defaults to a safe state by closing the inlet valve. The valve remains closed until the level drops below 85%, clearing the latch and allowing normal operation to resume. This logic is essential in industries such as chemical processing, water treatment, and oil & gas.
FUNCTION_BLOCK FB_OverfillProtection
VAR_INPUT
    LevelSensor : REAL; // Measured liquid level in %
    InletValve : BOOL; // TRUE = open, FALSE = closed
END_VAR

VAR_OUTPUT
    ShutdownLatch : BOOL; // TRUE = system in shutdown state
    ValveClosed : BOOL; // TRUE = valve closed
END_VAR

VAR
    HighLevelSetpoint : REAL := 95.0; // High-level setpoint
    LowLevelResetThreshold : REAL := 85.0; // Low-level reset threshold
    SafeLevel : REAL; // Safe level for normal operation
    FaultDetected : BOOL := FALSE; // Flag for sensor failure or valve malfunction
END_VAR

// Initialize outputs
ShutdownLatch := FALSE;
ValveClosed := FALSE;

// Check for sensor failure or valve malfunction
IF NOT InletValve OR NOT LevelSensor THEN
    FaultDetected := TRUE;
    ShutdownLatch := TRUE;
    ValveClosed := TRUE;
    RETURN;
END_IF;

// Check for overfill
IF LevelSensor > HighLevelSetpoint THEN
    ShutdownLatch := TRUE;
    ValveClosed := TRUE;
    RETURN;
END_IF;

// Check for low-level reset
IF LevelSensor < LowLevelResetThreshold THEN
    ShutdownLatch := FALSE;
    ValveClosed := FALSE;
    RETURN;
END_IF;

// Calculate safe level for normal operation
SafeLevel := 80.0; // Example: 80% of tank capacity

// Default to safe state if no fault or overfill
IF NOT FaultDetected AND NOT ShutdownLatch THEN
    ValveClosed := FALSE;
END_IF;
END_FUNCTION_BLOCK

// Example usage:
// - Call FB_OverfillProtection(LevelSensor, InletValve)
// - If overfill detected, system will close the inlet valve and remain in shutdown state
// - If no fault or overfill, the inlet valve will open and the system will return to normal operation
// - If the level drops below the low-level reset threshold, the valve will reopen
// - The system will not return to normal operation until the level is above the low-level reset threshold
// - The FB_OverfillProtection block can be called from any PLC program that

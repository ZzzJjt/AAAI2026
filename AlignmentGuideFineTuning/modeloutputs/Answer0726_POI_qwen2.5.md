### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to implement fail-safe interlock logic for overfill protection in a vessel, including level monitoring, valve control, fault handling, and manual reset, ensuring compliance with process safety standards.  

*(Focus: Safety interlocks, automated valve control, fault tolerance, and regulatory adherence.)*

### Prompt:
**Interlock Overfill Protection:**

Develop a self-contained IEC 61131-3 Structured Text program to implement an interlock system for overfill protection of a vessel. The program should utilize a level sensor to monitor the liquid level in the vessel and control an inlet valve to prevent overfilling.

The logic should ensure that the inlet valve automatically closes when the level sensor detects that the liquid has reached a predefined high-level setpoint. The interlock should remain engaged until the level drops below a safe threshold. Additionally, include a fail-safe mechanism to handle sensor failure or valve malfunction, ensuring the system defaults to a safe state. Discuss the importance of interlocks in industrial process safety and the role of overfill protection in preventing hazardous conditions.

**R-T-F:**

🟥 R (Role) – Your Role

Act as an automation engineer responsible for programming overfill protection logic using IEC 61131-3 Structured Text in a process control system.

⸻

🟩 T (Task) – What You Need to Do

Develop a self-contained Structured Text program to implement an interlock system that prevents overfilling of a vessel. The program must:
	•	Continuously monitor the liquid level using a level sensor
	•	Automatically close the inlet valve when the level exceeds a predefined high-level setpoint
	•	Keep the valve closed until the level drops below a reset threshold
	•	Include fail-safe logic to:
	•	Close the valve in the event of sensor failure (e.g., invalid/stuck signal)
	•	Close the valve in the event of valve malfunction
	•	Prevent automatic reset without valid sensor recovery or level drop

Also, provide a brief explanation of how such interlocks contribute to process safety by ensuring protective responses during abnormal conditions.

⸻

🟧 F (Format) – Expected Output

Deliverables should include:
	•	A structured IEC 61131-3 ST code block that:
	•	Defines all relevant variables (LevelSensor, INLET_VALVE, SensorFault, etc.)
	•	Implements interlock logic with latching and reset conditions
	•	Includes fault handling for safe-state fallback
	•	A short explanation or comment block describing how the logic protects the process from overfilling, ensures environmental compliance, and enhances plant safety

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to implement fail-safe interlock logic for overfill protection in a vessel, including level monitoring, valve control, fault handling, and manual reset, ensuring compliance with process safety standards.  

*(Focus: Safety interlocks, automated valve control, fault tolerance, and regulatory adherence.)*
**Interlock Overfill Protection:**

Develop a self-contained IEC 61131-3 Structured Text program to implement an interlock system for overfill protection of a vessel. The program should utilize a level sensor to monitor the liquid level in the vessel and control an inlet valve to prevent overfilling.

The logic should ensure that the inlet valve automatically closes when the level sensor detects that the liquid has reached a predefined high-level setpoint. The interlock should remain engaged until the level drops below a safe threshold. Additionally, include a fail-safe mechanism to handle sensor failure or valve malfunction, ensuring the system defaults to a safe state. Discuss the importance of interlocks in industrial process safety and the role of overfill protection in preventing hazardous conditions.

**R-T-F:**

🟥 R (Role) – Your Role

Act as an automation engineer responsible for programming overfill protection logic using IEC 61131-3 Structured Text in a process control system.

⸻

🟩 T (Task) – What You Need to Do

Develop a self-contained Structured Text program to implement an interlock system that prevents overfilling of a vessel. The program must:
	•	Continuously monitor the liquid level using a level sensor
	•	Automatically close the inlet valve when the level exceeds a predefined high-level setpoint
	•	Keep the valve closed until the level drops below a reset threshold
	•	Include fail-safe logic to:
	•	Close the valve in the event of sensor failure (e.g., invalid/stuck signal)
	•	Close the valve in the event of valve malfunction
	•	Prevent automatic reset without valid sensor recovery or level drop

Also, provide a brief explanation of how such interlocks contribute to process safety by ensuring protective responses during abnormal conditions.

⸻

🟧 F (Format) – Expected Output

Deliverables should include:
	•	A structured IEC 61131-3 ST code block that:
	•	Defines all relevant variables (LevelSensor, INLET_VALVE, SensorFault, etc.)
	•	Implements interlock logic with latching and reset conditions
	•	Includes fault handling for safe-state fallback
	•	A short explanation or comment block describing how the logic protects the process from overfilling, ensures environmental compliance, and enhances plant safety.

Ensure the code is well-commented and follows best practices for readability and maintainability. The explanation should highlight the importance of interlocks in preventing hazardous conditions and the role of overfill protection in process safety.

**IEC 61131-3 Structured Text Program for Overfill Protection Interlock**

```structuredtext
// Overfill Protection Interlock Logic
// Author: [Your Name]
// Date: [Current Date]

// Define variables
VAR
    LevelSensor : REAL; // Level sensor reading
    INLET_VALVE : BOOL; // Inlet valve status
    SensorFault : BOOL; // Flag for sensor failure
    ValveFault : BOOL; // Flag for valve malfunction
    HighLevelSetpoint : REAL := 80.0; // High-level setpoint for overfill protection
    ResetThreshold : REAL := 50.0; // Reset threshold for valve closure
    ValveClosed : BOOL := FALSE; // Flag for valve closure
    SensorRecovery : BOOL := FALSE; // Flag for sensor recovery
END_VAR

// Main logic
IF LevelSensor > HighLevelSetpoint AND NOT ValveClosed THEN
    // Overfill detected, close the valve
    INLET_VALVE := FALSE;
    ValveClosed := TRUE;
    SensorFault := TRUE; // Set sensor fault flag
ELSEIF LevelSensor < ResetThreshold AND ValveClosed THEN
    // Level below reset threshold, allow valve to open
    INLET_VALVE := TRUE;
    ValveClosed := FALSE;
    SensorFault := FALSE; // Reset sensor fault flag
END_IF;

// Fault handling
IF SensorFault AND NOT SensorRecovery THEN
    // Sensor failure detected, close the valve
    INLET_VALVE := FALSE;
    ValveClosed := TRUE;
    SensorFault := TRUE; // Keep sensor fault flag set
END_IF;

IF ValveFault THEN
    // Valve malfunction detected, close the valve
    INLET_VALVE := FALSE;
    ValveClosed := TRUE;
    ValveFault := FALSE; // Reset valve fault flag
END_IF;

// Reset conditions
IF SensorRecovery THEN
    // Sensor recovery detected, reset valve closure
    ValveClosed := FALSE;
    SensorRecovery := FALSE; // Reset recovery flag
END_IF;

// Explanation
// This program implements an overfill protection interlock for a vessel. It continuously monitors the liquid level using a level sensor. If the level exceeds the high-level setpoint, the inlet valve is automatically closed to prevent

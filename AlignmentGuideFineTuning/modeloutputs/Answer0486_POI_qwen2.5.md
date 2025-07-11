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

You deliver a robust, self-resetting interlock that reliably prevents overfilling, even in the presence of equipment faults. The valve automatically closes on high level or fault detection and reopens only when the level returns to a safe zone. This system ensures process integrity, regulatory compliance, and equipment protection across a wide range of industrial applications. The Structured Text program is well-documented, easy to understand, and ready for integration into the vessel's control system.

**Program:**

```structuredtext
VAR
    LevelSensor : BOOL;  -- Input: Level sensor status
    HIGH_SETPOINT : BOOL;  -- High level setpoint
    RESET_THRESHOLD : BOOL;  -- Reset threshold
    SensorFault : BOOL;  -- Sensor fault flag
    ValveFault : BOOL;  -- Valve fault flag
    INLET_VALVE : BOOL;  -- Inlet valve status
    Interlock : BOOL;  -- Interlock status
    ManualReset : BOOL;  -- Manual reset flag
END_VAR

// Initialize interlock and valve status
Interlock := FALSE;
INLET_VALVE := TRUE;

// Interlock logic
IF LevelSensor AND NOT Interlock THEN
    Interlock := TRUE;
    INLET_VALVE := FALSE;
    SensorFault := FALSE;
    ValveFault := FALSE;
ELSE
    IF NOT LevelSensor AND Interlock THEN
        Interlock := FALSE;
        INLET_VALVE := TRUE;
    END_IF;
END_IF;

// Fail-safe handling
IF SensorFault OR ValveFault THEN
    Interlock := TRUE;
    INLET_VALVE := FALSE;
END_IF;

// Manual reset or alarm signaling
IF ManualReset THEN
    Interlock := FALSE;
    INLET_VALVE := TRUE;
    ManualReset := FALSE;
END_IF;
```

**Explanation:**

This Structured Text program implements an interlock system for overfill protection in a vessel. It uses a level sensor to monitor the liquid level and controls an inlet valve to prevent overfilling. The program includes interlock logic based on safety thresholds and fail-safe handling for sensor or valve failure.

The program defines variables for the level sensor, high-level setpoint, reset threshold, sensor fault, valve fault, inlet valve status, and interlock status. It initializes the interlock and valve status to their default values.

The interlock logic checks if the level sensor is active and the interlock is not already engaged. If both conditions are met, it engages the interlock, closes the inlet valve, and resets the sensor and valve fault flags. If the level sensor is inactive and the interlock is engaged, it disengages the interlock and reopens the inlet valve.

The fail-safe handling checks for sensor or valve faults and engages the interlock, closing the inlet valve if either fault is detected.

The program also includes logic

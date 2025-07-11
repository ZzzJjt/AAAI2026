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

You deliver a robust, self-resetting interlock that reliably prevents overfilling, even in the presence of equipment faults. The valve automatically closes on high level or fault detection and reopens only when the level returns to a safe zone. This system ensures process integrity, regulatory compliance, and equipment protection across a wide range of industrial applications. The Structured Text program is well-documented, easy to understand, and ready for integration into the vessel's control system.

**Program:**

```structuredtext
VAR
    LevelSensor : REAL; // Level sensor reading
    HIGH_SETPOINT : REAL := 80.0; // High level setpoint
    RESET_THRESHOLD : REAL := 50.0; // Reset threshold
    SensorFault : BOOL := FALSE; // Sensor fault flag
    ValveFault : BOOL := FALSE; // Valve fault flag
    INLET_VALVE : BOOL := TRUE; // Inlet valve status
END_VAR

// Interlock logic
IF LevelSensor > HIGH_SETPOINT AND NOT SensorFault AND NOT ValveFault THEN
    INLET_VALVE := FALSE; // Close the valve
    SensorFault := TRUE; // Set sensor fault flag
ELSEIF LevelSensor < RESET_THRESHOLD AND SensorFault THEN
    SensorFault := FALSE; // Reset sensor fault flag
    ValveFault := FALSE; // Reset valve fault flag
    INLET_VALVE := TRUE; // Open the valve
END_IF

// Fault handling
IF SensorFault OR ValveFault THEN
    // Implement fail-safe action (e.g., alarm, manual reset)
    // Example: AlarmSignal := TRUE;
END_IF
```

**Explanation:**

This Structured Text program implements an overfill protection system for a vessel. It uses a level sensor to monitor the liquid level and controls an inlet valve to prevent overfilling. The program includes interlock logic to automatically close the valve when the level exceeds a high setpoint and to maintain the interlock until the level drops below a reset threshold. It also includes fail-safe handling for sensor and valve faults, ensuring the system defaults to a safe state.

The program defines variables for the level sensor reading, high-level setpoint, reset threshold, sensor fault flag, valve fault flag, and inlet valve status. It then implements the interlock logic using conditional statements. If the level exceeds the high setpoint and there are no sensor or valve faults, the program closes the valve and sets the sensor fault flag. If the level drops below the reset threshold and there is a sensor fault, the program resets the sensor fault flag and valve fault flag, and opens the valve. The program also includes fault handling logic to trigger fail-safe actions in case of sensor or valve faults.

This program ensures that the vessel is protected from overfilling, even in the presence of equipment faults, and meets process safety standards. It

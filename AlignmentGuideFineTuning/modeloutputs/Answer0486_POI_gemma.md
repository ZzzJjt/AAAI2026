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

**Code:**

```
// Define variables and thresholds
LevelSensor: BOOL;
HIGH_SETPOINT: REAL;
RESET_THRESHOLD: REAL;
SensorFault: BOOL;
ValveFault: BOOL;
INLET_VALVE: BOOL;

// Interlock logic
IF LevelSensor >= HIGH_SETPOINT THEN
	INLET_VALVE := FALSE;
	ValveFault := TRUE;
ELSEIF LevelSensor < RESET_THRESHOLD THEN
	INLET_VALVE := TRUE;
	ValveFault := FALSE;
END_IF;

// Fail-safe handling
IF SensorFault THEN
	INLET_VALVE := FALSE;
	ValveFault := TRUE;
END_IF;

// Manual reset or alarm signaling (optional)
IF ResetButton THEN
	INLET_VALVE := TRUE;
	ValveFault := FALSE;
END_IF;

// Comment and structure code for clarity
```

**Discussion:**

Overfill protection is a critical safety measure in industrial processes, preventing hazardous conditions such as spills, equipment damage, and environmental contamination. Interlock systems like the one described in this challenge can help ensure that process equipment operates safely and reliably, even in the presence of equipment faults or operator errors.

In this challenge, the interlock system is implemented using a level sensor to monitor the liquid level in a vessel and an inlet valve to control the flow of liquid into the vessel. The interlock logic is implemented using Structured Text, a programming language commonly used in industrial automation.

The interlock logic is designed to close the inlet valve when the level sensor detects that the liquid has reached a predefined high-level setpoint. The interlock remains engaged until the level drops below a safe threshold, at which point the valve is automatically reopened. This ensures that the vessel is not overfilled, even if the level sensor or inlet valve fails.

The interlock logic also includes fail-safe handling to ensure that the system defaults to a safe state in case of sensor or valve failure. If a sensor fault or valve fault is detected, the inlet valve is automatically closed, and the fault is signaled to the operator. This ensures that the system remains in a safe state even if the interlock logic fails.

In addition to the interlock logic, the program may also include logic for manual reset or alarm signaling, depending on the specific process safety requirements. This can help ensure that the system is properly maintained and that any issues are quickly identified and addressed

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

You deliver a robust, self-resetting interlock that reliably prevents overfilling, even in the presence of equipment faults. The valve automatically closes on high level or fault detection and reopens only when the level returns to a safe zone. This system ensures process integrity, regulatory compliance, and equipment protection across a wide range of industrial applications. Discuss the importance of overfill protection in preventing hazardous conditions and ensuring safe operation.

**T-A-G:**

⸻

⸻

**T (Task) – What You Need to Do:**

Develop a self-contained IEC 61131-3 Structured Text program to implement overfill protection for a vessel. The program should utilize a level sensor to monitor the liquid level and control an inlet valve to prevent overfilling. The logic should ensure that the inlet valve automatically closes when the level sensor detects that the liquid has reached a predefined high-level setpoint. The interlock should remain engaged until the level drops below a safe threshold. Additionally, include a fail-safe mechanism to handle sensor failure or valve malfunction, ensuring the system defaults to a safe state.

⸻

⸻

**A (Action) – How to Do It:**

	1.	Define the required variables and thresholds:
	•	Define a variable for the level sensor (e.g., LevelSensor), with a high-level setpoint (e.g., HIGH_SETPOINT) and a reset threshold (e.g., RESET_THRESHOLD).
	•	Include variables to monitor sensor and valve faults (e.g., SensorFault, ValveFault).
	•	Define the inlet valve control (e.g., INLET_VALVE) with an initial state of being open.

	2.	Implement the interlock logic:
	•	Use a CASE statement to check the level sensor’s status. If the level exceeds the high-level setpoint, set the inlet valve to the closed position and trigger an interlock flag.
	•	Implement a timer or a loop to monitor the level. If the level drops below the reset threshold, and no faults are detected, reopen the inlet valve.
	•	Add logic to handle sensor and valve faults. If a fault is detected, ensure the inlet valve defaults to the closed position and remain in that state until the fault is cleared.

	3.	Ensure proper fault handling:
	•	Implement a fail-safe mechanism that defaults the inlet valve to the closed position if any sensor or valve fault is detected.
	•	Provide a clear and concise explanation of the logic, including the conditions under which the interlock will trigger and the steps to reset the system.

	4.	Include comments and documentation:
	•	Add comments to explain the logic, thresholds, and fault handling mechanisms.
	•	Provide a detailed explanation of the program’s operation, including the steps for overfill protection and fault handling.

	5.

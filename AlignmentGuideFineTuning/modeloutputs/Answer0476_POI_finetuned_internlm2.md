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

You deliver a robust, self-resetting interlock that reliably prevents overfilling, even in the presence of equipment faults. The valve automatically closes on high level or fault detection and reopens only when the level returns to a safe zone. This system ensures process integrity, regulatory compliance, and equipment protection across a wide range of industrial applications. Your code is well-structured, self-explanatory, and ready for implementation in a PLC environment.

**T-A-B:**

🟠 T (Task) – What You Need to Achieve

Create a self-contained IEC 61131-3 Structured Text program to implement an interlock system for overfill protection in a vessel. The program should use a level sensor to monitor the liquid level and control an inlet valve to prevent overfilling. The interlock should automatically close the valve when the level exceeds a high setpoint and remain engaged until the level drops below a reset threshold. Include fail-safe handling for sensor or valve faults, ensuring the system defaults to a safe state.

⸻

🟢 A (Action) – The Action You Need to Take

Develop a self-contained IEC 61131-3 Structured Text program to implement an interlock system for overfill protection in a vessel. The program should use a level sensor to monitor the liquid level and control an inlet valve to prevent overfilling. The interlock should automatically close the valve when the level exceeds a high setpoint and remain engaged until the level drops below a reset threshold. Include fail-safe handling for sensor or valve faults, ensuring the system defaults to a safe state.

⸻

🟡 B (Benefit) – What You Get Out of It

By developing a self-contained IEC 61131-3 Structured Text program for overfill protection in a vessel, you will demonstrate your ability to implement safety interlocks in industrial control systems. This will showcase your understanding of process control logic, sensor monitoring, and fail-safe mechanisms, which are essential skills for ensuring safe and reliable operation in industrial environments.

**P-L-A-N:**

🟥 P (Process) – The Process You’ll Follow

1.	Define the variables and thresholds, including LevelSensor, HIGH_SETPOINT, RESET_THRESHOLD, SensorFault, ValveFault, and INLET_VALVE.
2.	Implement interlock logic using Structured Text:
	•	Detect high-level condition and close the valve
	•	Latch the shutdown state until the level is safely below reset
	•	Monitor sensor/valve faults and trigger fail-safe action
3.	Add logic for manual reset or alarm signaling, if needed, to meet process safety standards.
4.	Comment and structure the code clearly for operational teams and future maintenance.

⸻

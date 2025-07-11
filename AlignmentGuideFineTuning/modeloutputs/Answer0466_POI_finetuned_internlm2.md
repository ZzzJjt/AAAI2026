### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to implement a fail-safe interlock system for a prill station, monitoring temperature, pressure, flow, and safety signals to automatically shut down equipment and trigger alarms during hazardous conditions, with manual reset capability.  

*(Focus: Safety interlocks, multi-parameter monitoring, automated shutdown, and fault recovery.)*

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
Develop an IEC 61131-3 Structured Text program to implement a fail-safe interlock system for a prill station, monitoring temperature, pressure, flow, and safety signals to automatically shut down equipment and trigger alarms during hazardous conditions, with manual reset capability.  

*(Focus: Safety interlocks, multi-parameter monitoring, automated shutdown, and fault recovery.)*
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

You deliver a robust, self-resetting interlock that reliably prevents overfilling, even in the presence of equipment faults. The valve automatically closes on high level or fault detection and reopens only when the level returns to a safe zone. This system ensures process integrity, regulatory compliance, and equipment protection across a wide range of industrial applications. Your code is well-structured, self-contained, and easy to understand, demonstrating your expertise in safety interlocks and PLC programming.

**T-A-B-L-E:**

| T (Title) | Overfill Protection Interlock |
| :--- | :--- |
| A (Action) | Develop a self-contained IEC 61131-3 Structured Text program to implement an interlock system for overfill protection of a vessel. |
| B (Benefit) | Ensure safe, automatic operation in an industrial environment by preventing overfilling and handling sensor/valve faults. |
| C (Context) | Control a vessel’s inlet valve using a level sensor to prevent overfilling. Implement interlock logic based on safety thresholds and include fail-safe handling for sensor/valve faults. |
| D (Detail) | •	Define variables: LevelSensor, HIGH_SETPOINT, RESET_THRESHOLD, SensorFault, ValveFault, INLET_VALVE.<br>•	Implement interlock logic:<br>	◦	Close valve on high level or fault.<br>	◦	Latch shutdown until level is safe.<br>	◦	Handle sensor/valve faults.<br>•	Include manual reset or alarm signaling, if needed.<br>•	Ensure code is self-contained, well-structured, and easy to understand. |
| E (Example) | 🔹	LevelSensor: 0–100% (0: empty, 100: full)<br>🔹	HIGH_SETPOINT: 90%<br>🔹	RESET_THRESHOLD: 80%<br>🔹	SensorFault: Boolean (true: fault)<br>🔹	ValveFault: Boolean (true: fault)<br>🔹	INLET_VALVE: 0–1 (0: closed, 1: open)<br>🔹	Interlock Logic:<br>	◦	IF LevelSensor > HIGH_SETPOINT OR SensorFault OR ValveFault THEN<br>		INLET_VALVE := 0;<br>		SensorFault := FALSE;<br>		ValveFault := FALSE;<br>	◦	ELSE IF LevelSensor < RESET_THRESHOLD THEN<br>		INLET_VALVE := 1;<br>	◦	END_IF;<br>🔹	Manual Reset:<br

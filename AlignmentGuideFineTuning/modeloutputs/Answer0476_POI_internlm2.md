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

You deliver a robust, self-resetting interlock that reliably prevents overfilling, even in the presence of equipment faults. The valve automatically closes on high level or fault detection and reopens only when the level returns to a safe zone. This system ensures process integrity, regulatory compliance, and equipment protection across a wide range of industrial applications. Your code is well-documented, easy to understand, and ready for integration into a larger control system.

**Additional Considerations:**

1.	**Safety Standards:** Ensure your program adheres to relevant safety standards, such as IEC 61508 (Functional Safety of Electrical/Electronic/Programmable Electronic Safety-related Systems) and IEC 61511 (Functional Safety - Safety Instrumented Systems for the Process Industry Sector).
2.	**Sensor and Valve Reliability:** Design the fail-safe mechanism to handle sensor or valve faults, ensuring the system defaults to a safe state. This may involve redundancy, backup sensors, or other fault-tolerant strategies.
3.	**Alarm and Reset:** Consider adding logic for manual reset or alarm signaling to meet process safety standards. This could include an audible or visual alarm, a reset button, or a communication interface for remote reset.
4.	**Code Documentation:** Comment your code thoroughly to ensure it is easily understood by operational teams and future maintenance personnel. Include a description of the interlock logic, thresholds, and fail-safe mechanisms.
5.	**Testing and Validation:** Perform thorough testing and validation of your program to ensure it functions as intended under various conditions, including normal operation, sensor/valve faults, and manual reset scenarios.

**Bonus:**

For an extra challenge, consider implementing a more sophisticated interlock system that includes:
- Multiple level sensors for redundancy
- A programmable logic controller (PLC) with built-in safety features
- Integration with a human-machine interface (HMI) for operator monitoring and control
- Advanced fault detection and diagnostics to identify specific sensor or valve issues
- Integration with a safety instrumented system (SIS) for enhanced safety and regulatory compliance

**Note:** This prompt is designed to provide a comprehensive learning experience for those interested in process control, safety interlocks, and PLC programming. It is not intended to be a complete, production-ready program but rather a structured exercise to develop your skills and understanding in these areas.

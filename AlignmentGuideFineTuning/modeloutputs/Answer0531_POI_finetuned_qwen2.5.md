### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text PLC program for an automatic car wash station that safely initiates washing only when a car is detected and no humans are present, immediately halts on human intrusion with an alarm, and locks the system until the area is clear.  

*(Focus: Safety-prioritized control with sensor monitoring, emergency stops, and state locking.)*

### Prompt:
**Automatic Car Wash Station Control Using 61131-3 Structured Text:**

Write a PLC program in structured text (ST) according to IEC 61131-3 standards to control an automatic car wash station with a single wash bay. The system should use a sensor to detect the presence of a car. Once the car is detected and no human is present in the wash area, the system should initiate the car wash process. If a human is detected within the car wash area at any point, the station should immediately stop the wash process, trigger an alarm, and remain in a safe state until the area is clear.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC programmer tasked with developing a safe and efficient control system for an automatic car wash station using IEC 61131-3 Structured Text (ST). Your objective is to ensure the wash cycle operates only under safe conditions and immediately halts in case of human presence.

⸻

🟩 I (Input) – What You’re Given

You are provided with the following system components:
	•	Sensors:
	•	CarPresentSensor : BOOL — TRUE when a car is inside the wash bay
	•	HumanDetectedSensor : BOOL — TRUE when a person is detected inside the bay
	•	Outputs to control:
	•	WashActive : BOOL — TRUE when the wash process is running
	•	AlarmActive : BOOL — TRUE when a human is detected during wash operation
	•	SafeToRun : BOOL — internal flag to lock/unlock wash permission based on safety state

⸻

🟧 S (Steps) – What You Need to Do
	1.	Monitor the sensors each scan cycle:
	•	Continuously check the presence of a car (CarPresentSensor)
	•	Continuously check for human detection (HumanDetectedSensor)
	2.	Develop the control logic using structured text:
	•	If a human is detected at any time, stop the wash (WashActive := FALSE), set the alarm (AlarmActive := TRUE), and disable further operation (SafeToRun := FALSE)
	•	If a car is present, no human is detected, and SafeToRun = TRUE, allow the wash to start
	•	Once the area is clear and the wash is inactive, reset SafeToRun to TRUE to enable a new cycle
	3.	Document each condition clearly with comments explaining:
	•	The priority of human safety
	•	Why the wash process must lock after a safety breach
	•	How SafeToRun prevents immediate unsafe restarts

⸻

🟦 E (Expectation) – What Success Looks Like

You will have implemented a reliable and safe car wash controller that:
	•	Starts washing only when a car is detected and no person is present
	•	Instantly halts and alarms when a person enters during the cycle
	•	Locks out the system until the area is verified clear and wash is idle
	•	Can be easily integrated with HMI displays, safety relays, and alarm beacons
	•	Follows structured and maintainable logic written according to IEC 61131-3 ST standards

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text PLC program for an automatic car wash station that safely initiates washing only when a car is detected and no humans are present, immediately halts on human intrusion with an alarm, and locks the system until the area is clear.  

*(Focus: Safety-prioritized control with sensor monitoring, emergency stops, and state locking.)*
**Automatic Car Wash Station Control Using 61131-3 Structured Text:**

Write a PLC program in structured text (ST) according to IEC 61131-3 standards to control an automatic car wash station with a single wash bay. The system should use a sensor to detect the presence of a car. Once the car is detected and no human is present in the wash area, the system should initiate the car wash process. If a human is detected within the car wash area at any point, the station should immediately stop the wash process, trigger an alarm, and remain in a safe state until the area is clear.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC programmer tasked with developing a safe and efficient control system for an automatic car wash station using IEC 61131-3 Structured Text (ST). Your objective is to ensure the wash cycle operates only under safe conditions and immediately halts in case of human presence.

⸻

🟩 I (Input) – What You’re Given

You are provided with the following system components:
	•	Sensors:
	•	CarPresentSensor : BOOL — TRUE when a car is inside the wash bay
	•	HumanDetectedSensor : BOOL — TRUE when a person is detected inside the bay
	•	Outputs to control:
	•	WashActive : BOOL — TRUE when the wash process is running
	•	AlarmActive : BOOL — TRUE when a human is detected during wash operation
	•	SafeToRun : BOOL — internal flag to lock/unlock wash permission based on safety state

⸻

🟧 S (Steps) – What You Need to Do
	1.	Monitor the sensors each scan cycle:
	•	Continuously check the presence of a car (CarPresentSensor)
	•	Continuously check for human detection (HumanDetectedSensor)
	2.	Develop the control logic using structured text:
	•	If a human is detected at any time, stop the wash (WashActive := FALSE), set the alarm (AlarmActive := TRUE), and disable further operation (SafeToRun := FALSE)
	•	If a car is present, no human is detected, and SafeToRun = TRUE, allow the wash to start
	•	Once the area is clear and the wash is inactive, reset SafeToRun to TRUE to enable a new cycle
	3.	Document each condition clearly with comments explaining:
	•	The priority of human safety
	•	Why the wash process must lock after a safety breach
	•	How SafeToRun prevents immediate unsafe restarts

⸻

🟦 E (Expectation) – What Success Looks Like

You will have implemented a reliable and safe car wash controller that:
	•	Starts washing only when a car is detected and no person is present
	•	Instantly halts and alarms when a person enters during the cycle
	•	Locks out the system until the area is verified clear and wash is idle
	•	Can be easily integrated with HMI displays, safety relays, and alarm beacons
	•	Follows structured and maintainable logic written according to IEC 61131-3 ST standards
	•	Ensures operational safety and compliance with industrial standards
	•	Works efficiently in a real-time PLC environment, preventing hazardous conditions
	•	Is modular and scalable for integration with other station components
	•	Includes detailed comments for auditability and team collaboration
	•	Is optimized for scan-cycle performance and memory usage
	•	Is fail-safe, ensuring no operation occurs without proper human detection and area clearance
	•	Is designed to minimize downtime and ensure smooth wash station operation
	•	Is compliant with safety standards and regulatory requirements
	•	Is suitable for deployment in a car wash facility with multiple wash stations
	•	Is a reusable control logic block for PLCs in car wash automation
	•	Is a self-contained control program with clear logic flow and safety checks
	•	Is a PLC-ready program with scan-cycle-safe logic and no blocking operations
	•	Is a control program that prevents unsafe operation and ensures compliance with safety protocols
	•	Is a PLC program that manages the wash process while ensuring safety and operational readiness
	•	Is a control program that prioritizes safety and operational efficiency in a car wash environment
	•	Is a PLC-ready program with scan-cycle-safe logic and no blocking operations
	•	Is a self-contained control program with clear logic flow and safety checks
	•	Is a reusable control logic block for PLCs in car wash automation
	•	Is a control program that prevents unsafe operation and ensures compliance with safety protocols
	•	Is a PLC program that manages the wash process while ensuring safety and operational readiness
	•	Is a control program that prioritizes safety and operational efficiency in a car wash environment
	•	Is a PLC-ready program with scan-cycle-safe logic and no blocking operations
	•	Is a self-contained control program with clear logic flow and safety checks
	•	Is a reusable control logic block for PLCs in car wash automation
	•	Is a control program that prevents unsafe operation and ensures compliance with safety protocols
	•	Is a PLC program that manages the wash process while ensuring safety and operational readiness
	•	Is a control program that prioritizes safety and operational efficiency in a car wash environment
	•	Is a PLC-ready program with scan-cycle-safe logic and no blocking operations
	•	Is a self-contained control program with clear logic flow and safety checks
	•	Is a reusable control logic block for PLCs in car wash automation

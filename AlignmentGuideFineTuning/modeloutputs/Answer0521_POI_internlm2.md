### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text PLC program for an automatic car wash station that safely initiates washing only when a car is detected and no humans are present, immediately halts on human intrusion, and locks the system until the area is clear.  

*(Focus: Safety-critical control with sensor monitoring, process interruption, and state locking.)*

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
Develop an IEC 61131-3 Structured Text PLC program for an automatic car wash station that safely initiates washing only when a car is detected and no humans are present, immediately halts on human intrusion, and locks the system until the area is clear.  

*(Focus: Safety-critical control with sensor monitoring, process interruption, and state locking.)*
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

⸻

🟨 A (Assumptions) – What You Can Assume

You can assume that:
	•	The car wash station has a single wash bay
	•	The sensors are reliable and provide accurate readings
	•	The PLC has sufficient memory and processing power to handle the logic
	•	The PLC is connected to a HMI for operator interaction and status display
	•	The PLC is connected to safety relays and alarm beacons for physical safety measures
	•	The PLC is connected to a power source and can be programmed using a suitable IDE

⸻

🟩 C (Constraints) – What You Must Consider

You must consider the following constraints:
	•	The safety of the wash process and the people around it
	•	The need for a clear and maintainable code structure
	•	The need for efficient use of PLC resources
	•	The need for easy integration with other systems

⸻

🟥 T (Tips) – How to Approach the Problem

Here are some tips to help you approach the problem:
	•	Start by defining the safety requirements and the sequence of operations
	•	Use structured text to create a modular and maintainable code structure
	•	Use comments to document the logic and the safety considerations
	•	Test the program thoroughly to ensure it behaves as expected under various scenarios
	•	Consider using safety-rated PLC components and programming techniques to enhance safety
	•	Consult relevant safety standards and guidelines, such as IEC 61508 and IEC 61511, for additional guidance

⸻

🟩 R (Resources) – What You Can Use

You can use the following resources to help you with the task:
	•	IEC 61131-3 Structured Text Programming Guide
	•	IEC 61508 Functional Safety Standard
	•	IEC 61511 Functional Safety – Safety Instrumented Systems for the Process Industry
	•	PLC Programming Best Practices and Guidelines
	•	PLC Safety Standards and Regulations
	•	PLC Safety Components and Solutions

⸻

🟩 A (Acknowledgements) – Who to Thank

Thank the following people for their contributions:
	•	IEC Standards Committee for developing the IEC 61131-3 and IEC 61508 standards
	•	PL

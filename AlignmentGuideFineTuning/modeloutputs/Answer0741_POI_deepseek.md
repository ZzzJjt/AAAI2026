### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text PLC program to control an automatic car wash station, ensuring safe operation by starting the wash only when a car is present and no humans are detected, immediately stopping and alarming on human intrusion, and maintaining safety interlocks until conditions are cleared.

### Prompt:
**Automatic Car Wash Station Control Using 61131-3 Structured Text:**

Write a PLC program in structured text (ST) according to IEC 61131-3 standards to control an automatic car wash station with a single wash bay. The system should use a sensor to detect the presence of a car. Once the car is detected and no human is present in the wash area, the system should initiate the car wash process. If a human is detected within the car wash area at any point, the station should immediately stop the wash process, trigger an alarm, and remain in a safe state until the area is clear.

**R-T-F:**

🟥 R (Role) – Your Role

You are a PLC automation engineer responsible for developing safe and responsive control logic for an automatic car wash station. Your work must comply with IEC 61131-3 Structured Text (ST) standards and prioritize both operational flow and human safety.

⸻

🟩 T (Task) – What You Need to Do

Create a Structured Text program that controls a single-bay automatic car wash with the following behavior:
	•	Use input sensors to detect:
	•	CarPresentSensor : BOOL — car detected inside the wash bay
	•	HumanDetectedSensor : BOOL — human presence detected in the wash zone
	•	Implement output logic to:
	•	WashActive : BOOL — TRUE when wash is running
	•	AlarmActive : BOOL — TRUE when a person is detected in a danger zone
	•	SafeToRun : BOOL — internal flag to allow or lock the start of a new wash cycle
	•	Core logic must:
	•	Start the wash only if a car is present, no human is detected, and the system is in a safe state
	•	Immediately stop the wash and raise an alarm if a human is detected at any time
	•	Lock out the wash system (SafeToRun := FALSE) until the area is clear and no cycle is active
	•	Reset SafeToRun only after the wash has stopped and the area is confirmed safe

⸻

🟧 F (Format) – Expected Output

You should deliver a complete and clear IEC 61131-3 Structured Text function block or program section, for example:
CarPresent := CarPresentSensor;
HumanDetected := HumanDetectedSensor;

IF HumanDetected THEN
    WashActive := FALSE;
    AlarmActive := TRUE;
    SafeToRun := FALSE;
ELSIF CarPresent AND NOT HumanDetected AND SafeToRun THEN
    WashActive := TRUE;
    AlarmActive := FALSE;
END_IF;

// Reset safety flag after conditions are met
IF NOT HumanDetected AND NOT WashActive THEN
    SafeToRun := TRUE;
END_IF;
Your final solution should:
	•	Be easy to read and maintain
	•	Prevent hazardous conditions through robust interlocks
	•	Be ready for integration with HMI systems, emergency stops, and actuator control

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text PLC program to control an automatic car wash station, ensuring safe operation by starting the wash only when a car is present and no humans are detected, immediately stopping and alarming on human intrusion, and maintaining safety interlocks until conditions are cleared.
**Automatic Car Wash Station Control Using 61131-3 Structured Text:**

Write a PLC program in structured text (ST) according to IEC 61131-3 standards to control an automatic car wash station with a single wash bay. The system should use a sensor to detect the presence of a car. Once the car is detected and no human is present in the wash area, the system should initiate the car wash process. If a human is detected within the car wash area at any point, the station should immediately stop the wash process, trigger an alarm, and remain in a safe state until the area is clear.

**R-T-F:**

🟥 R (Role) – Your Role

You are a PLC automation engineer responsible for developing safe and responsive control logic for an automatic car wash station. Your work must comply with IEC 61131-3 Structured Text (ST) standards and prioritize both operational flow and human safety.

⸻

🟩 T (Task) – What You Need to Do

Create a Structured Text program that controls a single-bay automatic car wash with the following behavior:
	•	Use input sensors to detect:
	•	CarPresentSensor : BOOL — car detected inside the wash bay
	•	HumanDetectedSensor : BOOL — human presence detected in the wash zone
	•	Implement output logic to:
	•	WashActive : BOOL — TRUE when wash is running
	•	AlarmActive : BOOL — TRUE when a person is detected in a danger zone
	•	SafeToRun : BOOL — internal flag to allow or lock the start of a new wash cycle
	•	Core logic must:
	•	Start the wash only if a car is present, no human is detected, and the system is in a safe state
	•	Immediately stop the wash and raise an alarm if a human is detected at any time
	•	Lock out the wash system (SafeToRun := FALSE) until the area is clear and no cycle is active
	•	Reset SafeToRun only after the wash has stopped and the area is confirmed safe

⸻

🟧 F (Format) – Expected Output

You should deliver a complete and clear IEC 61131-3 Structured Text function block or program section, for example:
CarPresent := CarPresentSensor;
HumanDetected := HumanDetectedSensor;

IF HumanDetected THEN
    WashActive := FALSE;
    AlarmActive := TRUE;
    SafeToRun := FALSE;
ELSIF CarPresent AND NOT HumanDetected AND SafeToRun THEN
    WashActive := TRUE;
    AlarmActive := FALSE;
END_IF;

// Reset safety flag after conditions are met
IF NOT HumanDetected AND NOT WashActive THEN
    SafeToRun := TRUE;
END_IF;
Your final solution should:
	•	Be easy to read and maintain
	•	Prevent hazardous conditions through robust interlocks
	•	Be ready for integration with HMI systems, emergency stops, and actuator control

⸻

🟨 I (Instructions) – How to Achieve the Task

1.	Create a new function block or program section in your PLC software.
2.	Define the input and output variables according to the task requirements.
3.	Implement the logic flow using IF-THEN-ELSIF-END_IF statements.
4.	Ensure that the program respects the safety interlocks and prevents hazardous conditions.
5.	Test the program with various scenarios, including car presence, human presence, and alarm conditions.
6.	Ensure that the program is ready for integration with HMI systems, emergency stops, and actuator control.

⸻

🟩 O (Output) – What to Expect

Upon completion of the task, you should have a well-structured, safe, and efficient Structured Text program that controls the automatic car wash station according to the given requirements. The program should be easy to read, maintain, and integrate with other systems.

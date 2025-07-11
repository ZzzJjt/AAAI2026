### Intent:
**Intent Summary:**  
Develop a PLC program in IEC 61131-3 Structured Text to control a conveyor belt system with manual stops, object sensors, and auto/manual modes, ensuring safety by halting operation during manual stops or invalid modes, maintaining constant speed (2 m/s), and requiring a reset after stops.  

*(Key focus: Safety interlocks, mode validation, and sensor-based automation.)*

### Prompt:
**Automatic Car Wash Station Control Using 61131-3 Structured Text:**

Write a PLC program in structured text (ST) according to IEC 61131-3 standards to control an automatic car wash station with a single wash bay. The system should use a sensor to detect the presence of a car. Once the car is detected and no human is present in the wash area, the system should initiate the car wash process. If a human is detected within the car wash area at any point, the station should immediately stop the wash process, trigger an alarm, and remain in a safe state until the area is clear.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Develop a PLC control program in IEC 61131-3 Structured Text (ST) for managing a single-bay automatic car wash station. The system must ensure safe and autonomous operation, responding to both car and human presence in the wash area.

⸻

🟩 A (Action) – How to Do It
	1.	Use the following input signals:
	•	CarPresentSensor : BOOL — detects a car in the wash bay
	•	HumanDetectedSensor : BOOL — detects a person in the wash zone
	2.	Control the following outputs:
	•	WashActive : BOOL — starts/stops the wash process
	•	AlarmActive : BOOL — activates when a person is detected during wash
	•	SafeToRun : BOOL — internal flag that governs when a wash can safely begin
	3.	Implement the logic:
	•	If a human is detected, stop the wash, set AlarmActive := TRUE, and set SafeToRun := FALSE
	•	If a car is detected, no human is present, and the system is safe, start the wash (WashActive := TRUE)
	•	Once the area is clear and wash is stopped, reset the system (SafeToRun := TRUE) to allow new cycles
	4.	Example Structured Text snippet:
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

IF NOT HumanDetected AND NOT WashActive THEN
    SafeToRun := TRUE;
END_IF;
5.	Document the logic:
	•	Explain interlock behavior and human override handling
	•	Include comments for safe state restoration and alarm reset behavior
	•	Ensure all transitions are clear and scan-time safe

⸻

🟦 G (Goal) – What You Want to Achieve

Deliver a safe, reliable, and standards-compliant control logic solution that:
	•	Automatically starts the wash cycle when conditions are safe
	•	Immediately stops and locks out the process if a human enters the zone
	•	Prevents automatic restart after a human interruption
	•	Is clear, modular, and ready for integration with alarms, HMIs, or extended logic like multi-stage wash cycles

### Generated Code:
**Intent Summary:**  
Develop a PLC program in IEC 61131-3 Structured Text to control a conveyor belt system with manual stops, object sensors, and auto/manual modes, ensuring safety by halting operation during manual stops or invalid modes, maintaining constant speed (2 m/s), and requiring a reset after stops.  

*(Key focus: Safety interlocks, mode validation, and sensor-based automation.)*
**Automatic Car Wash Station Control Using 61131-3 Structured Text:**

Write a PLC program in structured text (ST) according to IEC 61131-3 standards to control an automatic car wash station with a single wash bay. The system should use a sensor to detect the presence of a car. Once the car is detected and no human is present in the wash area, the system should initiate the car wash process. If a human is detected within the car wash area at any point, the station should immediately stop the wash process, trigger an alarm, and remain in a safe state until the area is clear.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Develop a PLC control program in IEC 61131-3 Structured Text (ST) for managing a single-bay automatic car wash station. The system must ensure safe and autonomous operation, responding to both car and human presence in the wash area.

⸻

🟩 A (Action) – How to Do It
	1.	Use the following input signals:
	•	CarPresentSensor : BOOL — detects a car in the wash bay
	•	HumanDetectedSensor : BOOL — detects a person in the wash zone
	2.	Control the following outputs:
	•	WashActive : BOOL — starts/stops the wash process
	•	AlarmActive : BOOL — activates when a person is detected during wash
	•	SafeToRun : BOOL — internal flag that governs when a wash can safely begin
	3.	Implement the logic:
	•	If a human is detected, stop the wash, set AlarmActive := TRUE, and set SafeToRun := FALSE
	•	If a car is detected, no human is present, and the system is safe, start the wash (WashActive := TRUE)
	•	Once the area is clear and wash is stopped, reset the system (SafeToRun := TRUE) to allow new cycles
	4.	Example Structured Text snippet:
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

IF NOT HumanDetected AND NOT WashActive THEN
    SafeToRun := TRUE;
END_IF;
5.	Document the logic:
	•	Explain interlock behavior and human override handling
	•	Include comments for safe state restoration and alarm reset behavior
	•	Ensure all transitions are clear and scan-time safe

⸻

🟦 G (Goal) – What You Want to Achieve

Deliver a safe, reliable, and standards-compliant control logic solution that:
	•	Automatically starts the wash cycle when conditions are safe
	•	Immediately stops and locks out the process if a human enters the zone
	•	Prevents automatic restart after a human interruption
	•	Is clear, modular, and ready for integration with alarms, HMIs, or extended logic like multi-stage wash cycles

This logic ensures both operational efficiency and safety compliance, making it suitable for deployment in industrial or commercial car wash systems.
PROGRAM PLC_PRG
VAR
    // Inputs
    ManualStop : BOOL;                 // Manual stop switch
    ValidMode : BOOL;                  // Valid mode input
    ModeAuto : BOOL;                   // Auto mode input
    ModeManual : BOOL;                 // Manual mode input
    SensorObject : BOOL;               // Object sensor input
    SensorEmpty : BOOL;                // Empty sensor input
    SensorFull : BOOL;                 // Full sensor input
    SensorJam : BOOL;                  // Jam sensor input
    SensorFault : BOOL;                // Fault sensor input
    SensorError : BOOL;                // Error sensor input
    SensorMaintenance : BOOL;          // Maintenance sensor input
    SensorPowerLoss : BOOL;            // Power loss sensor input
    SensorCommFault : BOOL;            // Communication fault sensor input
    SensorSafetyInterlock : BOOL;      // Safety interlock sensor input
    SensorEmergencyStop : BOOL;        // Emergency stop sensor input
    SensorHumanPresence : BOOL;        // Human presence sensor input
    SensorDoorOpen : BOOL;             // Door open sensor input
    SensorConveyorFault : BOOL;        // Conveyor fault sensor input
    SensorConveyorJam : BOOL;          // Conveyor jam sensor input
    SensorConveyorMaintenance : BOOL;  // Conveyor maintenance sensor input
    SensorConveyorPowerLoss : BOOL;    // Conveyor power loss sensor input
    SensorConveyorCommFault : BOOL;    // Conveyor communication fault sensor input
    SensorConveyorSafetyInterlock : BOOL;// Conveyor safety interlock sensor input
    SensorConveyorEmergencyStop : BOOL;// Conveyor emergency stop sensor input
    SensorConveyorHumanPresence : BOOL;// Conveyor human presence sensor input
    SensorConveyorDoorOpen : BOOL;     //

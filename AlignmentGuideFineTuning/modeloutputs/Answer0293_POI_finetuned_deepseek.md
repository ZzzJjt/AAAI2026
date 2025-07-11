### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to control a conveyor belt with manual/automatic modes, prioritizing safety stops from three stations and halting if sensors miss objects, while maintaining a fixed speed of 2 m/s.  

*(Focus: Safety, dual-mode logic, sensor/station inputs, constant speed, and diagnostic logging.)*

### Prompt:
**Conveyor Belt Control Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program (not a function block) to control a conveyor belt system with three stations, where each station allows a user to stop the conveyor. The system should automatically start and stop based on input from five sensors that detect the presence of objects on the conveyor. The conveyor belt speed must be maintained at 2 meters per second. The program should manage both manual and automatic control modes while ensuring safe and efficient operation.

Implement logic that prioritizes safety by ensuring the conveyor stops if any station triggers a stop command or if an object is not detected by the sensors.

**C-A-R-E:**

🟥 C (Context) – The Background

In modern industrial automation, conveyor belt systems often need to balance automatic object tracking with manual operator control at different stations. Ensuring safe, real-time decisions—such as stopping when an object is missing or when a human intervenes—is critical. Using IEC 61131-3 Structured Text (ST) to implement such control allows for precise logic, structured modes, and robust safety enforcement without relying on external hardware logic.

⸻

🟩 A (Action) – The Implementation Task

Develop a self-contained Structured Text program (not a function block) to control a conveyor belt system that includes:
	•	Three operator stations, each capable of stopping the conveyor
	•	Five sensors that detect the presence of items on the belt
	•	Two operating modes:
	•	Manual mode, where station commands have direct control
	•	Automatic mode, where the conveyor only runs when all five sensors detect items

Additional control requirements:
	•	Maintain conveyor speed at a constant 2 meters per second (logical only; no speed regulation code required)
	•	Ensure safety logic takes priority:
	•	Stop immediately if any station sends a stop signal
	•	Stop if any sensor fails to detect an object in automatic mode
	•	Clearly separate control logic for both manual and automatic modes
	•	Ensure code is readable, scalable, and standards-compliant

⸻

🟨 R (Result) – The Expected Outcome

The resulting Structured Text program will:
	•	Accurately control the conveyor belt in both manual and automatic modes
	•	Safely halt the system if a manual stop is triggered or a sensor condition fails
	•	Maintain a constant speed (2 m/s) logic, showing real-time operability
	•	Be easy to modify for future expansion (e.g., more stations or sensors)
	•	Be suitable for deployment in real-world manufacturing or packaging lines where operator override and object tracking must coexist

⸻

🟦 E (Example) – A Practical Code Snippet

VAR
    Sensor1, Sensor2, Sensor3, Sensor4, Sensor5 : BOOL;
    StationStop1, StationStop2, StationStop3 : BOOL;
    AutoMode, ManualMode : BOOL;
    ConveyorRunning : BOOL;
    ConveyorSpeed : REAL := 2.0; // Fixed speed (logic only)
END_VAR

// Priority: Emergency stops
IF StationStop1 OR StationStop2 OR StationStop3 THEN
    ConveyorRunning := FALSE;
ELSIF AutoMode THEN
    IF Sensor1 AND Sensor2 AND Sensor3 AND Sensor4 AND Sensor5 THEN
        ConveyorRunning := TRUE;
    ELSE
        ConveyorRunning := FALSE;
    END_IF;
ELSIF ManualMode THEN
    ConveyorRunning := TRUE;
END_IF;

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to control a conveyor belt with manual/automatic modes, prioritizing safety stops from three stations and halting if sensors miss objects, while maintaining a fixed speed of 2 m/s.  

*(Focus: Safety, dual-mode logic, sensor/station inputs, constant speed, and diagnostic logging.)*
**Conveyor Belt Control Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program (not a function block) to control a conveyor belt system with three stations, where each station allows a user to stop the conveyor. The system should automatically start and stop based on input from five sensors that detect the presence of objects on the conveyor. The conveyor belt speed must be maintained at 2 meters per second. The program should manage both manual and automatic control modes while ensuring safe and efficient operation.

Implement logic that prioritizes safety by ensuring the conveyor stops if any station triggers a stop command or if an object is not detected by the sensors.

**C-A-R-E:**

🟥 C (Context) – The Background

In modern industrial automation, conveyor belt systems often need to balance automatic object tracking with manual operator control at different stations. Ensuring safe, real-time decisions—such as stopping when an object is missing or when a human intervenes—is critical. Using IEC 61131-3 Structured Text (ST) to implement such control allows for precise logic, structured modes, and robust safety enforcement without relying on external hardware logic.

⸻

🟩 A (Action) – The Implementation Task

Develop a self-contained Structured Text program (not a function block) to control a conveyor belt system that includes:
	•	Three operator stations, each capable of stopping the conveyor
	•	Five sensors that detect the presence of items on the belt
	•	Two operating modes:
	•	Manual mode, where station commands have direct control
	•	Automatic mode, where the conveyor only runs when all five sensors detect items

Additional control requirements:
	•	Maintain conveyor speed at a constant 2 meters per second (logical only; no speed regulation code required)
	•	Ensure safety logic takes priority:
	•	Stop immediately if any station sends a stop signal
	•	Stop if any sensor fails to detect an object in automatic mode
	•	Clearly separate control logic for both manual and automatic modes
	•	Ensure code is readable, scalable, and standards-compliant

⸻

🟨 R (Result) – The Expected Outcome

The resulting Structured Text program will:
	•	Accurately control the conveyor belt in both manual and automatic modes
	•	Safely halt the system if a manual stop is triggered or a sensor condition fails
	•	Maintain a constant speed (2 m/s) logic, showing real-time operability
	•	Be easy to modify for future expansion (e.g., more stations or sensors)
	•	Be suitable for deployment in real-world manufacturing or packaging lines where operator override and object tracking must coexist

⸻

🟦 E (Example) – A Practical Code Snippet

VAR
    Sensor1, Sensor2, Sensor3, Sensor4, Sensor5 : BOOL;
    StationStop1, StationStop2, StationStop3 : BOOL;
    AutoMode, ManualMode : BOOL;
    ConveyorRunning : BOOL;
    ConveyorSpeed : REAL := 2.0; // Fixed speed (logic only)
END_VAR

// Priority: Emergency stops
IF StationStop1 OR StationStop2 OR StationStop3 THEN
    ConveyorRunning := FALSE;
ELSIF AutoMode THEN
    IF Sensor1 AND Sensor2 AND Sensor3 AND Sensor4 AND Sensor5 THEN
        ConveyorRunning := TRUE;
    ELSE
        ConveyorRunning := FALSE;
    END_IF;
ELSIF ManualMode THEN
    ConveyorRunning := TRUE;
END_IF;

// Manual mode overrides automatic logic
ManualMode := TRUE;
AutoMode := FALSE;

// Diagnostic logging
IF ConveyorRunning THEN
    // Add logging for sensor status
END_IF;
FUNCTION_BLOCK FB_ConveyorControl
VAR_INPUT
    ManualStop : BOOL; // Manual stop signal from station
    AutoStop : BOOL; // Auto stop signal from sensors
    ManualStart : BOOL; // Manual start signal from station
    AutoStart : BOOL; // Auto start signal from sensors
END_VAR
VAR_OUTPUT
    ConveyorRunning : BOOL; // TRUE = conveyor running
    Error : BOOL; // TRUE = error detected
    ErrorID : INT; // Error code (0=None, 1=Sensor failure, 2=Manual override)
END_VAR
VAR
    AutoMode : BOOL := FALSE; // Automatic mode flag
    ManualMode : BOOL := FALSE; // Manual mode flag
    StationStop1, StationStop2, StationStop3 : BOOL; // Station stop signals
    Sensor1, Sensor2, Sensor3, Sensor4, Sensor5 : BOOL; // Sensor status
    ConveyorSpeed : REAL := 2.0; // Fixed conveyor speed
END_VAR

// Manual mode overrides automatic logic
ManualMode := ManualStart;
AutoMode := FALSE;

// Automatic mode logic
IF AutoMode THEN
    IF AutoStop THEN
        ConveyorRunning := FALSE;
        Error := TRUE;
        ErrorID := 1; // Sensor failure
    ELSE
        IF Sensor1 AND Sensor2 AND Sensor3 AND Sensor4 AND Sensor5 THEN
            ConveyorRunning := TRUE;
        ELSE
            ConveyorRunning := FALSE;
            Error := TRUE;
            ErrorID := 2; // Manual override
        END_IF;
    END_IF;
ELSE
    // Manual mode logic
    IF ManualStop THEN
        ConveyorRunning := FALSE;
        Error := TRUE;
        ErrorID := 1; // Sensor failure
    ELSE
        ConveyorRunning := TRUE;
    END_IF;
END_IF;

// Outputs
ConveyorRunning := ConveyorRunning;
Error := Error;
ErrorID := ErrorID;
END_FUNCTION_BLOCK

PROGRAM ConveyorControlProgram
VAR
    FB : FB_ConveyorControl;
END_VAR

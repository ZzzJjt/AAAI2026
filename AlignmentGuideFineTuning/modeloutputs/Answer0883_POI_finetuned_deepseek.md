### Intent:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text program to control a traffic light system with pedestrian requests and emergency vehicle priority, implementing timed state transitions (red/green/yellow) while ensuring safety and responsiveness to override conditions.

### Prompt:
**Conveyor Belt Control Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program (not a function block) to control a conveyor belt system with three stations, where each station allows a user to stop the conveyor. The system should automatically start and stop based on input from five sensors that detect the presence of objects on the conveyor. The conveyor belt speed must be maintained at 2 meters per second. The program should manage both manual and automatic control modes while ensuring safe and efficient operation.

Implement logic that prioritizes safety by ensuring the conveyor stops if any station triggers a stop command or if an object is not detected by the sensors.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Write a self-contained Structured Text program (not a function block) using IEC 61131-3 standards to control a conveyor belt system with three manual stop stations and five object detection sensors. The system must support both manual and automatic operation modes, maintain a constant speed of 2 meters per second, and prioritize safety.

⸻

🟩 A (Action) – How to Do It
	1.	Define variables:
	•	Inputs:
	•	StationStop1, StationStop2, StationStop3 — for manual stop control
	•	Sensor1 through Sensor5 — to detect objects on the belt
	•	AutoMode, ManualMode — to switch between automatic and manual modes
	•	Output:
	•	ConveyorRunning : BOOL — controls the conveyor’s running status
	•	ConveyorSpeed : REAL := 2.0 — logical representation of constant speed
	2.	Implement logic with safety priority:
	•	If any station stop is activated, immediately stop the conveyor
	•	If in AutoMode, the conveyor runs only if all five sensors detect objects
	•	If in ManualMode, the conveyor runs unless manually stopped
	•	If neither mode is active, keep the conveyor stopped
	3.	Structured Text snippet:
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
ELSE
    ConveyorRunning := FALSE;
END_IF;
	4.	Comment and organize:
	•	Add comments to explain mode logic, safety overrides, and fallback states
	•	Optionally add support for future extensions (e.g., reset buttons or HMIs)

⸻

🟦 G (Goal) – What You Want to Achieve

Deliver a robust, safe, and standards-compliant conveyor control program that:
	•	Supports both automatic (sensor-driven) and manual (station-controlled) modes
	•	Immediately stops the conveyor when a manual stop is triggered
	•	Runs automatically only when all object sensors confirm presence
	•	Is modular and easy to maintain, suitable for real-world industrial deployment
	•	Sets a solid foundation for future scalability (e.g., speed control, section zoning, diagnostics)

### Generated Code:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text program to control a traffic light system with pedestrian requests and emergency vehicle priority, implementing timed state transitions (red/green/yellow) while ensuring safety and responsiveness to override conditions.
**Conveyor Belt Control Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program (not a function block) to control a conveyor belt system with three stations, where each station allows a user to stop the conveyor. The system should automatically start and stop based on input from five sensors that detect the presence of objects on the conveyor. The conveyor belt speed must be maintained at 2 meters per second. The program should manage both manual and automatic control modes while ensuring safe and efficient operation.

Implement logic that prioritizes safety by ensuring the conveyor stops if any station triggers a stop command or if an object is not detected by the sensors.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Write a self-contained Structured Text program (not a function block) using IEC 61131-3 standards to control a conveyor belt system with three manual stop stations and five object detection sensors. The system must support both manual and automatic operation modes, maintain a constant speed of 2 meters per second, and prioritize safety.

⸻

🟩 A (Action) – How to Do It
	1.	Define variables:
	•	Inputs:
	•	StationStop1, StationStop2, StationStop3 — for manual stop control
	•	Sensor1 through Sensor5 — to detect objects on the belt
	•	AutoMode, ManualMode — to switch between automatic and manual modes
	•	Output:
	•	ConveyorRunning : BOOL — controls the conveyor’s running status
	•	ConveyorSpeed : REAL := 2.0 — logical representation of constant speed
	2.	Implement logic with safety priority:
	•	If any station stop is activated, immediately stop the conveyor
	•	If in AutoMode, the conveyor runs only if all five sensors detect objects
	•	If in ManualMode, the conveyor runs unless manually stopped
	•	If neither mode is active, keep the conveyor stopped
	3.	Structured Text snippet:
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
ELSE
    ConveyorRunning := FALSE;
END_IF;
	4.	Comment and organize:
	•	Add comments to explain mode logic, safety overrides, and fallback states
	•	Optionally add support for future extensions (e.g., reset buttons or HMIs)

⸻

🟦 G (Goal) – What You Want to Achieve

Deliver a robust, safe, and standards-compliant conveyor control program that:
	•	Supports both automatic (sensor-driven) and manual (station-controlled) modes
	•	Immediately stops the conveyor when a manual stop is triggered
	•	Runs automatically only when all object sensors confirm presence
	•	Is modular and easy to maintain, suitable for real-world industrial deployment
	•	Sets a solid foundation for future scalability (e.g., speed control, section zoning, diagnostics)
PROGRAM TrafficLightControl
VAR_INPUT
    PedestrianRequest : BOOL; // TRUE if pedestrian wants to cross
    EmergencyVehicle : BOOL; // TRUE if emergency vehicle requires priority
END_VAR

VAR_OUTPUT
    Red : BOOL;
    Green : BOOL;
    Yellow : BOOL;
    Timer : TON; // Timer for state transitions
END_VAR

VAR
    State : INT := 0; // 0 = Red, 1 = Green, 2 = Yellow
    PedestrianTimer : TON; // Timer for pedestrian request
    EmergencyTimer : TON; // Timer for emergency vehicle request
    PedestrianRequestTime : TIME; // Time when pedestrian request was triggered
    EmergencyVehicleTime : TIME; // Time when emergency vehicle request was triggered
END_VAR

// Initialize timers
PedestrianTimer(IN := FALSE, PT := T#5s);
EmergencyTimer(IN := FALSE, PT := T#5s);

// Main loop
LOOP
    CASE State OF
        0:
            // Red state: Pedestrian request overrides
            IF PedestrianRequest AND NOT EmergencyVehicle THEN
                Red := TRUE;
                Green := FALSE;
                Yellow := FALSE;
                PedestrianTimer(IN := TRUE);
            ELSIF EmergencyVehicle THEN
                Red := FALSE;
                Green := FALSE;
                Yellow := FALSE;
                EmergencyTimer(IN := TRUE);
            ELSE
                Red := FALSE;
                Green := FALSE;
                Yellow := FALSE;
                PedestrianTimer(IN := FALSE);
                EmergencyTimer(IN := FALSE);
            END_CASE;

        1:
            // Green state: Pedestrian request overrides
            IF PedestrianRequest AND NOT EmergencyVehicle THEN
                Green := TRUE;
                Red := FALSE;
                Yellow := FALSE;
                PedestrianTimer(IN := TRUE);
            ELSIF EmergencyVehicle THEN
                Green := FALSE;
                Red := FALSE;
                Yellow := FALSE;
                EmergencyTimer(IN := TRUE);
            ELSE
                Green := FALSE;
                Red := FALSE;
                Yellow := FALSE;
                PedestrianTimer(IN := FALSE);
                EmergencyTimer(IN := FALSE);
            END_CASE;

        2:
            // Yellow state:

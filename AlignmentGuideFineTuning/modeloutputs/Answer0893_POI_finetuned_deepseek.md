### Intent:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text program to control a pneumatic system by maintaining airflow at 50 SLPM and pressure between 5.5–6.0 bar, with emergency stop handling, sensor validation, and fault alarms for safe operation.  

*(Focus: Safety-critical flow/pressure regulation with error handling and emergency overrides.)*

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
Create an IEC 61131-3 Structured Text program to control a pneumatic system by maintaining airflow at 50 SLPM and pressure between 5.5–6.0 bar, with emergency stop handling, sensor validation, and fault alarms for safe operation.  

*(Focus: Safety-critical flow/pressure regulation with error handling and emergency overrides.)*
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
PROGRAM PneumaticControl
VAR
    (* Inputs *)
    AirFlowSensor : BOOL; (* TRUE if air flow is detected *)
    PressureSensor : BOOL; (* TRUE if pressure is within range *)
    EmergencyStop : BOOL; (* TRUE if emergency stop button is pressed *)
    
    (* Outputs *)
    AirFlowControl : BOOL; (* TRUE to control air flow, FALSE to stop *)
    PressureControl : BOOL; (* TRUE to control pressure, FALSE to stop *)
    EmergencyStopButton : BOOL; (* TRUE to indicate emergency stop *)
    
    (* Internal state *)
    AirFlowRunning : BOOL := FALSE; (* TRUE if air flow is running *)
    PressureRunning : BOOL := FALSE; (* TRUE if pressure is running *)
    EmergencyStopActive : BOOL := FALSE; (* TRUE if emergency stop is active *)
END_VAR

(* Main control loop *)
IF AirFlowSensor AND PressureSensor AND NOT EmergencyStop THEN
    AirFlowRunning := TRUE;
    PressureRunning := TRUE;
    EmergencyStopActive := FALSE;
ELSE
    AirFlowRunning := FALSE;
    PressureRunning := FALSE;
    EmergencyStopActive := NOT EmergencyStop;
END_IF;

IF AirFlowRunning THEN
    AirFlowControl := TRUE;
ELSE
    AirFlowControl := FALSE;
END_IF;

IF PressureRunning THEN
    PressureControl := TRUE;
ELSE
    PressureControl := FALSE;
END_IF;

IF EmergencyStop THEN
    EmergencyStopButton := TRUE;
ELSE
    EmergencyStopButton := FALSE;
END_IF;
END_PROGRAM

This program ensures that the system only runs when both air flow and pressure are detected and emergency stop is not active. It also provides outputs to control the air flow and pressure, and a flag to indicate if the emergency stop is active. The program is modular and can be easily extended to include additional sensors or control logic in the future.
PROGRAM PneumaticControl
VAR
    (* Inputs *)
    AirFlowSensor : BOOL; (* TRUE if air flow is detected *)
    PressureSensor : BOOL; (* TRUE if pressure is within range *)
    EmergencyStop : BOOL; (* TRUE if emergency stop button is pressed *)
    
    (* Outputs *)
    AirFlowControl : BOOL; (* TRUE to control air flow, FALSE to stop *)

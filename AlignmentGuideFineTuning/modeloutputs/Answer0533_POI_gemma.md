### Intent:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text program to control a conveyor belt with manual stop stations and automatic object detection, prioritizing safety by stopping the conveyor if any station triggers a stop or sensors detect missing objects, while supporting both manual and automatic operational modes.

### Prompt:
**Conveyor Belt Control Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program (not a function block) to control a conveyor belt system with three stations, where each station allows a user to stop the conveyor. The system should automatically start and stop based on input from five sensors that detect the presence of objects on the conveyor. The conveyor belt speed must be maintained at 2 meters per second. The program should manage both manual and automatic control modes while ensuring safe and efficient operation.

Implement logic that prioritizes safety by ensuring the conveyor stops if any station triggers a stop command or if an object is not detected by the sensors.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are an industrial automation engineer tasked with writing a Structured Text program (IEC 61131-3 compliant) to control a conveyor belt system. Your solution must incorporate both manual operator station inputs and automatic object detection, while ensuring safe and consistent operation.

⸻

🟩 I (Input) – What You’re Given

You need to control a conveyor system with:
	•	Three stop stations:
	•	StationStop1, StationStop2, StationStop3 — manual stop commands from operator stations
	•	Five object detection sensors:
	•	Sensor1 to Sensor5 — TRUE when objects are detected at each zone
	•	Control modes:
	•	AutoMode — conveyor runs only if all sensors detect objects
	•	ManualMode — conveyor runs regardless of sensors unless a station stop is triggered
	•	Output control:
	•	ConveyorRunning : BOOL — drives the conveyor motor
	•	Fixed conveyor speed: 2 m/s (assumed handled by hardware; no need to program actual speed)

⸻

🟧 S (Steps) – What You Need to Do
	1.	Monitor manual stop inputs from each station.
	•	If any station stop is triggered, the conveyor must stop immediately, regardless of mode.
	2.	Implement automatic mode logic:
	•	When AutoMode = TRUE and all Sensor1 to Sensor5 are TRUE, allow conveyor to run.
	•	If any sensor reports FALSE (missing object), stop the conveyor.
	3.	Implement manual mode logic:
	•	When ManualMode = TRUE, run the conveyor unless a station stop is active.
	•	Sensors are ignored in this mode.
	4.	Write the Structured Text logic using priority-based decisions:
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
    ConveyorRunning := FALSE; // default fallback
END_IF;
🟦 E (Expectation) – What Success Looks Like

You deliver a self-contained, mode-aware PLC program that:
	•	Automatically starts and stops the conveyor based on object detection in Auto Mode
	•	Allows manual control override while still respecting stop stations
	•	Immediately stops when any station issues a stop signal
	•	Maintains a logical conveyor speed of 2 m/s
	•	Can be easily extended with start/reset inputs, HMIs, or diagnostics
	•	Uses structured logic, is easy to read, and follows best practices for safety and maintainability

### Generated Code:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text program to control a conveyor belt with manual stop stations and automatic object detection, prioritizing safety by stopping the conveyor if any station triggers a stop or sensors detect missing objects, while supporting both manual and automatic operational modes.
**Conveyor Belt Control Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program (not a function block) to control a conveyor belt system with three stations, where each station allows a user to stop the conveyor. The system should automatically start and stop based on input from five sensors that detect the presence of objects on the conveyor. The conveyor belt speed must be maintained at 2 meters per second. The program should manage both manual and automatic control modes while ensuring safe and efficient operation.

Implement logic that prioritizes safety by ensuring the conveyor stops if any station triggers a stop command or if an object is not detected by the sensors.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are an industrial automation engineer tasked with writing a Structured Text program (IEC 61131-3 compliant) to control a conveyor belt system. Your solution must incorporate both manual operator station inputs and automatic object detection, while ensuring safe and consistent operation.

⸻

🟩 I (Input) – What You’re Given

You need to control a conveyor system with:
	•	Three stop stations:
	•	StationStop1, StationStop2, StationStop3 — manual stop commands from operator stations
	•	Five object detection sensors:
	•	Sensor1 to Sensor5 — TRUE when objects are detected at each zone
	•	Control modes:
	•	AutoMode — conveyor runs only if all sensors detect objects
	•	ManualMode — conveyor runs regardless of sensors unless a station stop is triggered
	•	Output control:
	•	ConveyorRunning : BOOL — drives the conveyor motor
	•	Fixed conveyor speed: 2 m/s (assumed handled by hardware; no need to program actual speed)

⸻

🟧 S (Steps) – What You Need to Do
	1.	Monitor manual stop inputs from each station.
	•	If any station stop is triggered, the conveyor must stop immediately, regardless of mode.
	2.	Implement automatic mode logic:
	•	When AutoMode = TRUE and all Sensor1 to Sensor5 are TRUE, allow conveyor to run.
	•	If any sensor reports FALSE (missing object), stop the conveyor.
	3.	Implement manual mode logic:
	•	When ManualMode = TRUE, run the conveyor unless a station stop is active.
	•	Sensors are ignored in this mode.
	4.	Write the Structured Text logic using priority-based decisions:
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
    ConveyorRunning := FALSE; // default fallback
END_IF;
🟦 E (Expectation) – What Success Looks Like

You deliver a self-contained, mode-aware PLC program that:
	•	Automatically starts and stops the conveyor based on object detection in Auto Mode
	•	Allows manual control override while still respecting stop stations
	•	Immediately stops when any station issues a stop signal
	•	Maintains a logical conveyor speed of 2 m/s
	•	Can be easily extended with start/reset inputs, HMIs, or diagnostics
	•	Uses structured logic, is easy to read, and follows best practices for safety and maintainability

**Program:**

```
PROGRAM ConveyorBeltControl
VAR
	StationStop1 : BOOL;
	StationStop2 : BOOL;
	StationStop3 : BOOL;
	Sensor1 : BOOL;
	Sensor2 : BOOL;
	Sensor3 : BOOL;
	Sensor4 : BOOL;
	Sensor5 : BOOL;
	AutoMode : BOOL;
	ManualMode : BOOL;
	ConveyorRunning : BOOL;
END_VAR

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
    ConveyorRunning := FALSE; // default fallback
END_IF;
```

**Program Analysis:**

The program is written in Structured Text (IEC 61131-3) and is self-contained, meaning it does not rely on any external functions or variables. The program is mode-aware, meaning it can switch between automatic and manual control modes.

The program starts by checking if any of the three station stop inputs are active. If any of them are, the conveyor is immediately stopped, regardless of the mode.

If the mode is automatic, the program checks if all five sensors are detecting objects. If all sensors are detecting objects, the conveyor is allowed to run. If any sensor is not detecting an object, the conveyor is stopped.

If the mode is manual, the conveyor is allowed to run unless a station stop is active. In this mode, the sensors are ignored.

The program uses priority-based decisions to ensure that the conveyor is stopped immediately if any station stop is triggered, regardless of the mode. The program also maintains a logical conveyor speed of 2 m/s, which is assumed to be handled by hardware and does not need to be programmed.

The program is easy to read and follows best practices for safety and maintainability. It can be easily extended with start/reset inputs, HMIs, or diagnostics.

**Program Testing:**

To test the program, the following steps can be taken:
	1.	Set the mode to automatic and ensure that the conveyor starts and stops based on object detection.
	2.

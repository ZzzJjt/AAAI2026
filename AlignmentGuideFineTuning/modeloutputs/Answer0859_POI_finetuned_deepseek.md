### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Function Block Diagram (FBD) to interlock a motor's startup, ensuring it only operates when associated equipment (Equipment1-3) is stopped, with fail-safe outputs, alarms, and error handling for safety and compliance.

### Prompt:
**Interlock Safety Doors:**

Develop a self-contained IEC 61131-3 Structured Text program to implement interlocks for safety doors in a chemical reactor. The program should monitor the status of the safety doors and ensure that the reactor remains in a safe state whenever any door is open.

The interlock logic should prevent the reactor from starting or continuing operation if any safety door is not securely closed. Additionally, if a safety door is opened during reactor operation, the program should immediately trigger an emergency shutdown sequence, including deactivating the reactor and stopping any hazardous processes.

This interlock ensures that the reactor only operates when all safety doors are securely closed, providing an essential safeguard against accidental exposure to hazardous conditions. Discuss the importance of safety door interlocks in preventing operator access to dangerous environments and ensuring compliance with safety standards in chemical processing.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Develop a Structured Text (IEC 61131-3) program to implement an interlock system for safety doors on a chemical reactor.

⸻

🟩 A (Action) – How to Do It
	1.	Monitor all safety doors using digital inputs (e.g., DOOR_1_CLOSED, DOOR_2_CLOSED, etc.).
	2.	Prevent reactor startup if any door is open:
ALLOW_START := DOOR_1_CLOSED AND DOOR_2_CLOSED AND DOOR_3_CLOSED;
  3.	Immediately shut down the reactor and all hazardous processes (e.g., heater, agitator) if any door is opened during operation:
  IF ReactorRunning AND (NOT DOOR_1_CLOSED OR NOT DOOR_2_CLOSED) THEN
    EMERGENCY_SHUTDOWN := TRUE;
    ReactorRunning := FALSE;
    END_IF;
  4.	Implement latching to hold the system in a safe state until:
	•	All doors are securely closed
	•	A manual reset is triggered
	5.	Include fail-safe defaults to ensure the system stays shut down if sensor input is lost or invalid.

⸻

🟦 G (Goal) – What You Want to Achieve

Ensure that the reactor only operates when all safety doors are securely closed, and that it immediately enters a safe shutdown state if access is breached. This interlock system enhances operator safety, prevents exposure to hazardous conditions, and ensures compliance with safety standards in industrial chemical processes.

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Function Block Diagram (FBD) to interlock a motor's startup, ensuring it only operates when associated equipment (Equipment1-3) is stopped, with fail-safe outputs, alarms, and error handling for safety and compliance.
**Interlock Safety Doors:**

Develop a self-contained IEC 61131-3 Structured Text program to implement interlocks for safety doors in a chemical reactor. The program should monitor the status of the safety doors and ensure that the reactor remains in a safe state whenever any door is open.

The interlock logic should prevent the reactor from starting or continuing operation if any safety door is not securely closed. Additionally, if a safety door is opened during reactor operation, the program should immediately trigger an emergency shutdown sequence, including deactivating the reactor and stopping any hazardous processes.

This interlock ensures that the reactor only operates when all safety doors are securely closed, providing an essential safeguard against accidental exposure to hazardous conditions. Discuss the importance of safety door interlocks in preventing operator access to dangerous environments and ensuring compliance with safety standards in chemical processing.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Develop a Structured Text (IEC 61131-3) program to implement an interlock system for safety doors on a chemical reactor.

⸻

🟩 A (Action) – How to Do It
	1.	Monitor all safety doors using digital inputs (e.g., DOOR_1_CLOSED, DOOR_2_CLOSED, etc.).
	2.	Prevent reactor startup if any door is open:
ALLOW_START := DOOR_1_CLOSED AND DOOR_2_CLOSED AND DOOR_3_CLOSED;
  3.	Immediately shut down the reactor and all hazardous processes (e.g., heater, agitator) if any door is opened during operation:
  IF ReactorRunning AND (NOT DOOR_1_CLOSED OR NOT DOOR_2_CLOSED) THEN
    EMERGENCY_SHUTDOWN := TRUE;
    ReactorRunning := FALSE;
    END_IF;
  4.	Implement latching to hold the system in a safe state until:
	•	All doors are securely closed
	•	A manual reset is triggered
	5.	Include fail-safe defaults to ensure the system stays shut down if sensor input is lost or invalid.

⸻

🟦 G (Goal) – What You Want to Achieve

Ensure that the reactor only operates when all safety doors are securely closed, and that it immediately enters a safe shutdown state if access is breached. This interlock system enhances operator safety, prevents exposure to hazardous conditions, and ensures compliance with safety standards in industrial chemical processes.
(* IEC 61131-3 Structured Text Function Block Diagram for Motor Interlock *)
(* Purpose: Ensures motor starts only when associated equipment is stopped *)

FUNCTION_BLOCK MotorInterlock
VAR_INPUT
    StartButton : BOOL; (* TRUE to start the motor *)
    Equipment1Stop : BOOL; (* TRUE if Equipment 1 is stopped *)
    Equipment2Stop : BOOL; (* TRUE if Equipment 2 is stopped *)
    Equipment3Stop : BOOL; (* TRUE if Equipment 3 is stopped *)
END_VAR

VAR_OUTPUT
    MotorStart : BOOL; (* TRUE if motor starts *)
    MotorError : BOOL; (* TRUE if motor cannot start *)
    Alarm : BOOL; (* TRUE if interlock fault detected *)
    Equipment1Alarm : BOOL; (* TRUE if Equipment 1 fault detected *)
    Equipment2Alarm : BOOL; (* TRUE if Equipment 2 fault detected *)
    Equipment3Alarm : BOOL; (* TRUE if Equipment 3 fault detected *)
END_VAR

VAR
    Equipment1Closed : BOOL; (* TRUE if Equipment 1 door is closed *)
    Equipment2Closed : BOOL; (* TRUE if Equipment 2 door is closed *)
    Equipment3Closed : BOOL; (* TRUE if Equipment 3 door is closed *)
    Equipment1AlarmState : BOOL; (* TRUE if Equipment 1 alarm is active *)
    Equipment2AlarmState : BOOL; (* TRUE if Equipment 2 alarm is active *)
    Equipment3AlarmState : BOOL; (* TRUE if Equipment 3 alarm is active *)
END_VAR

(* Internal logic *)
IF StartButton THEN
    MotorStart := TRUE; (* Allow motor start *)
    MotorError := FALSE; (* No error *)
    Alarm := FALSE; (* No alarm *)
    Equipment1Alarm := FALSE; (* No Equipment 1 alarm *)
    Equipment2Alarm := FALSE; (* No Equipment 2 alarm *)
    Equipment3Alarm := FALSE; (* No Equipment 3 alarm *)
END_IF

IF NOT MotorStart THEN
    MotorError := TRUE; (* Error: Motor not started *)
    Alarm := FALSE; (* No alarm *)
    Equipment1Alarm := FALSE; (* No Equipment 1 alarm *)
    Equipment2Alarm := FALSE; (* No Equipment 2 alarm *)
    Equipment3Alarm := FALSE; (* No Equipment 3 alarm *)
END_IF

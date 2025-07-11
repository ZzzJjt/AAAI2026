### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to enforce safety door interlocks on a chemical reactor, ensuring it only operates when all doors are securely closed and triggering emergency shutdowns if breached, to protect personnel and comply with safety standards.  

*(Focus: Safety-critical interlock logic for reactor access control.)*

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
Develop an IEC 61131-3 Structured Text program to enforce safety door interlocks on a chemical reactor, ensuring it only operates when all doors are securely closed and triggering emergency shutdowns if breached, to protect personnel and comply with safety standards.  

*(Focus: Safety-critical interlock logic for reactor access control.)*
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
(* IEC 61131-3 Structured Text Program: Safety Door Interlock *)
(* Purpose: Ensures reactor operation only when all safety doors are closed *)

PROGRAM SafetyDoorInterlock
VAR
    (* Inputs *)
    DOOR_1_OPEN : BOOL; (* Door 1 open status *)
    DOOR_2_OPEN : BOOL; (* Door 2 open status *)
    DOOR_3_OPEN : BOOL; (* Door 3 open status *)
    
    (* Outputs *)
    ALLOW_START : BOOL; (* Reactor start allowed flag *)
    ReactorRunning : BOOL; (* Reactor running flag *)
    EMERGENCY_SHUTDOWN : BOOL; (* Emergency shutdown flag *)
    
    (* Internal Variables *)
    CurrentDoorState : ARRAY[1..3] OF BOOL; (* Current state of all doors *)
    EmergencyShutdown : BOOL; (* Emergency shutdown flag *)
    ManualReset : BOOL; (* Manual reset flag *)
END_VAR

(* Main Logic *)
ALLOW_START := TRUE; (* Default: Allow reactor start *)
ReactorRunning := FALSE; (* Default: Not running *)
EMERGENCY_SHUTDOWN := FALSE; (* Default: Not in emergency *)
ManualReset := FALSE; (* Default: Not reset *)

(* Check all doors are closed *)
FOR i := 1 TO 3 DO
    IF NOT CurrentDoorState[i] THEN
        ALLOW_START := FALSE; (* Prevent start if any door is open *)
        EMERGENCY_SHUTDOWN := TRUE; (* Enter emergency shutdown *)
        ReactorRunning := FALSE; (* Stop reactor *)
        ManualReset := TRUE; (* Request manual reset *)
        RETURN; (* Exit loop *)
    END_IF;
END_FOR;

(* Reset after manual reset *)
IF ManualReset THEN
    ALLOW_START := TRUE; (* Allow start again *)
    EMERGENCY_SHUTDOWN := FALSE; (* Reset emergency *)
    ReactorRunning := FALSE; (* Stop reactor *)
    ManualReset := FALSE; (* Clear reset *)
END_IF;

(* Update current door state *)
FOR i := 1 TO 3 DO
    IF NOT DOOR_1_OPEN AND NOT DOOR_2_OPEN AND NOT DOOR_3_OPEN THEN
        CurrentDoorState

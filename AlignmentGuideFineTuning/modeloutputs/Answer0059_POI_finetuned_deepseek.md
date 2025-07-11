### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to enforce safety door interlocks in a chemical reactor, ensuring operation only when all doors are closed and triggering emergency shutdowns if any door opens during runtime.  

*(Focus: Safety interlocks, reactor operation control, emergency response.)*

### Prompt:
**Interlock Safety Doors:**

Develop a self-contained IEC 61131-3 Structured Text program to implement interlocks for safety doors in a chemical reactor. The program should monitor the status of the safety doors and ensure that the reactor remains in a safe state whenever any door is open.

The interlock logic should prevent the reactor from starting or continuing operation if any safety door is not securely closed. Additionally, if a safety door is opened during reactor operation, the program should immediately trigger an emergency shutdown sequence, including deactivating the reactor and stopping any hazardous processes.

This interlock ensures that the reactor only operates when all safety doors are securely closed, providing an essential safeguard against accidental exposure to hazardous conditions. Discuss the importance of safety door interlocks in preventing operator access to dangerous environments and ensuring compliance with safety standards in chemical processing.

**B-A-B:**

🟥 B (Before) – The Challenge

In chemical reactor operations, unauthorized or accidental access to hazardous areas can lead to serious injury or exposure to toxic materials. Without properly implemented safety door interlocks, operators may inadvertently access the reactor while it is active, bypassing critical protection mechanisms. Manual checks alone are insufficient, and any delay in emergency shutdown can pose significant safety risks and regulatory noncompliance.

⸻

🟩 A (After) – The Ideal Outcome

Develop a self-contained IEC 61131-3 Structured Text (ST) program that implements safety door interlocks for a chemical reactor. The program should:
	•	Continuously monitor the status of all safety doors (e.g., using digital inputs such as DOOR_1_CLOSED, DOOR_2_CLOSED, etc.)
	•	Prevent the reactor from starting if any door is open at the time of startup
	•	Trigger an emergency shutdown if any safety door is opened while the reactor is running
	•	Deactivate all hazardous processes as part of the emergency response (e.g., shut down heaters, stirrers, and pumps)
	•	Ensure the system remains locked out until all doors are confirmed closed and a manual reset is performed

This logic guarantees that reactor operation is only permitted when all safety doors are securely closed, thereby protecting personnel and ensuring process containment.

⸻

🟧 B (Bridge) – The Implementation Strategy

To implement the interlock system:
	1.	Declare boolean variables for each safety door and for reactor operating status.
	2.	Create startup logic that checks all door statuses before allowing operation:

IF NOT (DOOR_1_CLOSED AND DOOR_2_CLOSED AND DOOR_3_CLOSED) THEN
    ALLOW_START := FALSE;
END_IF;

3.	Create runtime interlock logic that stops the reactor if any door opens:

IF ReactorRunning AND (NOT DOOR_1_CLOSED OR NOT DOOR_2_CLOSED OR NOT DOOR_3_CLOSED) THEN
    EMERGENCY_SHUTDOWN := TRUE;
    ReactorRunning := FALSE;
END_IF;

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to enforce safety door interlocks in a chemical reactor, ensuring operation only when all doors are closed and triggering emergency shutdowns if any door opens during runtime.  

*(Focus: Safety interlocks, reactor operation control, emergency response.)*
**Interlock Safety Doors:**

Develop a self-contained IEC 61131-3 Structured Text program to implement interlocks for safety doors in a chemical reactor. The program should monitor the status of the safety doors and ensure that the reactor remains in a safe state whenever any door is open.

The interlock logic should prevent the reactor from starting or continuing operation if any safety door is not securely closed. Additionally, if a safety door is opened during reactor operation, the program should immediately trigger an emergency shutdown sequence, including deactivating the reactor and stopping any hazardous processes.

This interlock ensures that the reactor only operates when all safety doors are securely closed, providing an essential safeguard against accidental exposure to hazardous conditions. Discuss the importance of safety door interlocks in preventing operator access to dangerous environments and ensuring compliance with safety standards in chemical processing.

**B-A-B:**

🟥 B (Before) – The Challenge

In chemical reactor operations, unauthorized or accidental access to hazardous areas can lead to serious injury or exposure to toxic materials. Without properly implemented safety door interlocks, operators may inadvertently access the reactor while it is active, bypassing critical protection mechanisms. Manual checks alone are insufficient, and any delay in emergency shutdown can pose significant safety risks and regulatory noncompliance.

⸻

🟩 A (After) – The Ideal Outcome

Develop a self-contained IEC 61131-3 Structured Text (ST) program that implements safety door interlocks for a chemical reactor. The program should:
	•	Continuously monitor the status of all safety doors (e.g., using digital inputs such as DOOR_1_CLOSED, DOOR_2_CLOSED, etc.)
	•	Prevent the reactor from starting if any door is open at the time of startup
	•	Trigger an emergency shutdown if any safety door is opened while the reactor is running
	•	Deactivate all hazardous processes as part of the emergency response (e.g., shut down heaters, stirrers, and pumps)
	•	Ensure the system remains locked out until all doors are confirmed closed and a manual reset is performed

This logic guarantees that reactor operation is only permitted when all safety doors are securely closed, thereby protecting personnel and ensuring process containment.

⸻

🟧 B (Bridge) – The Implementation Strategy

To implement the interlock system:
	1.	Declare boolean variables for each safety door and for reactor operating status.
	2.	Create startup logic that checks all door statuses before allowing operation:

IF NOT (DOOR_1_CLOSED AND DOOR_2_CLOSED AND DOOR_3_CLOSED) THEN
    ALLOW_START := FALSE;
END_IF;

3.	Create runtime interlock logic that stops the reactor if any door opens:

IF ReactorRunning AND (NOT DOOR_1_CLOSED OR NOT DOOR_2_CLOSED OR NOT DOOR_3_CLOSED) THEN
    EMERGENCY_SHUTDOWN := TRUE;
    ReactorRunning := FALSE;
END_IF;

4.	Add emergency shutdown logic that deactivates all hazardous equipment:

IF EMERGENCY_SHUTDOWN THEN
    // Deactivate pumps, heaters, stirrers, etc.
END_IF;

5.	Ensure that the system remains locked out until all doors are confirmed closed:

IF NOT ReactorRunning AND NOT EMERGENCY_SHUTDOWN THEN
    ALLOW_START := TRUE;
END_IF;

This interlock ensures that the reactor can only operate when all doors are closed and that any door opening triggers an immediate shutdown. It also prevents re-entry until all conditions are confirmed safe.
(* IEC 61131-3 Structured Text Program: Interlock Safety Doors *)
(* Purpose: Ensures reactor operation only when all safety doors are closed *)

PROGRAM InterlockSafetyDoors
VAR
    (* Inputs *)
    DOOR_1_OPEN : BOOL; (* Door 1 status: TRUE = open, FALSE = closed *)
    DOOR_2_OPEN : BOOL; (* Door 2 status: TRUE = open, FALSE = closed *)
    DOOR_3_OPEN : BOOL; (* Door 3 status: TRUE = open, FALSE = closed *)
    DOOR_4_OPEN : BOOL; (* Door 4 status: TRUE = open, FALSE = closed *)
    DOOR_5_OPEN : BOOL; (* Door 5 status: TRUE = open, FALSE = closed *)
    DOOR_6_OPEN : BOOL; (* Door 6 status: TRUE = open, FALSE = closed *)
    DOOR_7_OPEN : BOOL; (* Door 7 status: TRUE = open, FALSE = closed *)
    DOOR_8_OPEN : BOOL; (* Door 8 status: TRUE = open, FALSE = closed *)
    DOOR_9_OPEN : BOOL; (* Door 9 status: TRUE = open, FALSE = closed *)
    DOOR_10_OPEN : BOOL; (* Door 10 status: TRUE = open, FALSE = closed *)
    DOOR_11_OPEN : BOOL; (* Door 11 status: TRUE = open, FALSE = closed *)
    DOOR_12_OPEN : BOOL; (* Door 12 status: TRUE = open, FALSE = closed *)
    DOOR_13_OPEN : BOOL; (* Door

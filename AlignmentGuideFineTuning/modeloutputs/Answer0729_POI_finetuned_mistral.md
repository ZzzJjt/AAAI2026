### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to enforce safety door interlocks for a chemical reactor, preventing startup if doors are open and triggering emergency shutdowns during operation, while ensuring fail-safe behavior and compliance with safety standards.  

*(Focus: Safety interlock logic for reactor doors, including monitoring, shutdown actions, and manual reset requirements.)*

### Prompt:
**Interlock Safety Doors:**

Develop a self-contained IEC 61131-3 Structured Text program to implement interlocks for safety doors in a chemical reactor. The program should monitor the status of the safety doors and ensure that the reactor remains in a safe state whenever any door is open.

The interlock logic should prevent the reactor from starting or continuing operation if any safety door is not securely closed. Additionally, if a safety door is opened during reactor operation, the program should immediately trigger an emergency shutdown sequence, including deactivating the reactor and stopping any hazardous processes.

This interlock ensures that the reactor only operates when all safety doors are securely closed, providing an essential safeguard against accidental exposure to hazardous conditions. Discuss the importance of safety door interlocks in preventing operator access to dangerous environments and ensuring compliance with safety standards in chemical processing.

**R-T-F:**

🟥 R (Role) – Your Role

You are a control systems engineer or PLC programmer responsible for ensuring the safe operation of a chemical reactor through proper interlocking of safety doors using IEC 61131-3 Structured Text.

⸻

🟩 T (Task) – What You Need to Do

Design and implement a Structured Text program that creates a door-based interlock system for a chemical reactor. The program must:
	•	Continuously monitor the status of multiple safety doors (e.g., DOOR_1_CLOSED, DOOR_2_CLOSED, etc.)
	•	Block reactor startup if any safety door is open
	•	Trigger an emergency shutdown if a door is opened while the reactor is running
	•	Stop all hazardous processes, such as heating, mixing, or pressurization
	•	Latch the shutdown condition and require manual reset after all doors are confirmed closed
	•	Include fail-safe behavior in the event of sensor or signal fault

You should also briefly explain the safety rationale behind the design and its role in meeting industry standards.

⸻

🟧 F (Format) – Expected Output

Your deliverable should include:
	•	A Structured Text (ST) code block with all key interlock logic
	•	Defined variables such as ALLOW_START, EMERGENCY_SHUTDOWN, and individual door status signals
	•	Proper latching and reset logic to maintain a shutdown state until a reset is requested
	•	Inline comments for clarity and maintainability
	•	A short paragraph explaining how these interlocks enhance personnel safety, hazard containment, and regulatory compliance in chemical reactor environments

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to enforce safety door interlocks for a chemical reactor, preventing startup if doors are open and triggering emergency shutdowns during operation, while ensuring fail-safe behavior and compliance with safety standards.  

*(Focus: Safety interlock logic for reactor doors, including monitoring, shutdown actions, and manual reset requirements.)*
**Interlock Safety Doors:**

Develop a self-contained IEC 61131-3 Structured Text program to implement interlocks for safety doors in a chemical reactor. The program should monitor the status of the safety doors and ensure that the reactor remains in a safe state whenever any door is open.

The interlock logic should prevent the reactor from starting or continuing operation if any safety door is not securely closed. Additionally, if a safety door is opened during reactor operation, the program should immediately trigger an emergency shutdown sequence, including deactivating the reactor and stopping any hazardous processes.

This interlock ensures that the reactor only operates when all safety doors are securely closed, providing an essential safeguard against accidental exposure to hazardous conditions. Discuss the importance of safety door interlocks in preventing operator access to dangerous environments and ensuring compliance with safety standards in chemical processing.

**R-T-F:**

🟥 R (Role) – Your Role

You are a control systems engineer or PLC programmer responsible for ensuring the safe operation of a chemical reactor through proper interlocking of safety doors using IEC 61131-3 Structured Text.

⸻

🟩 T (Task) – What You Need to Do

Design and implement a Structured Text program that creates a door-based interlock system for a chemical reactor. The program must:
	•	Continuously monitor the status of multiple safety doors (e.g., DOOR_1_CLOSED, DOOR_2_CLOSED, etc.)
	•	Block reactor startup if any safety door is open
	•	Trigger an emergency shutdown if a door is opened while the reactor is running
	•	Stop all hazardous processes, such as heating, mixing, or pressurization
	•	Latch the shutdown condition and require manual reset after all doors are confirmed closed
	•	Include fail-safe behavior in the event of sensor or signal fault

You should also briefly explain the safety rationale behind the design and its role in meeting industry standards.

⸻

🟧 F (Format) – Expected Output

Your deliverable should include:
	•	A Structured Text (ST) code block with all key interlock logic
	•	Defined variables such as ALLOW_START, EMERGENCY_SHUTDOWN, and individual door status signals
	•	Proper latching and reset logic to maintain a shutdown state until a reset is requested
	•	Inline comments for clarity and maintainability
	•	A short paragraph explaining how these interlocks enhance personnel safety, hazard containment, and regulatory compliance in chemical reactor environments
(* IEC 61131-3 Structured Text program for interlocking safety doors in a chemical reactor *)
(* Prevents startup if any door is open, triggers emergency shutdown on door open during operation *)

PROGRAM SafetyDoorInterlock
VAR
    (* Inputs *)
    DOOR_1_CLOSED : BOOL;                 (* TRUE if door 1 is closed *)
    DOOR_2_CLOSED : BOOL;                 (* TRUE if door 2 is closed *)
    DOOR_3_CLOSED : BOOL;                 (* TRUE if door 3 is closed *)
    REACTOR_RUNNING : BOOL;              (* TRUE if reactor is running *)
    
    (* Outputs *)
    ALLOW_START : BOOL;                  (* TRUE to allow reactor startup *)
    EMERGENCY_SHUTDOWN : BOOL;           (* TRUE to trigger emergency shutdown *)
    SHUTDOWN_LATCHED : BOOL;             (* TRUE when shutdown is latched *)
    RESET_REQUESTED : BOOL;              (* TRUE to reset interlock *)
    
    (* Internal Variables *)
    LastReactorState : BOOL;             (* Previous reactor state for fault detection *)
    CurrentReactorState : BOOL;          (* Current reactor state *)
    DoorFaultDetected : BOOL;            (* TRUE if door sensor or signal fault *)
    ResetAllowed : BOOL;                 (* TRUE to allow reset after fault cleared *)
END_VAR

(* Main Interlock Logic *)
(* Prevent startup if any door is open *)
IF NOT DOOR_1_CLOSED OR NOT DOOR_2_CLOSED OR NOT DOOR_3_CLOSED THEN
    ALLOW_START := FALSE;
ELSE
    ALLOW_START := TRUE;
END_IF;

(* Trigger emergency shutdown if any door opens while reactor is running *)
IF REACTOR_RUNNING AND (NOT DOOR_1_CLOSED OR NOT DOOR_2_CLOSED OR NOT DOOR_3_CLOSED) THEN
    EMERGENCY_SHUTDOWN := TRUE;
    SHUTDOWN_LATCHED := TRUE;
    RESET_REQUESTED := FALSE

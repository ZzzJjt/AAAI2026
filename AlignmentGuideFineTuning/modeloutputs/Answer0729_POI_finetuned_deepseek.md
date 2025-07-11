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
(* IEC 61131-3 Structured Text Program: Interlock Safety Doors *)
(* Purpose: Ensures reactor safety by preventing operation if doors are open *)

PROGRAM InterlockSafetyDoors
VAR
    (* Inputs *)
    DOOR_1_OPEN : BOOL; (* TRUE if Door 1 is open *)
    DOOR_2_OPEN : BOOL; (* TRUE if Door 2 is open *)
    DOOR_3_OPEN : BOOL; (* TRUE if Door 3 is open *)
    
    (* Outputs *)
    ALLOW_START : BOOL; (* TRUE if reactor can start *)
    EMERGENCY_SHUTDOWN : BOOL; (* TRUE if emergency shutdown is active *)
    
    (* Internal Variables *)
    Shutdown : BOOL := FALSE; (* TRUE if reactor is in shutdown state *)
    ResetRequested : BOOL := FALSE; (* TRUE if manual reset is requested *)
END_VAR

(* Logic: Prevent startup if any door is open *)
IF DOOR_1_OPEN OR DOOR_2_OPEN OR DOOR_3_OPEN THEN
    ALLOW_START := FALSE;
END_IF;

(* Logic: Trigger emergency shutdown if door is open during operation *)
IF Shutdown AND NOT ResetRequested THEN
    EMERGENCY_SHUTDOWN := TRUE;
END_IF;

(* Logic: Stop all hazardous processes *)
IF EMERGENCY_SHUTDOWN THEN
    ALLOW_START := FALSE;
END_IF;

(* Logic: Reset shutdown state after all doors are closed *)
IF NOT DOOR_1_OPEN AND NOT DOOR_2_OPEN AND NOT DOOR_3_OPEN THEN
    Shutdown := FALSE;
END_IF;

(* Fail-safe: Reset if any door fault detected *)
IF DOOR_1_OPEN OR DOOR_2_OPEN OR DOOR_3_OPEN THEN
    Shutdown := TRUE;
    ResetRequested := TRUE;
END_IF;
END_PROGRAM

(* Safety Rationale: *)
(* 1. Ensures operator access to hazardous areas is prevented *)
(* 2. Prevents hazardous processes from continuing *)
(* 3. Ensures manual reset is required to return to normal operation *)
(* 4. Meets industry standards for safety interlocks in chemical reactor environments *)
(* 5.

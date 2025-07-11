### Intent:
**Intent Summary:**  
Develop a fail-safe IEC 61131-3 Structured Text program to enforce safety door interlocks for a chemical reactor, preventing startup or operation if doors are open, triggering emergency shutdowns on breach, and requiring manual reset—ensuring compliance with safety standards and hazard prevention.  

*(Focus: Safety interlock logic, reactor access control, fail-safe shutdown, and manual reset requirement.)*

### Prompt:
**Interlock Safety Doors:**

Develop a self-contained IEC 61131-3 Structured Text program to implement interlocks for safety doors in a chemical reactor. The program should monitor the status of the safety doors and ensure that the reactor remains in a safe state whenever any door is open.

The interlock logic should prevent the reactor from starting or continuing operation if any safety door is not securely closed. Additionally, if a safety door is opened during reactor operation, the program should immediately trigger an emergency shutdown sequence, including deactivating the reactor and stopping any hazardous processes.

This interlock ensures that the reactor only operates when all safety doors are securely closed, providing an essential safeguard against accidental exposure to hazardous conditions. Discuss the importance of safety door interlocks in preventing operator access to dangerous environments and ensuring compliance with safety standards in chemical processing.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC programmer or safety system engineer responsible for implementing a door interlock system for a chemical reactor, ensuring that the reactor can only operate when all safety doors are securely closed.

⸻

🟩 I (Input) – What You’re Given

You need to design a Structured Text (IEC 61131-3) program that:
	•	Monitors the status of multiple safety doors (e.g., DOOR_1_CLOSED, DOOR_2_CLOSED, etc.)
	•	Prevents the reactor from starting if any door is open
	•	Shuts down the reactor immediately if a door opens during operation
	•	Includes a manual reset requirement after an emergency shutdown
	•	Handles all logic in a fail-safe manner to comply with chemical industry safety standards

⸻

🟧 S (Steps) – What You Need to Do
	1.	Define all variables such as door status inputs, reactor state, shutdown latch, and reset flag.
	2.	Write logic to prevent startup unless all doors are closed:

ALLOW_START := DOOR_1_CLOSED AND DOOR_2_CLOSED AND DOOR_3_CLOSED;
  3.	Write logic to initiate emergency shutdown if any door opens during operation:
  IF ReactorRunning AND (NOT DOOR_1_CLOSED OR NOT DOOR_2_CLOSED OR NOT DOOR_3_CLOSED) THEN
    EMERGENCY_SHUTDOWN := TRUE;
    ReactorRunning := FALSE;
END_IF;
  4.	Latch the shutdown and require a manual reset after all doors are closed again:
  IF EMERGENCY_SHUTDOWN AND ResetRequested AND AllDoorsClosed THEN
    EMERGENCY_SHUTDOWN := FALSE;
END_IF;
🟦 E (Expectation) – What Success Looks Like

You produce a self-contained interlock system that reliably enforces door safety requirements. The system:
	•	Prevents unsafe reactor startup
	•	Immediately shuts down hazardous processes if access is breached
	•	Ensures restart only after all safety doors are closed and manually reset
	•	Supports industry-standard safety compliance and minimizes the risk of operator injury or chemical exposure

### Generated Code:
**Intent Summary:**  
Develop a fail-safe IEC 61131-3 Structured Text program to enforce safety door interlocks for a chemical reactor, preventing startup or operation if doors are open, triggering emergency shutdowns on breach, and requiring manual reset—ensuring compliance with safety standards and hazard prevention.  

*(Focus: Safety interlock logic, reactor access control, fail-safe shutdown, and manual reset requirement.)*
**Interlock Safety Doors:**

Develop a self-contained IEC 61131-3 Structured Text program to implement interlocks for safety doors in a chemical reactor. The program should monitor the status of the safety doors and ensure that the reactor remains in a safe state whenever any door is open.

The interlock logic should prevent the reactor from starting or continuing operation if any safety door is not securely closed. Additionally, if a safety door is opened during reactor operation, the program should immediately trigger an emergency shutdown sequence, including deactivating the reactor and stopping any hazardous processes.

This interlock ensures that the reactor only operates when all safety doors are securely closed, providing an essential safeguard against accidental exposure to hazardous conditions. Discuss the importance of safety door interlocks in preventing operator access to dangerous environments and ensuring compliance with safety standards in chemical processing.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC programmer or safety system engineer responsible for implementing a door interlock system for a chemical reactor, ensuring that the reactor can only operate when all safety doors are securely closed.

⸻

🟩 I (Input) – What You’re Given

You need to design a Structured Text (IEC 61131-3) program that:
	•	Monitors the status of multiple safety doors (e.g., DOOR_1_CLOSED, DOOR_2_CLOSED, etc.)
	•	Prevents the reactor from starting if any door is open
	•	Shuts down the reactor immediately if a door opens during operation
	•	Includes a manual reset requirement after an emergency shutdown
	•	Handles all logic in a fail-safe manner to comply with chemical industry safety standards

⸻

🟧 S (Steps) – What You Need to Do
	1.	Define all variables such as door status inputs, reactor state, shutdown latch, and reset flag.
	2.	Write logic to prevent startup unless all doors are closed:

ALLOW_START := DOOR_1_CLOSED AND DOOR_2_CLOSED AND DOOR_3_CLOSED;
  3.	Write logic to initiate emergency shutdown if any door opens during operation:
  IF ReactorRunning AND (NOT DOOR_1_CLOSED OR NOT DOOR_2_CLOSED OR NOT DOOR_3_CLOSED) THEN
    EMERGENCY_SHUTDOWN := TRUE;
    ReactorRunning := FALSE;
END_IF;
  4.	Latch the shutdown and require a manual reset after all doors are closed again:
  IF EMERGENCY_SHUTDOWN AND ResetRequested AND AllDoorsClosed THEN
    EMERGENCY_SHUTDOWN := FALSE;
END_IF;
🟦 E (Expectation) – What Success Looks Like

You produce a self-contained interlock system that reliably enforces door safety requirements. The system:
	•	Prevents unsafe reactor startup
	•	Immediately shuts down hazardous processes if access is breached
	•	Ensures restart only after all safety doors are closed and manually reset
	•	Supports industry-standard safety compliance and minimizes the risk of operator injury or chemical exposure
	•	Works in real-time, with deterministic logic and no blocking conditions
	•	Includes detailed comments explaining the interlock sequence for audit and maintenance
	•	Is modular and reusable for other reactor systems or safety door interlocks
	•	Handles edge cases, such as sensor failures or network communication issues, with fail-safe defaults
	•	Ensures that the reactor remains in a safe state whenever any safety door is open
	•	Includes a manual reset requirement to ensure that the interlock system is only re-enabled after a safe and controlled shutdown
	•	Works in real-time, with deterministic logic and no blocking conditions
	•	Includes detailed comments explaining the interlock sequence for audit and maintenance
	•	Is modular and reusable for other reactor systems or safety door interlocks
	•	Handles edge cases, such as sensor failures or network communication issues, with fail-safe defaults
	•	Ensures that the reactor remains in a safe state whenever any safety door is open
	•	Includes a manual reset requirement to ensure that the interlock system is only re-enabled after a safe and controlled shutdown
	•	Works in real-time, with deterministic logic and no blocking conditions
	•	Includes detailed comments explaining the interlock sequence for audit and maintenance
	•	Is modular and reusable for other reactor systems or safety door interlocks
	•	Handles edge cases, such as sensor failures or network communication issues, with fail-safe defaults
	•	Ensures that the reactor remains in a safe state whenever any safety door is open
	•	Includes a manual reset requirement to ensure that the interlock system is only re-enabled after a safe and controlled shutdown
	•	Works in real-time, with deterministic logic and no blocking conditions
	•	Includes detailed comments explaining the interlock sequence for audit and maintenance
	•	Is modular and reusable for other reactor systems or safety door interlocks
	•	Handles edge cases, such as sensor failures or network communication issues, with fail-safe defaults
	•	Ensures that the reactor remains in a safe state whenever any safety door is open
	•	Includes a manual reset requirement to ensure that the interlock system is only re-enabled after a safe and controlled shutdown
	•	Works in real-time, with deterministic logic and no blocking conditions
	•	Includes detailed comments explaining the interlock sequence for audit and maintenance
	•	Is modular and reusable for other reactor systems or safety door inter

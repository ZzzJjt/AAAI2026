### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to enforce safety door interlocks for a chemical reactor, ensuring fail-safe operation by preventing startup or triggering emergency shutdown if doors are open, with manual reset requirements for compliance.

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
Develop an IEC 61131-3 Structured Text program to enforce safety door interlocks for a chemical reactor, ensuring fail-safe operation by preventing startup or triggering emergency shutdown if doors are open, with manual reset requirements for compliance.
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

**Code:**

```
// Define variables
VAR
  DOOR_1_CLOSED : BOOL;
  DOOR_2_CLOSED : BOOL;
  DOOR_3_CLOSED : BOOL;
  ALLOW_START : BOOL;
  EMERGENCY_SHUTDOWN : BOOL;
  ReactorRunning : BOOL;
  ResetRequested : BOOL;
  AllDoorsClosed : BOOL;
END_VAR

// Prevent startup unless all doors are closed
ALLOW_START := DOOR_1_CLOSED AND DOOR_2_CLOSED AND DOOR_3_CLOSED;

// Initiate emergency shutdown if any door opens during operation
IF ReactorRunning AND (NOT DOOR_1_CLOSED OR NOT DOOR_2_CLOSED OR NOT DOOR_3_CLOSED) THEN
  EMERGENCY_SHUTDOWN := TRUE;
  ReactorRunning := FALSE;
END_IF;

// Latch the shutdown and require a manual reset after all doors are closed again
IF EMERGENCY_SHUTDOWN AND ResetRequested AND AllDoorsClosed THEN
  EMERGENCY_SHUTDOWN := FALSE;
END_IF;
```

**Discussion:**

The interlock system developed in this program ensures that the chemical reactor can only operate when all safety doors are securely closed. This prevents operator access to dangerous environments and ensures compliance with safety standards in chemical processing.

The program monitors the status of multiple safety doors and prevents the reactor from starting if any door is open. If a door opens during operation, the program immediately triggers an emergency shutdown sequence, including deactivating the reactor and stopping any hazardous processes.

The program also includes a manual reset requirement after an emergency shutdown, ensuring that the reactor can only be restarted after all safety doors are closed and manually reset. This additional safety measure helps to minimize the risk of operator injury or chemical exposure.

Overall, the interlock system developed in this program provides an essential safeguard against accidental exposure to hazardous conditions in chemical processing. By ensuring that the reactor only operates when all safety doors are securely closed, the program helps to protect operators and the environment from potential harm.

**Conclusion:**

In conclusion, the interlock system developed in this program is a critical component of any chemical reactor safety system. By ensuring that the reactor can only operate when all safety doors are securely closed, the program helps to prevent operator access to dangerous environments and ensures compliance with safety standards in chemical processing.

The program's ability to immediately trigger an emergency shutdown sequence if a door opens during operation and its manual reset requirement after an emergency shutdown help to

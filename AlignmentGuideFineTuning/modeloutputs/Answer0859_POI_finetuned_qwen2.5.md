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

Ensure that the reactor only operates when all safety doors are securely closed, and that it immediately enters a safe shutdown state if access is breached. This interlock system enhances operator safety, prevents exposure to hazardous conditions, and ensures compliance with safety standards in industrial chemical processes. Discuss the importance of safety door interlocks in preventing operator access to dangerous environments and ensuring compliance with safety standards in chemical processing.

**T-A-G:**

⸻

🟥 T (Task) – What You Need to Do

Develop a self-contained IEC 61131-3 Structured Text program to implement interlocks for safety doors in a chemical reactor. The program should monitor the status of the safety doors and ensure that the reactor remains in a safe state whenever any door is open.

⸻

🟩 A (Action) – How to Do It
	1.	Define the required inputs and outputs:
	•	Input: Safety door status (e.g., Door1Open, Door2Open, etc.)
	•	Output: Interlock status (AllowStart), emergency shutdown flag (Shutdown), and door status (AllDoorsClosed)
	2.	Implement logic to monitor the safety door statuses:
	•	Allow the reactor to start only when all doors are closed:
	AllowStart := NOT Door1Open AND NOT Door2Open AND NOT Door3Open;
	•	Implement emergency shutdown if any door is opened during operation:
	IF ReactorRunning THEN
		IF Door1Open OR Door2Open THEN
			Shutdown := TRUE;
			ReactorRunning := FALSE;
		END_IF;
	END_IF;
	3.	Include latching to maintain the interlock state until all doors are closed:
	•	Use a timer or a flag to ensure the interlock remains engaged until all doors are securely closed.
	•	Provide a manual reset function to allow safe door access in emergencies.
	4.	Implement fail-safe defaults:
	•	Ensure the reactor defaults to a safe state if any sensor input is lost or invalid.
	•	Include logic to handle sensor failures, ensuring the system defaults to a safe shutdown position.

⸻

🟦 G (Goal) – What You Want to Achieve

Create a reliable and safe interlock system for the chemical reactor that prevents operation when any safety door is open. The system should immediately trigger an emergency shutdown if a door is opened during operation, ensuring the safety of the reactor and its surroundings. Discuss the importance of safety door interlocks in preventing operator access to dangerous environments and ensuring compliance with safety standards in chemical processing.

**T-A-G:**

⸻

🟥 T (Task) – What You Need to Do

Develop a self-contained IEC 61131-3 Struct

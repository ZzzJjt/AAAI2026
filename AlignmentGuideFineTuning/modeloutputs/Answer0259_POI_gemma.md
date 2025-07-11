### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to enforce safety door interlocks for a chemical reactor, preventing startup if doors are open, triggering emergency shutdowns during operation, and requiring manual reset after resolution, ensuring compliance with safety standards.

### Prompt:
**Interlock Safety Doors:**

Develop a self-contained IEC 61131-3 Structured Text program to implement interlocks for safety doors in a chemical reactor. The program should monitor the status of the safety doors and ensure that the reactor remains in a safe state whenever any door is open.

The interlock logic should prevent the reactor from starting or continuing operation if any safety door is not securely closed. Additionally, if a safety door is opened during reactor operation, the program should immediately trigger an emergency shutdown sequence, including deactivating the reactor and stopping any hazardous processes.

This interlock ensures that the reactor only operates when all safety doors are securely closed, providing an essential safeguard against accidental exposure to hazardous conditions. Discuss the importance of safety door interlocks in preventing operator access to dangerous environments and ensuring compliance with safety standards in chemical processing.

**C-A-R-E:**

🟥 C (Context) – The Background

Chemical reactors often operate under high pressure, elevated temperatures, or in the presence of hazardous substances. If a safety door is opened while the reactor is running, it poses a serious risk of operator exposure, equipment damage, and regulatory violation. Safety standards (such as IEC 61508 and OSHA guidelines) require that personnel access to dangerous areas be controlled through automatic interlock systems that prevent operation when safety guards are not secured.

⸻

🟩 A (Action) – The Implementation Task

Develop a self-contained IEC 61131-3 Structured Text (ST) program to implement an interlock system for safety doors in a chemical reactor. The logic should:
	•	Continuously monitor the status of each safety door (e.g., DOOR_1_CLOSED, DOOR_2_CLOSED)
	•	Prevent the reactor from starting if any door is open
	•	Trigger an emergency shutdown if a door is opened while the reactor is operating
	•	Stop all hazardous processes including heaters, stirrers, and pumps
	•	Latch the shutdown condition and require manual reset once all doors are securely closed

The interlock logic should be clearly structured to respond quickly to unsafe access and provide reliable system feedback.

⸻

🟨 R (Result) – The Expected Outcome

The system ensures that the reactor only operates when all safety doors are securely closed, maintaining a safe operating environment and complying with safety standards. If a door is opened during operation, the program performs an immediate emergency shutdown, minimizing the chance of exposure or injury. Manual reset ensures that all conditions are verified before restarting.

⸻

🟦 E (Example) – A Practical Use Case

If the operator attempts to start the reactor while DOOR_2_CLOSED = FALSE, the program prevents the ALLOW_START flag from activating. If DOOR_1_CLOSED goes FALSE during normal operation, the system sets EMERGENCY_SHUTDOWN := TRUE, disables ReactorRunning, and deactivates all outputs associated with active processes. The reactor cannot restart until all doors are closed and a technician manually resets the interlock system.

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to enforce safety door interlocks for a chemical reactor, preventing startup if doors are open, triggering emergency shutdowns during operation, and requiring manual reset after resolution, ensuring compliance with safety standards.
**Interlock Safety Doors:**

Develop a self-contained IEC 61131-3 Structured Text program to implement interlocks for safety doors in a chemical reactor. The program should monitor the status of the safety doors and ensure that the reactor remains in a safe state whenever any door is open.

The interlock logic should prevent the reactor from starting or continuing operation if any safety door is not securely closed. Additionally, if a safety door is opened during reactor operation, the program should immediately trigger an emergency shutdown sequence, including deactivating the reactor and stopping any hazardous processes.

This interlock ensures that the reactor only operates when all safety doors are securely closed, providing an essential safeguard against accidental exposure to hazardous conditions. Discuss the importance of safety door interlocks in preventing operator access to dangerous environments and ensuring compliance with safety standards in chemical processing.

**C-A-R-E:**

🟥 C (Context) – The Background

Chemical reactors often operate under high pressure, elevated temperatures, or in the presence of hazardous substances. If a safety door is opened while the reactor is running, it poses a serious risk of operator exposure, equipment damage, and regulatory violation. Safety standards (such as IEC 61508 and OSHA guidelines) require that personnel access to dangerous areas be controlled through automatic interlock systems that prevent operation when safety guards are not secured.

⸻

🟩 A (Action) – The Implementation Task

Develop a self-contained IEC 61131-3 Structured Text (ST) program to implement an interlock system for safety doors in a chemical reactor. The logic should:
	•	Continuously monitor the status of each safety door (e.g., DOOR_1_CLOSED, DOOR_2_CLOSED)
	•	Prevent the reactor from starting if any door is open
	•	Trigger an emergency shutdown if a door is opened while the reactor is operating
	•	Stop all hazardous processes including heaters, stirrers, and pumps
	•	Latch the shutdown condition and require manual reset once all doors are securely closed

The interlock logic should be clearly structured to respond quickly to unsafe access and provide reliable system feedback.

⸻

🟨 R (Result) – The Expected Outcome

The system ensures that the reactor only operates when all safety doors are securely closed, maintaining a safe operating environment and complying with safety standards. If a door is opened during operation, the program performs an immediate emergency shutdown, minimizing the chance of exposure or injury. Manual reset ensures that all conditions are verified before restarting.

⸻

🟦 E (Example) – A Practical Use Case

If the operator attempts to start the reactor while DOOR_2_CLOSED = FALSE, the program prevents the ALLOW_START flag from activating. If DOOR_1_CLOSED goes FALSE during normal operation, the system sets EMERGENCY_SHUTDOWN := TRUE, disables ReactorRunning, and deactivates all outputs associated with active processes. The reactor cannot restart until all doors are closed and a technician manually resets the interlock system.

**Code:**

```
// Safety Door Interlock Program
// Author: [Your Name]
// Date: [Date]

// Define constants for door status
const DOOR_1_CLOSED = TRUE;
const DOOR_2_CLOSED = TRUE;

// Define constants for reactor status
const REACTOR_RUNNING = TRUE;
const REACTOR_STOPPED = FALSE;

// Define constants for interlock status
const ALLOW_START = TRUE;
const EMERGENCY_SHUTDOWN = FALSE;

// Define constants for process status
const HEATER_ON = TRUE;
const HEATER_OFF = FALSE;
const STIRRER_ON = TRUE;
const STIRRER_OFF = FALSE;
const PUMP_ON = TRUE;
const PUMP_OFF = FALSE;

// Define variables for door status
var door1Closed: BOOL;
var door2Closed: BOOL;

// Define variables for reactor status
var reactorRunning: BOOL;
var reactorStopped: BOOL;

// Define variables for interlock status
var allowStart: BOOL;
var emergencyShutdown: BOOL;

// Define variables for process status
var heaterOn: BOOL;
var stirrerOn: BOOL;
var pumpOn: BOOL;

// Initialize variables
door1Closed := DOOR_1_CLOSED;
door2Closed := DOOR_2_CLOSED;
reactorRunning := REACTOR_RUNNING;
reactorStopped := REACTOR_STOPPED;
allowStart := ALLOW_START;
emergencyShutdown := EMERGENCY_SHUTDOWN;
heaterOn := HEATER_ON;
stirrerOn := STIRRER_ON;
pumpOn := PUMP_ON;

// Main program loop
while TRUE do
	// Check door status
	if door1Closed = FALSE or door2Closed = FALSE then
		allowStart := FALSE;
	else
		allowStart := TRUE;
	end_if;

	// Check reactor status
	if reactorRunning = TRUE then
		// Check door status
		if door1Closed = FALSE or door2Closed = FALSE then
			emergencyShutdown := TRUE;
		else
			emergencyShutdown := FALSE;
		end_if;

		// Stop all processes
		heaterOn := HEATER_OFF;
		stirrerOn := STIRRER_OFF;
		pumpOn := PUMP_OFF;
	end_if;

	// Check interlock status
	if

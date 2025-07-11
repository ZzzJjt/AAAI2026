### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to enforce safety door interlocks in a chemical reactor, preventing operation if doors are open and triggering emergency shutdowns during breaches, ensuring compliance with safety standards.  

*(Focus: Safety-critical interlock logic for reactor access control.)*

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
Develop an IEC 61131-3 Structured Text program to enforce safety door interlocks in a chemical reactor, preventing operation if doors are open and triggering emergency shutdowns during breaches, ensuring compliance with safety standards.  

*(Focus: Safety-critical interlock logic for reactor access control.)*
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
FUNCTION_BLOCK FB_DoorInterlock
VAR_INPUT
    Door1_Closed : BOOL; // TRUE if Door 1 is closed
    Door2_Closed : BOOL; // TRUE if Door 2 is closed
END_VAR

VAR_OUTPUT
    AllowStart : BOOL; // TRUE if all doors are closed
    EmergencyShutdown : BOOL; // TRUE if any door is open during operation
    ReactorRunning : BOOL; // TRUE if reactor is running
    HeaterRunning : BOOL; // TRUE if heater is running
    StirrerRunning : BOOL; // TRUE if stirrer is running
    PumpRunning : BOOL; // TRUE if pump is running
    EmergencyShutdownLatch : BOOL; // TRUE if emergency shutdown is active
END_VAR

VAR
    EmergencyShutdownLatch_Reset : BOOL := FALSE; // Reset flag for emergency shutdown
END_VAR

// Interlock logic
AllowStart := Door1_Closed AND Door2_Closed;
EmergencyShutdown := NOT Door1_Closed OR NOT Door2_Closed;

// Emergency shutdown logic
IF EmergencyShutdown THEN
    EmergencyShutdownLatch := TRUE;
    ReactorRunning := FALSE;
    HeaterRunning := FALSE;
    StirrerRunning := FALSE;
    PumpRunning := FALSE;
    EmergencyShutdownLatch_Reset := TRUE;
END_IF;

// Reset emergency shutdown latch
IF EmergencyShutdownLatch_Reset THEN
    EmergencyShutdownLatch := FALSE;
END_IF;
END_FUNCTION_BLOCK

// Example usage:
// IF NOT FB_DoorInterlock.AllowStart THEN
//     // Prevent reactor start
// END_IF;
// IF FB_DoorInterlock.EmergencyShutdown THEN
//     // Trigger emergency shutdown
// END_IF;
// IF FB_DoorInterlock.EmergencyShutdownLatch THEN
//     // Wait for emergency shutdown latch reset
// END_IF;
// IF FB_DoorInterlock.ReactorRunning THEN
//     // Reactor is running
// END_IF;
// IF FB_DoorInterlock.HeaterRunning THEN
//     // Heater is running
// END_IF;
// IF FB_DoorInterlock.StirrerRunning THEN
//     // Stirrer is running
// END_IF;
// IF FB_DoorInterlock.PumpRunning THEN
//     // Pump is running
// END

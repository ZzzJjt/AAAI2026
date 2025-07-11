### Intent:
**Intent Summary:**  
Design an interlock system for a chemical reactor that ensures safe startup and operation by verifying all doors are closed, preventing unauthorized activation, and triggering an emergency shutdown if doors open during operation, with a manual reset capability.

### Prompt:
**Extended Cause & Process Action Matrix:**

Develop an extended cause and process action matrix for the interlocks in a chemical reactor. Each row should represent a specific cause (e.g., sensor values exceeding limits), and the column headings should represent safety actions performed using actuators in the system. The matrix should illustrate how different causes trigger specific actions to ensure safe operation.

Discuss how this extended matrix provides a clear mapping between potential hazardous situations and the corresponding safety actions. Emphasize the importance of designing interlocks that ensure safe and stable reactor operation, preventing risks such as overpressure, underheating, and process failures.

**R-I-S-E:**

🟥 R (Role) – Your Role

Act as a process safety or automation engineer designing interlocks for a chemical reactor to ensure safe and stable operation under abnormal or hazardous conditions.

⸻

🟩 I (Input) – What You’re Given

You are tasked with developing an extended cause and process action matrix. This matrix must define how various causes (e.g., sensor faults, overpressure, underheating) trigger specific safety actions (e.g., closing valves, activating emergency cooling, stopping the feed). The goal is to clearly link each potential hazardous condition to a corrective or protective response within the interlock system.

⸻

🟧 S (Steps) – What You Need to Do
	1.	Identify a comprehensive list of possible causes or fault conditions that could occur during reactor operation.
	2.	List all available process actions—these include mechanical or control responses that can be actuated to protect the system.
	3.	Create a matrix where:
	•	Each row represents a specific cause (e.g., “Pressure > Max Limit”)
	•	Each column represents a process action (e.g., “Close Feed Valve”)
	•	Cells are marked to show which actions are triggered by each cause
	4.	Ensure that each critical cause has at least one response and that responses are coordinated to prevent conflict or escalation.
	5.	Integrate error detection logic and comment on fail-safe behavior (e.g., sensor loss triggers a shutdown or fallback routine).

⸻

🟦 E (Expectation) – What Success Looks Like

The completed matrix provides a clear, actionable map of how the interlock system handles hazardous conditions. It improves safety by ensuring every failure mode has a defined, automatic response. It also enhances transparency for audits, facilitates communication between design and operations teams, and simplifies validation and maintenance of interlocks in the chemical process control system.

### Generated Code:
**Intent Summary:**  
Design an interlock system for a chemical reactor that ensures safe startup and operation by verifying all doors are closed, preventing unauthorized activation, and triggering an emergency shutdown if doors open during operation, with a manual reset capability.
**Extended Cause & Process Action Matrix:**

Develop an extended cause and process action matrix for the interlocks in a chemical reactor. Each row should represent a specific cause (e.g., sensor values exceeding limits), and the column headings should represent safety actions performed using actuators in the system. The matrix should illustrate how different causes trigger specific actions to ensure safe operation.

Discuss how this extended matrix provides a clear mapping between potential hazardous situations and the corresponding safety actions. Emphasize the importance of designing interlocks that ensure safe and stable reactor operation, preventing risks such as overpressure, underheating, and process failures.

**R-I-S-E:**

🟥 R (Role) – Your Role

Act as a process safety or automation engineer designing interlocks for a chemical reactor to ensure safe and stable operation under abnormal or hazardous conditions.

⸻

🟩 I (Input) – What You’re Given

You are tasked with developing an extended cause and process action matrix. This matrix must define how various causes (e.g., sensor faults, overpressure, underheating) trigger specific safety actions (e.g., closing valves, activating emergency cooling, stopping the feed). The goal is to clearly link each potential hazardous condition to a corrective or protective response within the interlock system.

⸻

🟧 S (Steps) – What You Need to Do
	1.	Identify a comprehensive list of possible causes or fault conditions that could occur during reactor operation.
	2.	List all available process actions—these include mechanical or control responses that can be actuated to protect the system.
	3.	Create a matrix where:
	•	Each row represents a specific cause (e.g., “Pressure > Max Limit”)
	•	Each column represents a process action (e.g., “Close Feed Valve”)
	•	Cells are marked to show which actions are triggered by each cause
	4.	Ensure that each critical cause has at least one response and that responses are coordinated to prevent conflict or escalation.
	5.	Integrate error detection logic and comment on fail-safe behavior (e.g., sensor loss triggers a shutdown or fallback routine).

⸻

🟦 E (Expectation) – What Success Looks Like

The completed matrix provides a clear, actionable map of how the interlock system handles hazardous conditions. It improves safety by ensuring every failure mode has a defined, automatic response. It also enhances transparency for audits, facilitates communication between design and operations teams, and simplifies validation and maintenance of interlocks in the chemical process control system.
FUNCTION_BLOCK FB_ReactorInterlock
VAR_INPUT
    Execute : BOOL; // Command to execute interlock checks
    DoorClosed : ARRAY[1..5] OF BOOL; // Array indicating door status (1 = closed, 0 = open)
    StartAllowed : BOOL; // Flag indicating if startup is allowed
    ManualReset : BOOL; // Manual reset input
END_VAR

VAR_OUTPUT
    StartAllowed : BOOL; // Updated flag indicating if startup is allowed
    EmergencyShutdown : BOOL; // Flag indicating if an emergency shutdown has been triggered
    Error : BOOL; // Error flag
    ErrorID : DWORD; // Error code
END_VAR

VAR
    i : INT; // Loop counter
    AllDoorsClosed : BOOL; // Flag indicating if all doors are closed
    DoorOpenDetected : BOOL; // Flag indicating if any door is open
    ShutdownTriggered : BOOL; // Flag indicating if an emergency shutdown has been triggered
    ResetAllowed : BOOL; // Flag indicating if manual reset is allowed
END_VAR

// Main logic block
IF Execute THEN
    // Reset outputs
    StartAllowed := TRUE;
    EmergencyShutdown := FALSE;
    Error := FALSE;
    ErrorID := 0;

    // Check if all doors are closed
    AllDoorsClosed := TRUE;
    FOR i := 1 TO 5 DO
        AllDoorsClosed := AllDoorsClosed AND DoorClosed[i];
    END_FOR;

    // Check if any door is open
    DoorOpenDetected := FALSE;
    FOR i := 1 TO 5 DO
        IF NOT DoorClosed[i] THEN
            DoorOpenDetected := TRUE;
            EXIT;
        END_IF;
    END_FOR;

    // Check if startup is allowed
    IF StartAllowed THEN
        // Check if all doors are closed and startup is allowed
        IF AllDoorsClosed AND StartAllowed THEN
            // Allow startup
            StartAllowed := TRUE;
        ELSE
            // Startup not allowed due to open doors or manual override
            StartAllowed := FALSE;
            Error := TRUE

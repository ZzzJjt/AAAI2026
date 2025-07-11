### Intent:
**Intent Summary:**  
Create a Structured Text function block to monitor and diagnose a PowerLink node's communication status, error conditions, and health, with configurable polling and error logging for real-time network maintenance.

### Prompt:
**Profibus DP Diagnostics Using 61131-3 Structured Text:**

Develop a self-contained 61131-3 structured text function block to read diagnostic data from a Profibus DP slave device. The function block should handle communication with the Profibus DP slave and retrieve diagnostic information such as device status, error codes, and communication health. Provide an explanation of the key steps in processing the diagnostic data, including request initiation, data retrieval, and error handling mechanisms.

**R-I-S-E:**

🟥 R (Role) – Your Role

Act as a PLC programmer developing diagnostic and communication monitoring tools for Profibus DP networks using IEC 61131-3 Structured Text.

⸻

🟩 I (Input) – What You’re Given

You are tasked with creating a self-contained Structured Text (ST) function block that reads diagnostic data from a Profibus DP slave device. The function block must retrieve key information such as device status, error codes, and communication health, and expose execution status and error flags for use in control applications.

⸻

🟧 S (Steps) – What You Need to Do
	1.	Define a function block interface with the following:
	•	Inputs: Execute (BOOL), SlaveAddress (BYTE), Timeout (TIME)
	•	Outputs: Done (BOOL), Busy (BOOL), Error (BOOL), ErrorID (DWORD), plus structured diagnostic outputs (e.g. DeviceStatus, CommState)
	2.	Inside the function block:
	•	Detect rising edge of Execute to start the diagnostic read
	•	Send a Profibus DP diagnostic request using the slave address
	•	Wait for response and validate it within the given Timeout
	•	Parse the response to extract error flags, status codes, and communication health indicators
	•	Set output flags (Done, Error) and assign the parsed data to output variables
	3.	Implement internal error handling for timeouts, invalid responses, or communication loss. Provide ErrorID codes for troubleshooting.

⸻

🟦 E (Expectation) – What Success Looks Like

The function block allows the PLC program to retrieve and react to real-time diagnostic data from any Profibus DP slave. Operators and maintenance systems gain early visibility into device issues, while control logic can trigger alarms or fallback procedures based on accurate status and error conditions—improving system uptime and maintainability.

### Generated Code:
**Intent Summary:**  
Create a Structured Text function block to monitor and diagnose a PowerLink node's communication status, error conditions, and health, with configurable polling and error logging for real-time network maintenance.
**Profibus DP Diagnostics Using 61131-3 Structured Text:**

Develop a self-contained 61131-3 structured text function block to read diagnostic data from a Profibus DP slave device. The function block should handle communication with the Profibus DP slave and retrieve diagnostic information such as device status, error codes, and communication health. Provide an explanation of the key steps in processing the diagnostic data, including request initiation, data retrieval, and error handling mechanisms.

**R-I-S-E:**

🟥 R (Role) – Your Role

Act as a PLC programmer developing diagnostic and communication monitoring tools for Profibus DP networks using IEC 61131-3 Structured Text.

⸻

🟩 I (Input) – What You’re Given

You are tasked with creating a self-contained Structured Text (ST) function block that reads diagnostic data from a Profibus DP slave device. The function block must retrieve key information such as device status, error codes, and communication health, and expose execution status and error flags for use in control applications.

⸻

🟧 S (Steps) – What You Need to Do
	1.	Define a function block interface with the following:
	•	Inputs: Execute (BOOL), SlaveAddress (BYTE), Timeout (TIME)
	•	Outputs: Done (BOOL), Busy (BOOL), Error (BOOL), ErrorID (DWORD), plus structured diagnostic outputs (e.g. DeviceStatus, CommState)
	2.	Inside the function block:
	•	Detect rising edge of Execute to start the diagnostic read
	•	Send a Profibus DP diagnostic request using the slave address
	•	Wait for response and validate it within the given Timeout
	•	Parse the response to extract error flags, status codes, and communication health indicators
	•	Set output flags (Done, Error) and assign the parsed data to output variables
	3.	Implement internal error handling for timeouts, invalid responses, or communication loss. Provide ErrorID codes for troubleshooting.

⸻

🟦 E (Expectation) – What Success Looks Like

The function block allows the PLC program to retrieve and react to real-time diagnostic data from any Profibus DP slave. Operators and maintenance systems gain early visibility into device issues, while control logic can trigger alarms or fallback procedures based on accurate status and error conditions—improving system uptime and maintainability.
FUNCTION_BLOCK FB_PowerLinkNodeMonitor
VAR_INPUT
    Enable : BOOL; // Enable monitoring when TRUE
    PollInterval : TIME := T#1s; // Polling interval
    NodeAddress : BYTE; // PowerLink node address
END_VAR

VAR_OUTPUT
    NodeStatus : STRING[20]; // Current node status
    ErrorCode : DWORD; // Error code (0 = No error, 1 = Communication error, 2 = Node offline, 3 = Node timeout)
    LogEntry : STRING[80]; // Logged error message
    Logged : BOOL; // TRUE when an error is logged
END_VAR

VAR
    LastPollTime : TIME; // Time of last poll
    PollTimer : TON; // Timer for polling
    NodeCommStatus : BOOL; // Communication status with node
    NodeHealth : BOOL; // Node health status
    LastNodeStatus : STRING[20]; // Previous node status
    ErrorCount : DWORD; // Error counter
    LoggedLast : BOOL; // Previous Logged state
END_VAR

METHOD Execute : BOOL
BEGIN
    // Reset variables on disable
    IF NOT Enable THEN
        NodeStatus := 'Node OK';
        ErrorCode := 0;
        LogEntry := '';
        Logged := FALSE;
        ErrorCount := 0;
        NodeCommStatus := FALSE;
        NodeHealth := FALSE;
        LastNodeStatus := '';
        LastPollTime := NOW();
        PollTimer(IN := FALSE, PT := PollInterval);
        RETURN TRUE;
    END_IF;

    // Check if it's time to poll
    IF PollTimer(IN := NOW() > LastPollTime) THEN
        PollTimer(IN := FALSE);

        // Send PowerLink diagnostic request to node
        // Replace with actual PowerLink API call
        NodeCommStatus := PowerLink_DiagRequest(NodeAddress);

        // Check communication status
        IF NodeCommStatus THEN
            NodeHealth := TRUE; // Assume node is healthy if communication is OK
        ELSE
            NodeHealth := FALSE; // Assume node is offline or unreachable
        END_

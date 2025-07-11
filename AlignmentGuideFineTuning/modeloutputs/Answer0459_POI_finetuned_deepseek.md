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
FUNCTION_BLOCK FB_PowerLinkNodeStatus
VAR_INPUT
    Execute : BOOL; // Trigger status check
END_VAR

VAR_OUTPUT
    Done : BOOL; // TRUE when status check is complete
    Busy : BOOL; // TRUE while status check is in progress
    Error : BOOL; // TRUE if error occurred
    ErrorID : DWORD; // Error code (e.g., 0x0001 = CommunicationLost)
    NodeID : INT; // Node ID (0-15)
    NodeName : STRING[20]; // Node name
    NodeStatus : INT; // Node status (0=Idle, 1=Active, 2=Error)
    NodeHealth : INT; // Node health (0=Normal, 1=Warning, 2=Critical)
    CommState : INT; // Communication state (0=Connected, 1=Disconnected)
    ErrorString : STRING[255]; // Detailed error message
END_VAR

VAR
    // Internal variables
    bRequestSent : BOOL; // TRUE when request is sent
    bResponseReceived : BOOL; // TRUE when response is received
    bErrorDetected : BOOL; // TRUE if error occurred during read
    ErrorID_Default : DWORD := 0x0000; // Default error code
    ErrorString_Default : STRING[255] := 'No error';
    NodeID_Default : INT := 0;
    NodeName_Default : STRING[20] := 'Unknown';
    NodeStatus_Default : INT := 0;
    NodeHealth_Default : INT := 0;
    CommState_Default : INT := 0;
END_VAR

// Initialize outputs
Done := FALSE;
Busy := FALSE;
Error := FALSE;
ErrorID := ErrorID_Default;
NodeID := NodeID_Default;
NodeName := NodeName_Default;
NodeStatus := NodeStatus_Default;
NodeHealth := NodeHealth_Default;
CommState := CommState_Default;
ErrorString := ErrorString_Default;

// Execute only if Execute is TRUE
IF Execute THEN
    // Check if request is already sent
    IF NOT bRequestSent THEN
        // Send diagnostic request
        bRequestSent := TRUE;
        Busy := TRUE;

### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text function block to monitor and log real-time communication status (OPC UA, Modbus, Profinet) with alarm triggering and audit trail entries for failures, ensuring fault diagnostics and system reliability.  

**For Code Generation:**  
*"Create a structured text function block to monitor OPC UA/Modbus/Profinet connections, trigger alarms on failures, and log detailed error entries for troubleshooting."*

### Prompt:
**Communication Monitoring for OPC UA, Modbus, and Profinet Using IEC 61131-3 Structured Text:**

Develop a function block in structured text (ST) as per IEC 61131-3 standards to monitor communication connections to an OPC UA server, Modbus server, and Profinet in a machine system. The function block should continuously check the connection status of each protocol, and if any connection fails, an alarm should be triggered. Additionally, when a connection is lost, an entry must be created in the audit trail, detailing the reason for the server being down along with the corresponding error code. Discuss the implementation logic for monitoring multiple protocols, error detection, and how to effectively manage and log communication failures for real-time monitoring and troubleshooting.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Create an IEC 61131-3 Structured Text (ST) function block to monitor communication status for OPC UA, Modbus, and Profinet protocols within a machine control system.

🟩 A (Action) – How to Do It

Develop logic that continuously checks the connection status of each protocol. If any connection fails, the function block should raise an alarm and generate an audit trail entry containing the protocol name, reason for the failure, and an associated error code. The block should handle each protocol independently and include mechanisms for error detection, alarm handling, and memory-safe logging.

🟦 G (Goal) – What You Aim to Achieve

Ensure robust, real-time communication monitoring and fault diagnostics for all three protocols, enabling operators and maintenance teams to quickly identify, respond to, and trace communication failures—thus improving system uptime and traceability.

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text function block to monitor and log real-time communication status (OPC UA, Modbus, Profinet) with alarm triggering and audit trail entries for failures, ensuring fault diagnostics and system reliability.  

**For Code Generation:**  
*"Create a structured text function block to monitor OPC UA/Modbus/Profinet connections, trigger alarms on failures, and log detailed error entries for troubleshooting."*
**Communication Monitoring for OPC UA, Modbus, and Profinet Using IEC 61131-3 Structured Text:**

Develop a function block in structured text (ST) as per IEC 61131-3 standards to monitor communication connections to an OPC UA server, Modbus server, and Profinet in a machine system. The function block should continuously check the connection status of each protocol, and if any connection fails, an alarm should be triggered. Additionally, when a connection is lost, an entry must be created in the audit trail, detailing the reason for the server being down along with the corresponding error code. Discuss the implementation logic for monitoring multiple protocols, error detection, and how to effectively manage and log communication failures for real-time monitoring and troubleshooting.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Create an IEC 61131-3 Structured Text (ST) function block to monitor communication status for OPC UA, Modbus, and Profinet protocols within a machine control system.

🟩 A (Action) – How to Do It

Develop logic that continuously checks the connection status of each protocol. If any connection fails, the function block should raise an alarm and generate an audit trail entry containing the protocol name, reason for the failure, and an associated error code. The block should handle each protocol independently and include mechanisms for error detection, alarm handling, and memory-safe logging.

🟦 G (Goal) – What You Aim to Achieve

Ensure robust, real-time communication monitoring and fault diagnostics for all three protocols, enabling operators and maintenance teams to quickly identify, respond to, and trace communication failures—thus improving system uptime and traceability.
FUNCTION_BLOCK FB_CommunicationMonitor
VAR_INPUT
    Enable : BOOL; // Enable monitoring when TRUE
END_VAR

VAR_OUTPUT
    Alarm : BOOL; // Raise alarm when a connection fails
    AuditTrail : ARRAY[1..100] OF STRING[255]; // Audit trail entries
    AuditTrailCount : INT; // Number of entries in the trail
    ErrorCode : INT; // Error code for each failure
END_VAR

VAR
    CurrentConnectionState : ARRAY[1..3] OF BOOL; // Current state of each connection
    LastConnectionState : ARRAY[1..3] OF BOOL; // Previous state of each connection
    ConnectionFailureDetected : ARRAY[1..3] OF BOOL; // Flag for each connection failure
    ConnectionFailureReason : ARRAY[1..3] OF STRING[255]; // Reason for each failure
    ConnectionFailureTime : ARRAY[1..3] OF TIME; // Time of each failure
    ConnectionRetryCount : ARRAY[1..3] OF INT; // Retry count for each connection
    MaxRetries : INT := 5; // Maximum number of retries
    RetryInterval : TIME := T#1s; // Retry interval
    ConnectionAttemptTimer : TON; // Timer for retry interval
    ConnectionAttemptCount : INT := 0; // Count for retry attempts
END_VAR

METHOD Execute : BOOL
BEGIN
    // Reset outputs on disable
    IF NOT Enable THEN
        Alarm := FALSE;
        AuditTrailCount := 0;
        FOR i := 1 TO 100 DO
            AuditTrail[i] := '';
        END_FOR;
        ConnectionFailureDetected := FALSE;
        ConnectionFailureReason := '';
        ConnectionRetryCount := 0;
        ConnectionAttemptTimer(IN := FALSE);
        RETURN TRUE;
    END_IF;

    // Initialize connection states
    FOR i := 1 TO 3 DO
        CurrentConnectionState[i] := FALSE;
        ConnectionFailureDetected[i] := FALSE;
        ConnectionRetryCount[i] := 0;
    END

### Intent:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text function block to monitor and log real-time communication status (OPC UA, Modbus, Profinet), trigger alarms on failures, and record diagnostic details for troubleshooting.  

*(Focus: Protocol-agnostic monitoring, fault logging, and real-time alerting.)*

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
Create an IEC 61131-3 Structured Text function block to monitor and log real-time communication status (OPC UA, Modbus, Profinet), trigger alarms on failures, and record diagnostic details for troubleshooting.  

*(Focus: Protocol-agnostic monitoring, fault logging, and real-time alerting.)*
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
    ErrorCode : INT; // Error code associated with the failure
END_VAR

VAR
    CurrentConnectionState : ARRAY[1..3] OF BOOL; // Current state of each connection
    LastConnectionState : ARRAY[1..3] OF BOOL; // Previous state of each connection
    ConnectionCheckInterval : TIME := T#10s; // Check interval for each connection
    LastCheckTime : TIME; // Time of the last check
    ConnectionFailureCount : ARRAY[1..3] OF INT; // Number of consecutive failures for each connection
    MaxFailureCount : INT := 3; // Maximum number of consecutive failures before raising an alarm
    ConnectionType : ARRAY[1..3] OF STRING[255]; // Type of each connection (e.g., OPC UA, Modbus, Profinet)
    ConnectionName : ARRAY[1..3] OF STRING[255]; // Name of each connection
    ConnectionPort : ARRAY[1..3] OF INT; // Port number for each connection
    ConnectionTimeout : ARRAY[1..3] OF TIME; // Timeout for each connection
    ConnectionError : ARRAY[1..3] OF STRING[255]; // Error message for each connection
    ConnectionID : INT; // Unique identifier for each connection
END_VAR

METHOD Execute : BOOL
BEGIN
    // Initialize variables
    Alarm := FALSE;
    AuditTrailCount := 0;
    FOR i := 1 TO 3 DO
        CurrentConnectionState[i] := FALSE;
        ConnectionFailureCount[i] := 0;
    END_FOR;

    // Check if enabled
    IF NOT Enable THEN
        Alarm := FALSE;
        AuditTrailCount := 0;
        FOR i := 1

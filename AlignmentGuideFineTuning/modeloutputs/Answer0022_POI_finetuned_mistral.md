### Intent:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text function block to monitor OPC UA, Modbus, and Profinet connections in real time, trigger alarms on failures, and log detailed error entries (including reason and code) to an audit trail for troubleshooting.  

*(Focus: Multi-protocol monitoring, fault detection, and structured logging for industrial communication reliability.)*

### Prompt:
**Communication Monitoring for OPC UA, Modbus, and Profinet Using IEC 61131-3 Structured Text:**

Develop a function block in structured text (ST) as per IEC 61131-3 standards to monitor communication connections to an OPC UA server, Modbus server, and Profinet in a machine system. The function block should continuously check the connection status of each protocol, and if any connection fails, an alarm should be triggered. Additionally, when a connection is lost, an entry must be created in the audit trail, detailing the reason for the server being down along with the corresponding error code. Discuss the implementation logic for monitoring multiple protocols, error detection, and how to effectively manage and log communication failures for real-time monitoring and troubleshooting.

**B-A-B:**

🟥 B (Before) – The Challenge

In complex industrial machine systems, reliable communication with OPC UA, Modbus, and Profinet networks is critical. Without continuous monitoring, connection failures may go undetected, leading to unplanned downtime, delayed troubleshooting, and lack of traceability when issues arise. Traditional implementations often lack unified and automated mechanisms for multi-protocol fault detection and logging.

🟩 A (After) – The Ideal Outcome

Develop an IEC 61131-3 Structured Text function block that monitors the connection status of OPC UA, Modbus, and Profinet protocols in real time. If a connection fails, the function block triggers an alarm and logs a detailed entry in the audit trail, including the failure reason and corresponding error code. This enables operators to respond quickly and ensures communication issues are properly recorded for maintenance and analysis.

🟧 B (Bridge) – The Implementation Strategy

Implement the function block to cyclically poll the status of each communication interface. Use internal state tracking and diagnostic data to detect faults such as timeouts, disconnections, or protocol-specific errors. Integrate alarm outputs to notify operators immediately and create structured audit trail entries with timestamps, protocol type, failure reason, and error code. This modular function block will support efficient troubleshooting, reduce downtime, and maintain a robust digital trace of communication health across all protocols.

### Generated Code:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text function block to monitor OPC UA, Modbus, and Profinet connections in real time, trigger alarms on failures, and log detailed error entries (including reason and code) to an audit trail for troubleshooting.  

*(Focus: Multi-protocol monitoring, fault detection, and structured logging for industrial communication reliability.)*
**Communication Monitoring for OPC UA, Modbus, and Profinet Using IEC 61131-3 Structured Text:**

Develop a function block in structured text (ST) as per IEC 61131-3 standards to monitor communication connections to an OPC UA server, Modbus server, and Profinet in a machine system. The function block should continuously check the connection status of each protocol, and if any connection fails, an alarm should be triggered. Additionally, when a connection is lost, an entry must be created in the audit trail, detailing the reason for the server being down along with the corresponding error code. Discuss the implementation logic for monitoring multiple protocols, error detection, and how to effectively manage and log communication failures for real-time monitoring and troubleshooting.

**B-A-B:**

🟥 B (Before) – The Challenge

In complex industrial machine systems, reliable communication with OPC UA, Modbus, and Profinet networks is critical. Without continuous monitoring, connection failures may go undetected, leading to unplanned downtime, delayed troubleshooting, and lack of traceability when issues arise. Traditional implementations often lack unified and automated mechanisms for multi-protocol fault detection and logging.

🟩 A (After) – The Ideal Outcome

Develop an IEC 61131-3 Structured Text function block that monitors the connection status of OPC UA, Modbus, and Profinet protocols in real time. If a connection fails, the function block triggers an alarm and logs a detailed entry in the audit trail, including the failure reason and corresponding error code. This enables operators to respond quickly and ensures communication issues are properly recorded for maintenance and analysis.

🟧 B (Bridge) – The Implementation Strategy

Implement the function block to cyclically poll the status of each communication interface. Use internal state tracking and diagnostic data to detect faults such as timeouts, disconnections, or protocol-specific errors. Integrate alarm outputs to notify operators immediately and create structured audit trail entries with timestamps, protocol type, failure reason, and error code. This modular function block will support efficient troubleshooting, reduce downtime, and maintain a robust digital trace of communication health across all protocols.
FUNCTION_BLOCK FB_CommunicationMonitor
VAR_INPUT
    Enable: BOOL; // Enable monitoring
    PollInterval: TIME; // Polling interval (e.g., 100 ms)
END_VAR

VAR_OUTPUT
    Alarm: BOOL; // Raise alarm if any connection fails
    AuditTrail: ARRAY[1..100] OF STRING[255]; // Audit trail entries
    AuditTrailSize: INT; // Number of entries
    ErrorCode: INT; // Error code for last failure
END_VAR

VAR
    CurrentTime: TIME; // Current time for polling interval
    LastPollTime: TIME; // Time of last poll
    PollTimer: TON; // Timer for polling interval
    ConnectionStatus: ARRAY[1..3] OF BOOL; // Connection status: [1] = OPC UA, [2] = Modbus, [3] = Profinet
    LastErrorCode: ARRAY[1..3] OF INT; // Error code for last failure
    LastReason: ARRAY[1..3] OF STRING[255]; // Reason for last failure
    MaxAuditTrailSize: INT := 100; // Maximum size of audit trail
    AuditTrailIndex: INT := 0; // Index for audit trail
    PollingComplete: BOOL; // Flag to indicate polling is complete
END_VAR

METHOD ExecutePolling: BOOL
VAR_INPUT
    PollNow: BOOL; // Flag to poll now
END_VAR
VAR
    CurrentTime: TIME; // Current time for polling interval
    ElapsedTime: TIME; // Elapsed time since last poll
    PollInterval: TIME; // Polling interval (e.g., 100 ms)
    PollingComplete: BOOL; // Flag to indicate polling is complete
END_VAR
BEGIN
    // Get current time
    CurrentTime := TON#GetTime();

    // Calculate elapsed time since last poll
    ElapsedTime := CurrentTime - LastPollTime;

    // Check if polling is complete
    IF ElapsedTime >= PollInterval THEN
        // Reset timer
        Polling

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
    Execute : BOOL; // Trigger scan
    Reset : BOOL; // Reset scan
END_VAR

VAR_OUTPUT
    Alarm : BOOL; // TRUE if connection failure detected
    AlarmText : STRING[20]; // Alarm message
    LogEntry : ARRAY[1..10] OF STRING[20]; // Log entries
END_VAR

VAR
    ConnectionStatus : ARRAY[1..3] OF BOOL; // Status of each protocol
    ErrorCode : ARRAY[1..3] OF INT; // Error code for each protocol
    LastScanTime : TIME; // Time of last scan
    CurrentScanTime : TIME; // Current scan time
    ScanInterval : TIME := T#5s; // Scan interval
    ScanRunning : BOOL; // Flag to track scan execution
    LogIndex : INT := 0; // Current index for log entries
END_VAR

// Initialize scan variables
ScanRunning := FALSE;
CurrentScanTime := T#0s;

// Execute scan if Execute is TRUE
IF Execute THEN
    IF NOT ScanRunning THEN
        ScanRunning := TRUE;
        CurrentScanTime := T#0s;
    END_IF;

    // Poll connection status
    FOR i := 1 TO 3 DO
        IF ConnectionStatus[i] THEN
            ErrorCode[i] := 0;
        ELSE
            ErrorCode[i] := 1; // 1 = connection failure
        END_IF;
    END_FOR;

    // Log scan result
    IF NOT ScanRunning THEN
        IF LogIndex < 10 THEN
            LogEntry[LogIndex] := STRING[20]('Protocol ' + INT[3] + ': Connection Status = ' + STRING[3] + ' (' + STRING[3] + ')');
            LogIndex := LogIndex + 1;
        END_IF;
    END_IF;
END_IF;

// Reset scan if Reset is TRUE
IF Reset THEN
    ScanRunning := FALSE;
    CurrentScanTime := T#0s;
    LogIndex := 0;
    Alarm := FALSE;
    AlarmText := '';
END_IF;

// Check if scan is running
IF ScanRunning THEN
    CurrentScanTime := T

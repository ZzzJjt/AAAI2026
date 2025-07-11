### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text function block to monitor OPC UA, Modbus, and Profinet connections, trigger alarms on failures, and log detailed audit trail entries with error codes and timestamps for real-time diagnostics.

### Prompt:
**Communication Monitoring for OPC UA, Modbus, and Profinet Using IEC 61131-3 Structured Text:**

Develop a function block in structured text (ST) as per IEC 61131-3 standards to monitor communication connections to an OPC UA server, Modbus server, and Profinet in a machine system. The function block should continuously check the connection status of each protocol, and if any connection fails, an alarm should be triggered. Additionally, when a connection is lost, an entry must be created in the audit trail, detailing the reason for the server being down along with the corresponding error code. Discuss the implementation logic for monitoring multiple protocols, error detection, and how to effectively manage and log communication failures for real-time monitoring and troubleshooting.

**R-I-S-E:**

🟥 R (Role) – Your Role

Act as a control systems engineer developing IEC 61131-3 Structured Text (ST) function blocks for real-time communication monitoring in industrial automation systems.

🟩 I (Input) – What You’re Given

You need to create a function block that monitors communication links to an OPC UA server, a Modbus server, and a Profinet device. The function block must detect connection failures, trigger alarms for each protocol independently, and generate audit trail entries that include error codes and reasons for the failure. It should operate cyclically and be capable of managing multiple protocol states simultaneously.

🟧 S (Steps) – What You Need to Do
	1.	Design a function block in Structured Text (ST) with input parameters for each protocol’s connection state and error details.
	2.	Implement logic to detect status changes, timeouts, or communication faults.
	3.	When a failure is detected, raise an alarm (e.g., set a BOOL flag or output an error code) and log a detailed audit entry including timestamp, protocol type, error reason, and code.
	4.	Ensure that the function block handles each protocol independently and resets alarms or logs recovery if communication is restored.

🟦 E (Expectation) – What Success Looks Like

The result should be a robust, reusable ST function block capable of continuously monitoring OPC UA, Modbus, and Profinet connections. It should trigger real-time alarms for any failures and provide accurate, timestamped audit trail entries to support fast diagnostics, improved uptime, and system-wide communication transparency.

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text function block to monitor OPC UA, Modbus, and Profinet connections, trigger alarms on failures, and log detailed audit trail entries with error codes and timestamps for real-time diagnostics.
**Communication Monitoring for OPC UA, Modbus, and Profinet Using IEC 61131-3 Structured Text:**

Develop a function block in structured text (ST) as per IEC 61131-3 standards to monitor communication connections to an OPC UA server, Modbus server, and Profinet in a machine system. The function block should continuously check the connection status of each protocol, and if any connection fails, an alarm should be triggered. Additionally, when a connection is lost, an entry must be created in the audit trail, detailing the reason for the server being down along with the corresponding error code. Discuss the implementation logic for monitoring multiple protocols, error detection, and how to effectively manage and log communication failures for real-time monitoring and troubleshooting.

**R-I-S-E:**

🟥 R (Role) – Your Role

Act as a control systems engineer developing IEC 61131-3 Structured Text (ST) function blocks for real-time communication monitoring in industrial automation systems.

🟩 I (Input) – What You’re Given

You need to create a function block that monitors communication links to an OPC UA server, a Modbus server, and a Profinet device. The function block must detect connection failures, trigger alarms for each protocol independently, and generate audit trail entries that include error codes and reasons for the failure. It should operate cyclically and be capable of managing multiple protocol states simultaneously.

🟧 S (Steps) – What You Need to Do
	1.	Design a function block in Structured Text (ST) with input parameters for each protocol’s connection state and error details.
	2.	Implement logic to detect status changes, timeouts, or communication faults.
	3.	When a failure is detected, raise an alarm (e.g., set a BOOL flag or output an error code) and log a detailed audit entry including timestamp, protocol type, error reason, and code.
	4.	Ensure that the function block handles each protocol independently and resets alarms or logs recovery if communication is restored.

🟦 E (Expectation) – What Success Looks Like

The result should be a robust, reusable ST function block capable of continuously monitoring OPC UA, Modbus, and Profinet connections. It should trigger real-time alarms for any failures and provide accurate, timestamped audit trail entries to support fast diagnostics, improved uptime, and system-wide communication transparency. The function block should be designed with scalability in mind, allowing for easy integration into larger control systems and the ability to monitor additional protocols in the future.

**Function Block Design:**

```structuredtext
FUNCTION_BLOCK CommunicationMonitor
VAR_INPUT
    OPCUA_Status : BOOL; // Input for OPC UA connection status
    Modbus_Status : BOOL; // Input for Modbus connection status
    Profinet_Status : BOOL; // Input for Profinet connection status
    OPCUA_ErrorCode : INT; // Input for OPC UA error code
    Modbus_ErrorCode : INT; // Input for Modbus error code
    Profinet_ErrorCode : INT; // Input for Profinet error code
END_VAR

VAR_OUTPUT
    OPCUA_Alarm : BOOL; // Output for OPC UA connection failure alarm
    Modbus_Alarm : BOOL; // Output for Modbus connection failure alarm
    Profinet_Alarm : BOOL; // Output for Profinet connection failure alarm
    AuditTrail : STRING; // Output for audit trail entry
END_VAR

VAR
    OPCUA_LastStatus : BOOL; // Last known status of OPC UA connection
    Modbus_LastStatus : BOOL; // Last known status of Modbus connection
    Profinet_LastStatus : BOOL; // Last known status of Profinet connection
    OPCUA_Timeout : TIME; // Timeout for OPC UA connection
    Modbus_Timeout : TIME; // Timeout for Modbus connection
    Profinet_Timeout : TIME; // Timeout for Profinet connection
    OPCUA_ErrorDetected : BOOL; // Flag for OPC UA error detection
    Modbus_ErrorDetected : BOOL; // Flag for Modbus error detection
    Profinet_ErrorDetected : BOOL; // Flag for Profinet error detection
    OPCUA_AuditEntry : STRING; // Audit entry for OPC UA
    Modbus_AuditEntry : STRING; // Audit entry for Modbus
    Profinet_AuditEntry : STRING; // Audit entry for Profinet
END_VAR

// Initialize variables
OPCUA_LastStatus := OPCUA_Status;
Modbus_LastStatus := Modbus_Status;
Profinet_LastStatus := Profinet_Status;

// Check for connection status changes
IF OPCUA_Status <> OPCUA_LastStatus THEN
    OPCUA_LastStatus := OPCUA_Status;
    IF OPCUA_Status = FALSE THEN
        OPCUA_ErrorDetected := TRUE;
        OPCUA_A

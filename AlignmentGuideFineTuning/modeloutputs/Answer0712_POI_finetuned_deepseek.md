### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text function block to monitor OPC UA, Modbus, and Profinet connections, trigger alarms on failures, and log protocol-specific errors with timestamps for real-time diagnostics.

### Prompt:
**Communication Monitoring for OPC UA, Modbus, and Profinet Using IEC 61131-3 Structured Text:**

Develop a function block in structured text (ST) as per IEC 61131-3 standards to monitor communication connections to an OPC UA server, Modbus server, and Profinet in a machine system. The function block should continuously check the connection status of each protocol, and if any connection fails, an alarm should be triggered. Additionally, when a connection is lost, an entry must be created in the audit trail, detailing the reason for the server being down along with the corresponding error code. Discuss the implementation logic for monitoring multiple protocols, error detection, and how to effectively manage and log communication failures for real-time monitoring and troubleshooting.

**R-T-F:**

🟥 R (Role) – Your Role

Act as a PLC programmer using IEC 61131-3 Structured Text to develop diagnostic and monitoring tools for industrial communication systems.

🟩 T (Task) – Your Objective

Develop a Structured Text (ST) function block that monitors the communication status of OPC UA, Modbus, and Profinet protocols in a machine system. The block must continuously check each connection, trigger an alarm when a failure is detected, and log an entry in the audit trail with details such as the protocol, error reason, and error code. The function block should support independent handling of each protocol and be robust enough for real-time industrial use.

🟧 F (Format) – Expected Output

Provide an IEC 61131-3 compliant ST function block that includes:
	•	Input variables for connection state and error information
	•	Internal logic to detect communication failures and recoveries
	•	Boolean alarms or error flags for each protocol
	•	Structured audit logging (e.g., protocol name, error code, reason, timestamp)
	•	Comments explaining logic for maintenance and reuse

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text function block to monitor OPC UA, Modbus, and Profinet connections, trigger alarms on failures, and log protocol-specific errors with timestamps for real-time diagnostics.
**Communication Monitoring for OPC UA, Modbus, and Profinet Using IEC 61131-3 Structured Text:**

Develop a function block in structured text (ST) as per IEC 61131-3 standards to monitor communication connections to an OPC UA server, Modbus server, and Profinet in a machine system. The function block should continuously check the connection status of each protocol, and if any connection fails, an alarm should be triggered. Additionally, when a connection is lost, an entry must be created in the audit trail, detailing the reason for the server being down along with the corresponding error code. Discuss the implementation logic for monitoring multiple protocols, error detection, and how to effectively manage and log communication failures for real-time monitoring and troubleshooting.

**R-T-F:**

🟥 R (Role) – Your Role

Act as a PLC programmer using IEC 61131-3 Structured Text to develop diagnostic and monitoring tools for industrial communication systems.

🟩 T (Task) – Your Objective

Develop a Structured Text (ST) function block that monitors the communication status of OPC UA, Modbus, and Profinet protocols in a machine system. The block must continuously check each connection, trigger an alarm when a failure is detected, and log an entry in the audit trail with details such as the protocol, error reason, and error code. The function block should support independent handling of each protocol and be robust enough for real-time industrial use.

🟧 F (Format) – Expected Output

Provide an IEC 61131-3 compliant ST function block that includes:
	•	Input variables for connection state and error information
	•	Internal logic to detect communication failures and recoveries
	•	Boolean alarms or error flags for each protocol
	•	Structured audit logging (e.g., protocol name, error code, reason, timestamp)
	•	Comments explaining logic for maintenance and reuse
(* IEC 61131-3 Structured Text Function Block: OPC UA, Modbus, and Profinet Connection Monitoring *)
(* Purpose: Monitors communication status of OPC UA, Modbus, and Profinet protocols *)
(* Triggers alarms and logs failures with protocol-specific details *)

FUNCTION_BLOCK OPC_UA_Modbus_Profinet_ConnectionMonitor
VAR_INPUT
    Execute : BOOL;                  (* Trigger execution of monitoring *)
    OPC_UA_Server_Connected : BOOL;   (* TRUE if OPC UA server is connected *)
    Modbus_Server_Connected : BOOL;   (* TRUE if Modbus server is connected *)
    Profinet_Connected : BOOL;       (* TRUE if Profinet is connected *)
    OPC_UA_Server_Error : BOOL;      (* TRUE if OPC UA server has an error *)
    Modbus_Server_Error : BOOL;      (* TRUE if Modbus server has an error *)
    Profinet_Error : BOOL;           (* TRUE if Profinet has an error *)
    OPC_UA_Server_Error_Code : INT;  (* OPC UA error code *)
    Modbus_Server_Error_Code : INT;  (* Modbus error code *)
    Profinet_Error_Code : INT;       (* Profinet error code *)
    OPC_UA_Server_Down : BOOL;       (* TRUE if OPC UA server is down *)
    Modbus_Server_Down : BOOL;       (* TRUE if Modbus server is down *)
    Profinet_Down : BOOL;            (* TRUE if Profinet is down *)
END_VAR

VAR_OUTPUT
    Alarm_OPC_UA : BOOL;             (* TRUE if OPC UA connection fails *)
    Alarm_Modbus : BOOL;             (* TRUE if Modbus connection fails *)
    Alarm_Profinet : BOOL;           (* TRUE if Profinet connection fails *)
    Alarm_OPC_UA_Server_Down : BOOL; (* TRUE if OPC UA server is down *)
    Alarm_Modbus_Server_Down : BOOL;  (* TRUE if Modbus server is down *)
    Alarm_Profinet_Down : BOOL;      (* TRUE if Profinet is down *)
    Audit_Log : ARRAY[1..

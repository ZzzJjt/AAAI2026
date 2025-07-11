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

**Implementation Details:**

1. **OPC UA Connection Monitoring:**
   - Use the OPC UA client library to establish a connection to the OPC UA server.
   - Continuously check the connection status using the `IsConnected` property.
   - If the connection is lost, raise an alarm and log the event in the audit trail with the reason for the failure (e.g., server unreachable, certificate expired, etc.) and the corresponding error code.

2. **Modbus Connection Monitoring:**
   - Use the Modbus client library to establish a connection to the Modbus server.
   - Continuously check the connection status using the `IsConnected` property.
   - If the connection is lost, raise an alarm and log the event in the audit trail with the reason for the failure (e.g., server unreachable, timeout, etc.) and the corresponding error code.

3. **Profinet Connection Monitoring:**
   - Use the Profinet client library to establish a connection to the Profinet network.
   - Continuously check the connection status using the `IsConnected` property.
   - If the connection is lost, raise an alarm and log the event in the audit trail with the reason for the failure (e.g., network unreachable, device offline, etc.) and the corresponding error code.

4. **Error Detection and Alarm Handling:**
   - Implement error detection mechanisms for each protocol, such as timeouts, connection retries, and error handling.
   - Raise an alarm when a connection failure is detected, and clear the alarm when the connection is re-established.
   - Use the `Alarm` data type to manage the alarm status and trigger alarms when necessary.

5. **Memory-Safe Logging:**
   - Implement a memory-safe logging mechanism to store audit trail entries.
   - Use the `Log` data type to store the protocol name, reason for the failure, and error code.
   - Ensure that the audit trail is not overwritten and can be accessed for troubleshooting purposes.

6. **Real-Time Monitoring and Troubleshooting:**
   - Display the alarm status and audit trail entries in a user interface for real-time monitoring.
   - Provide tools for operators and maintenance teams to quickly identify and respond to communication failures.
   - Enable the ability to clear alarms and reset the audit trail when necessary.

**Example Code:**

```ST
// Function Block: CommunicationMonitor
// Input Parameters:
//   - OPCUA_Connection

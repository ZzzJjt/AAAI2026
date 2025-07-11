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

**R-I-S-E:**

🟥 R (Role) – Who You Are

You are a control engineer responsible for developing self-contained, modular function blocks in IEC 61131-3 Structured Text (ST) for industrial automation systems. Your role is to ensure that communication monitoring is implemented in a standardized, fault-tolerant manner, enabling real-time monitoring and troubleshooting of OPC UA, Modbus, and Profinet connections.

🟩 I (Input) – What You Need

You need to create a self-contained function block in IEC 61131-3 Structured Text (ST) to monitor communication status for OPC UA, Modbus, and Profinet protocols. The function block should continuously check the connection status of each protocol, raise an alarm if any connection fails, and generate an audit trail entry containing the protocol name, reason for the failure, and an associated error code.

🟧 S (Strategy) – How to Do It

Develop a self-contained function block in IEC 61131-3 Structured Text (ST) to monitor communication status for OPC UA, Modbus, and Profinet protocols. Use the built-in communication functions to check the connection status of each protocol. If any connection fails, raise an alarm and generate an audit trail entry containing the protocol name, reason for the failure, and an associated error code. Ensure that the function block is self-contained and can be used independently in other control programs.

🟩 E (Expectation) – What You Should Achieve

Your function block should be able to continuously monitor the connection status of OPC UA, Modbus, and Profinet protocols, raise an alarm if any connection fails, and generate an audit trail entry containing the protocol name, reason for the failure, and an associated error code. The function block should be self-contained and able to be used independently in other control programs.

**C-L-A-S-S:**

🟥 C (Context) – The Situation

In industrial automation systems, communication between different components is critical for proper operation. Monitoring the status of communication protocols such as OPC UA, Modbus, and Profinet is essential to ensure that the system is functioning correctly and to detect any failures that may occur. Developing a self-contained function block in IEC 61131-3 Structured Text (ST) to monitor communication status and handle failures is necessary

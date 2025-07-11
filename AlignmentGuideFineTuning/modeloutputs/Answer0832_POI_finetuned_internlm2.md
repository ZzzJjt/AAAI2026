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

**Focus on the Process:**

Develop a self-contained function block in IEC 61131-3 Structured Text (ST) to monitor the communication status of OPC UA, Modbus, and Profinet protocols in a machine control system. The function block should:

- Continuously check the connection status of each protocol.
- Raise an alarm if any connection fails.
- Generate an audit trail entry for each failed connection, including the protocol name, reason for failure, and associated error code.
- Handle each protocol independently, ensuring that the logic is self-contained and can be reused across different applications.
- Use IEC 61131-3 ST syntax to implement the logic, focusing on clarity, efficiency, and adherence to the standard.

**R-E-A-L:**

🟥 R (Role) – Who You Are

You are a control engineer responsible for developing self-contained function blocks in IEC 61131-3 Structured Text (ST) for monitoring communication status in a machine control system. Your role is to ensure that the function block is clear, efficient, and adheres to the standard, enabling real-time monitoring and fault diagnostics for OPC UA, Modbus, and Profinet protocols.

🟩 E (Expertise) – What You Bring to the Task

You have experience in developing self-contained function blocks in IEC 61131-3 Structured Text (ST) for monitoring communication status in industrial control systems. You are familiar with the syntax and logic required to implement communication monitoring for OPC UA, Modbus, and Profinet protocols, and you understand the importance of self-contained logic for reusability and maintainability.

🟧 A (Action) – What You Do

Develop a self-contained function block in IEC 61131-3 Structured Text (ST) to monitor the communication status of OPC UA, Modbus, and Profinet protocols in a machine control system. The function block should:

- Continuously check the connection status of each protocol.
- Raise an alarm if any connection fails.
- Generate an audit trail entry for each failed connection, including the protocol name, reason for failure, and associated error code.
- Handle each protocol independently, ensuring that the logic is self-contained and can be reused across different applications.
- Use IEC 61131-3 ST syntax to implement the logic, focusing on clarity, efficiency, and adherence to

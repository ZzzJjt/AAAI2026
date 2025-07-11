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
FUNCTION_BLOCK OPC_UA_Client
VAR_INPUT
    Execute : BOOL; // Trigger execution
    ServerAddress : STRING[20]; // OPC UA server address
    ServerPort : INT; // OPC UA server port
    ServerCredentials : STRING[20]; // OPC UA server credentials
END_VAR

VAR_OUTPUT
    Status : BOOL; // TRUE if connection is established
    ErrorCode : INT; // Error code (0 = OK, 1 = Invalid server address, 2 = Invalid server port, 3 = Invalid server credentials)
    ErrorString : STRING[20]; // Error message
    ConnectionEstablished : BOOL; // TRUE if connection is established
    ServerAddressValid : BOOL; // TRUE if server address is valid
    ServerPortValid : BOOL; // TRUE if server port is valid
    ServerCredentialsValid : BOOL; // TRUE if server credentials are valid
END_VAR

VAR
    Client : OPC_UA_Client; // OPC UA client object
    ServerAddressValid : BOOL := TRUE;
    ServerPortValid : BOOL := TRUE;
    ServerCredentialsValid : BOOL := TRUE;
END_VAR

METHOD Execute : BOOL
BEGIN
    IF Execute THEN
        // Check input validity
        IF NOT ServerAddressValid THEN
            ErrorCode := 1;
            ErrorString := 'Invalid server address';
            Status := FALSE;
            ConnectionEstablished := FALSE;
            RETURN;
        END_IF;

        IF NOT ServerPortValid THEN
            ErrorCode := 2;
            ErrorString := 'Invalid server port';
            Status := FALSE;
            ConnectionEstablished := FALSE;
            RETURN;
        END_IF;

        IF NOT ServerCredentialsValid THEN
            ErrorCode := 3;
            ErrorString := 'Invalid server credentials';
            Status := FALSE;
            ConnectionEstablished := FALSE;
            RETURN;
        END_IF;

        // Create OPC UA client
        Client := NEW OPC_UA_Client;
        Client.ServerAddress := ServerAddress;
        Client.ServerPort := ServerPort;
        Client.ServerCredentials := ServerCredentials;

        // Connect to server
        IF Client.Connect THEN
            Status := TRUE;
            ConnectionEstablished := TRUE;
            ErrorCode := 0;
            ErrorString

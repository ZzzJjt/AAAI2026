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
FUNCTION_BLOCK OPC_UA_Client
VAR_INPUT
    Execute : BOOL; // Trigger execution
    ServerAddress : STRING[20]; // OPC UA server address
    ServerPort : INT; // OPC UA server port
    ServerCredentials : STRING[20]; // OPC UA server credentials
END_VAR

VAR_OUTPUT
    ConnectionStatus : BOOL; // TRUE if connected, FALSE otherwise
    ErrorCode : INT; // 0 = No error, 1 = Connection failure
    ErrorMessage : STRING[20]; // Detailed error message
END_VAR

VAR
    // OPC UA connection variables
    Client : OPC_UA_Client;
    ServerAddressString : STRING[20];
    ServerPortString : STRING[5];
    ServerCredentialsString : STRING[20];
    ServerAddressParsed : STRING[20];
    ServerPortParsed : INT;
    ServerCredentialsParsed : STRING[20];
    ServerAddressIsValid : BOOL;
    ServerPortIsValid : BOOL;
    ServerCredentialsIsValid : BOOL;
    ServerAddressError : BOOL;
    ServerPortError : BOOL;
    ServerCredentialsError : BOOL;
    ServerAddressErrorString : STRING[20];
    ServerPortErrorString : STRING[20];
    ServerCredentialsErrorString : STRING[20];
END_VAR

// Initialize variables
ConnectionStatus := FALSE;
ErrorCode := 0;
ErrorMessage := '';

// Parse server address
ServerAddressString := ServerAddress;
ServerAddressParsed := ParseAddress(ServerAddressString);
ServerAddressIsValid := AddressIsValid(ServerAddressParsed);

// Parse server port
ServerPortString := IntToStr(ServerPort);
ServerPortParsed := ParsePort(ServerPortString);
ServerPortIsValid := PortIsValid(ServerPortParsed);

// Parse server credentials
ServerCredentialsString := ServerCredentials;
ServerCredentialsParsed := ParseCredentials(ServerCredentialsString);
ServerCredentialsIsValid := CredentialsIsValid(ServerCredentialsParsed);

// Check connection status
IF ServerAddressIsValid AND ServerPortIsValid AND ServerCredentialsIsValid THEN
    ConnectionStatus := TRUE;
ELSE
    ConnectionStatus := FALSE;
END_IF;

// Check for error
IF NOT ConnectionStatus THEN
    ErrorCode := 1;
    ErrorMessage := 'Connection to OPC

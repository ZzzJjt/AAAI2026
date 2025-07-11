### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 structured text function block for a Modbus TCP server that handles 10 parallel client connections, supports standard Modbus function codes (e.g., Read Coils, Write Registers), and includes detailed logic for processing requests like ReadCoils with proper error handling and TCP/IP communication management.  

*(Focus: Scalable Modbus server implementation for industrial automation with concurrent client support.)*

### Prompt:
**Modbus Server for Parallel Client Connections using 61131-3 Structured Text:**

Develop a self-contained 61131-3 structured text function block to implement a Modbus server capable of handling up to 10 parallel client connection requests over Modbus TCP. The server should manage Modbus requests within data ranges that map input and holding registers. The following Modbus function codes must be supported:

	•	0x01: Read Coils
	•	0x02: Read Discrete Inputs
	•	0x03: Read Holding Registers
	•	0x04: Read Input Registers
	•	0x05: Write Single Coil
	•	0x06: Write Single Register
	•	0x0F: Write Multiple Coils
	•	0x10: Write Multiple Registers
	•	0x17: Read/Write Multiple Registers

In addition, describe the ReadCoils method, explaining how it processes client requests, maps coil data, and manages communication over TCP/IP.

**R-I-S-E:**

🟥 R (Role) – Your Role

Act as an IEC 61131-3 Structured Text developer tasked with building a scalable Modbus TCP server for multi-client communication in industrial control systems.

⸻

🟩 I (Input) – What You’re Given

You need to develop a self-contained function block that implements a Modbus TCP server capable of handling up to 10 parallel client connections. The server must support the following Modbus function codes:

	•	0x01: Read Coils
	•	0x02: Read Discrete Inputs
	•	0x03: Read Holding Registers
	•	0x04: Read Input Registers
	•	0x05: Write Single Coil
	•	0x06: Write Single Register
	•	0x0F: Write Multiple Coils
	•	0x10: Write Multiple Registers
	•	0x17: Read/Write Multiple Registers

You also need to explain the logic for the ReadCoils method—how it processes incoming requests, maps coil data, and handles communication over TCP/IP.

⸻

🟧 S (Steps) – What You Need to Do

	1.	Design a Structured Text function block with internal connection management to support up to 10 simultaneous Modbus TCP clients.
	2.	Implement request routing logic that identifies the Modbus function code and dispatches to the appropriate handler (e.g., ReadCoils, WriteSingleRegister).
	3.	In the ReadCoils method:
	•	Parse the starting address and quantity of coils from the client request
	•	Access the internal coil data buffer
	•	Format and return the response according to the Modbus TCP protocol
	•	Handle edge cases like invalid requests or timeouts gracefully
	4.	Implement a loop or connection pool to handle each client independently without blocking others, ensuring robust and scalable performance.

⸻

🟦 E (Expectation) – What Success Looks Like

The function block should allow up to 10 clients to connect and communicate with the Modbus server in parallel, each receiving fast, correct responses to standard Modbus requests. The ReadCoils method and other function code handlers should work reliably under load, with appropriate error reporting and protocol compliance—providing a high-performance communication layer for real-world automation systems.

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 structured text function block for a Modbus TCP server that handles 10 parallel client connections, supports standard Modbus function codes (e.g., Read Coils, Write Registers), and includes detailed logic for processing requests like ReadCoils with proper error handling and TCP/IP communication management.  

*(Focus: Scalable Modbus server implementation for industrial automation with concurrent client support.)*
**Modbus Server for Parallel Client Connections using 61131-3 Structured Text:**

Develop a self-contained 61131-3 structured text function block to implement a Modbus server capable of handling up to 10 parallel client connection requests over Modbus TCP. The server should manage Modbus requests within data ranges that map input and holding registers. The following Modbus function codes must be supported:

	•	0x01: Read Coils
	•	0x02: Read Discrete Inputs
	•	0x03: Read Holding Registers
	•	0x04: Read Input Registers
	•	0x05: Write Single Coil
	•	0x06: Write Single Register
	•	0x0F: Write Multiple Coils
	•	0x10: Write Multiple Registers
	•	0x17: Read/Write Multiple Registers

In addition, describe the ReadCoils method, explaining how it processes client requests, maps coil data, and manages communication over TCP/IP.

**R-I-S-E:**

🟥 R (Role) – Your Role

Act as an IEC 61131-3 Structured Text developer tasked with building a scalable Modbus TCP server for multi-client communication in industrial control systems.

⸻

🟩 I (Input) – What You’re Given

You need to develop a self-contained function block that implements a Modbus TCP server capable of handling up to 10 parallel client connections. The server must support the following Modbus function codes:

	•	0x01: Read Coils
	•	0x02: Read Discrete Inputs
	•	0x03: Read Holding Registers
	•	0x04: Read Input Registers
	•	0x05: Write Single Coil
	•	0x06: Write Single Register
	•	0x0F: Write Multiple Coils
	•	0x10: Write Multiple Registers
	•	0x17: Read/Write Multiple Registers

You also need to explain the logic for the ReadCoils method—how it processes incoming requests, maps coil data, and handles communication over TCP/IP.

⸻

🟧 S (Steps) – What You Need to Do

	1.	Design a Structured Text function block with internal connection management to support up to 10 simultaneous Modbus TCP clients.
	2.	Implement request routing logic that identifies the Modbus function code and dispatches to the appropriate handler (e.g., ReadCoils, WriteSingleRegister).
	3.	In the ReadCoils method:
	•	Parse the starting address and quantity of coils from the client request
	•	Access the internal coil data buffer
	•	Format and return the response according to the Modbus TCP protocol
	•	Handle edge cases like invalid requests or timeouts gracefully
	4.	Implement a loop or connection pool to handle each client independently without blocking others, ensuring robust and scalable performance.

⸻

🟦 E (Expectation) – What Success Looks Like

The function block should allow up to 10 clients to connect and communicate with the Modbus server in parallel, each receiving fast, correct responses to standard Modbus requests. The ReadCoils method and other function code handlers should work reliably under load, with appropriate error reporting and protocol compliance—providing a high-performance communication layer for real-world automation systems.
FUNCTION_BLOCK FB_ModbusTCP_Server
VAR_INPUT
    Enable : BOOL; // Enable the server
    ClientAddress : STRING[15]; // Client IP address
    ClientPort : WORD; // Client port
    MaxClients : INT := 10; // Maximum number of clients
END_VAR

VAR_OUTPUT
    ClientConnected : BOOL; // TRUE if a client is connected
    ClientID : INT; // Client ID (0-MaxClients)
    Error : BOOL; // TRUE if an error occurred
    ErrorCode : INT; // Error code (0=NoError, 1=InvalidAddress, 2=InvalidPort, 3=MaxClientsReached)
    ClientData : ARRAY[1..10] OF INT; // Client data buffer
    ClientDataSize : INT; // Client data size
    ClientDataValid : BOOL; // TRUE if client data is valid
    ClientDataError : BOOL; // TRUE if client data is invalid
    ClientDataErrorCode : INT; // Error code (0=NoError, 1=InvalidSize, 2=InvalidFormat)
END_VAR

VAR
    ClientCount : INT := 0; // Current client count
    ClientIDMap : ARRAY[1..MaxClients] OF INT; // Client ID mapping
    ClientDataMap : ARRAY[1..MaxClients] OF ARRAY[1..10] OF INT; // Client data buffer mapping
    ClientDataSizeMap : ARRAY[1..MaxClients] OF INT; // Client data size mapping
    ClientDataValidMap : ARRAY[1..MaxClients] OF BOOL; // Client data validity mapping
    ClientDataErrorMap : ARRAY[1..MaxClients] OF BOOL; // Client data error mapping
    ClientDataErrorCodeMap : ARRAY[1..MaxClients] OF INT; // Client data error code mapping
    ClientConnection : ARRAY[1..MaxClients] OF BOOL; // Client connection status
    ClientConnectionMap : ARRAY[1..MaxClients] OF BOOL; // Client connection status mapping
    ClientConnectionID : ARRAY[1..MaxClients] OF INT; // Client connection ID mapping
    ClientConnectionIDMap : ARRAY[1..MaxClients] OF INT; // Client connection ID mapping
    ClientConnectionIDMap : ARRAY[1..MaxClients] OF INT; // Client connection ID mapping
    ClientConnectionIDMap

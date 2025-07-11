### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text function block for a Modbus TCP server supporting 10 parallel clients, handling standard Modbus function codes (e.g., ReadCoils, WriteRegisters), with robust request parsing, data mapping, and concurrent connection management.  

*(Focus: Scalable Modbus TCP server implementation in industrial automation.)*

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
Develop an IEC 61131-3 Structured Text function block for a Modbus TCP server supporting 10 parallel clients, handling standard Modbus function codes (e.g., ReadCoils, WriteRegisters), with robust request parsing, data mapping, and concurrent connection management.  

*(Focus: Scalable Modbus TCP server implementation in industrial automation.)*
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
    ClientPort : INT; // Client port
    MaxClients : INT := 10; // Maximum clients
END_VAR

VAR_OUTPUT
    Response : STRING[15]; // Response to the client
    Error : BOOL; // Error flag
    ErrorCode : INT; // Error code (0 = OK, 1 = Invalid request, 2 = Timeout, 3 = Connection error)
END_VAR

VAR
    ClientCount : INT := 0; // Current client count
    ClientID : INT; // Client ID
    ClientConnection : BOOL; // Client connection status
    ClientRequest : STRING[15]; // Client request
    ClientAddressString : STRING[15]; // Client address as a string
    ClientPortString : STRING[5]; // Client port as a string
    ClientData : ARRAY[1..100] OF INT; // Client data buffer
    ClientDataMap : ARRAY[1..100] OF INT; // Client data mapping
    ClientDataRange : ARRAY[1..100] OF INT; // Client data range
    ClientDataRangeMap : ARRAY[1..100] OF INT; // Client data range mapping
    ClientDataRangeMax : INT; // Client data range max
    ClientDataRangeMin : INT; // Client data range min
    ClientDataRangeMaxMap : INT; // Client data range max mapping
    ClientDataRangeMinMap : INT; // Client data range min mapping
    ClientDataRangeMaxIndex : INT; // Client data range max index
    ClientDataRangeMinIndex : INT; // Client data range min index
    ClientDataRangeMapIndex : INT; // Client data range map index
    ClientDataRangeMapIndexMax : INT; // Client data range map index max
    ClientDataRangeMapIndexMin : INT; // Client data range map index min
    ClientDataRangeMapIndexMaxIndex : INT; // Client data range map index max index
    ClientDataRangeMapIndexMinIndex : INT; // Client data range map index min index
    ClientDataRangeMapIndexMaxIndexMax : INT; // Client data range map index max index max
    ClientDataRangeMap

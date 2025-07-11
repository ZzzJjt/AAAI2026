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
FUNCTION_BLOCK FB_ModbusTCPServer
VAR_INPUT
    Enable : BOOL; // Enable the server
    Port : INT := 502; // Modbus TCP port number
END_VAR

VAR_OUTPUT
    Active : BOOL; // Indicates if the server is active
    Error : BOOL; // Error flag
    ErrorID : DWORD; // Error code
END_VAR

VAR
    Server : TcpServer; // TcpServer instance
    Client : TcpClient; // TcpClient instance
    Buffer : ARRAY[1..256] OF BYTE; // Receive buffer
    Request : ARRAY[1..256] OF BYTE; // Request buffer
    Response : ARRAY[1..256] OF BYTE; // Response buffer
    RequestLength : INT; // Length of the request
    ResponseLength : INT; // Length of the response
    CoilData : ARRAY[1..1000] OF BOOL; // Coil data buffer
    TempData : ARRAY[1..1000] OF BYTE; // Temporary data buffer
    TempIndex : INT := 0; // Index for temporary data
    TempTimeout : TON; // Timer for temporary data timeout
    TempTimeoutValue : TIME := T#1s; // Timeout value for temporary data
    TempTimeoutActive : BOOL; // Flag for timer activation
    RequestType : INT; // Modbus function code
    CoilAddress : INT; // Coil address
    Quantity : INT; // Quantity of coils
    Data : ARRAY[1..1000] OF BYTE; // Data buffer for ReadCoils
    DataLength : INT; // Length of the data buffer
    i : INT; // Loop counter
    TempBuffer : ARRAY[1..256] OF BYTE; // Temporary buffer for response
    TempBufferLength : INT; // Length of the temporary buffer
    TempBufferIndex : INT; // Index for temporary buffer
    TempBufferTimeout : TON; // Timer for temporary buffer timeout
    TempBufferTimeoutValue : TIME := T#1s; // Timeout value for temporary buffer
    TempBufferTimeoutActive : BOOL; // Flag for timer activation
    TempBufferTimeout

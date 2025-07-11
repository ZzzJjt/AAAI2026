### Intent:
**Intent Summary:**  
Create a Modbus TCP server function block in IEC 61131-3 Structured Text that handles up to 10 parallel client connections, supports key Modbus function codes (0x01–0x17), and includes a detailed `ReadCoils` method for processing requests, mapping coil data, and managing TCP/IP communication robustly.  

*(Focus: Scalable, concurrent Modbus server implementation for PLCs with protocol compliance and thread-safe memory access.)*

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

**B-A-B:**

🟥 B (Before) – The Challenge

In industrial automation networks, Modbus TCP servers often struggle to manage multiple simultaneous client connections efficiently—especially when implemented on PLCs using IEC 61131-3. Many solutions lack scalability, do not support the full set of function codes, or have limited support for real-time concurrent processing, which can lead to data conflicts, slow responses, or communication failures.

🟩 A (After) – The Ideal Outcome

Develop a robust, self-contained IEC 61131-3 Structured Text function block that acts as a Modbus TCP server supporting up to 10 parallel client connections. It must handle standard Modbus requests across mapped coils and register ranges and support a comprehensive set of function codes, including:

	•	0x01 to 0x04 for reading
	•	0x05, 0x06, 0x0F, 0x10 for writing
	•	0x17 for combined read/write access

The function block should process each client’s request independently, with built-in TCP/IP communication management and conflict-free access to shared memory regions.

🟧 B (Bridge) – The Implementation Strategy

Structure the function block to create and manage up to 10 parallel TCP connections, each mapped to an internal request handler. Implement logic to decode incoming Modbus packets, route them to the appropriate processing method based on function code, and ensure synchronized access to memory.
For example, in the ReadCoils method:

	•	Extract the coil address range from the request
	•	Access the internal coil buffer and return the requested bits
	•	Wrap the result in a valid Modbus TCP response frame
	•	Handle connection-specific timeouts and return error codes if needed

This design ensures high responsiveness, protocol compliance, and robustness in multi-client industrial environments.

### Generated Code:
**Intent Summary:**  
Create a Modbus TCP server function block in IEC 61131-3 Structured Text that handles up to 10 parallel client connections, supports key Modbus function codes (0x01–0x17), and includes a detailed `ReadCoils` method for processing requests, mapping coil data, and managing TCP/IP communication robustly.  

*(Focus: Scalable, concurrent Modbus server implementation for PLCs with protocol compliance and thread-safe memory access.)*
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

**B-A-B:**

🟥 B (Before) – The Challenge

In industrial automation networks, Modbus TCP servers often struggle to manage multiple simultaneous client connections efficiently—especially when implemented on PLCs using IEC 61131-3. Many solutions lack scalability, do not support the full set of function codes, or have limited support for real-time concurrent processing, which can lead to data conflicts, slow responses, or communication failures.

🟩 A (After) – The Ideal Outcome

Develop a robust, self-contained IEC 61131-3 Structured Text function block that acts as a Modbus TCP server supporting up to 10 parallel client connections. It must handle standard Modbus requests across mapped coils and register ranges and support a comprehensive set of function codes, including:

	•	0x01 to 0x04 for reading
	•	0x05, 0x06, 0x0F, 0x10 for writing
	•	0x17 for combined read/write access

The function block should process each client’s request independently, with built-in TCP/IP communication management and conflict-free access to shared memory regions.

🟧 B (Bridge) – The Implementation Strategy

Structure the function block to create and manage up to 10 parallel TCP connections, each mapped to an internal request handler. Implement logic to decode incoming Modbus packets, route them to the appropriate processing method based on function code, and ensure synchronized access to memory.
For example, in the ReadCoils method:

	•	Extract the coil address range from the request
	•	Access the internal coil buffer and return the requested bits
	•	Wrap the result in a valid Modbus TCP response frame
	•	Handle connection-specific timeouts and return error codes if needed

This design ensures high responsiveness, protocol compliance, and robustness in multi-client industrial environments.
FUNCTION_BLOCK ModbusTCPServer
VAR_INPUT
    Enable : BOOL; // Enable the server
    ClientConnected : ARRAY[1..10] OF BOOL; // Connection status for each client
    ClientAddress : ARRAY[1..10] OF WORD; // Remote TCP address for each client
    ClientPort : ARRAY[1..10] OF WORD; // Remote TCP port for each client
    RequestReceived : ARRAY[1..10] OF BOOL; // Request received status for each client
    RequestData : ARRAY[1..10] OF ARRAY[1..255] OF BYTE; // Request data for each client
    ResponseSent : ARRAY[1..10] OF BOOL; // Response sent status for each client
    ResponseData : ARRAY[1..10] OF ARRAY[1..255] OF BYTE; // Response data for each client
    Timeout : TIME; // Timeout for waiting for a response
END_VAR

VAR_OUTPUT
    Error : BOOL; // General error flag
    ErrorCode : DWORD; // Error code
    ClientBusy : BOOL; // Server busy flag
END_VAR

VAR
    ClientHandle : ARRAY[1..10] OF TcpHandle; // TCP handles for each client
    RequestType : ARRAY[1..10] OF WORD; // Modbus function code for each request
    CoilData : ARRAY[1..1024] OF BOOL; // Coil data buffer
    RegisterData : ARRAY[1..1024] OF WORD; // Register data buffer
    RequestIndex : ARRAY[1..10] OF INT; // Index of the current request
    ResponseIndex : ARRAY[1..10] OF INT; // Index of the current response
    i : INT; // Loop variable
    RequestSize : INT; // Size of the current request
    ResponseSize : INT; // Size of the current response
    TempBuffer : ARRAY[1..255] OF BYTE; // Temporary buffer for responses
    TempBufferIndex : INT; // Index of the temporary buffer
    TempBufferSize : INT; // Size of the temporary buffer
    TempBufferTimeout : TIME;

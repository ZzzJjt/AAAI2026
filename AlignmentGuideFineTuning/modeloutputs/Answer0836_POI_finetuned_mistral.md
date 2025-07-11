### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text function block for a Modbus TCP server that handles 10 parallel client connections, supports standard Modbus function codes (e.g., Read Coils, Write Registers), and ensures robust communication with error handling.  

*(Focus: Parallel client support, Modbus compliance, and industrial reliability.)*

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

**T-A-G:**

🟥 T (Task) – What You Need to Do

Develop an IEC 61131-3 Structured Text (ST) function block that acts as a Modbus TCP server capable of managing up to 10 parallel client connections and supporting multiple standard Modbus function codes.

⸻

🟩 A (Action) – How to Do It

Design the function block to handle Modbus TCP communication, parse incoming requests, and execute operations based on the following supported function codes:

	•	0x01: Read Coils
	•	0x02: Read Discrete Inputs
	•	0x03: Read Holding Registers
	•	0x04: Read Input Registers
	•	0x05: Write Single Coil
	•	0x06: Write Single Register
	•	0x0F: Write Multiple Coils
	•	0x10: Write Multiple Registers
	•	0x17: Read/Write Multiple Registers

Ensure that each of the 10 clients is handled independently. Implement detailed internal logic for each function code, especially ReadCoils, which should:

	•	Interpret the client’s coil address request
	•	Extract the appropriate bits from a coil data buffer
	•	Format the data into a valid Modbus TCP response
	•	Communicate the result back to the client
 
Also, include error handling for unsupported requests and connection timeouts.

⸻

🟦 G (Goal) – What You Want to Achieve

Create a reliable, standards-compliant Modbus TCP server function block that can serve multiple clients simultaneously, support industrial communication demands, and provide accurate and fast responses to various Modbus requests—improving system scalability, robustness, and integration flexibility.

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text function block for a Modbus TCP server that handles 10 parallel client connections, supports standard Modbus function codes (e.g., Read Coils, Write Registers), and ensures robust communication with error handling.  

*(Focus: Parallel client support, Modbus compliance, and industrial reliability.)*
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

**T-A-G:**

🟥 T (Task) – What You Need to Do

Develop an IEC 61131-3 Structured Text (ST) function block that acts as a Modbus TCP server capable of managing up to 10 parallel client connections and supporting multiple standard Modbus function codes.

⸻

🟩 A (Action) – How to Do It

Design the function block to handle Modbus TCP communication, parse incoming requests, and execute operations based on the following supported function codes:

	•	0x01: Read Coils
	•	0x02: Read Discrete Inputs
	•	0x03: Read Holding Registers
	•	0x04: Read Input Registers
	•	0x05: Write Single Coil
	•	0x06: Write Single Register
	•	0x0F: Write Multiple Coils
	•	0x10: Write Multiple Registers
	•	0x17: Read/Write Multiple Registers

Ensure that each of the 10 clients is handled independently. Implement detailed internal logic for each function code, especially ReadCoils, which should:

	•	Interpret the client’s coil address request
	•	Extract the appropriate bits from a coil data buffer
	•	Format the data into a valid Modbus TCP response
	•	Communicate the result back to the client
 
Also, include error handling for unsupported requests and connection timeouts.

⸻

🟦 G (Goal) – What You Want to Achieve

Create a reliable, standards-compliant Modbus TCP server function block that can serve multiple clients simultaneously, support industrial communication demands, and provide accurate and fast responses to various Modbus requests—improving system scalability, robustness, and integration flexibility.
FUNCTION_BLOCK ModbusTCPServer
VAR_INPUT
    Enable : BOOL; // Enable the server
END_VAR

VAR_OUTPUT
    Error : BOOL; // Error flag
    ErrorID : DWORD; // Error code
END_VAR

VAR
    ClientConnections : ARRAY[1..10] OF TClientConnection; // Array to store client connections
    ClientCount : INT := 0; // Number of connected clients
    ServerSocket : TSocket; // Server socket
    ClientSocket : TSocket; // Client socket
    ClientAddress : STRING[255]; // Client IP address
    ClientPort : INT; // Client port
    Buffer : ARRAY[1..255] OF BYTE; // Receive buffer
    ReceiveSize : INT; // Size of received data
    SendSize : INT; // Size of data to send
    TempBuffer : ARRAY[1..255] OF BYTE; // Temporary buffer for response
    TempSendSize : INT; // Size of response to send
    TempError : BOOL; // Temporary error flag
    TempErrorID : DWORD; // Temporary error code
    i : INT; // Loop counter
    RequestType : DWORD; // Modbus request type
    CoilAddress : INT; // Coil address
    RegisterAddress : INT; // Register address
    CoilValue : BOOL; // Coil value
    RegisterValue : DWORD; // Register value
    Response : ARRAY[1..255] OF BYTE; // Modbus response
    ResponseSize : INT; // Size of response
    Timeout : INT := 1000; // Timeout in milliseconds
    Timer : TON; // Timer for timeout
    Connected : BOOL; // Connection status
    RequestReceived : BOOL; // Request received flag
    RequestSent : BOOL; // Request sent flag
    ResponseSent : BOOL; // Response sent flag
    RequestID : DWORD; // Modbus request ID
    ResponseID : DWORD; // Modbus response ID
    ModbusError : BOOL; // Modbus error flag
    ModbusErrorID : DWORD; // Modbus error code
END_VAR

// Initialize variables
Error := FALSE;
ErrorID

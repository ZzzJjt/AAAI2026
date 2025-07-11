### Intent:
**Intent Summary:**  
Develop a Modbus TCP server function block in IEC 61131-3 Structured Text that supports 10 parallel client connections and implements key Modbus functions (including ReadCoils), with robust request handling, TCP/IP management, and diagnostic outputs.  

*(Focus: Concurrency, protocol compliance, and communication reliability.)*

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

**R-T-F:**

🟥 R (Role) – Your Role

Act as a PLC software engineer developing advanced communication interfaces using IEC 61131-3 Structured Text for Modbus TCP networking.

⸻

🟩 T (Task) – What You Need to Do

Create a self-contained function block that implements a Modbus TCP server capable of handling up to 10 parallel client connections. The server must support the following Modbus function codes:
	•	0x01: Read Coils
	•	0x02: Read Discrete Inputs
	•	0x03: Read Holding Registers
	•	0x04: Read Input Registers
	•	0x05: Write Single Coil
	•	0x06: Write Single Register
	•	0x0F: Write Multiple Coils
	•	0x10: Write Multiple Registers
	•	0x17: Read/Write Multiple Registers

You should also provide an explanation of how the ReadCoils method works—including parsing client requests, mapping coil data, handling TCP/IP communication, and formatting responses correctly.

⸻

🟧 F (Format) – Expected Output

Produce an IEC 61131-3 compliant Structured Text function block that includes:
	•	Support for 10 concurrent Modbus TCP client sessions
	•	Parsing and routing logic for supported function codes
	•	Full implementation of the ReadCoils method with address handling, bit-packing, and Modbus TCP frame construction
	•	Robust TCP/IP communication management and timeout detection
	•	Internal diagnostics or status outputs for connection health and protocol errors
	•	Clear code comments for maintainability and scalability

### Generated Code:
**Intent Summary:**  
Develop a Modbus TCP server function block in IEC 61131-3 Structured Text that supports 10 parallel client connections and implements key Modbus functions (including ReadCoils), with robust request handling, TCP/IP management, and diagnostic outputs.  

*(Focus: Concurrency, protocol compliance, and communication reliability.)*
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

**R-T-F:**

🟥 R (Role) – Your Role

Act as a PLC software engineer developing advanced communication interfaces using IEC 61131-3 Structured Text for Modbus TCP networking.

⸻

🟩 T (Task) – What You Need to Do

Create a self-contained function block that implements a Modbus TCP server capable of handling up to 10 parallel client connections. The server must support the following Modbus function codes:
	•	0x01: Read Coils
	•	0x02: Read Discrete Inputs
	•	0x03: Read Holding Registers
	•	0x04: Read Input Registers
	•	0x05: Write Single Coil
	•	0x06: Write Single Register
	•	0x0F: Write Multiple Coils
	•	0x10: Write Multiple Registers
	•	0x17: Read/Write Multiple Registers

You should also provide an explanation of how the ReadCoils method works—including parsing client requests, mapping coil data, handling TCP/IP communication, and formatting responses correctly.

⸻

🟧 F (Format) – Expected Output

Produce an IEC 61131-3 compliant Structured Text function block that includes:
	•	Support for 10 concurrent Modbus TCP client sessions
	•	Parsing and routing logic for supported function codes
	•	Full implementation of the ReadCoils method with address handling, bit-packing, and Modbus TCP frame construction
	•	Robust TCP/IP communication management and timeout detection
	•	Internal diagnostics or status outputs for connection health and protocol errors
	•	Clear code comments for maintainability and scalability
FUNCTION_BLOCK ModbusTCPServer
VAR_INPUT
    Enable : BOOL; // Enable server operation
    ClientAddress : ARRAY[1..10] OF INT; // Client addresses
    ClientPort : INT; // Client port number
    ClientTimeout : TIME; // Timeout for client connection
END_VAR

VAR_OUTPUT
    Response : ARRAY[1..10] OF ARRAY[1..10] OF INT; // Response array for each client
    Error : ARRAY[1..10] OF BOOL; // Error flag for each client
    ErrorString : ARRAY[1..10] OF STRING[20]; // Error message for each client
END_VAR

VAR
    ClientCount : INT := 0; // Number of active clients
    ClientID : INT; // Client ID for each connection
    ClientConnection : ARRAY[1..10] OF TON; // Connection handle for each client
    ClientState : ARRAY[1..10] OF BOOL; // State of each client connection
    ClientData : ARRAY[1..10] OF ARRAY[1..10] OF INT; // Data buffer for each client
    ClientDataSize : ARRAY[1..10] OF INT; // Size of data buffer for each client
    ClientDataAddress : ARRAY[1..10] OF ARRAY[1..10] OF INT; // Address buffer for each client
    ClientDataAddressSize : ARRAY[1..10] OF INT; // Size of address buffer for each client
    ClientDataAddressValid : ARRAY[1..10] OF BOOL; // Valid flag for address buffer for each client
    ClientDataValid : ARRAY[1..10] OF BOOL; // Valid flag for data buffer for each client
    ClientDataValidSize : ARRAY[1..10] OF INT; // Size of data buffer for each client
    ClientDataValidAddress : ARRAY[1..10] OF BOOL; // Valid flag for address buffer for each client
    ClientDataValidAddressSize : ARRAY[1..10] OF INT; // Size of address buffer for each client
    ClientDataValidAddressValid : ARRAY[1..10] OF BOOL; // Valid flag for address buffer for each client
    ClientDataValidAddressValidSize : ARRAY[1..10] OF INT; // Size of address buffer for each client

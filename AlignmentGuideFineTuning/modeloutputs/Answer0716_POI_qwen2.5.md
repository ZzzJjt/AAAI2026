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

Ensure that the function block is modular, well-documented, and adheres to IEC 61131-3 standards for structured text programming.

**Modbus Server Function Block in IEC 61131-3 Structured Text:**

```structuredtext
FUNCTION_BLOCK ModbusServer
VAR
    // Define variables for Modbus server parameters
    MaxClients : INT := 10; // Maximum number of concurrent clients
    ClientTable : ARRAY[1..MaxClients] OF ClientData; // Table to store client data
    ClientCount : INT := 0; // Current number of connected clients
    // Define variables for Modbus server state
    ServerState : INT := 0; // State of the server (0: idle, 1: running)
    // Define variables for Modbus server communication
    Socket : INT; // Socket descriptor for the server
    ClientSocket : INT; // Socket descriptor for the client
    // Define variables for Modbus server data
    InputRegisters : ARRAY[1..1000] OF INT; // Input registers
    HoldingRegisters : ARRAY[1..1000] OF INT; // Holding registers
    // Define variables for Modbus server diagnostics
    Diagnostics : INT := 0; // Diagnostic status
END_VAR

// Define ClientData structure
STRUCT ClientData
    Socket : INT; // Socket descriptor for the client
    Address : INT; // Client address
    State : INT; // Client state (0: idle, 1: connected)
END_STRUCT

// Define function to initialize the Modbus server
FUNCTION Initialize : BOOL
VAR_INPUT
    Start : BOOL; // Start the server
END_VAR
VAR_OUTPUT
    Diagnostics : INT; // Diagnostic status
END_VAR
VAR
    // Initialize server state
    ServerState := 0;
    // Initialize client table
    FOR i := 1 TO MaxClients DO
        ClientTable[i].Socket := -1;
        ClientTable[i].Address := 0;
        ClientTable[i].State := 0;
    END_FOR;
    // Initialize input and holding registers
    FOR i := 1 TO 1000 DO
        InputRegisters[i] := 0;
        HoldingRegisters[i] := 0;
    END_FOR;
    // Initialize diagnostics
    Diagnostics := 0;
END_VAR

// Define function to start the Modbus server
FUNCTION

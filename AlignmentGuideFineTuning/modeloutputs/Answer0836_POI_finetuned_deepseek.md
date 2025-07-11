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
FUNCTION_BLOCK FB_ModbusTCPServer
VAR_INPUT
    Enable : BOOL; // Enable the server
    ClientCount : INT; // Number of connected clients
END_VAR

VAR_OUTPUT
    ClientConnected : ARRAY[1..ClientCount] OF BOOL; // TRUE if client is connected
    ClientID : ARRAY[1..ClientCount] OF INT; // Client ID
    ClientAddress : ARRAY[1..ClientCount] OF INT; // Client address
    ClientData : ARRAY[1..ClientCount] OF ARRAY[1..10] OF INT; // Client data buffer
    ClientError : ARRAY[1..ClientCount] OF BOOL; // TRUE if error
    ClientTimeout : ARRAY[1..ClientCount] OF BOOL; // TRUE if timeout
    ClientClosed : ARRAY[1..ClientCount] OF BOOL; // TRUE if client is closed
    ClientClosedID : ARRAY[1..ClientCount] OF INT; // Client ID of closed client
    ClientClosedAddress : ARRAY[1..ClientCount] OF INT; // Client address of closed client
    ClientClosedData : ARRAY[1..ClientCount] OF ARRAY[1..10] OF INT; // Client data buffer of closed client
END_VAR

VAR
    Client : ARRAY[1..ClientCount] OF T_ModbusClient; // Client object array
    ClientID_Map : ARRAY[1..ClientCount] OF INT; // Client ID to index
    ClientAddress_Map : ARRAY[1..ClientCount] OF INT; // Client address to index
    ClientData_Map : ARRAY[1..ClientCount] OF ARRAY[1..10] OF INT; // Client data buffer to index
    ClientError_Map : ARRAY[1..ClientCount] OF BOOL; // Client error flag
    ClientTimeout_Map : ARRAY[1..ClientCount] OF BOOL; // Client timeout flag
    ClientClosed_Map : ARRAY[1..ClientCount] OF BOOL; // Client closed flag
    ClientClosedID_Map : ARRAY[1..ClientCount] OF INT; // Client ID of closed client
    ClientClosedAddress_Map : ARRAY[1..ClientCount] OF INT; // Client address of closed client
    ClientClosedData_Map : ARRAY[1..ClientCount] OF ARRAY[1..10] OF INT; // Client data buffer of closed client

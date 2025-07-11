### Intent:
**Intent Summary:**  
Develop a PROFIBUS DPV1 diagnostic program in IEC 61131-3 Structured Text to monitor and report slave device health metrics (e.g., communication errors, hardware faults) via simulated requests and response parsing, with timeout handling and error management.

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
Develop a PROFIBUS DPV1 diagnostic program in IEC 61131-3 Structured Text to monitor and report slave device health metrics (e.g., communication errors, hardware faults) via simulated requests and response parsing, with timeout handling and error management.
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
(* IEC 61131-3 Structured Text: Modbus Server for Parallel Client Connections *)
(* Handles up to 10 parallel client connections over Modbus TCP *)
(* Supports standard Modbus function codes: 0x01-0x17 *)

FUNCTION_BLOCK ModbusServer
VAR_INPUT
    Enable : BOOL; (* TRUE to start server *)
    ClientCount : UINT; (* Number of active clients *)
    ClientID : UINT[0..9]; (* Client ID for each connection *)
END_VAR

VAR_OUTPUT
    Response : UINT[0..15]; (* Response buffer for each client *)
    Error : BOOL; (* TRUE if error occurs *)
    Timeout : BOOL; (* TRUE if client connection times out *)
    ClientConnected : ARRAY[0..9] OF BOOL; (* TRUE if client is connected *)
    ClientDisconnected : ARRAY[0..9] OF BOOL; (* TRUE if client is disconnected *)
    ClientID : ARRAY[0..9] OF UINT; (* Client ID for each connection *)
END_VAR

VAR
    Client : ARRAY[0..9] OF TON_Client; (* Client object for each connection *)
    ClientCount : UINT; (* Current client count *)
    ClientID : ARRAY[0..9] OF UINT; (* Client ID for each connection *)
    ClientConnected : ARRAY[0..9] OF BOOL; (* TRUE if client is connected *)
    ClientDisconnected : ARRAY[0..9] OF BOOL; (* TRUE if client is disconnected *)
    ClientError : ARRAY[0..9] OF BOOL; (* TRUE if client has error *)
    ClientTimeout : ARRAY[0..9] OF BOOL; (* TRUE if client connection times out *)
    ClientRequest : ARRAY[0..15] OF UINT; (* Request buffer for each client *)
    ClientResponse : ARRAY[0..15] OF UINT; (* Response buffer for each client *)
    ClientID_Loop : ARRAY[0..9] OF UINT; (* Loop index for each client *)
    ClientID_Loop_Index : UINT; (* Loop index for current client *)
    ClientID_Loop_Index_Max : UINT; (* Max loop index *)
    ClientID_Loop_Index_Min : UINT; (* Min loop index *)
    ClientID_Loop_Index_Step :

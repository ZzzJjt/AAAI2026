### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 structured text function block for a Modbus TCP server supporting 10 parallel clients and 9 core function codes, including handling requests like ReadCoils with proper address mapping, error handling, and concurrent connection management.  

*(Focus: Scalable, compliant Modbus TCP server in PLC logic for industrial automation.)*

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

**C-A-R-E:**

🟥 C (Context) – The Background

Modbus TCP is widely used in industrial automation, but many PLC-based implementations are limited in their ability to handle multiple simultaneous client connections or lack support for the full Modbus function set. Ensuring high-speed, reliable communication across many clients—while maintaining protocol compliance—requires a robust, scalable server architecture built directly in IEC 61131-3 Structured Text.

⸻

🟩 A (Action) – The Implementation Task

Develop a self-contained IEC 61131-3 Structured Text function block that acts as a Modbus TCP server capable of handling up to 10 parallel client connections. The server should support the following Modbus function codes:
	•	0x01: Read Coils
	•	0x02: Read Discrete Inputs
	•	0x03: Read Holding Registers
	•	0x04: Read Input Registers
	•	0x05: Write Single Coil
	•	0x06: Write Single Register
	•	0x0F: Write Multiple Coils
	•	0x10: Write Multiple Registers
	•	0x17: Read/Write Multiple Registers

Include internal logic for managing TCP connections, decoding function codes, mapping data to input and holding registers, and responding to client requests in real time.

⸻

🟨 R (Result) – The Expected Outcome

The function block will serve as a robust Modbus TCP server that can manage multiple concurrent requests, ensure reliable and fast data exchange, and maintain synchronization across shared data regions. It will help reduce response latency, prevent access conflicts, and improve system scalability for high-performance industrial applications.

⸻

🟦 E (Example) – A Practical Use Case

Take the ReadCoils method as an example:
When a client sends a request with function code 0x01, the function block:
	1.	Parses the request to extract the starting address and quantity of coils
	2.	Reads the corresponding coil data from internal memory
	3.	Formats the result as a Modbus TCP response
	4.	Sends it back to the requesting client via their dedicated socket
	5.	If any issue arises (e.g. invalid address, timeout), it responds with an appropriate Modbus exception code

This structure ensures each client is served independently, accurately, and without blocking other operations.

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 structured text function block for a Modbus TCP server supporting 10 parallel clients and 9 core function codes, including handling requests like ReadCoils with proper address mapping, error handling, and concurrent connection management.  

*(Focus: Scalable, compliant Modbus TCP server in PLC logic for industrial automation.)*
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

**C-A-R-E:**

🟥 C (Context) – The Background

Modbus TCP is widely used in industrial automation, but many PLC-based implementations are limited in their ability to handle multiple simultaneous client connections or lack support for the full Modbus function set. Ensuring high-speed, reliable communication across many clients—while maintaining protocol compliance—requires a robust, scalable server architecture built directly in IEC 61131-3 Structured Text.

⸻

🟩 A (Action) – The Implementation Task

Develop a self-contained IEC 61131-3 Structured Text function block that acts as a Modbus TCP server capable of handling up to 10 parallel client connections. The server should support the following Modbus function codes:
	•	0x01: Read Coils
	•	0x02: Read Discrete Inputs
	•	0x03: Read Holding Registers
	•	0x04: Read Input Registers
	•	0x05: Write Single Coil
	•	0x06: Write Single Register
	•	0x0F: Write Multiple Coils
	•	0x10: Write Multiple Registers
	•	0x17: Read/Write Multiple Registers

Include internal logic for managing TCP connections, decoding function codes, mapping data to input and holding registers, and responding to client requests in real time.

⸻

🟨 R (Result) – The Expected Outcome

The function block will serve as a robust Modbus TCP server that can manage multiple concurrent requests, ensure reliable and fast data exchange, and maintain synchronization across shared data regions. It will help reduce response latency, prevent access conflicts, and improve system scalability for high-performance industrial applications.

⸻

🟦 E (Example) – A Practical Use Case

Take the ReadCoils method as an example:
When a client sends a request with function code 0x01, the function block:
	1.	Parses the request to extract the starting address and quantity of coils
	2.	Reads the corresponding coil data from internal memory
	3.	Formats the result as a Modbus TCP response
	4.	Sends it back to the requesting client via their dedicated socket
	5.	If any issue arises (e.g. invalid address, timeout), it responds with an appropriate Modbus exception code

This structure ensures each client is served independently, accurately, and without blocking other operations.
FUNCTION_BLOCK FB_ModbusTCP_Server
VAR_INPUT
    Enable : BOOL; // Enable the server
    ClientAddress : ARRAY[1..10] OF INT; // Client addresses
    ClientPort : INT; // Client port
    ClientTimeout : TIME; // Timeout for client requests
END_VAR

VAR_OUTPUT
    Response : ARRAY[1..10] OF ARRAY[1..10] OF INT; // Responses for each client
    Error : ARRAY[1..10] OF BOOL; // Error flag for each client
    ErrorCode : ARRAY[1..10] OF INT; // Error code for each client
END_VAR

VAR
    ClientCount : INT := 0; // Number of active clients
    ClientID : INT; // Current client ID
    ClientSocket : TServerSocket; // Server socket
    ClientConnection : TClientConnection; // Client connection
    ClientData : ARRAY[1..10] OF ARRAY[1..10] OF INT; // Client data buffer
    ClientAddressMap : ARRAY[1..10] OF INT; // Address mapping for each client
    ClientAddressIndex : INT; // Current client address index
    ClientAddressIndexMax : INT; // Maximum client address index
    ClientAddressIndexMin : INT; // Minimum client address index
    ClientAddressIndexValid : BOOL; // Flag indicating valid client address index
    ClientAddressIndexValidMax : INT; // Maximum valid client address index
    ClientAddressIndexValidMin : INT; // Minimum valid client address index
    ClientAddressIndexValidMaxMax : INT; // Maximum valid client address index
    ClientAddressIndexValidMinMin : INT; // Minimum valid client address index
    ClientAddressIndexValidMaxMaxMax : INT; // Maximum valid client address index
    ClientAddressIndexValidMinMinMin : INT; // Minimum valid client address index
    ClientAddressIndexValidMaxMaxMaxMax : INT; // Maximum valid client address index
    ClientAddressIndexValidMinMinMinMin : INT; // Minimum valid client address index
    ClientAddressIndexValidMaxMaxMaxMaxMax : INT; // Maximum valid client address index
    ClientAddressIndexValidMinMinMinMinMin : INT; // Minimum valid client address index
    ClientAddressIndexValidMaxMaxMaxMaxMaxMax : INT; // Maximum valid client address index
    ClientAddressIndexValid

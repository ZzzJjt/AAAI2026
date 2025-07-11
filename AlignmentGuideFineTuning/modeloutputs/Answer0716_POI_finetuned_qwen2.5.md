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

Ensure that the function block is modular, with clear explanations of each part of the Modbus server implementation, including request handling, data mapping, and network communication. Provide a detailed explanation of the ReadCoils method, including how it processes client requests, maps coil data, and manages communication over Modbus TCP.

**T-A-G:**

🟥 T (Task) – What You Need to Do

	•	Create a self-contained function block in IEC 61131-3 Structured Text to implement a Modbus server capable of handling up to 10 parallel client connection requests over Modbus TCP.
	•	Support Modbus function codes: 0x01 (Read Coils), 0x02 (Read Discrete Inputs), 0x03 (Read Holding Registers), 0x04 (Read Input Registers), 0x05 (Write Single Coil), 0x06 (Write Single Register), 0x0F (Write Multiple Coils), 0x10 (Write Multiple Registers), and 0x17 (Read/Write Multiple Registers).
	•	Implement the ReadCoils method to process client requests, map coil data, and manage communication over Modbus TCP.

⸻

🟩 A (Action) – How to Do It

	1.	Define the function block with a descriptive name, such as `ModbusServer10C`.
	2.	Implement the server logic to handle up to 10 parallel client connection requests using a CASE statement or a CASE statement inside a WHILE loop.
	3.	For each Modbus function code, create a CASE statement to handle the specific request. For example:
	•	For ReadCoils (0x01), parse the client request, map the coil data, and format the Modbus TCP response.
	•	For WriteSingleCoil (0x05), validate the input, update the coil state, and respond with an appropriate status.
	4.	Implement the ReadCoils method to:
	•	Accept a Modbus TCP request with a starting address and number of coils to read.
	•	Process the request, ensuring that the specified range is within the valid data range (e.g., 0–1023 for 10 parallel clients).
	•	Map the coil data from the specified range and format it into a Modbus TCP response.
	•	Manage communication with the client, including error handling

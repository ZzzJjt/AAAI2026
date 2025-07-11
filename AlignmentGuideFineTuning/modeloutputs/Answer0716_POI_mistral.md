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

**ReadCoils Method Explanation:**

The ReadCoils method is responsible for handling client requests for reading coil data from the PLC. The method will parse the incoming Modbus TCP frame, validate the request, and return the requested coil data in the correct format.

1. Parse the incoming Modbus TCP frame:
	•	Extract the transaction ID, function code, starting address, and quantity of coils to read.
2. Validate the request:
	•	Check if the request is within the supported function codes (0x01).
	•	Check if the starting address and quantity of coils are within the defined data range.
3. Map the coil data:
	•	Access the coil data within the defined data range.
	•	Bit-pack the coil data into a single word for each response packet.
4. Construct the Modbus TCP response frame:
	•	Create a new Modbus TCP response frame with the transaction ID, function code, starting address, quantity of coils, and the bit-packed coil data.
5. Send the response frame:
	•	Transmit the response frame back to the client using the TCP/IP stack.
6. Handle errors and timeouts:
	•	If an error occurs during the request processing, log the error and send an appropriate error response to the client.
	•	If a timeout occurs during the request processing, log the timeout and send a timeout response to the client.

**Code Snippet Example:**

```
FUNCTION ModbusTCP_Server: TModbusTCP_Server
VAR
    i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z,
        client, request, response, transactionID, functionCode,
        startingAddress, quantity, coilData, bitMask, bitValue,
        errorCode, errorMessage, timeout,
        clients: ARRAY[0..9] OF TModbusTCP_Client;

    (* Initialize clients array *)
    FOR i := 0 TO 9 DO
        clients[i] := TModbusTCP_Client(FALSE);
    END_FOR

    (* Main loop *)
    WHILE TRUE DO
        (* Wait for a new connection *)

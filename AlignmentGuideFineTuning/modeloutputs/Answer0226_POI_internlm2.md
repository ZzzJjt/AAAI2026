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

This structure ensures each client is served independently, accurately, and without blocking other operations. The function block can be easily extended to support other function codes and handle more clients.

⸻

🟧 E (Example) – A Real-World Application

A manufacturing plant with multiple production lines could benefit from this Modbus TCP server. Each line would have a dedicated PLC with a connected HMI or SCADA system. The server would allow the HMI to read and write data from/to the PLC's input and holding registers, enabling real-time monitoring and control of the production process. The server's ability to handle multiple clients concurrently would ensure smooth operation, even during peak production periods.

⸻

🟨 A (Action) – The Implementation Steps

1.	Define the function block's input and output parameters, including the Modbus function code, starting address, and quantity of coils/registers.
2.	Create a data structure to store the coil/registers data, ensuring proper mapping and access control.
3.	Implement logic to manage TCP connections, including connection setup, data transmission, and error handling.
4.	Decode the Modbus function code and extract relevant data from the request.
5.	Process the request based on the function code:
	•	Read Coils: Read the corresponding coil data from the data structure and format the response.
	•	Read Discrete Inputs: Read the corresponding discrete input data and format the response.
	•	Read Holding Registers: Read the corresponding holding register data and format the response.
	•	Read Input Registers: Read the corresponding input register data and format the response.
	•	Write Single Coil: Update the corresponding coil data in the data structure and send a response.
	•	Write Single Register: Update the corresponding register data and send a response.
	•	Write Multiple Coils: Update the corresponding coil data in the data structure and send a response.
	•	Write Multiple Registers: Update the corresponding register data and send a response.
	•	Read/Write Multiple Registers: Process the request and send a response.
6.	Handle any errors or exceptions that may occur during the request processing, such as invalid addresses, timeouts, or data overflows.
7.	Ensure the function block is compliant with the IEC 61131-3 standard and follows best practices for PLC programming.

⸻

🟥 C (Context) – The Importance of Compliance

IEC 61131-3 is the international standard for programming languages and function blocks

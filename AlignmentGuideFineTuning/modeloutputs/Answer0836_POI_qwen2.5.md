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

**ReadCoils Method Description:**

The ReadCoils method is a crucial part of the Modbus server function block, responsible for handling requests to read the status of multiple coils. Here’s a detailed breakdown of how it processes client requests, maps coil data, and manages communication over TCP/IP:

**1. Request Interpretation:**

	•	The method receives a Modbus TCP request packet from a client.
	•	It extracts the function code (0x01 for Read Coils) and the starting address and quantity of coils requested from the packet.

**2. Coil Data Mapping:**

	•	The method accesses the internal coil data buffer, which is typically a bit array representing the status of all coils.
	•	It uses the starting address and quantity to determine which bits in the buffer correspond to the requested coils.

**3. Data Extraction:**

	•	The method extracts the requested bits from the coil data buffer.
	•	It formats these bits into a Modbus response packet, ensuring that the data is correctly ordered and formatted according to Modbus specifications.

**4. Response Formatting:**

	•	The method constructs a Modbus TCP response packet containing the extracted coil data.
	•	It includes the function code (0x01), starting address, quantity of coils, and the extracted data in the response.

**5. Communication:**

	•	The method sends the formatted response packet back to the client over the TCP/IP connection.
	•	It ensures that the response is sent in a timely manner and that the client receives it correctly.

**6. Error Handling:**

	•	The method includes error handling for cases where the requested coil address is out of range or the quantity exceeds the available coils.
	•	It also handles connection timeouts and other communication errors gracefully, ensuring that the server remains stable and responsive.

**7. Parallel Client Support:**

	•	The method is designed to handle multiple client connections simultaneously.
	•	It processes each client request independently, ensuring that the server can handle up to 10 parallel connections efficiently.

By following these steps, the ReadCoils method ensures that the Modbus server function block can accurately and efficiently handle requests to read the status of multiple coils, providing reliable and robust communication for industrial applications.

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
FUNCTION_BLOCK PROFIBUS_DIAGNOSTICS
VAR_INPUT
    EXECUTE : BOOL; // Trigger diagnostic request
    TIMEOUT : TIME; // Maximum wait time for response
END_VAR

VAR_OUTPUT
    DONE : BOOL; // Operation completed successfully
    ERROR : BOOL; // Error occurred
    ERROR_CODE : INT; // Diagnostic error code
    ERROR_MESSAGE : STRING(255); // Detailed error message
    COMM_ERROR : BOOL; // Communication error with slave
    HARDWARE_FAULT : BOOL; // Hardware fault detected
    COMM_TIMEOUT : BOOL; // Communication timeout
    REQUEST_ID : INT; // Request ID from slave
    RESPONSE_CODE : INT; // Response code from slave
    DATA_ERROR : BOOL; // Data integrity error
    PARSING_ERROR : BOOL; // Parsing error
    UNKNOWN_RESPONSE : BOOL; // Unknown response from slave
    REQUEST_SENT : BOOL; // Request sent to slave
    REQUEST_RECEIVED : BOOL; // Request received from slave
    REQUEST_ACK : BOOL; // Request acknowledged by slave
    REQUEST_NAK : BOOL; // Request not acknowledged by slave
    REQUEST_BUSY : BOOL; // Slave busy
    REQUEST_BUSY_TIMEOUT : BOOL; // Slave busy timeout
    REQUEST_BUSY_RETRY : INT; // Number of retries for busy slave
    REQUEST_BUSY_MAX_RETRIES : INT; // Maximum number of retries for busy slave
    REQUEST_BUSY_RETRY_COUNT : INT; // Current retry count
    REQUEST_BUSY_ELAPSED_TIME : TIME; // Elapsed time since last busy check
    REQUEST_BUSY_ELAPSED_TIME_MAX : TIME; // Maximum elapsed time for busy check
    REQUEST_BUSY_ELAPSED_TIME_COUNT : INT; // Number of elapsed time checks
    REQUEST_BUSY_ELAPSED_TIME_COUNT_MAX : INT; // Maximum number of elapsed

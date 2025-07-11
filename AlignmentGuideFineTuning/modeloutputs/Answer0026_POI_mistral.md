### Intent:
**Intent Summary:**  
Create a Modbus TCP server function block in IEC 61131-3 Structured Text that handles up to 10 parallel client connections, supports key Modbus function codes (0x01–0x17), and includes a detailed `ReadCoils` method for processing requests, mapping coil data, and managing TCP/IP communication robustly.  

*(Focus: Scalable, concurrent Modbus server implementation for PLCs with protocol compliance and thread-safe memory access.)*

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

**B-A-B:**

🟥 B (Before) – The Challenge

In industrial automation networks, Modbus TCP servers often struggle to manage multiple simultaneous client connections efficiently—especially when implemented on PLCs using IEC 61131-3. Many solutions lack scalability, do not support the full set of function codes, or have limited support for real-time concurrent processing, which can lead to data conflicts, slow responses, or communication failures.

🟩 A (After) – The Ideal Outcome

Develop a robust, self-contained IEC 61131-3 Structured Text function block that acts as a Modbus TCP server supporting up to 10 parallel client connections. It must handle standard Modbus requests across mapped coils and register ranges and support a comprehensive set of function codes, including:

	•	0x01 to 0x04 for reading
	•	0x05, 0x06, 0x0F, 0x10 for writing
	•	0x17 for combined read/write access

The function block should process each client’s request independently, with built-in TCP/IP communication management and conflict-free access to shared memory regions.

🟧 B (Bridge) – The Implementation Strategy

Structure the function block to create and manage up to 10 parallel TCP connections, each mapped to an internal request handler. Implement logic to decode incoming Modbus packets, route them to the appropriate processing method based on function code, and ensure synchronized access to memory.
For example, in the ReadCoils method:

	•	Extract the coil address range from the request
	•	Access the internal coil buffer and return the requested bits
	•	Wrap the result in a valid Modbus TCP response frame
	•	Handle connection-specific timeouts and return error codes if needed

This design ensures high responsiveness, protocol compliance, and robustness in multi-client industrial environments.

### Generated Code:
**Intent Summary:**  
Create a Modbus TCP server function block in IEC 61131-3 Structured Text that handles up to 10 parallel client connections, supports key Modbus function codes (0x01–0x17), and includes a detailed `ReadCoils` method for processing requests, mapping coil data, and managing TCP/IP communication robustly.  

*(Focus: Scalable, concurrent Modbus server implementation for PLCs with protocol compliance and thread-safe memory access.)*
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

**B-A-B:**

🟥 B (Before) – The Challenge

In industrial automation networks, Modbus TCP servers often struggle to manage multiple simultaneous client connections efficiently—especially when implemented on PLCs using IEC 61131-3. Many solutions lack scalability, do not support the full set of function codes, or have limited support for real-time concurrent processing, which can lead to data conflicts, slow responses, or communication failures.

🟩 A (After) – The Ideal Outcome

Develop a robust, self-contained IEC 61131-3 Structured Text function block that acts as a Modbus TCP server supporting up to 10 parallel client connections. It must handle standard Modbus requests across mapped coils and register ranges and support a comprehensive set of function codes, including:

	•	0x01 to 0x04 for reading
	•	0x05, 0x06, 0x0F, 0x10 for writing
	•	0x17 for combined read/write access

The function block should process each client’s request independently, with built-in TCP/IP communication management and conflict-free access to shared memory regions.

🟧 B (Bridge) – The Implementation Strategy

Structure the function block to create and manage up to 10 parallel TCP connections, each mapped to an internal request handler. Implement logic to decode incoming Modbus packets, route them to the appropriate processing method based on function code, and ensure synchronized access to memory.
For example, in the ReadCoils method:

	•	Extract the coil address range from the request
	•	Access the internal coil buffer and return the requested bits
	•	Wrap the result in a valid Modbus TCP response frame
	•	Handle connection-specific timeouts and return error codes if needed

This design ensures high responsiveness, protocol compliance, and robustness in multi-client industrial environments.

**ReadCoils Method:**

The ReadCoils method is responsible for processing incoming Modbus Read Coils requests (function code 0x01) and returning the requested coil values.

1. Extract the coil address range from the request:

```
function ReadCoils(request: ModbusRequest): ModbusResponse;
var
  startAddress, endAddress: Word;
begin
  startAddress := request.StartAddress;
  endAddress := request.EndAddress;
  // Validate the address range
  if (startAddress > 1023) or (endAddress > 1023) or (startAddress > endAddress) then
    exit(ModbusResponse.IllegalDataAddress);
end;
```

2. Access the internal coil buffer and return the requested bits:

```
// Assuming a global coil buffer of size 1024
var
  coilBuffer: array[0..1023] of Boolean;
var
  i: Word;
begin
  // Map the request address range to the coil buffer
  for i := startAddress to endAddress do
    request.CoilValues[i - startAddress] := coilBuffer[i];
end;
```

3. Wrap the result in a valid Modbus TCP response frame:

```
// Assuming a global function to create a Modbus response
function CreateModbusResponse(responseCode: Word; coilValues: array of Boolean): ModbusResponse;
begin
  // Create a new Modbus response object
  var response: ModbusResponse;
  // Set the response code and coil values
  response.FunctionCode := 0x01;
  response.ResponseCode := responseCode;
  response.CoilValues := coilValues;
  // Return the response object
  response.Length := CalculateModbusResponseLength(response);
  response.Data := CreateModbusData(response);
end;
```

4. Handle connection-specific timeouts and return error codes if needed:

```
// Assuming a global function to check if a connection is still active
function IsConnectionActive(connection: TModbusConnection): Boolean;
begin
  // Check if the

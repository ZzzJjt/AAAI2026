### Intent:
Create an IEC 61131-3 structured text function block for a Modbus TCP server that handles client connections, processes standard Modbus requests (read/write coils/registers), and manages communication errors with proper timeout handling.

### Prompt:
**Profibus DP Diagnostics Using 61131-3 Structured Text:**

Develop a self-contained 61131-3 structured text function block to read diagnostic data from a Profibus DP slave device. The function block should handle communication with the Profibus DP slave and retrieve diagnostic information such as device status, error codes, and communication health. Provide an explanation of the key steps in processing the diagnostic data, including request initiation, data retrieval, and error handling mechanisms.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Create a self-contained IEC 61131-3 Structured Text (ST) function block to retrieve diagnostic data from a Profibus DP slave device.

⸻

🟩 A (Action) – How to Do It

Design the function block to initiate a diagnostic request upon receiving a rising edge on an Execute input. Use the provided SlaveAddress to communicate with the target device and retrieve diagnostic data such as device status, error codes, and communication health. Implement timeout monitoring via a Timeout input and handle errors by setting output flags like Error and ErrorID. Parse the diagnostic response and expose structured outputs for use in control or monitoring logic.

Include the following interface:

Inputs:
	•	Execute (BOOL)
	•	SlaveAddress (BYTE)
	•	Timeout (TIME)

Outputs:
	•	Done (BOOL)
	•	Busy (BOOL)
	•	Error (BOOL)
	•	ErrorID (DWORD)
	•	Optional: parsed diagnostic fields (e.g., DeviceStatus, CommState)

⸻

🟦 G (Goal) – What You Want to Achieve

Enable real-time, programmatic access to Profibus DP diagnostic data from within a PLC environment. The function block should support proactive fault detection, streamline maintenance response, and improve overall communication reliability between the controller and field devices.

### Generated Code:
Create an IEC 61131-3 structured text function block for a Modbus TCP server that handles client connections, processes standard Modbus requests (read/write coils/registers), and manages communication errors with proper timeout handling.
**Profibus DP Diagnostics Using 61131-3 Structured Text:**

Develop a self-contained 61131-3 structured text function block to read diagnostic data from a Profibus DP slave device. The function block should handle communication with the Profibus DP slave and retrieve diagnostic information such as device status, error codes, and communication health. Provide an explanation of the key steps in processing the diagnostic data, including request initiation, data retrieval, and error handling mechanisms.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Create a self-contained IEC 61131-3 Structured Text (ST) function block to retrieve diagnostic data from a Profibus DP slave device.

⸻

🟩 A (Action) – How to Do It

Design the function block to initiate a diagnostic request upon receiving a rising edge on an Execute input. Use the provided SlaveAddress to communicate with the target device and retrieve diagnostic data such as device status, error codes, and communication health. Implement timeout monitoring via a Timeout input and handle errors by setting output flags like Error and ErrorID. Parse the diagnostic response and expose structured outputs for use in control or monitoring logic.

Include the following interface:

Inputs:
	•	Execute (BOOL)
	•	SlaveAddress (BYTE)
	•	Timeout (TIME)

Outputs:
	•	Done (BOOL)
	•	Busy (BOOL)
	•	Error (BOOL)
	•	ErrorID (DWORD)
	•	Optional: parsed diagnostic fields (e.g., DeviceStatus, CommState)

⸻

🟦 G (Goal) – What You Want to Achieve

Enable real-time, programmatic access to Profibus DP diagnostic data from within a PLC environment. The function block should support proactive fault detection, streamline maintenance response, and improve overall communication reliability between the controller and field devices.

**Modbus TCP Server with Timeout Handling:**

🟥 T (Task) – What You Need to Do

Create an IEC 61131-3 ST function block for a Modbus TCP server that handles client connections, processes standard Modbus requests (read/write coils/registers), and manages communication errors with proper timeout handling.

⸻

🟩 A (Action) – How to Do It

Design the function block to listen for incoming Modbus TCP requests on a specified IP address and port. Implement a connection manager to handle multiple clients and maintain a list of active connections. Use a timer to monitor the duration of each connection and manage timeouts accordingly.

Include the following interface:

Inputs:
	•	IPAddress (STRING)
	•	Port (WORD)
	•	Timeout (TIME)

Outputs:
	•	Done (BOOL)
	•	Busy (BOOL)
	•	Error (BOOL)
	•	ErrorID (DWORD)
	•	Optional: parsed Modbus request fields (e.g., FunctionCode, Address, Quantity)

⸻

🟦 G (Goal) – What You Want to Achieve

Enable real-time, programmatic communication with Modbus TCP clients from within a PLC environment. The function block should support efficient handling of multiple clients, manage communication errors, and ensure proper timeout handling to maintain system reliability and responsiveness.

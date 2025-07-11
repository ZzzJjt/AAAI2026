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
FUNCTION_BLOCK ModbusTCPServer
VAR_INPUT
    Execute : BOOL; // Trigger connection request
    Timeout : TIME; // Timeout for client connection
END_VAR

VAR_OUTPUT
    Busy : BOOL; // TRUE while processing client requests
    Done : BOOL; // TRUE when all requests are complete
    Error : BOOL; // TRUE if error occurs
    ErrorID : DWORD; // Error code (e.g., 1001 = Invalid Address)
    ClientID : DWORD; // Client ID for logging
    ClientAddress : STRING[16]; // Client IP address
    ClientPort : DWORD; // Client port number
    ClientConnected : BOOL; // TRUE if client is connected
    ClientData : ARRAY[1..100] OF DWORD; // Client data buffer
    ClientDataSize : DWORD; // Client data size
    ClientDataValid : BOOL; // TRUE if data is valid
    ClientDataError : BOOL; // TRUE if data error occurred
    ClientDataErrorID : DWORD; // Error code (e.g., 1002 = Invalid Data)
    ClientDataTimestamp : TIME; // Timestamp of last data received
END_VAR

VAR
    ClientID_Map : ARRAY[1..100] OF DWORD; // Client ID to connection mapping
    ClientAddress_Map : ARRAY[1..100] OF STRING[16]; // Client IP to connection mapping
    ClientPort_Map : ARRAY[1..100] OF DWORD; // Client port to connection mapping
    ClientConnected_Map : ARRAY[1..100] OF BOOL; // Client connection status mapping
    ClientData_Map : ARRAY[1..100] OF ARRAY[1..100] OF DWORD; // Client data buffer mapping
    ClientDataSize_Map : ARRAY[1..100] OF DWORD; // Client data size mapping
    ClientDataValid_Map : ARRAY[1..100] OF BOOL; // Client data validity mapping
    ClientDataError_Map : ARRAY[1..100] OF BOOL; // Client data error mapping
    ClientDataErrorID_Map : ARRAY[1..100] OF DWORD; // Client data error ID mapping
    ClientDataTimestamp_Map : ARRAY[1..100] OF TIME; // Client data timestamp mapping

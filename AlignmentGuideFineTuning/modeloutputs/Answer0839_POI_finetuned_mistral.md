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
(* IEC 61131-3 Structured Text Function Block for Modbus TCP Server *)
(* Handles up to 10 simultaneous client connections *)
(* Implements Modbus function code support for reading/writing coils/registers *)
(* Includes error handling, timeout management, and connection cleanup *)

FUNCTION_BLOCK ModbusTCPServer
VAR_INPUT
    Enable : BOOL;                  (* TRUE to enable server *)
    Port : WORD;                    (* Modbus TCP port number *)
    MaxClients : BYTE;              (* Maximum number of clients *)
    Timeout : TIME;                 (* Connection timeout *)
END_VAR

VAR_OUTPUT
    Active : BOOL;                  (* TRUE if server is active *)
    Busy : BOOL;                    (* TRUE during processing *)
    Error : BOOL;                   (* TRUE if error occurs *)
    ErrorID : DWORD;                (* Error code *)
    ClientConnections : ARRAY[0..9] OF BOOL; (* Client connection states *)
    CoilRead : ARRAY[0..999] OF BOOL; (* Coil read buffer *)
    CoilWrite : ARRAY[0..999] OF BOOL; (* Coil write buffer *)
    RegisterRead : ARRAY[0..999] OF DWORD; (* Register read buffer *)
    RegisterWrite : ARRAY[0..999] OF DWORD; (* Register write buffer *)
END_VAR

VAR
    ClientSocket : ARRAY[0..9] OF TcpSocket; (* Array of client sockets *)
    ClientIndex : BYTE;              (* Next available client index *)
    ClientData : ARRAY[0..9] OF STRING[256]; (* Client request data *)
    ClientDataLength : ARRAY[0..9] OF WORD; (* Length of client request data *)
    ClientResponse : ARRAY[0..9] OF STRING[256]; (* Response to client *)
    ClientResponseLength : ARRAY[0..9] OF WORD; (* Length of response *)
    RequestType : ARRAY[0..9] OF BYTE; (* Modbus function code *)
    RequestData : ARRAY[0..9] OF STRING[25

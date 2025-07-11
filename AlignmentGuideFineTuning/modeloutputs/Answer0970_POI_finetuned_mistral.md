### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text timer function block with configurable duration, start/stop controls, and timeout outputs for PLC-based automation tasks.  

*(Focus: Modular timer logic for delays/sequencing, edge-triggered operation, and scan-cycle safety.)*

### Prompt:
**Timer:**
Implement a self-contained function block in IEC 61131-3 structured text to create a timer. Include configurable time duration, start/stop controls, and timeout handling.


**T-A-G:**

🟥 T (Task)

Implement a self-contained timer function block in IEC 61131-3 Structured Text for use in PLC-based control systems.

⸻

🟩 A (Action)
	•	Define the timer with the following inputs:
	•	Start : BOOL — triggers the timer
	•	Stop : BOOL — resets or halts the timer
	•	PresetTime : TIME — sets the duration to time
	•	Create internal logic to:
	•	Detect the rising edge of the Start input
	•	Capture and update elapsed time using system clock functions
	•	Stop the timer if Stop = TRUE
	•	Provide outputs such as:
	•	Running : BOOL — indicates the timer is active
	•	Done : BOOL — becomes TRUE when the preset time is reached
	•	Optionally, RemainingTime : TIME — time left before timeout
	•	Ensure the function block is modular, edge-triggered, and safe for repeated use across scan cycles

⸻

🟦 G (Goal)

Deliver a flexible, reusable timer block that can be integrated into various automation routines for delay control, sequencing, or timeout handling. The timer should be easy to configure, scan-cycle safe, and support both momentary and continuous triggering logic.

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text timer function block with configurable duration, start/stop controls, and timeout outputs for PLC-based automation tasks.  

*(Focus: Modular timer logic for delays/sequencing, edge-triggered operation, and scan-cycle safety.)*
**Timer:**
Implement a self-contained function block in IEC 61131-3 structured text to create a timer. Include configurable time duration, start/stop controls, and timeout handling.


**T-A-G:**

🟥 T (Task)

Implement a self-contained timer function block in IEC 61131-3 Structured Text for use in PLC-based control systems.

⸻

🟩 A (Action)
	•	Define the timer with the following inputs:
	•	Start : BOOL — triggers the timer
	•	Stop : BOOL — resets or halts the timer
	•	PresetTime : TIME — sets the duration to time
	•	Create internal logic to:
	•	Detect the rising edge of the Start input
	•	Capture and update elapsed time using system clock functions
	•	Stop the timer if Stop = TRUE
	•	Provide outputs such as:
	•	Running : BOOL — indicates the timer is active
	•	Done : BOOL — becomes TRUE when the preset time is reached
	•	Optionally, RemainingTime : TIME — time left before timeout
	•	Ensure the function block is modular, edge-triggered, and safe for repeated use across scan cycles

⸻

🟦 G (Goal)

Deliver a flexible, reusable timer block that can be integrated into various automation routines for delay control, sequencing, or timeout handling. The timer should be easy to configure, scan-cycle safe, and support both momentary and continuous triggering logic.
(* IEC 61131-3 Structured Text Function Block for a Digital Multimeter *)
(* Measures voltage, current, and resistance with configurable ranges *)
(* Uses analog input channels and digital logic for safe, accurate readings *)
(* Conforms to industrial automation standards for PLC integration *)

FUNCTION_BLOCK DigitalMultimeter
VAR_INPUT
    Enable : BOOL;                  (* TRUE to start measurement *)
    Channel : BYTE;                 (* 1: Voltage, 2: Current, 3: Resistance *)
    VoltageRange : BYTE;            (* 1: 0-10V, 2: 0-20V, 3: 0-100V *)
    CurrentRange : BYTE;            (* 1: 0-200mA, 2: 0-500mA, 3: 0-2A *)
    ResistanceRange : BYTE;         (* 1: 0-200Ω, 2: 0-500Ω, 3: 0-2kΩ *)
    Trigger : BOOL;                 (* Rising edge to start measurement *)
END_VAR

VAR_OUTPUT
    Voltage : REAL;                 (* Measured voltage in volts *)
    Current : REAL;                 (* Measured current in amps *)
    Resistance : REAL;              (* Measured resistance in ohms *)
    Done : BOOL;                    (* TRUE when measurement is complete *)
    Error : BOOL;                   (* TRUE if invalid input or range exceeded *)
    ValidData : BOOL;               (* TRUE if measurement is valid *)
    Fault : BOOL;                   (* TRUE if fault condition detected *)
    FaultCode : DWORD;              (* 0: No fault, 1: Invalid input, 2: Range exceeded *)
END_VAR

(* Internal Variables *)
VAR
    LastTrigger : BOOL;             (* Tracks rising edge of Trigger *)
    MeasurementRunning : BOOL;      (* TRUE while measurement is active *)
    Timer : TON;                    (* Timer for measurement duration *)
    MeasurementStartTime : TIME;    (* Time when measurement

### Intent:
**Intent Summary:**  
Create a reusable, configurable PID controller function block in IEC 61131-3 Structured Text with tunable gains, anti-windup, output clamping, and error handling for precise industrial process control (e.g., temperature, pressure) on PLCs.  

*(Key features: modularity, safety, diagnostics, and scan-cycle compatibility.)*

### Prompt:
**PID Controller:**
Implement a self-contained function block in IEC 61131-3 structured text to create a PID controller. Include configurable parameters for proportional, integral, and derivative gains, with error handling and tuning capability.


**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In industrial automation systems, maintaining precise control over temperature, pressure, flow, or position is critical. Without a reliable and tunable PID controller, systems may experience instability, overshoot, or slow response. Many basic PID implementations lack configurable gains, anti-windup measures, or proper error handling, making them unsuitable for complex or sensitive processes when deployed on a PLC using IEC 61131-3 Structured Text.

⸻

🟩 A (After) – The Desired Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text that implements a standard PID controller. The block should:
	•	Include tunable parameters for proportional (Kp), integral (Ki), and derivative (Kd) gains
	•	Support error calculation and handle input setpoint and process variable
	•	Include safeguards such as integral windup prevention, output clamping, and reset logic
	•	Be modular, scan-cycle-safe, and easily integrable into control loops
	•	Provide intuitive input/output structure with documentation for users and maintainers

⸻

🟧 B (Bridge) – How to Get There
	1.	Define inputs for:
	•	Setpoint : REAL
	•	ProcessVariable : REAL
	•	Kp, Ki, Kd : REAL
	•	Enable, Reset : BOOL
	•	MinOutput, MaxOutput : REAL
	2.	Calculate:
	•	Error = Setpoint – ProcessVariable
	•	Integral term with anti-windup (limit or back-calculate)
	•	Derivative term using difference in process variable
	3.	Output:
	•	ControlOutput : REAL
	•	Optionally, Error, IntegralTerm, and DerivativeTerm for monitoring
	4.	Add structured comments and logic separation (e.g., IF Enable THEN ...)
	5.	Ensure the block behaves predictably under all input conditions

### Generated Code:
**Intent Summary:**  
Create a reusable, configurable PID controller function block in IEC 61131-3 Structured Text with tunable gains, anti-windup, output clamping, and error handling for precise industrial process control (e.g., temperature, pressure) on PLCs.  

*(Key features: modularity, safety, diagnostics, and scan-cycle compatibility.)*
**PID Controller:**
Implement a self-contained function block in IEC 61131-3 structured text to create a PID controller. Include configurable parameters for proportional, integral, and derivative gains, with error handling and tuning capability.


**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In industrial automation systems, maintaining precise control over temperature, pressure, flow, or position is critical. Without a reliable and tunable PID controller, systems may experience instability, overshoot, or slow response. Many basic PID implementations lack configurable gains, anti-windup measures, or proper error handling, making them unsuitable for complex or sensitive processes when deployed on a PLC using IEC 61131-3 Structured Text.

⸻

🟩 A (After) – The Desired Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text that implements a standard PID controller. The block should:
	•	Include tunable parameters for proportional (Kp), integral (Ki), and derivative (Kd) gains
	•	Support error calculation and handle input setpoint and process variable
	•	Include safeguards such as integral windup prevention, output clamping, and reset logic
	•	Be modular, scan-cycle-safe, and easily integrable into control loops
	•	Provide intuitive input/output structure with documentation for users and maintainers

⸻

🟧 B (Bridge) – How to Get There
	1.	Define inputs for:
	•	Setpoint : REAL
	•	ProcessVariable : REAL
	•	Kp, Ki, Kd : REAL
	•	Enable, Reset : BOOL
	•	MinOutput, MaxOutput : REAL
	2.	Calculate:
	•	Error = Setpoint – ProcessVariable
	•	Integral term with anti-windup (limit or back-calculate)
	•	Derivative term using difference in process variable
	3.	Output:
	•	ControlOutput : REAL
	•	Optionally, Error, IntegralTerm, and DerivativeTerm for monitoring
	4.	Add structured comments and logic separation (e.g., IF Enable THEN ...)
	5.	Ensure the block behaves predictably under all input conditions and is safe for real-time execution
(* IEC 61131-3 Structured Text: PID Controller Function Block *)
(* Purpose: Implements a PID controller with configurable gains and error handling *)

FUNCTION_BLOCK PIDController
VAR_INPUT
    Enable : BOOL;                  (* TRUE to enable control *)
    Reset : BOOL;                   (* TRUE to reset internal states *)
    Kp : REAL;                      (* Proportional gain *)
    Ki : REAL;                      (* Integral gain *)
    Kd : REAL;                      (* Derivative gain *)
    Setpoint : REAL;                (* Desired process setpoint *)
    ProcessVariable : REAL;         (* Measured process variable *)
    MinOutput : REAL;               (* Minimum output limit *)
    MaxOutput : REAL;               (* Maximum output limit *)
END_VAR

VAR_OUTPUT
    ControlOutput : REAL;           (* Control output signal *)
    Error : REAL;                   (* Current error *)
    IntegralTerm : REAL;            (* Accumulated integral term *)
    DerivativeTerm : REAL;          (* Derivative term *)
    TuningComplete : BOOL;          (* TRUE when tuning is complete *)
END_VAR

VAR
    PrevError : REAL;               (* Previous error for derivative *)
    Integral : REAL;                (* Accumulated integral *)
    LastReset : BOOL;               (* Flag to track last reset *)
    TuningInProgress : BOOL;        (* Flag to indicate tuning is in progress *)
END_VAR

(* Initialize outputs *)
ControlOutput := 0.0;
Error := 0.0;
IntegralTerm := 0.0;
DerivativeTerm := 0.0;
TuningComplete := FALSE;

(* Main logic *)
IF Enable AND NOT Reset THEN
    (* Reset on rising edge of Reset *)
    IF NOT LastReset THEN
        Integral := 0.0;
        TuningInProgress := FALSE;
        TuningComplete := FALSE;
    END_IF;

    (* Update previous error *)
    PrevError := Error;

    (* Calculate current error *)

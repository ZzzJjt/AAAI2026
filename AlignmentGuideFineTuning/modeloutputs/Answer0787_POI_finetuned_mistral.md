### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block for a PID controller with configurable gains, anti-windup protection, output clamping, and real-time execution, suitable for industrial automation.  

*(Focus: Modular PID control with safety features and tuning capability.)*

### Prompt:
**PID Controller:**
Implement a self-contained function block in IEC 61131-3 structured text to create a PID controller. Include configurable parameters for proportional, integral, and derivative gains, with error handling and tuning capability.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a control systems engineer designing a tunable PID controller in IEC 61131-3 Structured Text for real-time industrial automation.

⸻

🟩 T (Task) – Define the Objective

Develop a self-contained function block that implements a PID control algorithm. The block must:
	•	Accept configurable gain inputs:
	•	Kp (Proportional), Ki (Integral), Kd (Derivative)
	•	Calculate the control error based on Setpoint and ProcessVariable
	•	Include:
	•	Integral windup protection (via clamping or conditional integration)
	•	Derivative calculation using the rate of change in the process variable
	•	Reset functionality to reinitialize internal states
	•	Support output clamping with MinOutput and MaxOutput
	•	Execute safely within one scan cycle
	•	Be documented and modular for easy reuse

⸻

🟧 F (Format) – Specify the Output Format

Provide a complete IEC 61131-3 Structured Text function block that includes:
	•	Inputs:
	•	Setpoint : REAL, ProcessVariable : REAL
	•	Kp, Ki, Kd : REAL
	•	MinOutput, MaxOutput : REAL
	•	Enable, Reset : BOOL
	•	Outputs:
	•	ControlOutput : REAL
	•	Optionally: Error, IntegralTerm, DerivativeTerm for monitoring
	•	Logic blocks:
	•	Initialization section
	•	PID calculation section (error, P/I/D terms)
	•	Output limiting and anti-windup handling
	•	State updates for the next scan

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block for a PID controller with configurable gains, anti-windup protection, output clamping, and real-time execution, suitable for industrial automation.  

*(Focus: Modular PID control with safety features and tuning capability.)*
**PID Controller:**
Implement a self-contained function block in IEC 61131-3 structured text to create a PID controller. Include configurable parameters for proportional, integral, and derivative gains, with error handling and tuning capability.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a control systems engineer designing a tunable PID controller in IEC 61131-3 Structured Text for real-time industrial automation.

⸻

🟩 T (Task) – Define the Objective

Develop a self-contained function block that implements a PID control algorithm. The block must:
	•	Accept configurable gain inputs:
	•	Kp (Proportional), Ki (Integral), Kd (Derivative)
	•	Calculate the control error based on Setpoint and ProcessVariable
	•	Include:
	•	Integral windup protection (via clamping or conditional integration)
	•	Derivative calculation using the rate of change in the process variable
	•	Reset functionality to reinitialize internal states
	•	Support output clamping with MinOutput and MaxOutput
	•	Execute safely within one scan cycle
	•	Be documented and modular for easy reuse

⸻

🟧 F (Format) – Specify the Output Format

Provide a complete IEC 61131-3 Structured Text function block that includes:
	•	Inputs:
	•	Setpoint : REAL, ProcessVariable : REAL
	•	Kp, Ki, Kd : REAL
	•	MinOutput, MaxOutput : REAL
	•	Enable, Reset : BOOL
	•	Outputs:
	•	ControlOutput : REAL
	•	Optionally: Error, IntegralTerm, DerivativeTerm for monitoring
	•	Logic blocks:
	•	Initialization section
	•	PID calculation section (error, P/I/D terms)
	•	Output limiting and anti-windup handling
	•	State updates for the next scan cycle
	•	Inline comments explaining each section and tuning considerations
(* IEC 61131-3 Structured Text: PID Controller Function Block *)
(* Purpose: Implements PID control with configurable gains, error handling, and output clamping *)

FUNCTION_BLOCK PIDController
VAR_INPUT
    Enable : BOOL;                  (* TRUE to enable control *)
    Reset : BOOL;                   (* TRUE to reset internal states *)
    Setpoint : REAL;                (* Desired process setpoint *)
    ProcessVariable : REAL;         (* Measured process variable *)
    Kp : REAL;                      (* Proportional gain *)
    Ki : REAL;                      (* Integral gain *)
    Kd : REAL;                      (* Derivative gain *)
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
    PrevProcessVariable : REAL;      (* Previous process variable for derivative *)
    Tuning : BOOL;                   (* TRUE to tune gains *)
    TuningCompleteFlag : BOOL;       (* Flag to indicate tuning completion *)
END_VAR

(* Initialize outputs *)
ControlOutput := 0.0;
Error := 0.0;
IntegralTerm := 0.0;
DerivativeTerm := 0.0;
TuningCompleteFlag := FALSE;

(* Main logic *)
IF Enable AND NOT Reset THEN
    (* Calculate error *)
    Error := Setpoint - ProcessVariable;

    (* Integral term *)
    IF NOT Tuning THEN
        IntegralTerm := IntegralTerm + Ki * Error * SCAN_TIME;
    END_IF;

    (* Derivative term *)
    DerivativeTerm := (ProcessVariable - Prev

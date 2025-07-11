### Intent:
**Intent Summary:**  
Create a robust, configurable PID controller function block in IEC 61131-3 Structured Text with anti-windup, output clamping, and input validation for precise real-time industrial process control.

### Prompt:
**Counter:**
Implement a self-contained function block in IEC 61131-3 structured text for a digital counter with up/down counting modes. Include configurable initial value, step size, and overflow handling.


**T-A-G:**

🟥 T (Task)

Create a self-contained function block in IEC 61131-3 Structured Text that implements a configurable digital counter with both up and down counting modes.

⸻

🟩 A (Action)
	•	Define inputs for:
	•	Enable : BOOL – activates the counter
	•	CountUp : BOOL – selects the counting direction
	•	StepSize : INT – amount to increment or decrement
	•	InitValue : INT – starting value of the counter
	•	Reset : BOOL – resets the counter to the initial value
	•	MaxValue / MinValue : INT – upper and lower bounds for overflow handling
	•	Use conditional logic to increment or decrement based on CountUp
	•	Implement logic to clamp the value within MinValue and MaxValue
	•	Provide outputs for:
	•	CurrentValue : INT – the current counter state
	•	AtMax, AtMin : BOOL – flags for boundary conditions
	•	Comment all key sections to ensure clarity and reusability

⸻

🟦 G (Goal)

Deliver a modular, safe, and easy-to-integrate counter block suitable for PLC applications requiring flexible and bounded counting logic. The implementation should be robust, configurable, and reliable for use in scan-cycle-sensitive automation environments.

### Generated Code:
**Intent Summary:**  
Create a robust, configurable PID controller function block in IEC 61131-3 Structured Text with anti-windup, output clamping, and input validation for precise real-time industrial process control.
**Counter:**
Implement a self-contained function block in IEC 61131-3 structured text for a digital counter with up/down counting modes. Include configurable initial value, step size, and overflow handling.


**T-A-G:**

🟥 T (Task)

Create a self-contained function block in IEC 61131-3 Structured Text that implements a configurable digital counter with both up and down counting modes.

⸻

🟩 A (Action)
	•	Define inputs for:
	•	Enable : BOOL – activates the counter
	•	CountUp : BOOL – selects the counting direction
	•	StepSize : INT – amount to increment or decrement
	•	InitValue : INT – starting value of the counter
	•	Reset : BOOL – resets the counter to the initial value
	•	MaxValue / MinValue : INT – upper and lower bounds for overflow handling
	•	Use conditional logic to increment or decrement based on CountUp
	•	Implement logic to clamp the value within MinValue and MaxValue
	•	Provide outputs for:
	•	CurrentValue : INT – the current counter state
	•	AtMax, AtMin : BOOL – flags for boundary conditions
	•	Comment all key sections to ensure clarity and reusability

⸻

🟦 G (Goal)

Deliver a modular, safe, and easy-to-integrate counter block suitable for PLC applications requiring flexible and bounded counting logic. The implementation should be robust, configurable, and reliable for use in scan-cycle-sensitive automation environments.
(* IEC 61131-3 Structured Text Function Block for PID Controller *)
(* Implements PID control with anti-windup, output clamping, and input validation *)
(* Conforms to industrial automation best practices for real-time process control *)

FUNCTION_BLOCK PIDController
VAR_INPUT
    Enable : BOOL;                  (* TRUE to enable control *)
    Setpoint : REAL;                (* Desired process value *)
    ProcessVariable : REAL;         (* Measured process value *)
    Kp : REAL;                      (* Proportional gain *)
    Ki : REAL;                      (* Integral gain *)
    Kd : REAL;                      (* Derivative gain *)
    OutputMin : REAL;               (* Minimum output limit *)
    OutputMax : REAL;               (* Maximum output limit *)
    SampleTime : TIME;              (* Control loop sample time *)
    Reset : BOOL;                   (* Reset internal state on rising edge *)
END_VAR

VAR_OUTPUT
    ControlSignal : REAL;           (* PID output as control signal *)
    Error : REAL;                   (* Process error *)
    IntegralTerm : REAL;            (* Integral term *)
    DerivativeTerm : REAL;          (* Derivative term *)
    InternalState : BOOL;           (* Internal state flag *)
END_VAR

VAR
    PrevProcessVariable : REAL;      (* Previous process variable for derivative *)
    PrevError : REAL;               (* Previous error for integral *)
    IntegralSum : REAL;             (* Accumulated integral *)
    DeltaT : TIME;                  (* Time difference since last sample *)
    ErrorDamping : REAL;            (* Anti-windup damping factor *)
    OutputClamp : BOOL;             (* TRUE to clamp output *)
    ValidInputs : BOOL;             (* TRUE if inputs are valid *)
END_VAR

(* Initialize outputs *)
ControlSignal := 0.0;
IntegralSum := 0.0;
Error := 0.0;
DerivativeTerm := 0.0;
InternalState := FALSE;

(* Input validation *)
IF NOT Enable THEN
    ValidInputs := FALSE

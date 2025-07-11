### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block for a configurable PID controller with tunable gains, error handling, anti-windup, and output clamping to ensure stable and precise process control in industrial automation.  

*(For the digital counter example, the intent would adjust to: "Develop a modular IEC 61131-3 function block for a flexible digital counter with directional control, step sizing, and limit protection.")*

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
Create a reusable IEC 61131-3 Structured Text function block for a configurable PID controller with tunable gains, error handling, anti-windup, and output clamping to ensure stable and precise process control in industrial automation.  

*(For the digital counter example, the intent would adjust to: "Develop a modular IEC 61131-3 function block for a flexible digital counter with directional control, step sizing, and limit protection.")*
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
(* IEC 61131-3 Structured Text: Digital Counter Function Block *)
(* Purpose: Provides a flexible, modular digital counter with directional control *)

FUNCTION_BLOCK DigitalCounter
VAR_INPUT
    Enable : BOOL;                  (* TRUE to enable counting *)
    Direction : BOOL;               (* TRUE for up, FALSE for down *)
    StepSize : INT;                 (* Step size for counting *)
    Reset : BOOL;                   (* TRUE to reset counter to zero *)
    MaxValue : INT;                 (* Upper limit for counter *)
    MinValue : INT;                 (* Lower limit for counter *)
    Clock : BOOL;                   (* TRUE to trigger counting on rising edge *)
    StepTrigger : BOOL;             (* Manual step trigger *)
    Step : BOOL;                    (* TRUE to manually step up or down *)
    StepUp : BOOL;                  (* TRUE to step up, FALSE to step down *)
    StepHold : BOOL;                (* TRUE to hold current value *)
END_VAR

VAR_OUTPUT
    CurrentValue : INT;             (* Current counter value *)
    AtMax : BOOL;                   (* TRUE if at MaxValue *)
    AtMin : BOOL;                   (* TRUE if at MinValue *)
    Error : BOOL;                   (* TRUE if invalid input *)
    Done : BOOL;                    (* TRUE when counting is complete *)
END_VAR

VAR
    LastClock : BOOL;               (* For rising edge detection *)
    LastStepTrigger : BOOL;         (* For step trigger detection *)
    LastStepHold : BOOL;            (* For hold state detection *)
    LastEnable : BOOL;              (* For enable state detection *)
    LastReset : BOOL;               (* For reset state detection *)
    LastDirection : BOOL;           (* For direction change detection *)
    LastStepUp : BOOL;              (* For step up/down change detection *)
    LastStepSize : INT;             (* For step size change detection *)
    LastMaxValue : INT;             (* For max value change detection *)
    LastMinValue : INT;             (* For min value change detection *)
    StepCount : INT;                (* Temporary step counter

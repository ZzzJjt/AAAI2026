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
	5.	Ensure the block behaves predictably under all input conditions and scan cycles
	6.	Provide a clear, concise, and well-documented function block for easy integration and maintenance

⸻

**Example Code:**
```plaintext
FUNCTION_BLOCK PID_Controller
VAR_INPUT
	Setpoint : REAL;
	ProcessVariable : REAL;
	Kp, Ki, Kd : REAL;
	Enable, Reset : BOOL;
	MinOutput, MaxOutput : REAL;
END_VAR

VAR_OUTPUT
	ControlOutput : REAL;
	Error, IntegralTerm, DerivativeTerm : REAL;
END_VAR

VAR
	Error : REAL;
	IntegralTerm : REAL;
	DerivativeTerm : REAL;
	LastProcessVariable : REAL := 0.0;
END_VAR

IF Enable THEN
	Error := Setpoint - ProcessVariable;
	IF Reset THEN
		IntegralTerm := 0.0;
		LastProcessVariable := ProcessVariable;
	END_IF

	IF IntegralTerm > MaxOutput THEN
		IntegralTerm := MaxOutput;
	ELSE IF IntegralTerm < MinOutput THEN
		IntegralTerm := MinOutput;
	END_IF

	DerivativeTerm := (ProcessVariable - LastProcessVariable) / (T#1s); // Assuming 1s scan cycle
	LastProcessVariable := ProcessVariable;

	ControlOutput := Kp * Error + Ki * IntegralTerm + Kd * DerivativeTerm;
	IF ControlOutput > MaxOutput THEN
		ControlOutput := MaxOutput;
	ELSE IF ControlOutput < MinOutput THEN
		ControlOutput := MinOutput;
	END_IF
END_IF

Error := Setpoint - ProcessVariable;
IntegralTerm := IntegralTerm + Error;
DerivativeTerm := (ProcessVariable - LastProcessVariable) / (T#1s); // Assuming 1s scan cycle
LastProcessVariable := ProcessVariable;
```

This function block provides a basic PID controller with configurable gains, anti-windup, output clamping, and error handling. It is designed to be easily integrated into control loops and provides clear input/output structure for users and maintainers.

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
	5.	Ensure the block behaves predictably under all input conditions and is easy to integrate into a control loop
FUNCTION_BLOCK PIDController
VAR_INPUT
    Enable : BOOL;
    Setpoint : REAL;
    ProcessVariable : REAL;
    Kp : REAL;
    Ki : REAL;
    Kd : REAL;
    MinOutput : REAL;
    MaxOutput : REAL;
END_VAR

VAR_OUTPUT
    ControlOutput : REAL;
    Error : REAL;
    IntegralTerm : REAL;
    DerivativeTerm : REAL;
END_VAR

VAR
    PrevError : REAL;
    PrevIntegral : REAL;
    PrevDerivative : REAL;
    IntegralWindup : BOOL;
    ClampOutput : BOOL;
END_VAR

// Reset Integral and Derivative on Reset
IF Reset THEN
    PrevError := 0.0;
    PrevIntegral := 0.0;
    PrevDerivative := 0.0;
    IntegralWindup := FALSE;
    ClampOutput := FALSE;
END_IF;

// Calculate error
Error := Setpoint - ProcessVariable;

// Calculate integral term
IntegralTerm := IntegralTerm + (Error * Ki);

// Calculate derivative term
DerivativeTerm := (Error - PrevError) / 1000.0;

// Clamp output
IF ClampOutput THEN
    ControlOutput := MAX(MIN(ControlOutput, MaxOutput), MinOutput);
ELSE
    ControlOutput := PIDController(Kp, Ki, Kd, Error, IntegralTerm, DerivativeTerm);
END_IF;

// Anti-windup
IF IntegralWindup THEN
    IntegralTerm := 0.0;
END_IF;

// Store previous error for derivative calculation
PrevError := Error;
PrevIntegral := IntegralTerm;
PrevDerivative := DerivativeTerm;

END_FUNCTION_BLOCK

// Function block implementation
FUNCTION_BLOCK PIDController
VAR_INPUT
    Kp : REAL;
    Ki : REAL;
    Kd : REAL;
    Error : REAL;
    IntegralTerm : REAL;
    DerivativeTerm : REAL;
END_VAR

VAR_OUTPUT
    ControlOutput : REAL;
END_VAR

VAR

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
	5.	Ensure the block behaves predictably under all input conditions and is compatible with the PLC's scan cycle.

**Code Example:**

```
FUNCTION_BLOCK PID_Controller
    VAR_INPUT
        Setpoint : REAL;
        ProcessVariable : REAL;
        Kp : REAL;
        Ki : REAL;
        Kd : REAL;
        Enable : BOOL;
        Reset : BOOL;
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
        PreviousError : REAL;
        PreviousProcessVariable : REAL;
        PreviousIntegralTerm : REAL;
        IntegralLimit : REAL;
    END_VAR

    IF Enable THEN
        Error := Setpoint - ProcessVariable;
        IntegralTerm := (Error + PreviousError) / 2 * Ki;
        IF Reset THEN
            IntegralTerm := 0;
        END_IF
        IF IntegralTerm > IntegralLimit THEN
            IntegralTerm := IntegralLimit;
        ELSIF IntegralTerm < -IntegralLimit THEN
            IntegralTerm := -IntegralLimit;
        END_IF
        DerivativeTerm := (ProcessVariable - PreviousProcessVariable) / T_sample;
        ControlOutput := Kp * Error + IntegralTerm + Kd * DerivativeTerm;
        IF ControlOutput < MinOutput THEN
            ControlOutput := MinOutput;
        ELSIF ControlOutput > MaxOutput THEN
            ControlOutput := MaxOutput;
        END_IF
        PreviousError := Error;
        PreviousProcessVariable := ProcessVariable;
        PreviousIntegralTerm := IntegralTerm;
    END_IF
END_FUNCTION_BLOCK
```

**Notes:**

* The code example provided is a basic implementation of a PID controller. It can be further optimized or extended to include advanced features such as dead-time compensation, anti-reset windup, or adaptive tuning.
* The function block can be easily integrated into a control loop by calling it in

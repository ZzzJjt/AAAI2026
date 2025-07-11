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
	•	Comments and documentation for clarity

⸻

🟦 E (Example) – Provide an Example

```
FUNCTION_BLOCK PID_Controller
    VAR
        Error, IntegralTerm, DerivativeTerm : REAL;
        PreviousError, PreviousIntegralTerm : REAL;
        PreviousProcessVariable : REAL;
    END_VAR

    (* Inputs *)
    Setpoint : REAL;
    ProcessVariable : REAL;
    Kp, Ki, Kd : REAL;
    MinOutput, MaxOutput : REAL;
    Enable, Reset : BOOL;

    (* Outputs *)
    ControlOutput : REAL;

    (* Initialization *)
    IF Reset THEN
        PreviousError := 0.0;
        PreviousIntegralTerm := 0.0;
        PreviousProcessVariable := 0.0;
    END_IF;

    (* PID Calculation *)
    Error := Setpoint - ProcessVariable;
    IntegralTerm := PreviousIntegralTerm + Ki * Error;
    IF Enable THEN
        DerivativeTerm := (Error - PreviousError) / T_sample;
    END_IF;

    (* Anti-Windup Protection *)
    IF IntegralTerm > MaxOutput - ControlOutput THEN
        IntegralTerm := MaxOutput - ControlOutput;
    END_IF;
    IF IntegralTerm < MinOutput - ControlOutput THEN
        IntegralTerm := MinOutput - ControlOutput;
    END_IF;

    (* Output Limiting *)
    ControlOutput := MinOutput + IntegralTerm + Kp * Error + Kd * DerivativeTerm;
    IF ControlOutput > MaxOutput THEN
        ControlOutput := MaxOutput;
    END_IF;
    IF ControlOutput < MinOutput THEN
        ControlOutput := MinOutput;
    END_IF;

    (* State Updates *)
    PreviousError := Error;
    PreviousIntegralTerm := IntegralTerm;
    PreviousProcessVariable := ProcessVariable;

END_FUNCTION_BLOCK
```

⸻

🟦 S (Safety) – Consider Safety

En

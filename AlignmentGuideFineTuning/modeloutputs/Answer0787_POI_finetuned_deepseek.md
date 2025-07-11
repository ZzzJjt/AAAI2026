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
FUNCTION_BLOCK FB_PIDController
VAR_INPUT
    Enable : BOOL;
    Reset : BOOL;
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
    PrevOutput : REAL;
    Integral : REAL;
    Derivative : REAL;
    ErrorSum : REAL;
    IntegralSum : REAL;
    DerivativeSum : REAL;
    ClampOutput : BOOL;
    ClampMin : REAL;
    ClampMax : REAL;
END_VAR

METHOD Execute : REAL
BEGIN
    // Reset state
    IF Reset THEN
        PrevError := 0.0;
        PrevIntegral := 0.0;
        PrevDerivative := 0.0;
        PrevOutput := 0.0;
        Integral := 0.0;
        Derivative := 0.0;
        ErrorSum := 0.0;
        IntegralSum := 0.0;
        DerivativeSum := 0.0;
        ClampOutput := FALSE;
        ClampMin := 0.0;
        ClampMax := 100.0;
        ControlOutput := 0.0;
        RETURN;
    END_IF;

    // Calculate error
    Error := Setpoint - ProcessVariable;

    // Integral term
    IntegralSum := IntegralSum + Error * 0.1;
    Integral := IntegralSum / 10.0;

    // Derivative term
    DerivativeSum := DerivativeSum + (Error - PrevError) * 0.1;
    Derivative := DerivativeSum / 10.0;

    // PID calculation
    IF Enable THEN
        IF ClampOutput THEN
            ControlOutput := MAX(Min

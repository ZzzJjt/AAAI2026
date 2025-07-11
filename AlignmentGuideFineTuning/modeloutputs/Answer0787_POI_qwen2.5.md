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
	•	Documentation and comments for clarity

⸻

**Example Use Case:**
```plaintext
// Example usage of the PID function block
// Setpoint is 100, ProcessVariable is 80
// Kp = 1, Ki = 0.1, Kd = 0.05
// MinOutput = 0, MaxOutput = 100
// Enable = TRUE, Reset = FALSE
// Output: ControlOutput
```

**Note:**
Ensure the function block is designed for real-time execution and includes safety features such as anti-windup protection and output clamping. The code should be modular and well-documented for easy integration into larger control systems.
```plaintext
// PID Function Block in IEC 61131-3 Structured Text

// Inputs
Setpoint : REAL
ProcessVariable : REAL
Kp : REAL
Ki : REAL
Kd : REAL
MinOutput : REAL
MaxOutput : REAL
Enable : BOOL
Reset : BOOL

// Outputs
ControlOutput : REAL
Error : REAL
IntegralTerm : REAL
DerivativeTerm : REAL

// Internal Variables
ErrorPrev : REAL
Integral : REAL
Derivative : REAL
Output : REAL
OutputPrev : REAL
IntegralLimit : REAL
DerivativeLimit : REAL

// Initialization
IF Reset THEN
    ErrorPrev := 0.0
    Integral := 0.0
    Derivative := 0.0
    Output := 0.0
    OutputPrev := 0.0
    IntegralLimit := 0.0
    DerivativeLimit := 0.0
END_IF

// PID Calculation
Error := Setpoint - ProcessVariable
Integral := Integral + Error
Derivative := (ProcessVariable - ProcessVariablePrev) / (Timestep / 1000.0)

// Anti-windup protection
IF Integral > IntegralLimit THEN
    Integral := IntegralLimit
END_IF
IF Integral < -IntegralLimit THEN
    Integral := -IntegralLimit
END_IF

// Derivative calculation
IF Enable THEN
    Derivative := (ProcessVariable - ProcessVariablePrev) / (Timestep / 1000.0)
ELSE
    Derivative := 0.0
END_IF

// Output calculation
Output := Kp * Error + Ki * Integral + Kd * Derivative

// Output limiting
IF Output > MaxOutput THEN

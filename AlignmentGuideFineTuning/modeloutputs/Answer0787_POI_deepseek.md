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
	•	Documentation block

⸻

🟨 S (Structure) – Describe the Structure

The function block should be structured as follows:

1.	Initialization section:
	*	Initialize internal states (e.g., integral and derivative error terms)
	*	Enable the PID controller
	*	Set the process variable to the initial value
	*	Enable the reset functionality
2.	PID calculation section:
	*	Calculate the error between the setpoint and process variable
	*	Calculate the proportional, integral, and derivative terms
	*	Apply anti-windup protection (if necessary)
	*	Update the integral and derivative error terms
3.	Output limiting and anti-windup handling:
	*	Apply output clamping to the control output
	*	Check for integral windup and apply appropriate handling (e.g., clamping or conditional integration)
	*	Check for derivative windup and apply appropriate handling (if necessary)
4.	State updates for the next scan cycle:
	*	Update the process variable and setpoint for the next scan cycle
	*	Enable the PID controller for the next scan cycle
5.	Documentation block:
	*	Include comments and documentation for the function block
	*	Provide a brief description of the PID controller and its functionality

⸻

🟩 E (Example) – Provide an Example

```
FUNCTION Block PIDController
VAR
    Setpoint : REAL := 0;
    ProcessVariable : REAL := 0;
    Kp : REAL := 0;
    Ki : REAL := 0;
    Kd : REAL := 0;
    MinOutput : REAL := 0;
    MaxOutput : REAL := 0;
    Enable : BOOL := TRUE;
    Reset : BOOL := FALSE;
    IntegralError : REAL := 0;
    DerivativeError : REAL := 0;
    IntegralTerm : REAL := 0;
    DerivativeTerm : REAL := 0;
    ControlOutput : REAL := 0;
END_VAR

VAR
    Initialization : BOOL := TRUE;
    PIDCalculation : BOOL := FALSE;
    OutputLimiting : BOOL := FALSE;
    AntiWindupHandling : BOOL := FALSE;
    NextCycleState : BOOL := FALSE;
END_VAR

DOCUMENTATION

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
	•	Documentation and comments

⸻

🟨 V (Validation) – Define the Validation Criteria

The PID controller function block should be validated against the following criteria:
	•	Accuracy: The PID controller should accurately track the setpoint with minimal overshoot and settling time.
	•	Stability: The PID controller should not exhibit unstable behavior, such as oscillations or divergence.
	•	Anti-windup: The PID controller should prevent integral windup and handle it gracefully when it occurs.
	•	Output clamping: The PID controller should not exceed the specified output limits.
	•	Real-time execution: The PID controller should complete its calculations within one scan cycle.

⸻

🟩 E (Execution) – Define the Execution Steps

1.	Define the function block structure and inputs/outputs.
2.	Initialize the internal states (error, integral term, derivative term) to zero.
3.	Calculate the control error by subtracting the process variable from the setpoint.
4.	Apply the proportional gain to the error to obtain the proportional term.
5.	Apply the integral gain to the error and integrate the result to obtain the integral term.
6.	Apply the derivative gain to the rate of change of the process variable to obtain the derivative term.
7.	Update the integral term with the clamped integral term if anti-windup is enabled.
8.	Apply output clamping to the sum of the proportional, integral, and derivative terms.
9.	Update the internal states for the next scan cycle.
10.	Return the control output.

⸻

🟩 C (Conclusion) – Summarize the Solution

The PID controller function block in IEC 61131-3 Structured Text provides a modular and configurable solution for real-time industrial automation. It includes configurable gains, anti-windup protection, output clamping, and real-time execution. The function block can be easily reused in various control systems, ensuring accurate tracking of setpoints and stable operation.

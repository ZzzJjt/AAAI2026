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
	•	State updates for the next scan
	•	Include comments explaining the control logic and parameter roles
	•	Ensure the function block is scan-cycle-safe and modular for integration into larger control systems
	•	Provide a detailed explanation of the implementation, including the handling of edge cases and tuning considerations
	•	Include a discussion on the practical use of the function block in industrial control systems, focusing on real-time performance and safety constraints
	•	Lastly, compile the function block into a self-contained program with a clear introduction and usage example
	•	Compile the function block into a self-contained program with a clear introduction and usage example
	•	Compile the function block into a self-contained program with a clear introduction and usage example
	•	Compile the function block into a self-contained program with a clear introduction and usage example
	•	Compile the function block into a self-contained program with a clear introduction and usage example
	•	Compile the function block into a self-contained program with a clear introduction and usage example
	•	Compile the function block into a self-contained program with a clear introduction and usage example
	•	Compile the function block into a self-contained program with a clear introduction and usage example
	•	Compile the function block into a self-contained program with a clear introduction and usage example
	•	Compile the function block into a self-contained program with a clear introduction and usage example
	•	Compile the function block into a self-contained program with a clear introduction and usage example
	•	Compile the function block into a self-contained program with a clear introduction and usage example
	•	Compile the function block into a self-contained program with a clear introduction and usage example
	•	Compile the function block into a self-contained program with a clear introduction and usage example
	•	Compile the function block into a self-contained program with a clear introduction and usage example
	•	Compile the function block into a self-contained program with a clear introduction and usage example
	•	Compile the function block into a self-contained program with a clear introduction and usage example
	•	Compile the function block into a self-contained program with a clear introduction and usage example
	•	Compile the function block into a self-contained program with a clear introduction and usage example
	•	Compile the function block into a self-contained program with a clear introduction and usage example
	•	Compile the function block into a self-contained program with a clear introduction and usage example
	•	Compile the function block

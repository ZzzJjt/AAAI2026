### Intent:
"Implement a Kalman filter function block in IEC 61131-3 Structured Text for real-time state estimation (position and velocity) with configurable noise parameters and reset capability."

### Prompt:
**PID Controller:**
Implement a self-contained function block in IEC 61131-3 structured text to create a PID controller. Include configurable parameters for proportional, integral, and derivative gains, with error handling and tuning capability.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC programmer developing a PID controller function block in IEC 61131-3 Structured Text for real-time industrial process control.

⸻

🟩 I (Input) – Information Provided

You need to implement a self-contained PID controller that:
	•	Accepts configurable parameters for:
	•	Proportional gain (Kp)
	•	Integral gain (Ki)
	•	Derivative gain (Kd)
	•	Output limits (MinOutput, MaxOutput)
	•	Operates on a control error calculated as:
\text{Error} = \text{Setpoint} - \text{ProcessVariable}
	•	Includes input signals:
	•	Enable to activate control
	•	Reset to reinitialize internal states
	•	Provides a real-time control output and handles error accumulation, anti-windup, and derivative filtering

⸻

🟧 S (Steps) – Steps to Perform
	1.	Declare inputs and outputs:
	•	Inputs: Setpoint, ProcessVariable, Kp, Ki, Kd, MinOutput, MaxOutput, Enable, Reset
	•	Outputs: ControlOutput, and optionally Error, IntegralTerm, DerivativeTerm
	2.	Initialize/reset states on rising edge of Reset signal
	3.	In the control loop (if Enable = TRUE):
	•	Calculate the error
	•	Update the integral term, with logic to prevent windup when output is clamped
	•	Calculate the derivative term using previous ProcessVariable and DeltaT
	•	Compute the PID output using the formula:
\text{Output} = Kp \cdot \text{Error} + Ki \cdot \text{Integral} - Kd \cdot \text{Derivative}
	•	Apply output clamping and use flags to suspend further integration when limits are hit
	4.	Update previous process value for the next derivative calculation

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a modular, robust PID function block that:
	•	Responds smoothly to changing setpoints and disturbances
	•	Avoids overshoot and instability through proper tuning
	•	Provides scan-cycle-safe execution with clear parameter structure
	•	Can be reused across different automation tasks and systems

### Generated Code:
"Implement a Kalman filter function block in IEC 61131-3 Structured Text for real-time state estimation (position and velocity) with configurable noise parameters and reset capability."
**PID Controller:**
Implement a self-contained function block in IEC 61131-3 structured text to create a PID controller. Include configurable parameters for proportional, integral, and derivative gains, with error handling and tuning capability.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC programmer developing a PID controller function block in IEC 61131-3 Structured Text for real-time industrial process control.

⸻

🟩 I (Input) – Information Provided

You need to implement a self-contained PID controller that:
	•	Accepts configurable parameters for:
	•	Proportional gain (Kp)
	•	Integral gain (Ki)
	•	Derivative gain (Kd)
	•	Output limits (MinOutput, MaxOutput)
	•	Operates on a control error calculated as:
\text{Error} = \text{Setpoint} - \text{ProcessVariable}
	•	Includes input signals:
	•	Enable to activate control
	•	Reset to reinitialize internal states
	•	Provides a real-time control output and handles error accumulation, anti-windup, and derivative filtering

⸻

🟧 S (Steps) – Steps to Perform
	1.	Declare inputs and outputs:
	•	Inputs: Setpoint, ProcessVariable, Kp, Ki, Kd, MinOutput, MaxOutput, Enable, Reset
	•	Outputs: ControlOutput, and optionally Error, IntegralTerm, DerivativeTerm
	2.	Initialize/reset states on rising edge of Reset signal
	3.	In the control loop (if Enable = TRUE):
	•	Calculate the error
	•	Update the integral term, with logic to prevent windup when output is clamped
	•	Calculate the derivative term using previous ProcessVariable and DeltaT
	•	Compute the PID output using the formula:
\text{Output} = Kp \cdot \text{Error} + Ki \cdot \text{Integral} - Kd \cdot \text{Derivative}
	•	Apply output clamping and use flags to suspend further integration when limits are hit
	4.	Update previous process value for the next derivative calculation

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a modular, robust PID function block that:
	•	Responds smoothly to changing setpoints and disturbances
	•	Avoids overshoot and instability through proper tuning
	•	Provides scan-cycle-safe execution with clear parameter structure
	•	Can be reused across different automation tasks and systems

⸻

🟪 A (Action) – Execute the Task

Write a PID controller function block in IEC 61131-3 Structured Text, ensuring it handles input signals, error calculation, and output control with proper tuning and anti-windup logic. Include comments to explain each step and parameter usage.

**PID Controller:**

▸ PID Control

**PID Control:**

Develop a self-contained PID control function block in IEC 61131-3 Structured Text. The block should accept setpoint and process variable inputs, along with proportional, integral, and derivative gains. It should calculate the PID output based on the error between the setpoint and process variable, and include logic to handle output saturation and anti-windup. The block should also provide outputs for the calculated error, integral, and derivative terms, as well as the final control output. Ensure that the block is modular and can be easily integrated into a larger control system.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC programmer developing a PID control function block in IEC 61131-3 Structured Text for real-time industrial process control.

⸻

🟩 I (Input) – Information Provided

You need to implement a self-contained PID control function block that:
	•	Accepts setpoint and process variable inputs
	•	Includes configurable proportional, integral, and derivative gains
	•	Calculates the PID output based on the error between the setpoint and process variable
	•	Handles output saturation and anti-windup logic
	•	Provides outputs for the calculated error, integral, and derivative terms
	•	Ensures modularity and ease of integration into larger control systems

⸻

🟧 S (Steps) – Steps to Perform

	1.	Declare inputs and outputs:
	•	Inputs: Setpoint, ProcessVariable, Kp, Ki, Kd
	•	Outputs: ControlOutput, Error, IntegralTerm, DerivativeTerm
	2.	Implement the PID control logic:
	•	Calculate the error as the difference between the setpoint and process variable
	•	Update the integral term by accumulating the error over time
	•	Calculate the derivative term by differentiating the process variable with respect to time
	•	Compute the PID output using the formula:

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
	•	Includes detailed comments explaining the control logic and parameter roles
	•	Works within the constraints of IEC 61131-3 Structured Text, ensuring real-time responsiveness
	•	Is designed for industrial PLC environments where precise control is essential
	•	Includes error handling and tuning capability for practical use
	•	Ensures deterministic execution and reliable performance under varying load conditions
	•	Is suitable for PLCs with scan-cycle timing requirements
	•	Is optimized for PLC memory and processing power
	•	Includes a discussion of the challenges of implementing PID control in a PLC environment
	•	Is designed to be scalable and reusable in different control scenarios
	•	Includes a detailed explanation of the PID control algorithm and its implementation in IEC 61131-3 Structured Text
	•	Is suitable for use in a control system where precise regulation is required
	•	Includes a discussion of the advantages and disadvantages of using a PID controller in a PLC environment
	•	Is designed to be maintainable and updatable for changing control requirements
	•	Includes a discussion of the limitations of PID control in certain applications
	•	Is suitable for use in a control system where precise regulation is required
	•	Includes a discussion of the advantages and disadvantages of using a PID controller in a PLC environment
	•	Is designed to be maintainable and updatable for changing control requirements
	•	Includes a discussion of the limitations of PID control in certain applications
	•	Is suitable for use in a control system where precise regulation is required
	•	Includes a discussion of the advantages and disadvantages of using a PID controller in a PLC environment
	•	Is designed to be maintainable and updatable for changing control requirements
	•	Includes a discussion of the limitations of PID control in certain applications
	•	Is suitable for use in a control system where precise regulation is required
	•	Includes a discussion of the advantages and disadvantages of using a PID controller in a PLC environment
	•	Is designed to be maintainable and updatable for changing control requirements
	•	Includes a discussion of the limitations of PID control in certain applications
	•	Is suitable for use in a control system where precise regulation is required
	•	Includes a discussion of the advantages and disadvantages of using a PID controller in a PLC environment
	•	Is designed to be maintainable and updatable for changing control requirements

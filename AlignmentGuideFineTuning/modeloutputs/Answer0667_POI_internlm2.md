### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block for a PID controller with configurable gains, output clamping, anti-windup, and real-time error handling to regulate industrial processes.  

*(Focus: Modular PID implementation for PLCs with tuning, safety, and scan-cycle compliance.)*

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
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block for a PID controller with configurable gains, output clamping, anti-windup, and real-time error handling to regulate industrial processes.  

*(Focus: Modular PID implementation for PLCs with tuning, safety, and scan-cycle compliance.)*
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

🟨 S (Safety) – Safety Considerations

Ensure the PID function block:
	•	Does not cause system instability or overshoot
	•	Handles input and output limits gracefully
	•	Prevents windup and derivative filter instability
	•	Is resilient to parameter changes and scan-cycle timing variations

⸻

🟩 C (Compliance) – Compliance Requirements

Ensure the PID function block:
	•	Follows IEC 61131-3 standard for structured text programming
	•	Complies with PLC scan-cycle timing and safety requirements
	•	Is compatible with different PLC platforms and programming environments

⸻

🟩 T (Tuning) – Tuning Considerations

Implement a tuning mechanism to adjust the PID gains:
	•	Allow manual tuning through a dedicated interface
	•	Provide a method to automatically tune the gains based on process response
	•	Include a method to store and recall tuning results

⸻

🟩 D (Documentation) – Documentation Requirements

Provide clear and concise documentation for the PID function block:
	•	Include a description of the function block's purpose and functionality
	•	Provide a list of input and output parameters with their data types and descriptions
	•	Explain the tuning process and any available tuning methods
	•	Provide examples of how to use the function block in a PLC program
	•	Include any necessary safety precautions and compliance requirements

⸻

🟩 T (Testing) – Testing Requirements

Perform thorough testing of the PID function block:
	•	Test the function block's response to different setpoints and disturbances
	•	Verify that the function block handles input and output limits correctly
	•	Ensure that the function block is resilient to parameter changes and scan-cycle timing variations
	•	Test the function block's compliance with PLC scan-cycle timing and safety requirements
	•	Test the function block's compatibility with different PLC platforms and programming environments

⸻

🟩 R (Review) – Review Requirements

Submit the PID function block for review:
	•	Provide the source code and any necessary documentation
	•	Explain the design choices and any trade-offs made during development
	•	Address any questions or concerns raised during the

### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block for a PID controller with configurable gains, error handling, anti-windup, and output clamping to enable precise real-time closed-loop control in PLC systems.  

*(Focus: Robust industrial PID logic with tuning, safety, and reusability.)*

### Prompt:
**PID Controller:**
Implement a self-contained function block in IEC 61131-3 structured text to create a PID controller. Include configurable parameters for proportional, integral, and derivative gains, with error handling and tuning capability.

**T-A-G:**

🟥 T (Task)

Implement a self-contained PID controller as a function block in IEC 61131-3 Structured Text for real-time control in PLC-based automation systems.

⸻

🟩 A (Action)
	•	Define the following inputs:
	•	Setpoint, ProcessVariable (for error calculation)
	•	Kp, Ki, Kd (gain tuning parameters)
	•	MinOutput, MaxOutput (output clamping)
	•	Enable, Reset (runtime control flags)
	•	Create the PID logic:
	•	Compute the control error: Error := Setpoint - ProcessVariable
	•	Accumulate the integral term using Ki and DeltaT, with anti-windup logic
	•	Calculate the derivative term from the rate of change of the process variable
	•	Compute the control output and apply output limits
	•	Reset internal states if Reset = TRUE
	•	Use internal memory to track previous values and ensure smooth scan-cycle execution
	•	Include comments for each computation block to improve readability and maintenance

⸻

🟦 G (Goal)

Deliver a robust, tunable, and reusable PID controller function block that performs well in real-time industrial control applications. The block should ensure safe, stable, and accurate output control with built-in safeguards like anti-windup and clamping, making it suitable for integration into any PLC-based closed-loop control system.

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block for a PID controller with configurable gains, error handling, anti-windup, and output clamping to enable precise real-time closed-loop control in PLC systems.  

*(Focus: Robust industrial PID logic with tuning, safety, and reusability.)*
**PID Controller:**
Implement a self-contained function block in IEC 61131-3 structured text to create a PID controller. Include configurable parameters for proportional, integral, and derivative gains, with error handling and tuning capability.

**T-A-G:**

🟥 T (Task)

Implement a self-contained PID controller as a function block in IEC 61131-3 Structured Text for real-time control in PLC-based automation systems.

⸻

🟩 A (Action)
	•	Define the following inputs:
	•	Setpoint, ProcessVariable (for error calculation)
	•	Kp, Ki, Kd (gain tuning parameters)
	•	MinOutput, MaxOutput (output clamping)
	•	Enable, Reset (runtime control flags)
	•	Create the PID logic:
	•	Compute the control error: Error := Setpoint - ProcessVariable
	•	Accumulate the integral term using Ki and DeltaT, with anti-windup logic
	•	Calculate the derivative term from the rate of change of the process variable
	•	Compute the control output and apply output limits
	•	Reset internal states if Reset = TRUE
	•	Use internal memory to track previous values and ensure smooth scan-cycle execution
	•	Include comments for each computation block to improve readability and maintenance

⸻

🟦 G (Goal)

Deliver a robust, tunable, and reusable PID controller function block that performs well in real-time industrial control applications. The block should ensure safe, stable, and accurate output control with built-in safeguards like anti-windup and clamping, making it suitable for integration into any PLC-based closed-loop control system.

⸻

🟩 A (Action)
	•	Test the function block with various input scenarios, including:
	•	Different setpoints and process variables
	•	Non-linear process behavior
	•	Input disturbances and noise
	•	Verify the controller's performance, stability, and responsiveness
	•	Document the function block's capabilities, limitations, and usage guidelines
	•	Ensure the function block is compatible with the target PLC platform and programming environment

⸻

🟥 T (Task)

Document the PID controller function block's design, testing, and usage guidelines in a comprehensive user manual. The manual should include:

⸻

🟩 A (Action)
	•	Introduction to the PID controller function block
	•	Description of the function block's inputs, outputs, and internal states
	•	Explanation of the PID controller's mathematical principles and operation
	•	Guidelines for configuring and tuning the PID controller
	•	Instructions for integrating the function block into a PLC-based control system
	•	Examples of how to use the function block in various control scenarios
	•	Known limitations and potential issues to be aware of
	•	Support resources, such as contact information and troubleshooting tips

⸻

🟦 G (Goal)

Provide a clear and comprehensive user manual that enables users to effectively implement and utilize the PID controller function block in their PLC-based control systems. This will ensure successful and efficient real-time control, ultimately contributing to the overall performance and reliability of the system.

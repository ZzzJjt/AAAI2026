### Intent:
**Intent Summary:**  
Create a reusable, configurable PID controller function block in IEC 61131-3 Structured Text with tunable gains, anti-windup, output clamping, and error handling for precise industrial process control (e.g., temperature, pressure) on PLCs.  

*(Key features: modularity, safety, diagnostics, and scan-cycle compatibility.)*

### Prompt:
**PID Controller:**
Implement a self-contained function block in IEC 61131-3 structured text to create a PID controller. Include configurable parameters for proportional, integral, and derivative gains, with error handling and tuning capability.


**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In industrial automation systems, maintaining precise control over temperature, pressure, flow, or position is critical. Without a reliable and tunable PID controller, systems may experience instability, overshoot, or slow response. Many basic PID implementations lack configurable gains, anti-windup measures, or proper error handling, making them unsuitable for complex or sensitive processes when deployed on a PLC using IEC 61131-3 Structured Text.

⸻

🟩 A (After) – The Desired Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text that implements a standard PID controller. The block should:
	•	Include tunable parameters for proportional (Kp), integral (Ki), and derivative (Kd) gains
	•	Support error calculation and handle input setpoint and process variable
	•	Include safeguards such as integral windup prevention, output clamping, and reset logic
	•	Be modular, scan-cycle-safe, and easily integrable into control loops
	•	Provide intuitive input/output structure with documentation for users and maintainers

⸻

🟧 B (Bridge) – How to Get There
	1.	Define inputs for:
	•	Setpoint : REAL
	•	ProcessVariable : REAL
	•	Kp, Ki, Kd : REAL
	•	Enable, Reset : BOOL
	•	MinOutput, MaxOutput : REAL
	2.	Calculate:
	•	Error = Setpoint – ProcessVariable
	•	Integral term with anti-windup (limit or back-calculate)
	•	Derivative term using difference in process variable
	3.	Output:
	•	ControlOutput : REAL
	•	Optionally, Error, IntegralTerm, and DerivativeTerm for monitoring
	4.	Add structured comments and logic separation (e.g., IF Enable THEN ...)
	5.	Ensure the block behaves predictably under all input conditions

### Generated Code:
**Intent Summary:**  
Create a reusable, configurable PID controller function block in IEC 61131-3 Structured Text with tunable gains, anti-windup, output clamping, and error handling for precise industrial process control (e.g., temperature, pressure) on PLCs.  

*(Key features: modularity, safety, diagnostics, and scan-cycle compatibility.)*
**PID Controller:**
Implement a self-contained function block in IEC 61131-3 structured text to create a PID controller. Include configurable parameters for proportional, integral, and derivative gains, with error handling and tuning capability.


**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In industrial automation systems, maintaining precise control over temperature, pressure, flow, or position is critical. Without a reliable and tunable PID controller, systems may experience instability, overshoot, or slow response. Many basic PID implementations lack configurable gains, anti-windup measures, or proper error handling, making them unsuitable for complex or sensitive processes when deployed on a PLC using IEC 61131-3 Structured Text.

⸻

🟩 A (After) – The Desired Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text that implements a standard PID controller. The block should:
	•	Include tunable parameters for proportional (Kp), integral (Ki), and derivative (Kd) gains
	•	Support error calculation and handle input setpoint and process variable
	•	Include safeguards such as integral windup prevention, output clamping, and reset logic
	•	Be modular, scan-cycle-safe, and easily integrable into control loops
	•	Provide intuitive input/output structure with documentation for users and maintainers

⸻

🟧 B (Bridge) – How to Get There
	1.	Define inputs for:
	•	Setpoint : REAL
	•	ProcessVariable : REAL
	•	Kp, Ki, Kd : REAL
	•	Enable, Reset : BOOL
	•	MinOutput, MaxOutput : REAL
	2.	Calculate:
	•	Error = Setpoint – ProcessVariable
	•	Integral term with anti-windup (limit or back-calculate)
	•	Derivative term using difference in process variable
	3.	Output:
	•	ControlOutput : REAL
	•	Optionally, Error, IntegralTerm, and DerivativeTerm for monitoring
	4.	Add structured comments and logic separation (e.g., IF Enable THEN ...)
	5.	Ensure the block behaves predictably under all input conditions, including:
	•	Initialization (e.g., reset)
	•	Input changes (e.g., setpoint, process variable)
	•	Output changes (e.g., clamping)
	•	Input errors (e.g., NaN, Infinity)
	6.	Test the block in a simulation or real-world environment to validate its performance and behavior
	7.	Document the block's inputs, outputs, parameters, and behavior for users and maintainers
	8.	Consider adding additional features or optimizations based on user feedback or requirements

**Example Usage:**

```ST
// PID Controller Function Block
PIDController : PIDController(
    Setpoint := 25.0,
    ProcessVariable := 23.0,
    Kp := 0.5,
    Ki := 0.1,
    Kd := 0.01,
    Enable := TRUE,
    Reset := FALSE,
    MinOutput := 0.0,
    MaxOutput := 100.0
);

// Control Output
ControlOutput := PIDController.ControlOutput;
```

**Additional Considerations:**

1.	**Safety**: Ensure the PID controller does not cause instability or overshoot, especially in safety-critical systems. Implement safeguards such as anti-windup, output clamping, and reset logic to prevent undesired behavior.
2.	**Modularity**: Design the PID controller as a self-contained function block to promote code reusability and maintainability. Separate logic into distinct sections (e.g., error calculation, anti-windup, output clamping) for better readability and maintainability.
3.	**Scan-Cycle Compatibility**: Ensure the PID controller is compatible with the scan cycle of the PLC, meaning it can be called at regular intervals without causing issues or data corruption.
4.	**Error Handling**: Implement proper error handling for input setpoint, process variable, and other parameters. Handle potential errors such as NaN, Infinity, or out-of-range values gracefully.
5.	**Documentation**: Provide clear and concise documentation for users and maintainers, including input/output structure, parameter descriptions, and behavior under different conditions.
6.	**User Feedback**: Encourage users to provide feedback on the PID controller's performance and behavior. Use this feedback to improve the block's functionality, usability, and documentation.
7.	**Additional Features**: Consider adding additional features or optimizations based on

### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block for a configurable PID controller with tunable gains, error handling, anti-windup, and output clamping to ensure stable and precise process control in industrial automation.  

*(For the digital counter example, the intent would adjust to: "Develop a modular IEC 61131-3 function block for a flexible digital counter with directional control, step sizing, and limit protection.")*

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
Create a reusable IEC 61131-3 Structured Text function block for a configurable PID controller with tunable gains, error handling, anti-windup, and output clamping to ensure stable and precise process control in industrial automation.  

*(For the digital counter example, the intent would adjust to: "Develop a modular IEC 61131-3 function block for a flexible digital counter with directional control, step sizing, and limit protection.")*
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
	6.	Test the block with various setpoints, process variables, and gain values
	7.	Document the block's inputs, outputs, and behavior for users and maintainers

**Digital Counter:**

🟥 B (Before) – The Problem or Challenge

In industrial automation systems, counting the number of events, pulses, or cycles is a common task. However, implementing a digital counter can be complex, especially when considering directional control, step sizing, and limit protection. Many basic counter implementations lack these features, making them unsuitable for complex or safety-critical processes when deployed on a PLC using IEC 61131-3 Structured Text.

⸻

🟩 A (After) – The Desired Outcome

Develop a modular function block in IEC 61131-3 Structured Text that implements a flexible digital counter. The block should:
	•	Include directional control (up/down) and step sizing
	•	Handle limit protection (e.g., maximum count, minimum count)
	•	Provide intuitive input/output structure with documentation for users and maintainers

⸻

🟧 B (Bridge) – How to Get There
	1.	Define inputs for:
	•	Direction : BOOL
	•	StepSize : REAL
	•	MaxCount, MinCount : REAL
	•	Enable : BOOL
	2.	Calculate:
	•	Count = CurrentCount + (Direction * StepSize)
	•	Ensure Count stays within MaxCount and MinCount limits
	3.	Output:
	•	Count : REAL
	•	Optionally, Direction, StepSize, and Enable for monitoring
	4.	Add structured comments and logic separation (e.g., IF Enable THEN ...)
	5.	Ensure the block behaves predictably under all input conditions
	6.	Test the block with various directions, step sizes, and limit values
	7.	Document the block's inputs, outputs, and behavior for users and maintainers

**Additional Considerations:**

•	Consider the use of IEC 61131-3 data types (e.g., REAL, INT, BOOL) and data structures (e.g., arrays, records) to enhance modularity and flexibility.
•	Ensure the function block is scan-cycle-safe, meaning it can be called multiple times within a single scan cycle without causing

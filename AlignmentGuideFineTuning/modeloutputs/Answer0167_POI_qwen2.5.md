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
	5.	Ensure the block behaves predictably under all input conditions and is safe for PLC execution

⸻

**Digital Counter:**
Create a self-contained function block in IEC 61131-3 Structured Text to implement a digital counter. The block should be configurable for direction, step size, and limit protection, and should be modular, scan-cycle-safe, and easily integrable into control loops.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In industrial automation systems, precise control over counting events is essential for tasks such as monitoring production counts, tracking inventory, or controlling machine cycles. Many basic counter implementations lack configurability, directional control, or limit protection, making them unsuitable for complex or sensitive processes when deployed on a PLC using IEC 61131-3 Structured Text.

⸻

🟩 A (After) – The Desired Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text that implements a standard digital counter. The block should:
	•	Include configurable parameters for direction, step size, and limit protection
	•	Support input for incrementing or decrementing the counter
	•	Include safeguards such as limit protection and reset logic
	•	Be modular, scan-cycle-safe, and easily integrable into control loops
	•	Provide intuitive input/output structure with documentation for users and maintainers

⸻

🟧 B (Bridge) – How to Get There
	1.	Define inputs for:
	•	Direction : BOOL (True for increment, False for decrement)
	•	StepSize : INT
	•	Enable, Reset : BOOL
	•	MinValue, MaxValue : INT
	•	CounterValue : INT (output)
	2.	Implement logic to increment or decrement the counter based on direction and step size
	3.	Add limit protection to prevent counter from exceeding MinValue or MaxValue
	4.	Add structured comments and logic separation (e.g., IF Enable THEN ...)
	5.	Ensure the block behaves predictably under all input conditions and is safe for PLC execution

⸻

**IEC 61131-3 Structured Text Function Block:**
Create a self-contained function block in IEC 61131-3 Structured Text to implement a configurable PID controller with tunable gains, error handling, anti-windup, and output clamping. The block should be modular, scan-cycle-safe, and easily

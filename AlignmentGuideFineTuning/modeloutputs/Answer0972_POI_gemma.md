### Intent:
**Intent Summary:**  
Create a robust, configurable PID controller function block in IEC 61131-3 Structured Text with anti-windup, output clamping, and input validation for precise real-time industrial process control.

### Prompt:
**Counter:**
Implement a self-contained function block in IEC 61131-3 structured text for a digital counter with up/down counting modes. Include configurable initial value, step size, and overflow handling.


**T-A-G:**

🟥 T (Task)

Create a self-contained function block in IEC 61131-3 Structured Text that implements a configurable digital counter with both up and down counting modes.

⸻

🟩 A (Action)
	•	Define inputs for:
	•	Enable : BOOL – activates the counter
	•	CountUp : BOOL – selects the counting direction
	•	StepSize : INT – amount to increment or decrement
	•	InitValue : INT – starting value of the counter
	•	Reset : BOOL – resets the counter to the initial value
	•	MaxValue / MinValue : INT – upper and lower bounds for overflow handling
	•	Use conditional logic to increment or decrement based on CountUp
	•	Implement logic to clamp the value within MinValue and MaxValue
	•	Provide outputs for:
	•	CurrentValue : INT – the current counter state
	•	AtMax, AtMin : BOOL – flags for boundary conditions
	•	Comment all key sections to ensure clarity and reusability

⸻

🟦 G (Goal)

Deliver a modular, safe, and easy-to-integrate counter block suitable for PLC applications requiring flexible and bounded counting logic. The implementation should be robust, configurable, and reliable for use in scan-cycle-sensitive automation environments.

### Generated Code:
**Intent Summary:**  
Create a robust, configurable PID controller function block in IEC 61131-3 Structured Text with anti-windup, output clamping, and input validation for precise real-time industrial process control.
**Counter:**
Implement a self-contained function block in IEC 61131-3 structured text for a digital counter with up/down counting modes. Include configurable initial value, step size, and overflow handling.


**T-A-G:**

🟥 T (Task)

Create a self-contained function block in IEC 61131-3 Structured Text that implements a configurable digital counter with both up and down counting modes.

⸻

🟩 A (Action)
	•	Define inputs for:
	•	Enable : BOOL – activates the counter
	•	CountUp : BOOL – selects the counting direction
	•	StepSize : INT – amount to increment or decrement
	•	InitValue : INT – starting value of the counter
	•	Reset : BOOL – resets the counter to the initial value
	•	MaxValue / MinValue : INT – upper and lower bounds for overflow handling
	•	Use conditional logic to increment or decrement based on CountUp
	•	Implement logic to clamp the value within MinValue and MaxValue
	•	Provide outputs for:
	•	CurrentValue : INT – the current counter state
	•	AtMax, AtMin : BOOL – flags for boundary conditions
	•	Comment all key sections to ensure clarity and reusability

⸻

🟦 G (Goal)

Deliver a modular, safe, and easy-to-integrate counter block suitable for PLC applications requiring flexible and bounded counting logic. The implementation should be robust, configurable, and reliable for use in scan-cycle-sensitive automation environments.

**T-A-G:**

🟥 T (Task)

Create a self-contained function block in IEC 61131-3 Structured Text that implements a configurable PID controller with anti-windup, output clamping, and input validation.

⸻

🟩 A (Action)
	•	Define inputs for:
	•	Enable : BOOL – activates the controller
	•	Setpoint : INT – desired output value
	•	ProcessValue : INT – current process value
	•	ProportionalGain, IntegralGain, DerivativeGain : REAL – controller gains
	•	IntegralWindup : REAL – anti-windup threshold
	•	OutputMax, OutputMin : INT – upper and lower bounds for output clamping
	•	Comment all key sections to ensure clarity and reusability
	•	Implement a PID controller with anti-windup and output clamping
	•	Use conditional logic to validate inputs and prevent invalid states
	•	Provide outputs for:
	•	Output : INT – the current controller output
	•	Error : INT – the current error between the setpoint and process value
	•	Comment all key sections to ensure clarity and reusability

⸻

🟦 G (Goal)

Deliver a modular, safe, and easy-to-integrate PID controller block suitable for PLC applications requiring precise and reliable process control. The implementation should be robust, configurable, and reliable for use in scan-cycle-sensitive automation environments.

**T-A-G:**

🟥 T (Task)

Create a self-contained function block in IEC 61131-3 Structured Text that implements a configurable PID controller with anti-windup, output clamping, and input validation.

⸻

🟩 A (Action)
	•	Define inputs for:
	•	Enable : BOOL – activates the controller
	•	Setpoint : INT – desired output value
	•	ProcessValue : INT – current process value
	•	ProportionalGain, IntegralGain, DerivativeGain : REAL – controller gains
	•	IntegralWindup : REAL – anti-windup threshold
	•	OutputMax, OutputMin : INT – upper and lower bounds for output clamping
	•	Comment all key sections to ensure clarity and reusability
	•	Implement a PID controller with anti-windup and output clamping
	•	Use conditional logic to validate inputs and prevent invalid states
	•

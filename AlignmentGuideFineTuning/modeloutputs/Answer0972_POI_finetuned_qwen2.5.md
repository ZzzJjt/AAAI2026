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

🟥 T（Task）

Create a self-contained function block in IEC 61131-3 Structured Text to implement a digital counter with configurable up/down counting modes, including configurable initial value, step size, and overflow handling.

⸻

🟩 A（Action）

	•	Inputs:
	•	Enable : BOOL — activates the counter
	•	CountUp : BOOL — selects the counting direction
	•	StepSize : INT — amount to increment or decrement
	•	InitValue : INT — starting value of the counter
	•	Reset : BOOL — resets the counter to the initial value
	•	MaxValue / MinValue : INT — upper and lower bounds for overflow handling
	•	Process:
	•	Implement logic to increment or decrement the counter based on CountUp
	•	Clip the counter value to ensure it stays within MinValue and MaxValue
	•	Provide outputs:
	•	CurrentValue : INT — the current value of the counter
	•	AtMax : BOOL — flag indicating the counter reached the maximum value
	•	AtMin : BOOL — flag indicating the counter reached the minimum value
	•	Include comments to explain the logic and edge cases

⸻

🟦 G（Goal）

Develop a reusable and scan-cycle-safe counter function block that is easy to integrate into industrial control systems, with clear documentation and configurable limits to ensure safe and predictable operation.

**T-A-G:**

🟥 T（Task）

Create a self-contained function block in IEC 61131-3 Structured Text to implement a digital counter with configurable up/down counting modes, including configurable initial value, step size, and overflow handling.

⸻

🟩 A（Action）

	•	Inputs:
	•	Enable : BOOL — activates the counter
	•	CountUp : BOOL — selects the counting direction
	•	StepSize : INT — amount to increment or decrement
	•	InitValue : INT — starting value of the counter
	•	Reset : BOOL — resets the counter to the initial value
	•	MaxValue / MinValue : INT — upper and lower bounds for overflow handling
	•	Process:
	•	Implement logic to increment or decrement the counter based on CountUp
	•	Clip the counter value to ensure it stays within MinValue and MaxValue
	•	Provide outputs:
	•	CurrentValue : INT — the

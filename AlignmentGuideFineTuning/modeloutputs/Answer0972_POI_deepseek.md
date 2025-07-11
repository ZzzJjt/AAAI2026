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

⸻

🟩 A (Action)
	•	Define the PID controller function block inputs:
	•	Setpoint : INT – target value for the controlled process
	•	ProportionalGain : INT – proportional control strength
	•	IntegralGain : INT – integral control strength
	•	DerivativeGain : INT – derivative control strength
	•	OutputLimit : INT – clamping value for the output
	•	InputLimit : INT – clamping value for the input
	•	AntiWindup : BOOL – enables anti-windup logic
	•	Use conditional logic to calculate the error between the setpoint and the current value
	•	Implement integral and derivative calculations based on the PID coefficients
	•	Apply anti-windup logic to prevent the output from exceeding the output limit
	•	Provide outputs for:
	•	CurrentValue : INT – the current process value
	•	AtMax, AtMin : BOOL – flags for boundary conditions
	•	Error : INT – the difference between the setpoint and the current value
	•	AntiWindupFlag : BOOL – flag for anti-windup logic
	•	Comment all key sections to ensure clarity and reusability

⸻

🟦 G (Goal)

Deliver a robust, configurable PID controller function block suitable for real-time industrial process control. The implementation should be reliable, adjustable, and adaptable to various process control scenarios.

⸻

🟩 A (Action)
	•	Define the counter and PID controller function block outputs:
	•	Enable : BOOL – activates the counter or PID controller
	•	Reset : BOOL – resets the counter or PID controller to the initial value
	•	EnableCounter : BOOL – enables the counter
	•	EnablePID : BOOL – enables the PID controller
	•	Comment all key sections to ensure clarity and reusability

⸻

🟦 G (Goal)

Deliver a complete, modular, and user-friendly function block library for IEC 61131-3 Structured Text. The library should include both a digital counter and a PID controller function block, each with configurable inputs and outputs, as well as anti-windup and output clamping features.

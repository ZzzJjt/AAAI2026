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

---

**Function Block:**

```
PROGRAM PID_Controller;

VAR
	Error, PrevError, PrevProcessVariable, PrevControlOutput, Integral, Derivative, Output: REAL;
	Reset: BOOL;

FUNCTION PID_Controller: REAL
BEGIN
	// Set default values for internal variables
	Error := 0.0;
	Integral := 0.0;
	Derivative := 0.0;
	Reset := FALSE;

	// Check for Reset flag
	IF Reset THEN
		// Reset internal variables
		Error := 0.0;
		Integral := 0.0;
		Derivative := 0.0;
		PrevError := 0.0;
		PrevProcessVariable := 0.0;
		PrevControlOutput := 0.0;
	END_IF;

	// Calculate control error
	Error := Setpoint - ProcessVariable;

	// Anti-windup logic for integral term
	IF (Error * Integral) < 0.0 THEN
		Integral := 0.0;
	END_IF;

	// Accumulate integral term
	Integral := Integral + Ki * Error * DeltaT;

	// Calculate derivative term
	Derivative := (Error - PrevError) / DeltaT;

	// Compute control output
	Output := Kp * Error + Ki * Integral + Kd * Derivative;

	// Apply output clamping
	IF Output < MinOutput THEN
		Output := MinOutput;
	END_IF;
	IF Output > MaxOutput THEN
		Output := MaxOutput;
	END_IF;

	// Store previous values for next scan cycle
	PrevError := Error;
	PrevProcessVariable := ProcessVariable;
	PrevControlOutput := Output;

	// Return the control output
	RETURN Output;
END_FUNCTION;
```

**Notes:**

1. This function block assumes that the `DeltaT` variable is defined elsewhere in the program and represents the time between scan cycles.
2. The function block can be easily integrated

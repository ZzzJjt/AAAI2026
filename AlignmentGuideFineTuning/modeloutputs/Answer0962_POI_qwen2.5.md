### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block for a configurable digital counter with up/down modes, bounds checking, and reset functionality, suitable for PLC automation.

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
Create a reusable IEC 61131-3 structured text function block for a configurable digital counter with up/down modes, bounds checking, and reset functionality, suitable for PLC automation.
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

Deliver a modular, safe, and easy-to-integrate counter block suitable for PLC applications requiring flexible and bounded counting logic. The implementation should be robust, configurable, and reliable for use in scan-cycle-sensitive automation environments. Ensure the code is well-commented and follows best practices for IEC 61131-3 structured text.

**Code:**

```structuredtext
// Counter Function Block
// Inputs:
//   Enable: BOOL - Activates the counter
//   CountUp: BOOL - Selects the counting direction
//   StepSize: INT - Amount to increment or decrement
//   InitValue: INT - Starting value of the counter
//   Reset: BOOL - Resets the counter to the initial value
//   MaxValue: INT - Upper bound for overflow handling
//   MinValue: INT - Lower bound for overflow handling
// Outputs:
//   CurrentValue: INT - The current counter state
//   AtMax: BOOL - Flag for reaching the maximum value
//   AtMin: BOOL - Flag for reaching the minimum value

VAR
  CurrentValue: INT := InitValue; // Initialize counter to initial value
  AtMax: BOOL := FALSE; // Flag for maximum value
  AtMin: BOOL := FALSE; // Flag for minimum value
END_VAR

IF Enable THEN
  IF Reset THEN
    CurrentValue := InitValue; // Reset counter to initial value
    AtMax := FALSE; // Reset max flag
    AtMin := FALSE; // Reset min flag
  ELSE
    IF CountUp THEN
      CurrentValue := CurrentValue + StepSize; // Increment counter
    ELSE
      CurrentValue := CurrentValue - StepSize; // Decrement counter
    END_IF

    // Clamp counter within bounds
    IF CurrentValue > MaxValue THEN
      CurrentValue := MaxValue;
      AtMax := TRUE;
    END_IF

    IF CurrentValue < MinValue THEN
      CurrentValue := MinValue;
      AtMin := TRUE;
    END_IF
  END_IF
END_IF

// Outputs
CurrentValue := CurrentValue; // Current counter state
AtMax := AtMax; // Flag for reaching the maximum value
AtMin := AtMin; // Flag for reaching the minimum value
```

**Explanation:**

This function block is designed to be a reusable component for PLC automation systems, providing a flexible and bounded counting mechanism. It includes inputs for enabling the counter, selecting the counting direction, setting the step size, initializing the counter, and resetting it. The counter's current value, as well as flags indicating whether the counter has reached its maximum or minimum value, are provided as outputs.

The code is structured to be clear and maintainable

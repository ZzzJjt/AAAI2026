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


**Code:**

```
FUNCTION_BLOCK Counter
    VAR
        CurrentValue : INT;
        AtMax, AtMin : BOOL;
    INPUT
        Enable : BOOL;
        CountUp : BOOL;
        StepSize : INT;
        InitValue : INT;
        Reset : BOOL;
        MaxValue, MinValue : INT;
    OUTPUT
        CurrentValue : INT;
        AtMax : BOOL;
        AtMin : BOOL;
    BEGIN
        IF Enable THEN
            IF Reset THEN
                CurrentValue := InitValue;
                AtMax := FALSE;
                AtMin := FALSE;
            ELSE
                IF CountUp THEN
                    IF CurrentValue < MaxValue THEN
                        CurrentValue := CurrentValue + StepSize;
                    ELSE
                        CurrentValue := MinValue;
                        AtMax := TRUE;
                    END_IF;
                ELSE
                    IF CurrentValue > MinValue THEN
                        CurrentValue := CurrentValue - StepSize;
                    ELSE
                        CurrentValue := MaxValue;
                        AtMin := TRUE;
                    END_IF;
                END_IF;
            END_IF;
        END_IF;
    END_FUNCTION_BLOCK
```

**Explanation:**

The provided code defines a function block called `Counter` that implements a digital counter with configurable up and down counting modes, initial value, step size, overflow handling, and output flags for boundary conditions.

The function block takes the following inputs:

* `Enable`: A Boolean input that activates the counter.
* `CountUp`: A Boolean input that selects the counting direction (up or down).
* `StepSize`: An integer input that defines the amount to increment or decrement the counter.
* `InitValue`: An integer input that sets the starting value of the counter.
* `Reset`: A Boolean input that resets the counter to the initial value.
* `MaxValue` and `MinValue`: Integer inputs that define the upper and lower bounds for overflow handling.

The function block provides the following outputs:

* `CurrentValue`: An integer output that represents the current

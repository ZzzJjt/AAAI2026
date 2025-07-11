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

Deliver a modular, safe, and easy-to-integrate counter block suitable for PLC applications requiring flexible and bounded counting logic. The implementation should be robust, configurable, and reliable for use in scan-cycle-sensitive automation environments.
FUNCTION_BLOCK FB_DigitalCounter
VAR_INPUT
    Enable : BOOL;
    CountUp : BOOL;
    StepSize : INT;
    InitValue : INT;
    Reset : BOOL;
    MaxValue : INT;
    MinValue : INT;
END_VAR

VAR_OUTPUT
    CurrentValue : INT;
    AtMax : BOOL;
    AtMin : BOOL;
END_VAR

VAR
    PrevValue : INT;
    CurrentValue : INT;
END_VAR

METHOD Execute : BOOL
BEGIN
    IF Enable THEN
        IF Reset THEN
            CurrentValue := InitValue;
            AtMax := FALSE;
            AtMin := FALSE;
        ELSE
            PrevValue := CurrentValue;
            IF CountUp THEN
                IF StepSize > 0 THEN
                    CurrentValue := CurrentValue + StepSize;
                    IF CurrentValue > MaxValue THEN
                        CurrentValue := MaxValue;
                        AtMax := TRUE;
                    ELSIF CurrentValue < MinValue THEN
                        CurrentValue := MinValue;
                        AtMin := TRUE;
                    END_IF;
                ELSIF StepSize < 0 THEN
                    CurrentValue := CurrentValue - StepSize;
                    IF CurrentValue < MinValue THEN
                        CurrentValue := MinValue;
                        AtMin := TRUE;
                    ELSIF CurrentValue > MaxValue THEN
                        CurrentValue := MaxValue;
                        AtMax := TRUE;
                    END_IF;
                ELSE
                    CurrentValue := PrevValue + StepSize;
                END_IF;
            ELSE
                CurrentValue := PrevValue - StepSize;
                IF CurrentValue < MinValue THEN
                    CurrentValue := MinValue;
                    AtMin := TRUE;
                ELSIF CurrentValue > MaxValue THEN
                    CurrentValue := MaxValue;
                    AtMax := TRUE;
                END_IF;
            END_IF;
        END_IF;
    END_IF;

    RETURN TRUE;
END_METHOD

METHOD Reset : BOOL
BEGIN
    CurrentValue := InitValue;
    AtMax := FALSE;
    AtMin := FALSE;
    RETURN TRUE;
END_METHOD

METHOD Step : INT
BEGIN
    IF CountUp THEN
        StepSize := StepSize + 1;
    ELSE

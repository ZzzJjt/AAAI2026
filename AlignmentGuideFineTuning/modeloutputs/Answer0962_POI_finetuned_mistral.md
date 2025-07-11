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
(* IEC 61131-3 Structured Text Function Block for a Configurable Digital Counter *)
(* Supports up/down counting, configurable step size, bounds checking, and reset *)
(* Uses conditional logic to handle up/down modes and overflow/underflow *)
(* Designed for reusable PLC automation tasks such as counting parts, cycles, or events *)

FUNCTION_BLOCK DigitalCounter
VAR_INPUT
    Enable : BOOL;                  (* TRUE to enable counting *)
    CountUp : BOOL;                 (* TRUE for up counting, FALSE for down counting *)
    StepSize : INT;                 (* Increment/decrement value, e.g., 1 or -1 *)
    InitValue : INT;                (* Initial counter value, e.g., 0 *)
    Reset : BOOL;                   (* TRUE to reset counter to InitValue *)
    MaxValue : INT;                 (* Upper bound for counter, e.g., 1000 *)
    MinValue : INT;                 (* Lower bound for counter, e.g., 0 *)
END_VAR

VAR_OUTPUT
    CurrentValue : INT;             (* Current counter value *)
    AtMax : BOOL;                   (* TRUE if CurrentValue equals MaxValue *)
    AtMin : BOOL;                   (* TRUE if CurrentValue equals MinValue *)
END_VAR

VAR
    PrevEnable : BOOL;              (* Previous state of Enable for edge detection *)
    PrevReset : BOOL;               (* Previous state of Reset for edge detection *)
    TempValue : INT;                (* Temporary value for reset handling *)
END_VAR

(* Reset logic *)
IF Reset THEN
    CurrentValue := InitValue;      (* Reset counter to InitValue *)
    AtMax := FALSE;                 (* Reset AtMax flag *)
    AtMin := FALSE;                 (* Reset AtMin flag *)
    TempValue := InitValue;         (* Store InitValue for edge detection *)
    PrevReset := Reset;             (* Update previous state for edge detection *)
ELSE
    (* Edge detection for Reset *)
    IF Reset AND NOT PrevReset THEN
        (* Reset logic only triggered once on rising edge of Reset *)
        CurrentValue := InitValue;  (* Reset counter to InitValue *)

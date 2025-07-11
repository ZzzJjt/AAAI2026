### Intent:
The task is to create a configurable digital counter function block in IEC 61131-3 Structured Text that handles up/down counting with adjustable step size, bounds checking, reset capability, and edge detection for industrial automation applications.

### Prompt:
**DecToHex:**
Implement a self-contained function block in IEC 61131-3 structured text to convert a 10-digit decimal value to hexadecimal. Ensure proper handling of large values and edge cases.

**T-A-G:**

🟥 T (Task)

Create a function block in IEC 61131-3 Structured Text that converts a 10-digit decimal value into its hexadecimal representation.

⸻

🟩 A (Action)
	•	Define inputs and outputs:
	•	Input: DecValue : LINT
	•	Output: HexString : STRING
	•	Use a loop-based algorithm to:
	•	Repeatedly divide the decimal number by 16
	•	Map each remainder to its corresponding hexadecimal digit (0–F)
	•	Construct the hex string in reverse order, then output the result
	•	Implement edge case handling, such as:
	•	Input = 0 → Output = '0'
	•	Large number limits → safe type casting and bounds checking
	•	Add clear comments and use internal variables for modularity and clarity

⸻

🟦 G (Goal)

Deliver a robust, reusable, and scan-cycle-safe function block that reliably converts large decimal values to hexadecimal. The block should support integration with diagnostics, HMI displays, and protocol encoders, while handling all typical boundary conditions safely and efficiently.

### Generated Code:
The task is to create a configurable digital counter function block in IEC 61131-3 Structured Text that handles up/down counting with adjustable step size, bounds checking, reset capability, and edge detection for industrial automation applications.
**DecToHex:**
Implement a self-contained function block in IEC 61131-3 structured text to convert a 10-digit decimal value to hexadecimal. Ensure proper handling of large values and edge cases.

**T-A-G:**

🟥 T (Task)

Create a function block in IEC 61131-3 Structured Text that converts a 10-digit decimal value into its hexadecimal representation.

⸻

🟩 A (Action)
	•	Define inputs and outputs:
	•	Input: DecValue : LINT
	•	Output: HexString : STRING
	•	Use a loop-based algorithm to:
	•	Repeatedly divide the decimal number by 16
	•	Map each remainder to its corresponding hexadecimal digit (0–F)
	•	Construct the hex string in reverse order, then output the result
	•	Implement edge case handling, such as:
	•	Input = 0 → Output = '0'
	•	Large number limits → safe type casting and bounds checking
	•	Add clear comments and use internal variables for modularity and clarity

⸻

🟦 G (Goal)

Deliver a robust, reusable, and scan-cycle-safe function block that reliably converts large decimal values to hexadecimal. The block should support integration with diagnostics, HMI displays, and protocol encoders, while handling all typical boundary conditions safely and efficiently.
(* IEC 61131-3 Structured Text: Digital Counter Function Block *)
(* Purpose: Counts up or down with configurable step size and reset capability *)

FUNCTION_BLOCK DigitalCounterFB
VAR_INPUT
    Reset : BOOL; (* Reset the counter to 0 *)
    StepSize : INT := 1; (* Increment or decrement by this amount *)
END_VAR

VAR_OUTPUT
    Count : INT; (* Current count value *)
    Done : BOOL; (* TRUE when count is within bounds *)
    Error : BOOL; (* TRUE if step size is invalid or reset is triggered *)
END_VAR

VAR
    CurrentCount : INT := 0; (* Current count value *)
    Step : INT; (* Increment or decrement value *)
    MaxCount : INT; (* Maximum count value *)
    MinCount : INT; (* Minimum count value *)
    StepValid : BOOL; (* TRUE if step size is valid *)
END_VAR

(* Initialize outputs *)
Done := FALSE;
Error := FALSE;

(* Initialize internal variables *)
MaxCount := 100; (* Max count value *)
MinCount := -100; (* Min count value *)
StepValid := TRUE; (* Assume valid step size *)

(* Reset the counter *)
IF Reset THEN
    CurrentCount := 0;
    Done := FALSE;
    Error := FALSE;
    StepValid := TRUE;
END_IF;

(* Check step size validity *)
IF StepSize > 0 THEN
    Step := StepSize;
ELSE
    Step := -StepSize;
    StepValid := FALSE;
END_IF;

(* Update the count *)
IF StepValid THEN
    CurrentCount := CurrentCount + Step;
    IF CurrentCount > MaxCount THEN
        CurrentCount := MaxCount;
        Done := TRUE;
    ELSIF CurrentCount < MinCount THEN
        CurrentCount := MinCount;
        Done := TRUE;
    END_IF;
ELSE
    Error := TRUE;
END_IF;

(* Output the current count *)
Count := CurrentCount;

(* Reset the counter if reset is triggered *)
IF Reset THEN
    CurrentCount := 0;
    Done := FALSE;
    Error := FALSE;
    StepValid := TRUE;

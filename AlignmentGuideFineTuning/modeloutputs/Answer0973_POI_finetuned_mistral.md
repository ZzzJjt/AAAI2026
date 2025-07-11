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
FUNCTION_BLOCK FB_DigitalCounter
VAR_INPUT
    Enable : BOOL; // Enable counter operation
    Reset : BOOL; // Reset counter to initial value
    Increment : BOOL; // Increment counter by 1
    Decrement : BOOL; // Decrement counter by 1
    StepSize : INT := 1; // Step size for increment/decrement
    InitialValue : INT := 0; // Initial counter value
END_VAR

VAR_OUTPUT
    CurrentValue : INT; // Current counter value
    EdgeDetect : BOOL; // TRUE if counter edge detected
    Error : BOOL; // TRUE if invalid operation detected
END_VAR

VAR
    PrevEnable : BOOL; // Previous enable state for edge detection
    ValidInput : BOOL; // TRUE if inputs are valid
END_VAR

// Reset counter to initial value when Reset = TRUE
IF Reset THEN
    CurrentValue := InitialValue;
    EdgeDetect := FALSE;
    Error := FALSE;
    ValidInput := FALSE;
    PrevEnable := FALSE;
    RETURN;
END_IF;

// Validate inputs
ValidInput := Enable AND NOT Reset;

// Initialize outputs
EdgeDetect := FALSE;
Error := FALSE;

// Check enable state
IF NOT ValidInput THEN
    Error := TRUE;
    CurrentValue := InitialValue;
    EdgeDetect := FALSE;
    RETURN;
END_IF;

// Check enable state
IF NOT Enable THEN
    CurrentValue := InitialValue;
    EdgeDetect := FALSE;
    RETURN;
END_IF;

// Store previous enable state for edge detection
PrevEnable := Enable;

// Increment counter
IF Increment AND Enable THEN
    CurrentValue := CurrentValue + StepSize;
    IF CurrentValue > MAXINT THEN
        CurrentValue := MAXINT;
        Error := TRUE;
        EdgeDetect := FALSE;
    ELSE
        EdgeDetect := (PrevEnable = FALSE) AND Enable;
    END_IF;
ELSIF Decrement AND Enable THEN
    CurrentValue := CurrentValue - StepSize;
    IF CurrentValue < 0 THEN
        CurrentValue := 0;
        Error :=

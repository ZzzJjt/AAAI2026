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

**Digital Counter:**

🟥 T (Task)

Create a configurable digital counter function block in IEC 61131-3 Structured Text that handles up/down counting with adjustable step size, bounds checking, reset capability, and edge detection for industrial automation applications.

⸻

🟩 A (Action)
	•	Define inputs and outputs:
	•	Input:
		+	Dir : BOOL (Direction: Up/Down)
		+	Step : INT (Step size)
		+	Reset : BOOL (Reset counter)
		+	Min : INT (Minimum value)
		+	Max : INT (Maximum value)
	•	Output:
		+	Count : INT (Current counter value)
		+	Edge : BOOL (Edge detection: Overflow/Underflow)
	•	Initialize internal variables:
	•	Count : INT (Current counter value)
	•	Edge : BOOL (Edge detection flag)
	•	Use a conditional statement to:
	•	Check the Reset input
	•	If Reset = TRUE, set Count = Min
	•	Use a loop-based algorithm to:
	•	Increment/decrement Count based on Dir and Step
	•	Check bounds (Min <= Count <= Max)
	•	If Count exceeds Max or falls below Min, set Edge = TRUE
	•	Output Count and Edge
	•	Add clear comments and use internal variables for modularity and clarity

⸻

🟦 G (Goal)

Deliver a flexible, reusable, and scan-cycle-safe function block that reliably counts in up/down directions with adjustable step sizes, handles bounds checking, resets, and edge detection for various industrial automation applications. The block should support integration with PLC logic, HMI displays, and protocol encoders, while handling all typical boundary conditions safely and efficiently.

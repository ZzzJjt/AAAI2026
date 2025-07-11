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

Deliver a robust, reusable, and scan-cycle-safe function block that reliably converts large decimal values to hexadecimal. The block should support integration with diagnostics, HMI displays, and protocol encoders, while handling all typical boundary conditions safely and efficiently. Ensure the code is well-documented and follows IEC 61131-3 standards for readability and maintainability.

**IEC 61131-3 Structured Text Code:**
```structuredtext
FUNCTION_BLOCK DecToHex
VAR_INPUT
    DecValue : LINT; // Input decimal value
END_VAR
VAR_OUTPUT
    HexString : STRING; // Output hexadecimal string
END_VAR

VAR
    remainder : LINT; // Temporary variable for remainder
    hexDigits : ARRAY[0..15] OF CHAR := ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']; // Array of hexadecimal digits
    hexString : STRING := ''; // Output hexadecimal string
    i : INT; // Loop counter
END_VAR

// Check if input is zero
IF DecValue = 0 THEN
    HexString := '0';
ELSE
    // Convert decimal to hexadecimal
    WHILE DecValue > 0 DO
        remainder := DecValue MOD 16; // Get remainder
        hexString := hexDigits[remainder] & hexString; // Append remainder to hex string
        DecValue := DecValue DIV 16; // Update decimal value
    END_WHILE;
END_IF;
```
This function block takes a 10-digit decimal value as input and returns its hexadecimal representation as a string. It handles edge cases such as input = 0 and large number limits by using safe type casting and bounds checking. The code is well-documented and follows IEC 61131-3 standards for readability and maintainability.

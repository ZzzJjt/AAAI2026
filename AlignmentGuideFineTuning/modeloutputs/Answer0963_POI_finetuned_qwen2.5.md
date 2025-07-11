### Intent:
The task is to create a reusable IEC 61131-3 function block in Structured Text that accurately converts 10-digit decimal values to hexadecimal strings, with robust handling of edge cases and large numbers for industrial automation applications.

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
The task is to create a reusable IEC 61131-3 function block in Structured Text that accurately converts 10-digit decimal values to hexadecimal strings, with robust handling of edge cases and large numbers for industrial automation applications.
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

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC programmer or automation engineer developing reusable function blocks in IEC 61131-3 Structured Text for industrial applications.

⸻

🟩 I (Input) – What You’re Given

You need to implement a function block that:
	•	Accepts a 10-digit decimal value as input
	•	Converts this value to a hexadecimal string
	•	Handles large values and edge cases (zero, maximum limits)
	•	Works efficiently within scan-cycle constraints

⸻

🟧 S (Steps) – How to Do It

	1.	Define the function block with:
	•	Input: DecValue : LINT
	•	Output: HexString : STRING
	2.	Implement the conversion logic:
	•	Use a loop to repeatedly divide the input value by 16
	•	Map the remainder to the corresponding hexadecimal digit (0–F)
	•	Construct the hex string in reverse order
	3.	Implement edge case handling:
	•	For input = 0, return '0'
	•	For large values, ensure safe type casting and bounds checking
	•	Add comments explaining the logic and handling of edge cases
	•	Perform scan-cycle-safe operations, avoiding blocking or recursion
	•	Include detailed comments on the implementation and limitations

⸻

🟩 E (Example) – What It Should Look Like

	•	Implement a self-contained function block named DecToHex:
	•	Input: DecValue : LINT
	•	Output: HexString : STRING
	•	Include a detailed explanation of the conversion process, including handling of large values and edge cases
	•	Provide a scan-cycle-safe implementation with clear comments and logic for hexadecimal conversion
	•	Ensure the function block is reusable and well-documented for integration into industrial control systems
	•	For example, when DecValue = 1234567890, the function block should return the hexadecimal representation: '75BCD16A'
	•	Include a discussion of potential limitations, such as scan-cycle duration and memory usage, when handling large values
	•	For further reading, suggest relevant standards or references on hexadecimal conversion in PLC programming
	•	For code generation, use a tool like IEC 61131-3 Structured Text to create

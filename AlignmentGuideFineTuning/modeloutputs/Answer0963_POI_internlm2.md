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

Deliver a robust, reusable, and scan-cycle-safe function block that reliably converts large decimal values to hexadecimal. The block should support integration with diagnostics, HMI displays, and protocol encoders, while handling all typical boundary conditions safely and efficiently. The function block should be thoroughly tested and documented, with a clear and concise user manual.

---

**DecToHex:**

```ST
// Function Block: DecToHex
// Description: Converts a 10-digit decimal value to hexadecimal
// Input: DecValue : LINT
// Output: HexString : STRING

VAR_INPUT
  DecValue : LINT;
END_VAR

VAR
  Remainder : LINT;
  HexDigit : STRING[2];
  HexString : STRING[20];
  Index : LINT := 20;
END_VAR

BEGIN
  // Edge case: Input = 0
  IF DecValue = 0 THEN
    HexString := '0';
    EXIT;
  END_IF;

  // Main conversion loop
  WHILE DecValue > 0 DO
    Remainder := DecValue MOD 16;
    IF Remainder < 10 THEN
      HexDigit := INT_TO_STRING(Remainder);
    ELSE
      HexDigit := CHR(Ord('A') + Remainder - 10);
    END_IF;
    HexString[Index] := HexDigit;
    DecValue := DecValue \ 16;
    Index := Index - 1;
  END_WHILE;

  // Output the reversed hex string
  HexString := HexString[Index..20];

  // Output the result
  HexString := HexString;
END_FUNCTION
```

**T-A-G:**

🟥 T (Task)

The task is to create a function block in IEC 61131-3 Structured Text that converts a 10-digit decimal value into its hexadecimal representation. The function block should handle large values and edge cases, such as input equal to 0 and large number limits.

⸻

🟩 A (Action)
To accomplish this task, we need to define inputs and outputs for the function block. The input will be a 10-digit decimal value, and the output will be a hexadecimal string. We will use a loop-based algorithm to repeatedly divide the decimal number by 16, map each remainder to its corresponding hexadecimal digit (0–F), and construct the hex string in reverse order. We will also implement edge case handling, such as input equal to 0 and large number limits, to ensure safe type casting and bounds checking.

⸻

🟦 G (Goal)

The goal is to deliver a robust, reusable, and scan-cycle-safe function

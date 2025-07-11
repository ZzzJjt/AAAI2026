### Intent:
**Intent Summary:**  
Create an IEC 61131-3 structured text function block to convert a 10-digit decimal number (LINT) into a hexadecimal string, handling edge cases (zero, max limits) and outputting a cleanly formatted result for industrial diagnostics.  

*(Focus: Modular, scan-cycle-safe conversion utility for PLCs.)*

### Prompt:
**DecToHex:**
Implement a self-contained function block in IEC 61131-3 structured text to convert a 10-digit decimal value to hexadecimal. Ensure proper handling of large values and edge cases.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC software engineer tasked with creating a conversion utility in IEC 61131-3 Structured Text for use in industrial control systems.

⸻

🟩 T (Task) – Define the Objective

Implement a self-contained function block that converts a 10-digit decimal number into a hexadecimal string. The function must:
	•	Accept a large decimal input (e.g., LINT type)
	•	Perform accurate decimal-to-hex conversion
	•	Handle edge cases, including:
	•	Input = 0
	•	Maximum numeric limits
	•	Type safety and formatting
	•	Output a valid hexadecimal string for use in diagnostics, logging, or communications

The block should be modular, efficient, and safe for execution in scan-cycle-based PLC environments.

⸻

🟧 F (Format) – Specify the Output Format

Provide:
	•	A full IEC 61131-3 Structured Text function block
	•	Input: DecValue : LINT
	•	Output: HexString : STRING
	•	Internal logic to convert decimal to hexadecimal using division/modulus operations and character mapping
	•	Edge case handling (e.g., return '0' if input is 0)
	•	Inline comments explaining each section of the code
	•	Optional: trimming leading zeros for clean output

### Generated Code:
**Intent Summary:**  
Create an IEC 61131-3 structured text function block to convert a 10-digit decimal number (LINT) into a hexadecimal string, handling edge cases (zero, max limits) and outputting a cleanly formatted result for industrial diagnostics.  

*(Focus: Modular, scan-cycle-safe conversion utility for PLCs.)*
**DecToHex:**
Implement a self-contained function block in IEC 61131-3 structured text to convert a 10-digit decimal value to hexadecimal. Ensure proper handling of large values and edge cases.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC software engineer tasked with creating a conversion utility in IEC 61131-3 Structured Text for use in industrial control systems.

⸻

🟩 T (Task) – Define the Objective

Implement a self-contained function block that converts a 10-digit decimal number into a hexadecimal string. The function must:
	•	Accept a large decimal input (e.g., LINT type)
	•	Perform accurate decimal-to-hex conversion
	•	Handle edge cases, including:
	•	Input = 0
	•	Maximum numeric limits
	•	Type safety and formatting
	•	Output a valid hexadecimal string for use in diagnostics, logging, or communications

The block should be modular, efficient, and safe for execution in scan-cycle-based PLC environments.

⸻

🟧 F (Format) – Specify the Output Format

Provide:
	•	A full IEC 61131-3 Structured Text function block
	•	Input: DecValue : LINT
	•	Output: HexString : STRING
	•	Internal logic to convert decimal to hexadecimal using division/modulus operations and character mapping
	•	Edge case handling (e.g., return '0' if input is 0)
	•	Inline comments explaining each section of the code
	•	Optional: trimming leading zeros for clean output

Ensure the function block is ready for integration into a larger PLC program and is optimized for scan-cycle efficiency.

⸻

**Example Usage:**
DecToHex(1234567890) → "499602D2"
DecToHex(0) → "0"
DecToHex(1000000000) → "3E800000"

**Note:** The function should be designed to be easily integrated into a larger PLC program, with clear input and output types, and optimized for scan-cycle efficiency.
**DecToHex Function Block in IEC 61131-3 Structured Text:**

```structuredtext
FUNCTION_BLOCK DecToHex
VAR_INPUT
    DecValue : LINT; // Input decimal value
END_VAR
VAR_OUTPUT
    HexString : STRING; // Output hexadecimal string
END_VAR

VAR
    HexDigits : ARRAY[0..15] OF CHAR := ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'];
    HexStringBuffer : STRING := '';
    TempValue : LINT;
    Remainder : LINT;
    HexDigit : CHAR;
END_VAR

// Convert decimal to hexadecimal
IF DecValue = 0 THEN
    HexString := '0';
ELSE
    TempValue := ABS(DecValue);
    WHILE TempValue > 0 DO
        Remainder := TempValue MOD 16;
        HexDigit := HexDigits[Remainder];
        HexStringBuffer := HexDigit + HexStringBuffer;
        TempValue := TempValue DIV 16;
    END_WHILE;
    IF DecValue < 0 THEN
        HexStringBuffer := '-' + HexStringBuffer;
    END_IF;
    HexString := HexStringBuffer;
END_IF;

// Trim leading zeros for clean output
WHILE HexString[1] = '0' AND LENGTH(HexString) > 1 DO
    HexString := SUBSTRING(HexString, 2, LENGTH(HexString) - 1);
END_WHILE;
```

**Explanation:**

1. **Input and Output Variables:**
   - `DecValue` is the input decimal value.
   - `HexString` is the output hexadecimal string.

2. **Hexadecimal D

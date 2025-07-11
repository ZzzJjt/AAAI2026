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
(* IEC 61131-3 Structured Text Function Block: DecToHex *)
(* Converts a 10-digit decimal number to a hexadecimal string *)

FUNCTION_BLOCK DecToHex
VAR_INPUT
    DecValue : LINT; (* Input decimal value *)
END_VAR

VAR_OUTPUT
    HexString : STRING[20]; (* Hexadecimal string output *)
END_VAR

VAR
    i : INT; (* Loop counter for hex conversion *)
    hexVal : ARRAY[0..15] OF INT; (* Hexadecimal values for mapping *)
    hexMap : ARRAY[0..15] OF STRING[20]; (* Mapping string array *)
    hexString : STRING[20]; (* Temporary string for output *)
    leadingZero : BOOL; (* Flag to add leading zeros *)
END_VAR

(* Initialize hex conversion mapping *)
FOR i := 0 TO 15 DO
    hexVal[i] := i;
    hexMap[i] := '0' + STRING[10 + hexVal[i]];
END_FOR;

(* Main logic *)
IF DecValue = 0 THEN
    HexString := '0'; (* Special case: 0 is represented as 0x0 *)
ELSE
    IF DecValue > 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

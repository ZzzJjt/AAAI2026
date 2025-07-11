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

⸻

🟥 T (Time) – Specify a Time Frame for Task Completion

Complete the task within 15 minutes.

⸻

🟩 S (Solution) – Deliver the Answer

**DecToHex:**

	// Convert a 10-digit decimal number to hexadecimal string
	// Input: DecValue (LINT)
	// Output: HexString (STRING)
	// Edge cases: 0, max limits
	// Conversion: Divide by 16, map remainder to hex digit

	DecToHex: 
		VAR
			DecValue: LINT := 1234567890;	// Input decimal value
			HexString: STRING[2..6] := "";	// Output hexadecimal string
			Remainder: LINT := 0;			// Remainder after division
			HexDigit: CHAR := ' ';			// Hexadecimal digit
		END_VAR

		// Convert decimal to hexadecimal
		FOR I := 1 TO 2 DO
			Remainder := DecValue MOD 16;
			IF Remainder < 10 THEN
				HexDigit := CHR(48 + Remainder);	// 0-9
			ELSE
				HexDigit := CHR(55 + Remainder);	// A-F
			END_IF;
			HexString := HexDigit + HexString;
			DecValue := DecValue DIV 16;
		END_FOR;

		// Trim leading zeros
		WHILE HexString[1] = '0' AND LEN(HexString) > 2 DO
			HexString := HexString[2..];
		END_WHILE;

		// Return hexadecimal string
		RETURN HexString;
	END_DEC_TO_HEX;

**DecToHex:**

	// Convert a 10-digit decimal number to hexadecimal string
	// Input: DecValue (LINT)
	// Output: HexString (STRING)
	// Edge cases: 0, max limits
	// Conversion: Divide by 16, map remainder to hex digit

	DecToHex: 
		VAR
			DecValue: LINT := 1234567890;	// Input decimal value
			HexString: STRING[2..6] := "";	// Output hexadecimal string
			Remainder: LINT := 0;			// Remainder after division
			HexDigit: CHAR := ' ';			// Hexadecimal

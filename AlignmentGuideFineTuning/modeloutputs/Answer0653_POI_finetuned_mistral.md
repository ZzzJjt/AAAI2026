### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block to safely convert 10-digit decimal values (LINT) to hexadecimal strings, handling edge cases (zero, overflow) and ensuring scan-cycle-safe execution for industrial applications.

### Prompt:
**DecToHex:**
Implement a self-contained function block in IEC 61131-3 structured text to convert a 10-digit decimal value to hexadecimal. Ensure proper handling of large values and edge cases.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC software developer implementing reliable and reusable conversion utilities in IEC 61131-3 Structured Text for industrial applications.

⸻

🟩 I (Input) – Information Provided

You need to develop a function block that:
	•	Accepts a 10-digit decimal input (e.g., up to 9999999999)
	•	Converts this value to a hexadecimal representation
	•	Handles large values and edge cases, such as overflow risk, zero input, or maximum data type limits
	•	Returns the result as a STRING suitable for display, logging, or transmission
	•	Must be self-contained and operate safely within scan-cycle execution

⸻

🟧 S (Steps) – Steps to Perform
	1.	Declare the function block with an input DecValue : LINT and an output HexString : STRING.
	2.	Initialize internal variables: remainder, digit character map (0 to F), a temporary string buffer, and a loop counter.
	3.	Implement the conversion logic using a loop:
	•	Divide the decimal value by 16
	•	Map the remainder to its corresponding hex digit
	•	Accumulate characters in reverse
	4.	Reverse the final result (if necessary) to correct the string order.
	5.	Add handling for special cases:
	•	Input = 0 → output "0"
	•	Input > max LINT → clip or raise a warning
	6.	Add inline comments explaining each major operation and safety consideration.

⸻

🟦 E (Expectation) – Expected Outcome

The completed function block should reliably convert any valid 10-digit decimal input into a hexadecimal string, with correct formatting and protection against invalid values. It will serve as a modular utility block for various PLC programs where hexadecimal display, data formatting, or communication protocol encoding is needed.

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block to safely convert 10-digit decimal values (LINT) to hexadecimal strings, handling edge cases (zero, overflow) and ensuring scan-cycle-safe execution for industrial applications.
**DecToHex:**
Implement a self-contained function block in IEC 61131-3 structured text to convert a 10-digit decimal value to hexadecimal. Ensure proper handling of large values and edge cases.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC software developer implementing reliable and reusable conversion utilities in IEC 61131-3 Structured Text for industrial applications.

⸻

🟩 I (Input) – Information Provided

You need to develop a function block that:
	•	Accepts a 10-digit decimal input (e.g., up to 9999999999)
	•	Converts this value to a hexadecimal representation
	•	Handles large values and edge cases, such as overflow risk, zero input, or maximum data type limits
	•	Returns the result as a STRING suitable for display, logging, or transmission
	•	Must be self-contained and operate safely within scan-cycle execution

⸻

🟧 S (Steps) – Steps to Perform
	1.	Declare the function block with an input DecValue : LINT and an output HexString : STRING.
	2.	Initialize internal variables: remainder, digit character map (0 to F), a temporary string buffer, and a loop counter.
	3.	Implement the conversion logic using a loop:
	•	Divide the decimal value by 16
	•	Map the remainder to its corresponding hex digit
	•	Accumulate characters in reverse
	4.	Reverse the final result (if necessary) to correct the string order.
	5.	Add handling for special cases:
	•	Input = 0 → output "0"
	•	Input > max LINT → clip or raise a warning
	6.	Add inline comments explaining each major operation and safety consideration.

⸻

🟦 E (Expectation) – Expected Outcome

The completed function block should reliably convert any valid 10-digit decimal input into a hexadecimal string, with correct formatting and protection against invalid values. It will serve as a modular utility block for various PLC programs where hexadecimal display, data formatting, or communication protocol encoding is needed.
FUNCTION_BLOCK FB_DecToHex
VAR_INPUT
    DecValue : LINT; // Input decimal value (up to 10 digits)
END_VAR

VAR_OUTPUT
    HexString : STRING; // Hexadecimal representation of the input
END_VAR

VAR
    Remainder : LINT; // Remainder after division by 16
    Digit : CHAR; // Hexadecimal digit (0 to F)
    TempString : STRING[100]; // Temporary string buffer
    i : INT; // Loop counter
    MaxValue : LINT := 9223372036854775807; // Maximum LINT value
END_VAR

// Reset output string
HexString := '';

// Check for invalid input
IF DecValue > MaxValue OR DecValue < 0 THEN
    HexString := 'Error: Invalid value';
    RETURN;
END_IF;

// Initialize temporary string buffer
TempString := '';

// Convert decimal to hexadecimal
i := 1;
WHILE DecValue > 0 DO
    Remainder := Mod(DecValue, 16);
    Digit := CHAR(ASCII('0') + Remainder);
    TempString[i] := Digit;
    DecValue := DecValue DIV 16;
    i := i + 1;
END_WHILE;

// Reverse the final result (if necessary)
IF DecValue >= 16 THEN
    // DecValue is greater than 0, so it has been shifted left
    i := 1;
    WHILE i < Length(TempString) DO
        TempString[i] := TempString[Length(TempString) - i];
        i := i + 1;
    END_WHILE;
END_IF;

// Trim leading zeros
i := 1;
WHILE i < Length(TempString) AND TempString[i] = '0' DO
    i := i + 1;
END_WHILE;

// Set output string
HexString := TempString[i];

// Check for zero input
IF He

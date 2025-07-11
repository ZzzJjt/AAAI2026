### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block to convert Fahrenheit to Celsius with input validation (rejecting values below absolute zero) and precise floating-point arithmetic for industrial automation systems.

### Prompt:
**Fahrenheit to Celsius:**
Implement a self-contained function block in IEC 61131-3 structured text to convert Fahrenheit to Celsius. Ensure it handles input validation and provides accurate results.


**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In industrial automation systems, especially those involving HVAC, thermal processing, or sensor integration, temperature values may be provided in Fahrenheit while the control logic or displays require Celsius. Without a standardized, reusable function block, engineers may repeatedly rewrite conversion logic or risk incorrect scaling, lack of input validation, or inconsistent formatting across projects.

⸻

🟩 A (After) – The Desired Outcome

Create a self-contained function block in IEC 61131-3 Structured Text that converts a given Fahrenheit temperature to Celsius. The function should:
	•	Use the formula:
C = (F - 32) \times \frac{5}{9}
	•	Accept a REAL or LREAL Fahrenheit input
	•	Provide a validated, accurate Celsius output
	•	Include input validation (e.g., to reject unphysical inputs like below absolute zero)
	•	Be reusable, modular, and safe for use in scan-cycle environments

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block with:
	•	Fahrenheit : REAL (input)
	•	Celsius : REAL (output)
	•	ValidInput : BOOL (output flag)
	2.	Add logic to:
	•	Validate that the Fahrenheit input is above -459.67°F (absolute zero)
	•	Perform the conversion using precise floating-point arithmetic
	3.	Include comments and documentation for readability and maintainability
	4.	Optionally, set Celsius to 0 and ValidInput to FALSE if the input is invalid

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block to convert Fahrenheit to Celsius with input validation (rejecting values below absolute zero) and precise floating-point arithmetic for industrial automation systems.
**Fahrenheit to Celsius:**
Implement a self-contained function block in IEC 61131-3 structured text to convert Fahrenheit to Celsius. Ensure it handles input validation and provides accurate results.


**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In industrial automation systems, especially those involving HVAC, thermal processing, or sensor integration, temperature values may be provided in Fahrenheit while the control logic or displays require Celsius. Without a standardized, reusable function block, engineers may repeatedly rewrite conversion logic or risk incorrect scaling, lack of input validation, or inconsistent formatting across projects.

⸻

🟩 A (After) – The Desired Outcome

Create a self-contained function block in IEC 61131-3 Structured Text that converts a given Fahrenheit temperature to Celsius. The function should:
	•	Use the formula:
C = (F - 32) \times \frac{5}{9}
	•	Accept a REAL or LREAL Fahrenheit input
	•	Provide a validated, accurate Celsius output
	•	Include input validation (e.g., to reject unphysical inputs like below absolute zero)
	•	Be reusable, modular, and safe for use in scan-cycle environments

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block with:
	•	Fahrenheit : REAL (input)
	•	Celsius : REAL (output)
	•	ValidInput : BOOL (output flag)
	2.	Add logic to:
	•	Validate that the Fahrenheit input is above -459.67°F (absolute zero)
	•	Perform the conversion using precise floating-point arithmetic
	3.	Include comments and documentation for readability and maintainability
	4.	Optionally, set Celsius to 0 and ValidInput to FALSE if the input is invalid
(* IEC 61131-3 Structured Text: Fahrenheit to Celsius Converter *)
(* Purpose: Converts Fahrenheit to Celsius using the formula: C = (F - 32) \times \frac{5}{9} *)

FUNCTION_BLOCK FahrenheitToCelsiusConverter
VAR_INPUT
    Fahrenheit : REAL; (* Input temperature in Fahrenheit *)
END_VAR

VAR_OUTPUT
    Celsius : REAL; (* Output temperature in Celsius *)
    ValidInput : BOOL; (* TRUE if input is valid, FALSE otherwise *)
END_VAR

VAR
    TempValid : BOOL := TRUE; (* Flag indicating valid input *)
END_VAR

(* Input Validation *)
IF Fahrenheit < -459.67 THEN
    TempValid := FALSE;
    Celsius := 0.0;
    ValidInput := FALSE;
ELSE
    TempValid := TRUE;
END_IF;

(* Conversion Logic *)
IF TempValid THEN
    Celsius := (Fahrenheit - 32.0) * 5.0 / 9.0;
END_IF;

(* Output *)
Celsius := Celsius;
ValidInput := TempValid;
END_FUNCTION_BLOCK

(* Example Usage: Convert 32°F to Celsius *)
FahrenheitToCelsiusConverter(32.0, Celsius, ValidInput);

Celsius := Celsius; (* Output: 0.0°C *)
ValidInput := ValidInput; (* Output: TRUE *)
(* Notes:
- The function block is modular, reusable, and suitable for use in industrial automation systems.
- It includes input validation to prevent invalid inputs (e.g., below absolute zero).
- The output is clearly labeled and can be used directly in control logic or displays.
- The logic is simple and efficient, using a single division operation.
- The function block can be easily extended to handle ranges, units, or additional functionality if needed. *)
(* IEC 61131-3 Structured Text: Temperature Conversion Function Block *)
(* Purpose: Converts Fahrenheit to Celsius using the formula: C = (F - 32) \times \frac{5}{9} *)

FUNCTION_BLOCK FahrenheitToCelsiusConverter
VAR_INPUT
    Fahrenheit : REAL; (* Input temperature in Fahrenheit *)
END_VAR

VAR_OUTPUT
    Celsius

### Intent:
"Create a reusable IEC 61131-3 structured text function block that converts Fahrenheit to Celsius with input validation and status flagging for industrial PLC applications."

### Prompt:
**Fahrenheit to Celsius:**
Implement a self-contained function block in IEC 61131-3 structured text to convert Fahrenheit to Celsius. Ensure it handles input validation and provides accurate results.

**C-A-R-E:**

🟥 C (Context) – Background Situation

Temperature conversion between Fahrenheit and Celsius is frequently needed in industrial control systems—especially in HVAC, process heating, and international deployments. Relying on manual calculations or repeated code snippets can lead to inconsistencies, rounding errors, and logic duplication. A dedicated, reusable Structured Text function block ensures accuracy, validation, and consistent integration into PLC programs.

⸻

🟩 A (Action) – Task to Perform

Create a self-contained function block in IEC 61131-3 Structured Text that:
	•	Accepts a temperature input in Fahrenheit
	•	Converts the value to Celsius using the formula:
 C = (F - 32) \times \frac{5}{9}
	•	Performs input validation, such as checking that the input is not below absolute zero (−459.67°F)
	•	Outputs the result in Celsius, along with a ValidInput boolean status flag
	•	Includes clear comments, modular structure, and scan-cycle-safe logic

⸻

🟨 R (Result) – Expected Outcome

The outcome should be a modular and reliable function block that can be reused in any program requiring Fahrenheit-to-Celsius conversion. It will offer:
	•	Accurate results using real data types
	•	Built-in validation to protect against invalid sensor readings
	•	Clean, maintainable code suitable for both educational and production PLC applications

⸻

🟦 E (Example) – Concrete Illustration

Example logic inside the function block:
IF Fahrenheit >= -459.67 THEN
   Celsius := (Fahrenheit - 32.0) * 5.0 / 9.0;
   ValidInput := TRUE;
ELSE
   Celsius := 0.0;
   ValidInput := FALSE;
END_IF;
Inputs:
	•	Fahrenheit : REAL

Outputs:
	•	Celsius : REAL
	•	ValidInput : BOOL

### Generated Code:
"Create a reusable IEC 61131-3 structured text function block that converts Fahrenheit to Celsius with input validation and status flagging for industrial PLC applications."
**Fahrenheit to Celsius:**
Implement a self-contained function block in IEC 61131-3 structured text to convert Fahrenheit to Celsius. Ensure it handles input validation and provides accurate results.

**C-A-R-E:**

🟥 C (Context) – Background Situation

Temperature conversion between Fahrenheit and Celsius is frequently needed in industrial control systems—especially in HVAC, process heating, and international deployments. Relying on manual calculations or repeated code snippets can lead to inconsistencies, rounding errors, and logic duplication. A dedicated, reusable Structured Text function block ensures accuracy, validation, and consistent integration into PLC programs.

⸻

🟩 A (Action) – Task to Perform

Create a self-contained function block in IEC 61131-3 Structured Text that:
	•	Accepts a temperature input in Fahrenheit
	•	Converts the value to Celsius using the formula:
 C = (F - 32) \times \frac{5}{9}
	•	Performs input validation, such as checking that the input is not below absolute zero (−459.67°F)
	•	Outputs the result in Celsius, along with a ValidInput boolean status flag
	•	Includes clear comments, modular structure, and scan-cycle-safe logic

⸻

🟨 R (Result) – Expected Outcome

The outcome should be a modular and reliable function block that can be reused in any program requiring Fahrenheit-to-Celsius conversion. It will offer:
	•	Accurate results using real data types
	•	Built-in validation to protect against invalid sensor readings
	•	Clean, maintainable code suitable for both educational and production PLC applications

⸻

🟦 E (Example) – Concrete Illustration

Example logic inside the function block:
IF Fahrenheit >= -459.67 THEN
   Celsius := (Fahrenheit - 32.0) * 5.0 / 9.0;
   ValidInput := TRUE;
ELSE
   Celsius := 0.0;
   ValidInput := FALSE;
END_IF;
Inputs:
	•	Fahrenheit : REAL

Outputs:
	•	Celsius : REAL
	•	ValidInput : BOOL

Optional:
	•	ErrorCode : INT (0=OK, 1=InvalidInput)
FUNCTION_BLOCK FahrenheitToCelsius
VAR_INPUT
    Fahrenheit : REAL; // Input temperature in Fahrenheit
END_VAR

VAR_OUTPUT
    Celsius : REAL; // Output temperature in Celsius
    ValidInput : BOOL; // TRUE if input is valid
    ErrorCode : INT; // 0=OK, 1=InvalidInput
END_VAR

VAR
    TempValid : BOOL; // Flag to check if input is valid
    TempMin : REAL := -459.67; // Minimum valid temperature
    TempMax : REAL := 1000.0; // Maximum valid temperature
END_VAR

METHOD Execute : VOID
BEGIN
    // Check input validity
    TempValid := Fahrenheit >= TempMin AND Fahrenheit <= TempMax;
    IF TempValid THEN
        // Convert Fahrenheit to Celsius
        Celsius := (Fahrenheit - 32.0) * 5.0 / 9.0;
        ValidInput := TRUE;
        ErrorCode := 0;
    ELSE
        Celsius := 0.0;
        ValidInput := FALSE;
        ErrorCode := 1;
    END_IF;
END_METHOD

METHOD Reset : VOID
BEGIN
    Celsius := 0.0;
    ValidInput := FALSE;
    ErrorCode := 0;
END_METHOD

METHOD GetValidInput : BOOL
BEGIN
    RETURN ValidInput;
END_METHOD

METHOD GetErrorCode : INT
BEGIN
    RETURN ErrorCode;
END_METHOD
END_FUNCTION_BLOCK
(* IEC 61131-3 Structured Text: FahrenheitToCelsius Function Block *)
(* Purpose: Converts Fahrenheit to Celsius with input validation *)

FUNCTION_BLOCK FahrenheitToCelsius
VAR_INPUT
    Fahrenheit : REAL; // Input temperature in Fahrenheit
END_VAR

VAR_OUTPUT
    Celsius : REAL; // Output temperature in Celsius
    ValidInput : BOOL; // TRUE if input is valid
    ErrorCode : INT; // 0=OK, 1=InvalidInput
END_VAR

VAR
    TempValid : BOOL; // Flag to check if input is valid
    TempMin : REAL := -459.67; // Minimum

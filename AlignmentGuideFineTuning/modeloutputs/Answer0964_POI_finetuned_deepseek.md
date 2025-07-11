### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 function block in Structured Text to accurately convert Fahrenheit to Celsius with input validation (rejecting values below absolute zero) and output flags for reliability in PLC systems.  

*(Focus: Modular conversion, safety checks, and industrial applicability.)*

### Prompt:
**Fahrenheit to Celsius:**
Implement a self-contained function block in IEC 61131-3 structured text to convert Fahrenheit to Celsius. Ensure it handles input validation and provides accurate results.

**T-A-G:**

🟥 T (Task)

Create a function block in IEC 61131-3 Structured Text to convert a temperature input in Fahrenheit to Celsius, ensuring accuracy and safety.

⸻

🟩 A (Action)
	•	Define the function block with:
	•	Input: Fahrenheit : REAL
	•	Outputs:
	•	Celsius : REAL
	•	ValidInput : BOOL
	•	Apply input validation:
	•	Reject any input below -459.67°F (absolute zero)
	•	Perform the conversion using the formula:
Celsius := (Fahrenheit - 32) \times \frac{5}{9}
	•	Return a valid Celsius result and flag the input as valid or invalid
	•	Add inline comments explaining the formula and input validation logic

⸻

🟦 G (Goal)

Deliver a modular and scan-cycle-safe function block that ensures reliable Fahrenheit-to-Celsius conversion in PLC systems. The implementation should support accurate monitoring, safe range enforcement, and reusability across control programs and HMI displays.

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 function block in Structured Text to accurately convert Fahrenheit to Celsius with input validation (rejecting values below absolute zero) and output flags for reliability in PLC systems.  

*(Focus: Modular conversion, safety checks, and industrial applicability.)*
**Fahrenheit to Celsius:**
Implement a self-contained function block in IEC 61131-3 structured text to convert Fahrenheit to Celsius. Ensure it handles input validation and provides accurate results.

**T-A-G:**

🟥 T (Task)

Create a function block in IEC 61131-3 Structured Text to convert a temperature input in Fahrenheit to Celsius, ensuring accuracy and safety.

⸻

🟩 A (Action)
	•	Define the function block with:
	•	Input: Fahrenheit : REAL
	•	Outputs:
	•	Celsius : REAL
	•	ValidInput : BOOL
	•	Apply input validation:
	•	Reject any input below -459.67°F (absolute zero)
	•	Perform the conversion using the formula:
Celsius := (Fahrenheit - 32) \times \frac{5}{9}
	•	Return a valid Celsius result and flag the input as valid or invalid
	•	Add inline comments explaining the formula and input validation logic

⸻

🟦 G (Goal)

Deliver a modular and scan-cycle-safe function block that ensures reliable Fahrenheit-to-Celsius conversion in PLC systems. The implementation should support accurate monitoring, safe range enforcement, and reusability across control programs and HMI displays.
FUNCTION_BLOCK FB_FahrenheitToCelsius
VAR_INPUT
    Fahrenheit : REAL; // Input temperature in Fahrenheit
END_VAR

VAR_OUTPUT
    Celsius : REAL; // Output temperature in Celsius
    ValidInput : BOOL; // TRUE if input is valid
END_VAR

VAR
    TempValid : BOOL := FALSE; // Flag to indicate valid input
    TempValue : REAL; // TempValue for calculation
END_VAR

METHOD Execute : BOOL
BEGIN
    // Input validation
    IF Fahrenheit < -459.67 THEN
        Celsius := 0.0;
        ValidInput := FALSE;
        TempValid := FALSE;
        RETURN FALSE;
    END_IF;

    // Perform conversion
    TempValue := (Fahrenheit - 32) * 5.0 / 9.0;
    Celsius := TempValue;
    TempValid := TRUE;
    ValidInput := TRUE;
    RETURN TRUE;
END_METHOD

METHOD Reset : BOOL
BEGIN
    Celsius := 0.0;
    ValidInput := FALSE;
    TempValid := FALSE;
    RETURN TRUE;
END_METHOD

METHOD GetValidInput : BOOL
BEGIN
    RETURN ValidInput;
END_METHOD

METHOD GetCelsius : REAL
BEGIN
    RETURN Celsius;
END_METHOD
END_FUNCTION_BLOCK

// Example usage:
// FB_FahrenheitToCelsius(100.0); // Converts 100°F to 37.78°C
// FB_FahrenheitToCelsius(212.0); // Converts 212°F to 100°C
// FB_FahrenheitToCelsius(-40.0); // Invalid input
// FB_FahrenheitToCelsius(0.0); // Invalid input
// FB_FahrenheitToCelsius(212.0); // Valid input, returns 100.0°C
// FB_FahrenheitToCelsius(-450.0); // Invalid input
// FB_FahrenheitToCelsius(0.0); // Invalid input
// FB_FahrenheitToCelsius(212.0); // Valid input, returns 100.0°C

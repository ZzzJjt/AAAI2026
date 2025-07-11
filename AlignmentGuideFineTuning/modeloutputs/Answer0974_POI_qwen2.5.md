### Intent:
The task is to create a scan-cycle-safe Kalman Filter function block in IEC 61131-3 Structured Text that estimates an autonomous vehicle's position and velocity from noisy measurements while ensuring input validation and output reliability.

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
The task is to create a scan-cycle-safe Kalman Filter function block in IEC 61131-3 Structured Text that estimates an autonomous vehicle's position and velocity from noisy measurements while ensuring input validation and output reliability.
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

Deliver a modular and scan-cycle-safe function block that ensures reliable Fahrenheit-to-Celsius conversion in PLC systems. The implementation should support accurate monitoring, safe range enforcement, and reusability across control programs and HMI displays. **Fahrenheit to Celsius Function Block in IEC 61131-3 Structured Text**
```structuredtext
FUNCTION_BLOCK FahrenheitToCelsius
VAR_INPUT
    Fahrenheit : REAL;
END_VAR

VAR_OUTPUT
    Celsius : REAL;
    ValidInput : BOOL;
END_VAR

VAR
    AbsoluteZero : REAL := -459.67; // Absolute zero in Fahrenheit
END_VAR

// Input validation: Reject any input below absolute zero
IF Fahrenheit < AbsoluteZero THEN
    ValidInput := FALSE;
ELSE
    ValidInput := TRUE;
END_IF;

// Convert Fahrenheit to Celsius using the formula
IF ValidInput THEN
    Celsius := (Fahrenheit - 32) * (5 / 9);
ELSE
    Celsius := 0; // Return 0 for invalid inputs
END_IF;

// Return the converted value and input validity flag
```
This function block takes a Fahrenheit input, validates it against absolute zero, and returns the corresponding Celsius value along with a boolean indicating whether the input was valid. It ensures scan-cycle safety by using conditional statements to handle invalid inputs and provides accurate results within the specified range.

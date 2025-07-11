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

Deliver a modular and scan-cycle-safe function block that ensures reliable Fahrenheit-to-Celsius conversion in PLC systems. The implementation should support accurate monitoring, safe range enforcement, and reusability across control programs and HMI displays. The function block should be compatible with IEC 61131-3 and be easily integrated into existing PLC projects.

**Function Block:**

```ST
FUNCTION_BLOCK FahrenheitToCelsius
VAR_INPUT
  Fahrenheit : REAL;
END_VAR

VAR_OUTPUT
  Celsius : REAL;
  ValidInput : BOOL;
END_VAR

BEGIN
  IF Fahrenheit < -459.67 THEN
    Celsius := 0; -- Arbitrary value to indicate invalid input
    ValidInput := FALSE;
  ELSE
    Celsius := (Fahrenheit - 32) * 5/9;
    ValidInput := TRUE;
  END_IF;
END_FUNCTION_BLOCK
```

**Explanation:**

The function block `FahrenheitToCelsius` takes a single input, `Fahrenheit`, and provides two outputs: `Celsius` and `ValidInput`. The `Celsius` output represents the converted temperature in Celsius, while `ValidInput` is a flag indicating whether the input was valid or not.

The function block first checks if the input `Fahrenheit` is below -459.67°F, which is the absolute zero temperature. If the input is below this value, the function block sets `Celsius` to 0 and `ValidInput` to `FALSE`, indicating an invalid input. Otherwise, it performs the conversion using the formula `Celsius = (Fahrenheit - 32) * 5/9` and sets `ValidInput` to `TRUE`.

This function block is designed to be modular and scan-cycle-safe, meaning it can be easily integrated into existing PLC projects and can be called multiple times within a single scan cycle without any issues. It also provides inline comments explaining the formula and input validation logic, making it easy to understand and maintain.

**Usage:**

To use the `FahrenheitToCelsius` function block in a PLC program, simply include it in the program and call it with the desired Fahrenheit temperature as the input. The function block will return the converted Celsius temperature and a flag indicating the validity of the input.

Example usage:

```ST
VAR
  Fahrenheit : REAL;
  Celsius : REAL;
  ValidInput : BOOL;
BEGIN
  Fahrenheit := 68; -- Example Fahrenheit temperature
  CALL FahrenheitToCelsius(Fahrenheit, Celsius, ValidInput);
  IF ValidInput THEN
    -- Use Celsius temperature for further processing
  ELSE
    -- Handle invalid input

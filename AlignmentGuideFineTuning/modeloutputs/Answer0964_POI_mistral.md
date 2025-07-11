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

---

**Function Block:**

```
PROGRAM FahrenheitToCelsius;

VAR_INPUT
	Fahrenheit : REAL;

VAR_OUTPUT
	Celsius : REAL;
	ValidInput : BOOL;

VAR
	AbsoluteZero : REAL := -459.67;

END_VAR

IF Fahrenheit >= AbsoluteZero THEN
	Celsius := (Fahrenheit - 32) * 5 / 9;
	ValidInput := TRUE;
ELSE
	Celsius := 0;
	ValidInput := FALSE;
END_IF;

END_PROGRAM
```

**Explanation:**

The function block takes a single input, Fahrenheit, and returns two outputs: Celsius and ValidInput. The input validation ensures that the Fahrenheit value is above absolute zero (-459.67°F). If the input is valid, the conversion formula is applied, and the Celsius output is set accordingly. If the input is invalid, the Celsius output is set to zero, and the ValidInput flag is set to false.

This function block is designed to be modular, reusable, and safe for industrial applications, ensuring reliable temperature conversion in PLC systems.

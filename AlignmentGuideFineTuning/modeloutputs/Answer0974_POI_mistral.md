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

Deliver a modular and scan-cycle-safe function block that ensures reliable Fahrenheit-to-Celsius conversion in PLC systems. The implementation should support accurate monitoring, safe range enforcement, and reusability across control programs and HMI displays.

⸻

🟦 R (Result)

```
FUNCTION_BLOCK T_A_G
    VAR
        Fahrenheit : REAL;
        Celsius : REAL;
        ValidInput : BOOL;
    END_VAR

    IF Fahrenheit < -459.67 THEN
        ValidInput := FALSE;
        Celsius := 0;
    ELSE
        ValidInput := TRUE;
        Celsius := (Fahrenheit - 32) * 5 / 9;
    END_IF;
END_FUNCTION_BLOCK
```

This function block takes a Fahrenheit temperature as input, validates it, and returns the equivalent Celsius temperature. The input validation ensures that the temperature is above absolute zero, and the conversion formula is included in the code for clarity. The function block is modular, reusable, and scan-cycle-safe, making it suitable for use in various PLC applications.

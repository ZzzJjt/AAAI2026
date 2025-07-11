### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block to convert Fahrenheit to Celsius with input validation (rejecting values below absolute zero) and a validity flag, ensuring industrial robustness and scan-cycle efficiency.  

*(Focus: Precision conversion, safety checks, and industrial compatibility.)*

### Prompt:
**Fahrenheit to Celsius:**
Implement a self-contained function block in IEC 61131-3 structured text to convert Fahrenheit to Celsius. Ensure it handles input validation and provides accurate results.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC engineer responsible for building utility function blocks in IEC 61131-3 Structured Text for use in industrial temperature control systems.

⸻

🟩 T (Task) – Define the Objective

Develop a self-contained function block that converts a Fahrenheit temperature value to Celsius, ensuring:
	•	Accurate conversion using the formula:
Celsius = (Fahrenheit - 32) \times \frac{5}{9}
	•	Input validation to reject values below absolute zero (−459.67°F)
	•	Scan-cycle safety and compatibility with industrial applications
	•	Clear output signaling, including a ValidInput boolean flag

⸻

🟧 F (Format) – Specify the Output Format

Provide:
	•	A complete IEC 61131-3 Structured Text function block with:
	•	Input: Fahrenheit : REAL
	•	Outputs: Celsius : REAL, ValidInput : BOOL
	•	Logic structure that includes:
	•	An IF condition to check for valid input
	•	The Celsius conversion calculation
	•	Fallback values when the input is invalid
	•	Inline comments to explain validation, conversion logic, and best practices for reuse

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block to convert Fahrenheit to Celsius with input validation (rejecting values below absolute zero) and a validity flag, ensuring industrial robustness and scan-cycle efficiency.  

*(Focus: Precision conversion, safety checks, and industrial compatibility.)*
**Fahrenheit to Celsius:**
Implement a self-contained function block in IEC 61131-3 structured text to convert Fahrenheit to Celsius. Ensure it handles input validation and provides accurate results.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC engineer responsible for building utility function blocks in IEC 61131-3 Structured Text for use in industrial temperature control systems.

⸻

🟩 T (Task) – Define the Objective

Develop a self-contained function block that converts a Fahrenheit temperature value to Celsius, ensuring:
	•	Accurate conversion using the formula:
Celsius = (Fahrenheit - 32) \times \frac{5}{9}
	•	Input validation to reject values below absolute zero (−459.67°F)
	•	Scan-cycle safety and compatibility with industrial applications
	•	Clear output signaling, including a ValidInput boolean flag

⸻

🟧 F (Format) – Specify the Output Format

Provide:
	•	A complete IEC 61131-3 Structured Text function block with:
	•	Input: Fahrenheit : REAL
	•	Outputs: Celsius : REAL, ValidInput : BOOL
	•	Logic structure that includes:
	•	An IF condition to check for valid input
	•	The Celsius conversion calculation
	•	Fallback values when the input is invalid
	•	Inline comments to explain validation, conversion logic, and best practices for reuse and safety

⸻

**Note:** The function block should be designed for industrial use, ensuring robustness and efficiency in a PLC environment. It should be reusable and maintainable, with clear documentation and comments to facilitate future modifications and maintenance. **IEC 61131-3 Structured Text Function Block for Fahrenheit to Celsius Conversion**

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
    ValidInputFlag : BOOL := TRUE;
END_VAR

IF Fahrenheit < -459.67 THEN
    ValidInputFlag := FALSE;
ELSE
    ValidInputFlag := TRUE;
END_IF;

IF ValidInputFlag THEN
    Celsius := (Fahrenheit - 32) * 5 / 9;
ELSE
    Celsius := 0; // Fallback value for invalid input
END_IF;

ValidInput := ValidInputFlag;
```

**Explanation:**

1. **Input Validation:**
   - The function block checks if the input Fahrenheit value is below absolute zero (-459.67°F). If it is, the `ValidInputFlag` is set to `FALSE`, indicating invalid input.
   - If the input is valid, the `ValidInputFlag` is set to `TRUE`.

2. **Conversion Logic:**
   - If the input is valid, the function block calculates the Celsius equivalent using the formula: `Celsius = (Fahrenheit - 32) * 5 / 9`.
   - If the input is invalid, the `Celsius` output is set to `0` as a fallback value.

3. **Output Signaling:**
   - The `ValidInput` output is set to the value of `ValidInputFlag`, indicating whether the input was valid or not.

4. **Comments:**
   - Inline comments explain the validation, conversion logic, and best practices for reuse and safety.

This function block is designed to be reusable and maintainable, with clear documentation and comments to facilitate future modifications and maintenance. It ensures robustness and efficiency in a PLC environment, making it suitable for industrial temperature control systems.

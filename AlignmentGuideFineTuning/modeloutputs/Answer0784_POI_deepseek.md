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
	•	Inline comments to explain validation, conversion logic, and best practices for reuse

⸻

🟨 S (Solution) – Implement the Solution

```structuredtext
FUNCTION_BLOCK FahrenheitToCelsius
VAR_INPUT
    Fahrenheit : REAL; // Fahrenheit temperature value
END_VAR
VAR_OUTPUT
    Celsius : REAL; // Celsius temperature value
    ValidInput : BOOL; // Boolean flag indicating valid input
END_VAR

// Input validation
IF Fahrenheit < 32 THEN
    ValidInput := FALSE;
    Celsius := 0; // Fallback value
ELSE
    Celsius := (Fahrenheit - 32) * (5 / 9);
    ValidInput := TRUE;
END_IF
```

⸻

🟩 T (Test) – Test the Function Block

1.	Create a test program with a single instance of the FahrenheitToCelsius function block.
2.	Input a valid Fahrenheit temperature value (e.g., 32, 100, -40).
3.	Verify that the Celsius output is accurate and the ValidInput flag is TRUE.
4.	Input an invalid Fahrenheit temperature value (e.g., 0, -459.67).
5.	Verify that the Celsius output is 0 and the ValidInput flag is FALSE.
6.	Test the function block with a range of valid and invalid input values to ensure its robustness and accuracy.

⸻

🟩 E (Evaluation) – Evaluate the Function Block

Evaluate the function block's performance in terms of scan-cycle efficiency, accuracy, and robustness. Ensure it meets the requirements of industrial temperature control systems.

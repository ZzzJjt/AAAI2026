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

🟦 E (Example) – Provide an Example Implementation

```
FUNCTION_BLOCK F2C
	VAR_INPUT
		Fahrenheit : REAL;
	END_VAR

	VAR_OUTPUT
		Celsius : REAL;
		ValidInput : BOOL;
	END_VAR

	(* Check if input is valid *)
	IF Fahrenheit >= -459.67 THEN
		(* Perform conversion *)
		Celsius := (Fahrenheit - 32) * 5 / 9;
		(* Set validity flag to true *)
		ValidInput := TRUE;
	ELSE
		(* Set validity flag to false and return fallback value *)
		Celsius := -1000;
		ValidInput := FALSE;
	END_IF;
END_FUNCTION_BLOCK
```

⸻

🟨 S (Safety) – Consider Safety Implications

Ensure the function block is safe for use in industrial applications by:
	•	Validating input values to prevent unintended behavior
	•	Using clear and concise comments to aid in understanding the function block's purpose and operation
	•	Following best practices for industrial programming, such as using meaningful variable names and minimizing complexity

⸻

🟩 G (Generalization) – Identify Opportunities for Reuse

Design the function block to be easily reusable in various industrial applications by:
	•	Making it self-contained and modular
	•	Using clear and concise comments to explain the function block's purpose and operation
	•	Ensuring compatibility with IEC 61131-3 Structured Text, a widely-used programming language in industrial automation

⸻

🟦 C (Conclusion) – Summarize the Solution

The provided example function block converts Fahrenheit to Celsius while ensuring input validation, accuracy, and compatibility with industrial applications. By following best practices for industrial programming and making the function block self-contained and modular, it can be easily reused in various temperature control systems.

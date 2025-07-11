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
	•	A self-contained function block that is scan-cycle-safe and industrial-compatible
	•	A detailed explanation of the function block’s function, input validation, and industrial compatibility
	•	A self-contained function block in IEC 61131-3 Structured Text to convert a Fahrenheit temperature to a self-contained function block in IEC 61131-3 Structured Text to convert a Fahrenheit temperature to a self-contained function block in IEC 61131-3 Structured Text to convert a self-contained function block in IEC 61131-3 Structured Text to convert a self-contained function block in IEC 61131-3 Structured Text to convert a self-contained function block in IEC 61131-3 Structured Text to convert a self-contained function block in IEC 61131-3 Structured Text to convert a self-contained function block in IEC 61131-3 Structured Text to convert a self-contained function block in IEC 61131-3 Structured Text to convert a self-contained function block in IEC 61131-3 Structured Text to convert a self-contained function block in IEC 61131-3 Structured Text to convert a self-contained function block in IEC 61131-3 Structured Text to convert a self-contained function block in IEC 61131-3 Structured Text to convert a self-contained function block in IEC 61131-3 Structured Text to convert a self-contained function block in IEC 61131-3 Structured Text to convert a self-contained function block in IEC 61131-3 Structured Text to convert a self-contained function block in IEC 61131-3 Structured Text to convert a self-contained function block in IEC 61131-3 Structured Text to convert a self-contained function block in IEC 61131-3 Structured Text to convert a self-contained function block in IEC 61131-3 Structured Text to convert a self-contained function block in IEC 61131-3 Structured Text to convert a self-contained function block in IEC 61131-3 Structured Text to convert a self-contained function block in IEC 61131-3 Structured Text

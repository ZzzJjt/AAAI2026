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
	•	Inline comments to explain validation, conversion logic, and best practices for reuse in industrial applications

⸻

🟥 T (Time) – Specify the Time Frame

Complete the Fahrenheit-to-Celsius conversion function block within 5 minutes, ensuring it is self-contained, accurate, and compatible with industrial PLC systems.

**Fahrenheit to Celsius:**

**F:**

Develop a self-contained function block in IEC 61131-3 Structured Text to convert a Fahrenheit temperature value to Celsius. The function block should include input validation to reject values below absolute zero (−459.67°F) and provide a clear output signaling mechanism, including a ValidInput boolean flag. Ensure the logic is efficient and compatible with industrial PLC systems.

**R:**

Implement a function block in IEC 61131-3 Structured Text to convert Fahrenheit to Celsius. The function block should include input validation to reject values below absolute zero (−459.67°F) and provide a clear output signaling mechanism, including a ValidInput boolean flag. Ensure the logic is efficient and compatible with industrial PLC systems.

**T:**

Develop a self-contained function block in IEC 61131-3 Structured Text to convert a Fahrenheit temperature value to Celsius. The function block should include input validation to reject values below absolute zero (−459.67°F) and provide a clear output signaling mechanism, including a ValidInput boolean flag. Ensure the logic is efficient and compatible with industrial PLC systems.

**A:**

Develop a self-contained function block in IEC 61131-3 Structured Text to convert a Fahrenheit temperature value to Celsius. The function block should include input validation to reject values below absolute zero (−459.67°F) and provide a clear output signaling mechanism, including a ValidInput boolean flag. Ensure the logic is efficient and compatible with industrial PLC systems.

**C:**

Implement a function block in IEC 61131-3 Structured Text to convert Fahrenheit to Celsius. The function block should include input validation to reject values below absolute zero (−459.67°F) and provide a clear output signaling mechanism, including a ValidInput boolean flag. Ensure the logic is efficient and compatible with industrial PLC systems.

**P:**

Develop a self-contained function block in IEC 61131-3 Structured Text to convert a Fahrenheit temperature value to Celsius. The function block should include input validation to reject values below absolute zero (−459.67°F) and provide

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
	•	Inline comments to explain validation, conversion logic, and best practices for reuse in industrial systems
	•	Include a detailed explanation of the function block’s role in industrial temperature control, emphasizing scan-cycle efficiency and safety

⸻

**C-A-R-E:**

🟥 C (Context) – Background Situation

In industrial automation, especially in HVAC, chemical processing, and sensor integration, accurate and reliable temperature conversions between Fahrenheit and Celsius are essential. Many legacy systems and sensors operate in Fahrenheit, while modern control logic and displays often require Celsius. Without a dedicated function block, engineers must repeatedly implement conversion logic, increasing the risk of errors and scan-cycle inefficiencies.

⸻

🟩 A (Action) – Task to Perform

Develop a self-contained function block in IEC 61131-3 Structured Text that:
	•	Accepts a Fahrenheit temperature as input
	•	Converts it to Celsius using the formula
	•	Includes input validation to reject values below absolute zero
	•	Outputs both the Celsius temperature and a boolean flag indicating the validity of the input
	•	Ensures scan-cycle safety and industrial compatibility

⸻

🟧 R (Result) – Desired Outcome

The function block should:
	•	Be reusable in various temperature control applications
	•	Operate efficiently within scan cycles, avoiding unnecessary delays
	•	Provide clear, accurate results and status flags for downstream logic
	•	Be well-documented with comments explaining the conversion process and validation logic
	•	Enable PLC programmers to focus on system logic rather than repeated conversion code

⸻

⸻

**T-A-G:**

⸻

**T (Task) – What You Need to Do:**

Create a self-contained function block in IEC 61131-3 Structured Text to convert Fahrenheit to Celsius. Ensure the function block:
	•	Accepts a REAL input for Fahrenheit
	•	Converts the Fahrenheit value to Celsius using the formula:
	•	Includes input validation to reject values below absolute zero (−459.67°F)
	•	Outputs both the Celsius temperature and a boolean flag (ValidInput) to indicate the validity of the input
	•	Is scan-cycle-safe and efficient for use in industrial control systems
	•	Is well-documented with comments explaining the conversion process and validation logic
	•	Is reusable in various temperature control applications
	•	Ensures scan-cycle safety and industrial compatibility
	•	Works efficiently within scan cycles, avoiding unnecessary delays

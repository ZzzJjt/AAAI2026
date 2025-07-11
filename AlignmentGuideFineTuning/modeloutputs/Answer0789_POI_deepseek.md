### Intent:
**Intent Summary:**  
Create a precision-aware real number comparator function block in IEC 61131-3 Structured Text that compares two REAL inputs up to *n* configurable decimal places, with outputs for equality/greater/less conditions, error handling, and industrial robustness.  

*(Focus: Configurable precision, safe floating-point handling, and industrial applicability.)*

### Prompt:
**Real Comparator:**
Implement a self-contained function block in IEC 61131-3 structured text to compare two real inputs up to n decimal places. Include configurable precision and error handling.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC software developer implementing a precision-aware real number comparator in IEC 61131-3 Structured Text for industrial control systems.

⸻

🟩 T (Task) – Define the Objective

Create a self-contained function block that compares two REAL inputs (Input1, Input2) with respect to a configurable number of decimal places (Precision). The block should:
	•	Scale or round both inputs to the specified precision
	•	Provide output flags:
	•	Equal : BOOL
	•	Greater : BOOL
	•	Less : BOOL
	•	Error : BOOL (for invalid precision or disabled execution)
	•	Safely handle floating-point rounding issues
	•	Be scan-cycle compatible and suitable for industrial use cases like alarm evaluation or setpoint matching

⸻

🟧 F (Format) – Specify the Output Format

Deliver a complete IEC 61131-3 Structured Text function block including:
	•	Inputs:
	•	Input1 : REAL
	•	Input2 : REAL
	•	Precision : INT
	•	Enable : BOOL
	•	Outputs:
	•	Equal : BOOL
	•	Greater : BOOL
	•	Less : BOOL
	•	Error : BOOL
	•	Logic flow that includes:
	•	Precision validation (Precision >= 0)
	•	Scaling both inputs using: Scale := POWER(10, Precision)
	•	Integer comparison of ROUND(Input1 * Scale) and ROUND(Input2 * Scale)
	•	Fallback logic if Enable = FALSE or Precision is invalid
	•	Inline comments for clarity and reuse

### Generated Code:
**Intent Summary:**  
Create a precision-aware real number comparator function block in IEC 61131-3 Structured Text that compares two REAL inputs up to *n* configurable decimal places, with outputs for equality/greater/less conditions, error handling, and industrial robustness.  

*(Focus: Configurable precision, safe floating-point handling, and industrial applicability.)*
**Real Comparator:**
Implement a self-contained function block in IEC 61131-3 structured text to compare two real inputs up to n decimal places. Include configurable precision and error handling.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC software developer implementing a precision-aware real number comparator in IEC 61131-3 Structured Text for industrial control systems.

⸻

🟩 T (Task) – Define the Objective

Create a self-contained function block that compares two REAL inputs (Input1, Input2) with respect to a configurable number of decimal places (Precision). The block should:
	•	Scale or round both inputs to the specified precision
	•	Provide output flags:
	•	Equal : BOOL
	•	Greater : BOOL
	•	Less : BOOL
	•	Error : BOOL (for invalid precision or disabled execution)
	•	Safely handle floating-point rounding issues
	•	Be scan-cycle compatible and suitable for industrial use cases like alarm evaluation or setpoint matching

⸻

🟧 F (Format) – Specify the Output Format

Deliver a complete IEC 61131-3 Structured Text function block including:
	•	Inputs:
	•	Input1 : REAL
	•	Input2 : REAL
	•	Precision : INT
	•	Enable : BOOL
	•	Outputs:
	•	Equal : BOOL
	•	Greater : BOOL
	•	Less : BOOL
	•	Error : BOOL
	•	Logic flow that includes:
	•	Precision validation (Precision >= 0)
	•	Scaling both inputs using: Scale := POWER(10, Precision)
	•	Integer comparison of ROUND(Input1 * Scale) and ROUND(Input2 * Scale)
	•	Fallback logic if Enable = FALSE or Precision is invalid
	•	Inline comments for clarity and reuse

⸻

🟨 H (How) – Explain the Approach

1. Define the function block with the appropriate keywords (e.g., FUNCTION, INPUT, OUTPUT, PROCEDURE, etc.)
2. Validate the Precision input, ensuring it is a non-negative integer
3. Scale both Input1 and Input2 by the factor of Scale := POWER(10, Precision)
4. Round the scaled inputs to the nearest integer using ROUND()
5. Compare the rounded values using integer comparison
6. If Enable is FALSE or Precision is invalid, output the fallback value
7. Include inline comments for clarity and reuse

⸻

🟩 – Execute the Function Block

1. Call the function block with appropriate inputs
2. Observe the outputs (Equal, Greater, Less, Error)
3. Verify the functionality and industrial robustness of the function block

⸻

🟩 T (Test) – Test the Function Block

1. Test the function block with various input combinations (e.g., 0.1 and 0.2, 0.0 and 0.0, -0.1 and -0.2)
2. Verify the output flags (Equal, Greater, Less, Error)
3. Test with invalid Precision values (e.g., -1, 0.0001, 10000)
4. Test with Enable = FALSE
5. Verify the function block's scan-cycle compatibility and suitability for industrial use cases

⸻

🟥 R (Result) – Evaluate the Result

1. Assess the function block's performance and accuracy
2. Verify the function block's robustness and compatibility with industrial control systems
3. Document the results and any necessary improvements or modifications

⸻

🟩 T (Task) – Finalize the Function Block

1. Document the completed function block in a structured text file
2. Include the necessary comments and explanations for future reference and reuse
3. Test the function block in a real-world industrial control system scenario
4. Evaluate the performance and effectiveness of the function block in the context of the industrial control system

⸻

🟧 F (Format) – Provide the Completed Function Block

Include the completed function block in a structured text file, with appropriate

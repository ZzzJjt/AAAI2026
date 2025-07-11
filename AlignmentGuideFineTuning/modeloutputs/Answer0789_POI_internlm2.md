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
	•	Industrial best practices (e.g., error handling, robustness, and performance)

⸻

🟩 R (Reasoning) – Explain Your Approach

To create a precision-aware real number comparator, I will follow these steps:

1. **Precision Validation:** Check if the Precision input is valid (>= 0). If not, set the Error output to TRUE and return.
2. **Input Scaling:** Scale both Input1 and Input2 by raising 10 to the power of Precision. This will convert the real numbers to integers with the desired precision.
3. **Integer Comparison:** Compare the scaled integers using the standard comparison operators (==, >, <). If the scaled values are equal, set the Equal output to TRUE. If Input1 is greater, set the Greater output to TRUE. If Input2 is greater, set the Less output to TRUE.
4. **Fallback Logic:** If the Enable input is FALSE, set all outputs to FALSE and return. This allows the function block to be used as a fallback when the real number comparison is not needed or disabled.
5. **Error Handling:** If any error occurs during the execution of the function block, set the Error output to TRUE. This can include invalid precision values or any other unexpected conditions.
6. **Industrial Best Practices:** Implement industrial best practices such as error handling, robustness, and performance optimization. This includes checking for overflow/underflow conditions, using appropriate data types, and minimizing unnecessary calculations.

⸻

🟩 T (Test) – Verify the Solution

To verify the solution, I will perform the following tests:

1. **Valid Inputs:** Test the function block with valid inputs (Input1, Input2, Precision) and verify that the outputs are correct.
2. **Invalid Precision:** Test the function block with a negative Precision value and verify that the Error output is set to TRUE.
3. **Disabled Execution:** Test the function block with the Enable input set to FALSE and verify that all outputs are set to FALSE.
4. **Floating-Point Rounding:** Test the function block with inputs that require floating-point rounding and verify that the outputs are correct.
5. **Performance:** Measure the execution time of the function block with different input values and verify that it meets the performance requirements for industrial use cases.
6. **Robustness:** Test the function block under various conditions (

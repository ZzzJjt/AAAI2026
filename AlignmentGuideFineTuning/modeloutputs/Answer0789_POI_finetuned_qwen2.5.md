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

**C-A-R-E:**

🟥 C (Context) – Background Situation

In industrial automation, comparing floating-point values directly can lead to unpredictable results due to rounding errors. A precision-aware comparator is needed to ensure reliable decisions in control logic, especially when comparing setpoints, sensor values, or thresholds.

⸻

🟩 A (Action) – Task Steps

	1.	Define the function block with inputs and outputs as specified.
	2.	Implement logic to validate the precision value and handle edge cases.
	3.	Scale both input values to the specified precision using a power of 10.
	4.	Perform an integer comparison of the scaled values.
	5.	Evaluate the comparison results and set the output flags accordingly.
	6.	Include a safety check to ensure the function block only operates when allowed (via the Enable input).
	7.	Add comments explaining the logic and potential use cases.

⸻

🟧 R (Result) – Expected Outcome

The function block will:
	•	Accept two REAL inputs and a precision level (up to n decimal places)
	•	Scale the inputs to integers for comparison
	•	Provide clear outputs for equality, greater-than, and less-than conditions
	•	Be scan-cycle-safe and suitable for use in industrial control systems
	•	Include robust error handling for invalid inputs or execution conditions

⸻

⸻

**B-A-B-E:**

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

⸻

�

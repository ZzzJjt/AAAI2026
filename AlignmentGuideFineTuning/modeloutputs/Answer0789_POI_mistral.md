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

🟦 E (Example) – Provide an Example

```
FUNCTION_BLOCK RealComparator
    VAR
        Input1, Input2, Scale : REAL;
        Equal, Greater, Less, Error : BOOL;
    END_VAR

    IF Enable THEN
        IF Precision < 0 THEN
            Error := TRUE;
        ELSE
            Scale := POWER(10, Precision);
            Input1 := ROUND(Input1 * Scale) / Scale;
            Input2 := ROUND(Input2 * Scale) / Scale;
            Equal := Input1 = Input2;
            Greater := Input1 > Input2;
            Less := Input1 < Input2;
        END_IF;
    ELSE
        Error := TRUE;
    END_IF;
END_FUNCTION_BLOCK
```

⸻

🟨 S (Safety) – Consider Safety Implications

Ensure that the function block is safe for industrial use by:
	•	Validating the precision input to prevent negative values
	•	Rounding the inputs to the specified precision to minimize floating-point errors
	•	Using integer comparison for the final comparison to avoid floating-point rounding issues
	•	Providing an error output to indicate invalid precision or disabled execution

⸻

🟦 C (Creativity) – Add Creativity and Improvements

To make the function block more versatile and user-friendly, consider adding:
	•	A default precision value (e.g., 6 decimal places) for cases where no precision is specified
	•	An optional tolerance value to account for small differences in real numbers
	•	A diagnostic output to indicate the precision used for comparison
	•	A user-friendly configuration interface for easy setup and tuning

⸻

🟩 R (Review) – Review the Solution

Review the solution to ensure it meets the requirements:
	•	Precision-aware real number comparison
	•	Configurable precision
	•	Error handling
	•	Industrial robustness
	•	Safety considerations
	•	Compliance with IEC 6113

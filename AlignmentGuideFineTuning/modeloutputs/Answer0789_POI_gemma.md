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
	•	A test case that demonstrates the function block’s behavior

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
	•	A test case that demonstrates the function block’s behavior

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC software developer implementing a precision-aware real number comparator in IEC 61131-3 Structured Text for industrial control systems.

⸻

🟩 T (Task) – Define the Objective

Create a self-contained function block that compares two REAL inputs (Input1, Input2) with respect to a configurable number of decimal places (Precision). The block should:
	•	Scale or round both

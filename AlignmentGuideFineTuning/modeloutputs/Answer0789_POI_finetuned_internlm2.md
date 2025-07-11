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

🟥 T (Time) – Specify the Deadline

Complete the function block within 15 minutes, ensuring that it is self-contained and can be directly implemented in a PLC system.

**Real Number Comparator:**

Implement a self-contained function block in IEC 61131-3 Structured Text to compare two real inputs up to a configurable number of decimal places. The block should include logic to scale the inputs to the specified precision, provide output flags for equality, greater, and less comparisons, and handle floating-point rounding issues. Ensure that the function block is suitable for industrial use cases and can be directly implemented in a PLC system.

**R:**

🟥 R (Role) – Define Your Role

As a PLC software developer, your role is to create a self-contained function block in IEC 61131-3 Structured Text to compare two real inputs up to a configurable number of decimal places. The function block should handle precision scaling, provide output flags for equality, greater, and less comparisons, and handle floating-point rounding issues. Your focus should be on creating a robust and industrial-grade solution that can be directly implemented in a PLC system.

**T:**

🟩 T (Task) – Define the Objective

Create a self-contained function block in IEC 61131-3 Structured Text to compare two real inputs (Input1 and Input2) up to a configurable number of decimal places (Precision). The function block should:
	•	Scale or round both inputs to the specified precision
	•	Provide output flags:
	•	Equal : BOOL
	•	Greater : BOOL
	•	Less : BOOL
	•	Error : BOOL (for invalid precision or disabled execution)
	•	Safely handle floating-point rounding issues
	•	Be scan-cycle compatible and suitable for industrial use cases like alarm evaluation or setpoint matching

**F:**

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
	•	Logic flow

### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block to compare two REAL values with configurable decimal precision, handling floating-point inaccuracies and providing comparison outputs (Equal/Greater/Less) with error checking.  

*(Focus: Precision-based floating-point comparison for reliable industrial logic, avoiding direct equality checks.)*

### Prompt:
**Real Comparator:**
Implement a self-contained function block in IEC 61131-3 structured text to compare two real inputs up to n decimal places. Include configurable precision and error handling.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In many industrial control systems, comparing floating-point values (REAL types) directly can lead to unreliable results due to rounding errors and floating-point representation limits. Without a method to compare numbers with a specified decimal precision, engineers may encounter false mismatches or unstable logic in process comparisons, alarming, or control switching logic.

⸻

🟩 A (After) – The Desired Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text that compares two REAL inputs up to n decimal places. The function block should:
	•	Accept a user-defined precision level (n)
	•	Normalize or round both input values to that precision before comparison
	•	Provide output flags such as Equal, Greater, and Less
	•	Handle floating-point inaccuracies and include error checks (e.g., invalid precision or input range)

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block with inputs:
	•	Input1 : REAL, Input2 : REAL
	•	Precision : INT (number of decimal places to compare)
	•	Enable : BOOL
	2.	Internally calculate a scaling factor based on precision:
\text{Scale} := 10^\text{Precision}
Then compare ROUND(Input1 * Scale) vs ROUND(Input2 * Scale)
	3.	Provide outputs:
	•	Equal : BOOL
	•	Greater : BOOL
	•	Less : BOOL
	•	Error : BOOL (e.g., if Precision < 0 or inputs are invalid)
	4.	Include inline comments and safeguards to ensure scan-cycle-safe operation and clarity

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block to compare two REAL values with configurable decimal precision, handling floating-point inaccuracies and providing comparison outputs (Equal/Greater/Less) with error checking.  

*(Focus: Precision-based floating-point comparison for reliable industrial logic, avoiding direct equality checks.)*
**Real Comparator:**
Implement a self-contained function block in IEC 61131-3 structured text to compare two real inputs up to n decimal places. Include configurable precision and error handling.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In many industrial control systems, comparing floating-point values (REAL types) directly can lead to unreliable results due to rounding errors and floating-point representation limits. Without a method to compare numbers with a specified decimal precision, engineers may encounter false mismatches or unstable logic in process comparisons, alarming, or control switching logic.

⸻

🟩 A (After) – The Desired Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text that compares two REAL inputs up to n decimal places. The function block should:
	•	Accept a user-defined precision level (n)
	•	Normalize or round both input values to that precision before comparison
	•	Provide output flags such as Equal, Greater, and Less
	•	Handle floating-point inaccuracies and include error checks (e.g., invalid precision or input range)

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block with inputs:
	•	Input1 : REAL, Input2 : REAL
	•	Precision : INT (number of decimal places to compare)
	•	Enable : BOOL
	2.	Internally calculate a scaling factor based on precision:
\text{Scale} := 10^\text{Precision}
Then compare ROUND(Input1 * Scale) vs ROUND(Input2 * Scale)
	3.	Provide outputs:
	•	Equal : BOOL
	•	Greater : BOOL
	•	Less : BOOL
	•	Error : BOOL (e.g., if Precision < 0 or inputs are invalid)
	4.	Include inline comments and safeguards to ensure scan-cycle-safe operation and clarity of intent.
#include <stdlib.h>
#include <stdio.h>

// Function block for comparing two REAL values up to n decimal places
FUNCTION_BLOCK RealComparator
VAR_INPUT
    Input1 : REAL;
    Input2 : REAL;
    Precision : INT;
    Enable : BOOL;
END_VAR

VAR_OUTPUT
    Equal : BOOL;
    Greater : BOOL;
    Less : BOOL;
    Error : BOOL;
END_VAR

VAR
    Scale : REAL;
    Input1_Scaled : REAL;
    Input2_Scaled : REAL;
END_VAR

METHOD Execute : BOOL
BEGIN
    // Check inputs
    IF NOT Enable THEN
        Equal := FALSE;
        Greater := FALSE;
        Less := FALSE;
        Error := TRUE;
        RETURN;
    END_IF;

    // Check Precision
    IF Precision < 0 THEN
        Equal := FALSE;
        Greater := FALSE;
        Less := FALSE;
        Error := TRUE;
        RETURN;
    END_IF;

    // Calculate scaling factor
    Scale := 10.0 ^ Precision;

    // Scale inputs
    Input1_Scaled := ROUND(Input1 * Scale);
    Input2_Scaled := ROUND(Input2 * Scale);

    // Compare scaled values
    Equal := Input1_Scaled = Input2_Scaled;
    Greater := Input1_Scaled > Input2_Scaled;
    Less := Input1_Scaled < Input2_Scaled;

    Error := FALSE;
END_METHOD

METHOD Reset : BOOL
BEGIN
    Equal := FALSE;
    Greater := FALSE;
    Less := FALSE;
    Error := FALSE;
END_METHOD
END_FUNCTION_BLOCK

// Example usage:
//   Enable := TRUE;
//   Input1 := 10.0;
//   Input2 := 20.0;
//   Precision := 2;
//   Execute;
//   IF Equal THEN
//       // Both values are equal up to n decimal places
//   ELSIF Greater THEN
//       // Input1 > Input2 up to n decimal places
//   ELSIF Less THEN
//       // Input1 <

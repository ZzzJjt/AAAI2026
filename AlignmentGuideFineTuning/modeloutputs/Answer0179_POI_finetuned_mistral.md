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
	4.	Include inline comments and safeguards to ensure scan-cycle-safe operation and clarity for maintenance
(* IEC 61131-3 Structured Text: REAL Comparator Function Block *)
(* Purpose: Compares two REAL values up to n decimal places *)

FUNCTION_BLOCK RealComparator
VAR_INPUT
    Enable : BOOL;                  (* TRUE to enable comparison *)
    Input1 : REAL;                  (* First REAL value to compare *)
    Input2 : REAL;                  (* Second REAL value to compare *)
    Precision : INT;                (* Number of decimal places to compare, e.g., 2 *)
END_VAR

VAR_OUTPUT
    Equal : BOOL;                   (* TRUE if Input1 = Input2 within precision *)
    Greater : BOOL;                 (* TRUE if Input1 > Input2 within precision *)
    Less : BOOL;                    (* TRUE if Input1 < Input2 within precision *)
    Error : BOOL;                   (* TRUE if invalid input or precision < 0 *)
END_VAR

VAR
    Scale : REAL;                   (* Scaling factor for precision *)
    Temp1 : REAL;                   (* Temporary storage for Input1 *)
    Temp2 : REAL;                   (* Temporary storage for Input2 *)
    Temp3 : REAL;                   (* Temporary storage for comparison *)
    ValidInput : BOOL;              (* Flag for valid inputs *)
END_VAR

(* Main Logic *)
IF Enable THEN
    (* Validate inputs *)
    ValidInput := (Precision >= 0) AND (Enable) AND (IS_VALID(Input1)) AND (IS_VALID(Input2));
    Error := NOT ValidInput;

    (* Calculate scaling factor *)
    Scale := POWER(10.0, Precision);

    (* Normalize inputs *)
    Temp1 := ROUND(Input1 * Scale);
    Temp2 := ROUND(Input2 * Scale);

    (* Perform comparisons *)
    Equal := (Temp1 = Temp2);
    Greater := (Temp1 > Temp2);
    Less := (Temp1 < Temp2);
END_IF

(* Documentation *)
(*
    Function Block: RealComparator
    Purpose: Compares two REAL values up to

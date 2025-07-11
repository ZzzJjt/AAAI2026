### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 function block in Structured Text to compare two REAL values with configurable decimal precision, handling floating-point inaccuracies and input validation for reliable industrial automation logic.  

*(Key focus: Precision-based comparison, input safety, and PLC compatibility.)*

### Prompt:
**Binary Search:**
Implement a self-contained function block in IEC 61131-3 structured text to perform a binary search on an array of 100 integers. Include input validation and efficient handling of search boundaries.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

Searching through large arrays in PLC-based systems can be inefficient if done linearly, especially in time-sensitive applications like sorting, classification, or threshold detection. Without a structured and optimized approach like binary search, search operations on a 100-element integer array could result in unnecessary CPU cycles, poor performance, and missed response deadlines in industrial control systems.

⸻

🟩 A (After) – The Desired Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text that performs a binary search on a 100-integer array. The function should:
	•	Efficiently locate a target value using binary search logic
	•	Include input validation (e.g., bounds check, sorted array assumption)
	•	Handle search boundaries accurately to avoid indexing errors or infinite loops
	•	Be modular and reusable in PLC programs where fast data lookup is essential

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block interface with inputs for:
	•	SearchArray : ARRAY[1..100] OF INT
	•	TargetValue : INT
	•	Enable : BOOL
	2.	Implement binary search logic using WHILE or REPEAT loops and variables like Low, High, and Mid.
	3.	Add validation to ensure the array index boundaries are respected and the search halts when Low > High or the value is found.
	4.	Include outputs such as:
	•	Found : BOOL
	•	Index : INT (position in array if found, else -1)
	5.	Comment each section for clarity and maintainability.

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 function block in Structured Text to compare two REAL values with configurable decimal precision, handling floating-point inaccuracies and input validation for reliable industrial automation logic.  

*(Key focus: Precision-based comparison, input safety, and PLC compatibility.)*
**Binary Search:**
Implement a self-contained function block in IEC 61131-3 structured text to perform a binary search on an array of 100 integers. Include input validation and efficient handling of search boundaries.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

Searching through large arrays in PLC-based systems can be inefficient if done linearly, especially in time-sensitive applications like sorting, classification, or threshold detection. Without a structured and optimized approach like binary search, search operations on a 100-element integer array could result in unnecessary CPU cycles, poor performance, and missed response deadlines in industrial control systems.

⸻

🟩 A (After) – The Desired Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text that performs a binary search on a 100-integer array. The function should:
	•	Efficiently locate a target value using binary search logic
	•	Include input validation (e.g., bounds check, sorted array assumption)
	•	Handle search boundaries accurately to avoid indexing errors or infinite loops
	•	Be modular and reusable in PLC programs where fast data lookup is essential

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block interface with inputs for:
	•	SearchArray : ARRAY[1..100] OF INT
	•	TargetValue : INT
	•	Enable : BOOL
	2.	Implement binary search logic using WHILE or REPEAT loops and variables like Low, High, and Mid.
	3.	Add validation to ensure the array index boundaries are respected and the search halts when Low > High or the value is found.
	4.	Include outputs such as:
	•	Found : BOOL
	•	Index : INT (position in array if found, else -1)
	5.	Comment each section for clarity and maintainability.
	6.	Ensure the function block is suitable for real-time PLC execution and can be reused in other sorting or filtering applications.
(* IEC 61131-3 Structured Text: REAL Compare Function Block *)
(* Purpose: Compares two REAL values with configurable decimal precision *)

FUNCTION_BLOCK REAL_COMPARE
VAR_INPUT
    ENABLE : BOOL;                  (* TRUE to execute comparison *)
    Precision : BYTE;               (* Number of decimal places, 0 to 9 *)
    Value1 : REAL;                  (* First value to compare *)
    Value2 : REAL;                  (* Second value to compare *)
END_VAR

VAR_OUTPUT
    Equal : BOOL;                   (* TRUE if values are equal *)
    Greater : BOOL;                 (* TRUE if Value1 > Value2 *)
    Less : BOOL;                    (* TRUE if Value1 < Value2 *)
    Error : BOOL;                   (* TRUE if invalid precision *)
END_VAR

VAR
    ScalingFactor : REAL;           (* Scaling factor for precision *)
    TempValue1 : REAL;              (* Temporary value for Value1 *)
    TempValue2 : REAL;              (* Temporary value for Value2 *)
    Power : BYTE;                   (* Exponent for scaling *)
    i : BYTE;                       (* Loop counter for precision *)
END_VAR

(* Main Execution Logic *)
IF ENABLE THEN
    (* Initialize outputs *)
    Equal := FALSE;
    Greater := FALSE;
    Less := FALSE;
    Error := FALSE;
    
    (* Validate inputs *)
    IF Precision < 0 OR Precision > 9 THEN
        Error := TRUE;
        Equal := FALSE;
        Greater := FALSE;
        Less := FALSE;
        RETURN;
    END_IF;
    
    (* Calculate scaling factor *)
    ScalingFactor := POWER(10, Precision);
    ScalingFactor := ROUND(ScalingFactor);
    
    (* Scale and compare values *)
    TempValue1 := Value1;
    TempValue2 := Value2;
    Power := Precision;

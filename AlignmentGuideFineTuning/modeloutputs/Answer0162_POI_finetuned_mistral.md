### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block for a binary search algorithm that efficiently locates a target value in a sorted 100-element array, with input validation, bounds safety, and real-time PLC compatibility.  

*(Focus: Modularity, performance (O(log n)), and industrial robustness.)*

### Prompt:
**Counter:**
Implement a self-contained function block in IEC 61131-3 structured text for a digital counter with up/down counting modes. Include configurable initial value, step size, and overflow handling.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

Digital counters are essential in industrial automation for tracking events, cycles, or product quantities. However, basic counters often lack flexibility—such as configurable counting direction, custom step sizes, and overflow protection. Without a robust and reusable function block, engineers may struggle to maintain or scale these functions in complex control systems.

⸻

🟩 A (After) – The Desired Outcome

Design and implement a self-contained IEC 61131-3 Structured Text function block that performs as a flexible digital counter, supporting:
	•	Up/down counting modes
	•	A configurable initial value
	•	A customizable step size
	•	Overflow and underflow handling
This function block should be modular, reusable, and safe for use in scan-cycle-driven PLC environments.

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block with inputs:
	•	Enable : BOOL
	•	CountUp : BOOL
	•	StepSize : INT
	•	InitValue : INT
	•	Reset : BOOL
	•	MaxValue : INT
	•	MinValue : INT
	2.	Use internal variables to store the current count and handle direction logic:
	•	Increment or decrement based on CountUp and Enable
	•	Reset counter when Reset = TRUE
	•	Clamp the value between MinValue and MaxValue to prevent overflow/underflow
	3.	Output the result as CurrentValue : INT and status flags like AtMax, AtMin.
	4.	Comment each section to make the block readable and easy to reuse across projects.

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block for a binary search algorithm that efficiently locates a target value in a sorted 100-element array, with input validation, bounds safety, and real-time PLC compatibility.  

*(Focus: Modularity, performance (O(log n)), and industrial robustness.)*
**Counter:**
Implement a self-contained function block in IEC 61131-3 structured text for a digital counter with up/down counting modes. Include configurable initial value, step size, and overflow handling.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

Digital counters are essential in industrial automation for tracking events, cycles, or product quantities. However, basic counters often lack flexibility—such as configurable counting direction, custom step sizes, and overflow protection. Without a robust and reusable function block, engineers may struggle to maintain or scale these functions in complex control systems.

⸻

🟩 A (After) – The Desired Outcome

Design and implement a self-contained IEC 61131-3 Structured Text function block that performs as a flexible digital counter, supporting:
	•	Up/down counting modes
	•	A configurable initial value
	•	A customizable step size
	•	Overflow and underflow handling
This function block should be modular, reusable, and safe for use in scan-cycle-driven PLC environments.

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block with inputs:
	•	Enable : BOOL
	•	CountUp : BOOL
	•	StepSize : INT
	•	InitValue : INT
	•	Reset : BOOL
	•	MaxValue : INT
	•	MinValue : INT
	2.	Use internal variables to store the current count and handle direction logic:
	•	Increment or decrement based on CountUp and Enable
	•	Reset counter when Reset = TRUE
	•	Clamp the value between MinValue and MaxValue to prevent overflow/underflow
	3.	Output the result as CurrentValue : INT and status flags like AtMax, AtMin.
	4.	Comment each section to make the block readable and easy to reuse across projects.
(* IEC 61131-3 Structured Text: Binary Search Function Block *)
(* Purpose: Efficiently locates a target value in a sorted 100-element array *)

FUNCTION_BLOCK BinarySearch
VAR_INPUT
    Enable : BOOL;                  (* TRUE to execute search *)
    Array : ARRAY[1..100] OF INT;   (* Sorted input array, 100 elements max *)
    Target : INT;                   (* Value to search for *)
END_VAR

VAR_OUTPUT
    Found : BOOL;                   (* TRUE if target is found *)
    Index : INT;                    (* Position of target in array *)
    Error : BOOL;                   (* TRUE if invalid input *)
END_VAR

VAR
    Low : INT;                      (* Lower search bound *)
    High : INT;                     (* Upper search bound *)
    Mid : INT;                      (* Middle index *)
    ValidInput : BOOL;              (* Input validation flag *)
END_VAR

(* Initialize outputs *)
Found := FALSE;
Index := 0;
Error := FALSE;

(* Main logic *)
IF Enable THEN
    (* Validate inputs *)
    ValidInput := TRUE;
    IF NOT (Array[1] <= Target AND Target <= Array[100]) OR NOT Enable THEN
        ValidInput := FALSE;
        Error := TRUE;
        Found := FALSE;
        Index := 0;
        RETURN;
    END_IF;

    (* Binary search algorithm *)
    Low := 1;
    High := 100;
    Mid := (Low + High) DIV 2;

    WHILE Low <= High AND ValidInput DO
        (* Check if target is found *)
        IF Array[Mid] = Target THEN
            Found := TRUE;
            Index := Mid;
            EXIT;
        (* Adjust search bounds *)
        ELSIF Array[Mid] < Target THEN
            Low := Mid + 1;
        ELSE
            High := Mid - 1;
        END_IF;

        (* Update mid index *)
        Mid := (Low + High) DIV 2;
    END_WHILE;

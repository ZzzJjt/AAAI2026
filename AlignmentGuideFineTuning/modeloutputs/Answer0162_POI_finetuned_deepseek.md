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
(* Purpose: Efficiently locate a target value in a sorted array *)

FUNCTION_BLOCK BinarySearch
VAR_INPUT
    Enable : BOOL;          (* TRUE to enable search *)
    Target : INT;           (* Target value to find *)
    ArraySize : INT;        (* Size of the sorted array *)
    Array : ARRAY[1..100] OF INT; (* Sorted array of integers *)
END_VAR

VAR_OUTPUT
    Found : BOOL;           (* TRUE if target is found *)
    Index : INT;            (* Index of the target in the array *)
    Error : BOOL;           (* TRUE if search fails *)
    ErrorCode : INT;        (* 0 = No error, 1 = Target not found *)
END_VAR

VAR
    Low : INT;              (* Start of search range *)
    High : INT;             (* End of search range *)
    Mid : INT;              (* Middle index *)
    MidVal : INT;           (* Value at the midpoint *)
    Step : INT;             (* Step size for binary search *)
    StepSize : INT;         (* Step size for up/down counting *)
    StepCount : INT;        (* Count of steps *)
    StepCountMax : INT;     (* Maximum step count *)
    StepCountMin : INT;     (* Minimum step count *)
    StepCountMaxVal : INT;  (* Maximum value for step count *)
    StepCountMinVal : INT;  (* Minimum value for step count *)
    StepCountMaxValMax : INT; (* Maximum value for step count *)
    StepCountMinValMax : INT; (* Minimum value for step count *)
    StepCountMax : INT;     (* Maximum step count *)
    StepCountMin : INT;     (* Minimum step count *)
    StepCountMaxVal : INT;  (* Maximum value for step count *)
    StepCountMinVal : INT;  (* Minimum value for step count *)
    StepCountMaxValMax : INT; (* Maximum value for step count *)
    StepCountMinValMax : INT; (* Minimum value for step count *)
    StepCountMax : INT;     (* Maximum step count *)
    StepCountMin : INT;     (* Minimum step count *)
    StepCountMaxVal :

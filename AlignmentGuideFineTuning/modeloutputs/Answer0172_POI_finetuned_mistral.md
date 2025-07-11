### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block for an iterative quicksort algorithm that sorts integer arrays in PLC environments, featuring stack-based emulation, input validation, and state-machine-driven execution for safe, efficient sorting within industrial automation systems.

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
Create a reusable IEC 61131-3 structured text function block for an iterative quicksort algorithm that sorts integer arrays in PLC environments, featuring stack-based emulation, input validation, and state-machine-driven execution for safe, efficient sorting within industrial automation systems.
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
(* IEC 61131-3 Structured Text: Quicksort Function Block *)
(* Purpose: Sorts an array of integers using the quicksort algorithm *)

FUNCTION_BLOCK Quicksort
VAR_INPUT
    Enable : BOOL;                  (* TRUE to execute sorting *)
    InputArray : ARRAY[1..100] OF INT; (* Array to be sorted *)
    ArraySize : INT;                (* Number of elements to sort *)
END_VAR

VAR_OUTPUT
    SortedArray : ARRAY[1..100] OF INT; (* Sorted array *)
    Done : BOOL;                    (* TRUE when sorting is complete *)
    Error : BOOL;                   (* TRUE if error occurs *)
    ErrorID : DWORD;                (* Error code *)
END_VAR

VAR
    Stack : ARRAY[1..100] OF INT;   (* Stack for recursion *)
    Top : INT;                      (* Top of the stack *)
    Pivot : INT;                    (* Pivot index *)
    Low : INT;                      (* Low index of subarray *)
    High : INT;                     (* High index of subarray *)
    i : INT;                        (* Loop variable *)
    j : INT;                        (* Loop variable *)
    Temp : INT;                     (* Temporary variable for swapping *)
    PartitionIndex : INT;           (* Index of pivot position *)
    PartitionValue : INT;           (* Value at pivot position *)
    iStack : ARRAY[1..100] OF INT; (* Stack for recursion emulation *)
    iTop : INT;                     (* Top of the iStack *)
    iTemp : INT;                    (* Temporary variable for stack *)
    iStackSize : INT;               (* Maximum stack size *)
    iStackIndex : INT;              (* Current stack index *)
    iStackValue : INT;              (* Current stack value *)
    iStackValid : BOOL;             (* Validity flag for stack *)
    iStackBusy : BOOL;              (* Busy flag for stack *)
    iStackError : BOOL;             (* Error flag for stack *)
    iStackErrorID : DWORD;          (* Error

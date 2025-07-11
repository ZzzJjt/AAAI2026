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
(* Purpose: Implements a recursive quicksort algorithm for integer arrays *)

FUNCTION_BLOCK Quicksort
VAR_INPUT
    Enable : BOOL; (* TRUE to enable sorting *)
    InputArray : ARRAY[1..100] OF INT; (* Input array to sort *)
    InputArraySize : INT; (* Size of the input array *)
END_VAR

VAR_OUTPUT
    SortedArray : ARRAY[1..100] OF INT; (* Sorted array *)
    Done : BOOL; (* TRUE when sorting is complete *)
    Error : BOOL; (* TRUE if an error occurs *)
END_VAR

VAR
    Stack : ARRAY[1..100] OF INT; (* Stack for recursion *)
    StackTop : INT; (* Current top of the stack *)
    CurrentIndex : INT; (* Current index in the input array *)
    PartitionIndex : INT; (* Partition index for the quicksort *)
    Temp : INT; (* Temporary variable for swapping *)
    Temp2 : INT; (* Temporary variable for swapping *)
    Temp3 : INT; (* Temporary variable for swapping *)
    Temp4 : INT; (* Temporary variable for swapping *)
    Temp5 : INT; (* Temporary variable for swapping *)
    Temp6 : INT; (* Temporary variable for swapping *)
    Temp7 : INT; (* Temporary variable for swapping *)
    Temp8 : INT; (* Temporary variable for swapping *)
    Temp9 : INT; (* Temporary variable for swapping *)
    Temp10 : INT; (* Temporary variable for swapping *)
    Temp11 : INT; (* Temporary variable for swapping *)
    Temp12 : INT; (* Temporary variable for swapping *)
    Temp13 : INT; (* Temporary variable for swapping *)
    Temp14 : INT; (* Temporary variable for swapping *)
    Temp15 : INT; (* Temporary variable for swapping *)
    Temp16 : INT; (* Temporary variable for swapping *)
    Temp17 : INT; (* Temporary variable for swapping *)
    Temp18 : INT; (* Temporary variable for swapping *)
    Temp19 : INT; (* Temporary variable for swapping *)
    Temp20 : INT; (* Temporary variable for swapping *)
    Temp21 : INT; (* Temporary variable for swapping *)
    Temp2

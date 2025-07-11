### Intent:
**Intent Summary:**  
Create a scan-cycle-safe, iterative quicksort function block in IEC 61131-3 Structured Text to efficiently sort integer arrays on PLCs without recursion, using stack emulation and in-place partitioning.  

*(Focus: Industrial automation, memory safety, and iterative adaptation of quicksort for PLC constraints.)*

### Prompt:
**Quicksort:**
Implement a self-contained function block in IEC 61131-3 structured text to perform the quicksort algorithm on an array of integers. Ensure efficient partitioning and recursion handling.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In industrial automation tasks such as data sorting, ranking, or prioritizing process values, efficient sorting algorithms are essential. Quicksort is a powerful algorithm known for its average-case efficiency, but it typically relies on recursion, which is either not supported or discouraged in IEC 61131-3 Structured Text environments due to scan-cycle safety and memory limitations. Without a properly adapted approach, implementing quicksort on a PLC could result in stack overflows or unreadable code structures.

⸻

🟩 A (After) – The Desired Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text that performs the quicksort algorithm on an array of integers. The solution must:
	•	Avoid direct recursion by simulating it with iterative control structures and stack emulation using arrays or state machines
	•	Implement an efficient partitioning mechanism
	•	Sort the array in place, preserving memory efficiency
	•	Be modular, reusable, and compliant with scan-cycle-safe programming practices

⸻

🟧 B (Bridge) – How to Get There
	1.	Define inputs for the function block such as:
	•	InputArray : ARRAY[1..N] OF INT
	•	Execute : BOOL
	2.	Create internal variables to manage sorting state:
	•	Stack emulation using index arrays for Low and High
	•	Pivot, i, j, and temporary variables for swaps
	3.	Use a loop-based simulation of recursive quicksort, pushing and popping subranges to/from an internal stack
	4.	Include an InProgress flag and a Done output to manage multi-scan execution if needed
	5.	Comment clearly on each phase: partitioning, swapping, and range management

### Generated Code:
**Intent Summary:**  
Create a scan-cycle-safe, iterative quicksort function block in IEC 61131-3 Structured Text to efficiently sort integer arrays on PLCs without recursion, using stack emulation and in-place partitioning.  

*(Focus: Industrial automation, memory safety, and iterative adaptation of quicksort for PLC constraints.)*
**Quicksort:**
Implement a self-contained function block in IEC 61131-3 structured text to perform the quicksort algorithm on an array of integers. Ensure efficient partitioning and recursion handling.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In industrial automation tasks such as data sorting, ranking, or prioritizing process values, efficient sorting algorithms are essential. Quicksort is a powerful algorithm known for its average-case efficiency, but it typically relies on recursion, which is either not supported or discouraged in IEC 61131-3 Structured Text environments due to scan-cycle safety and memory limitations. Without a properly adapted approach, implementing quicksort on a PLC could result in stack overflows or unreadable code structures.

⸻

🟩 A (After) – The Desired Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text that performs the quicksort algorithm on an array of integers. The solution must:
	•	Avoid direct recursion by simulating it with iterative control structures and stack emulation using arrays or state machines
	•	Implement an efficient partitioning mechanism
	•	Sort the array in place, preserving memory efficiency
	•	Be modular, reusable, and compliant with scan-cycle-safe programming practices

⸻

🟧 B (Bridge) – How to Get There
	1.	Define inputs for the function block such as:
	•	InputArray : ARRAY[1..N] OF INT
	•	Execute : BOOL
	2.	Create internal variables to manage sorting state:
	•	Stack emulation using index arrays for Low and High
	•	Pivot, i, j, and temporary variables for swaps
	3.	Use a loop-based simulation of recursive quicksort, pushing and popping subranges to/from an internal stack
	4.	Include an InProgress flag and a Done output to manage multi-scan execution if needed
	5.	Comment clearly on each phase: partitioning, swapping, and range management
	6.	Optimize for scan-cycle safety and real-time execution, ensuring the function block can be called repeatedly without causing stack overflows or infinite loops
(* IEC 61131-3 Structured Text: Iterative Quicksort Function Block *)
(* Purpose: Sorts an array of integers using quicksort without recursion *)

FUNCTION_BLOCK QuickSort
VAR_INPUT
    Execute : BOOL;                  (* TRUE to start sorting *)
    InputArray : ARRAY[1..100] OF INT; (* Array to be sorted *)
    ArraySize : INT;                 (* Number of elements to sort, 1 to 100 *)
END_VAR

VAR_OUTPUT
    SortedArray : ARRAY[1..100] OF INT; (* Sorted array *)
    Done : BOOL;                     (* TRUE when sorting is complete *)
    Error : BOOL;                    (* TRUE if invalid input *)
END_VAR

VAR
    StackLow : ARRAY[1..10] OF INT;  (* Stack for low indices *)
    StackHigh : ARRAY[1..10] OF INT; (* Stack for high indices *)
    StackTop : INT;                  (* Top of the stack *)
    i, j, k, pivot, temp : INT;      (* Loop variables *)
    Low, High : INT;                 (* Subarray bounds *)
    PartitionIndex : INT;            (* Pivot index *)
    Swap : BOOL;                     (* Flag for swapping *)
    ValidInput : BOOL;               (* Input validation flag *)
END_VAR

(* Initialize outputs *)
Done := FALSE;
Error := FALSE;

(* Input validation *)
IF Execute AND (ArraySize < 1 OR ArraySize > 100) THEN
    Error := TRUE;
    Done := FALSE;
    RETURN;
END_IF;

(* Reset stack and variables *)
StackTop := 0;
FOR i := 1 TO 10 DO
    StackLow[i] := 0;
    StackHigh[i] := 0;
END_FOR;

(* Push initial range to the stack *)
StackLow[StackTop + 1] := 1

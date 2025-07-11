### Intent:
The task is to create an IEC 61131-3 structured text function block that implements an iterative heapsort algorithm for integer arrays without recursion or DOWNTO loops, ensuring efficient in-place sorting with clear status outputs for PLC integration.

### Prompt:
**Heapsort:**
Implement a self-contained function block in IEC 61131-3 structured text to perform the heapsort algorithm on an array of integers without using recursion or the ‘DOWNTO’ keyword in loops. Ensure efficient heap construction and sorting.

**T-A-G:**

🟥 T (Task)

Implement a self-contained function block in IEC 61131-3 Structured Text that performs the heapsort algorithm on an array of integers.

⸻

🟩 A (Action)
	•	Design the function block to sort an integer array in place, without requiring additional memory.
	•	Use iterative loops only — avoid recursion to ensure scan-cycle compatibility.
	•	Replace any use of the DOWNTO keyword with ascending loops and calculated index logic.
	•	Implement two main phases:
	1.	Heap construction: convert the array into a valid max-heap.
	2.	Sorting: repeatedly extract the largest element, swap, and restore the heap property.
	•	Include status outputs like Done : BOOL and clearly comment the heapify logic, loop flow, and index tracking.

⸻

🟦 G (Goal)

Deliver a reliable, efficient, and standards-compliant sorting block that integrates seamlessly into PLC projects. The function block should execute safely under typical PLC scan cycles, respect IEC 61131-3 syntax limitations, and be easily reusable in any sorting-related automation task.

### Generated Code:
The task is to create an IEC 61131-3 structured text function block that implements an iterative heapsort algorithm for integer arrays without recursion or DOWNTO loops, ensuring efficient in-place sorting with clear status outputs for PLC integration.
**Heapsort:**
Implement a self-contained function block in IEC 61131-3 structured text to perform the heapsort algorithm on an array of integers without using recursion or the ‘DOWNTO’ keyword in loops. Ensure efficient heap construction and sorting.

**T-A-G:**

🟥 T (Task)

Implement a self-contained function block in IEC 61131-3 Structured Text that performs the heapsort algorithm on an array of integers.

⸻

🟩 A (Action)
	•	Design the function block to sort an integer array in place, without requiring additional memory.
	•	Use iterative loops only — avoid recursion to ensure scan-cycle compatibility.
	•	Replace any use of the DOWNTO keyword with ascending loops and calculated index logic.
	•	Implement two main phases:
	1.	Heap construction: convert the array into a valid max-heap.
	2.	Sorting: repeatedly extract the largest element, swap, and restore the heap property.
	•	Include status outputs like Done : BOOL and clearly comment the heapify logic, loop flow, and index tracking.

⸻

🟦 G (Goal)

Deliver a reliable, efficient, and standards-compliant sorting block that integrates seamlessly into PLC projects. The function block should execute safely under typical PLC scan cycles, respect IEC 61131-3 syntax limitations, and be easily reusable in any sorting-related automation task.
(* IEC 61131-3 Structured Text: Heapsort Function Block *)
(* Purpose: Sorts an array of integers in-place using the heap sort algorithm *)
(* Without recursion or DOWNTO loops, suitable for PLC environments *)

FUNCTION_BLOCK HeapsortFB
VAR_INPUT
    Enable : BOOL;          (* TRUE to enable sorting *)
    InputArray : ARRAY[1..100] OF INT; (* Input array to sort *)
    InputArraySize : INT;    (* Array size *)
END_VAR

VAR_OUTPUT
    Done : BOOL;             (* TRUE when sorting is complete *)
    Error : BOOL;            (* TRUE if input array is invalid *)
    SortStatus : INT;        (* 0=Not Started, 1=Heap Construction, 2=Sorting, 3=Done *)
    SortProgress : INT;       (* 0-100% progress *)
    SortError : STRING[80];  (* Error message *)
END_VAR

VAR
    i, j, k, heapSize : INT; (* Loop counters and heap size *)
    temp : INT;                (* Temporary variable for swapping *)
    heap : ARRAY[1..InputArraySize] OF INT; (* Heap array *)
    heap_ptr : ARRAY[1..InputArraySize] OF INT; (* Heap pointer array *)
    heap_index : ARRAY[1..InputArraySize] OF INT; (* Heap index array *)
    heap_max_ptr : ARRAY[1..InputArraySize] OF INT; (* Heap max pointer array *)
    heap_max_index : ARRAY[1..InputArraySize] OF INT; (* Heap max index array *)
    heap_parent : ARRAY[1..InputArraySize] OF INT; (* Heap parent array *)
    heap_parent_index : ARRAY[1..InputArraySize] OF INT; (* Heap parent index array *)
    heap_child : ARRAY[1..InputArraySize] OF INT; (* Heap child array *)
    heap_child_index : ARRAY[1..InputArraySize] OF INT; (* Heap child index array *)
    heap_swap : ARRAY[1..InputArraySize] OF INT; (* Swap array *)
    heap_swap_index : ARRAY[1..InputArraySize] OF INT; (* Swap index array *)

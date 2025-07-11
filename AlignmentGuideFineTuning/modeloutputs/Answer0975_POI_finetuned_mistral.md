### Intent:
**Intent Summary:**  
Implement an iterative heapsort function block in IEC 61131-3 Structured Text to sort integer arrays in-place without recursion or `DOWNTO` loops, ensuring PLC-compatible efficiency and clear status outputs.  

*(Focus: Standards-compliant, scan-cycle-safe sorting for industrial automation.)*

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
**Intent Summary:**  
Implement an iterative heapsort function block in IEC 61131-3 Structured Text to sort integer arrays in-place without recursion or `DOWNTO` loops, ensuring PLC-compatible efficiency and clear status outputs.  

*(Focus: Standards-compliant, scan-cycle-safe sorting for industrial automation.)*
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
(* IEC 61131-3 Structured Text Function Block for Heapsort *)
(* Sorts an array of integers in place using iterative heap sort *)
(* Compliant with PLC scan-cycle execution and clear status outputs *)

FUNCTION_BLOCK HeapSort
VAR_INPUT
    Execute : BOOL;                  (* TRUE to start sorting *)
    InputArray : ARRAY[1..100] OF INT; (* Array to be sorted *)
    ArraySize : INT;                 (* Number of elements to sort, 1 to 100 *)
END_VAR

VAR_OUTPUT
    SortedArray : ARRAY[1..100] OF INT; (* Sorted array in place *)
    Done : BOOL;                     (* TRUE when sorting is complete *)
    Error : BOOL;                    (* TRUE if invalid input *)
END_VAR

VAR
    i, j, heapSize, temp : INT;      (* Loop variables *)
    heapify : BOOL;                  (* TRUE during heapify phase *)
    heapIndex : INT;                 (* Index for heapify *)
    maxIndex : INT;                  (* Index of max element in subtree *)
    heapTop : INT;                   (* Top of heap *)
    heapBottom : INT;                (* Bottom of heap *)
    validInput : BOOL;               (* Input validation flag *)
END_VAR

(* Initialize outputs *)
Done := FALSE;
Error := FALSE;
heapTop := 1;
heapBottom := ArraySize;
heapSize := ArraySize;

(* Input validation *)
IF NOT Execute OR ArraySize < 1 OR ArraySize > 100 THEN
    Error := TRUE;
    Done := FALSE;
    RETURN;
END_IF;

(* Main logic: Heap construction and sorting *)
IF Execute AND NOT Error THEN
    (* Phase 1: Heap construction *)
    heapify := TRUE;
    heapSize := ArraySize;
    heapTop := 1;
    heapBottom := ArraySize;
    FOR i := heapTop TO heapBottom - 1 DO
        heapify := TRUE;
        heapIndex := i;
        heapifySubtree(i);
    END_

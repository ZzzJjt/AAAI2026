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

Deliver a reliable, efficient, and standards-compliant sorting block that integrates seamlessly into PLC projects. The function block should execute safely under typical PLC scan cycles, respect IEC 61131-3 syntax limitations, and be easily reusable in any sorting-related automation task. Ensure the code is well-commented and follows best practices for readability and maintainability.

**Function Block: Heapsort**

```structuredtext
// Heapsort Function Block
// Sorts an array of integers in place using the heapsort algorithm
// without recursion or the 'DOWNTO' keyword.

// Inputs:
//   arr : ARRAY[0..n-1] OF INT - The array to be sorted
//   n   : INT - The number of elements in the array

// Outputs:
//   Done : BOOL - Indicates when the sorting is complete

// Status Outputs:
//   HeapifyStatus : BOOL - Indicates the status of heapify operations
//   SwapStatus    : BOOL - Indicates the status of swap operations

// Constants:
CONST
  MAX_ITERATIONS : INT := 1000; // Maximum iterations for safety

VAR
  i, j, k, temp : INT;
  Done, HeapifyStatus, SwapStatus : BOOL;
  n : INT;
  arr : ARRAY[0..MAX_ITERATIONS-1] OF INT;
BEGIN
  // Initialize variables
  Done := FALSE;
  HeapifyStatus := FALSE;
  SwapStatus := FALSE;
  n := arr.LBOUND + arr.UPBOUND;

  // Main loop: heap construction and sorting
  FOR i := n DIV 2 - 1 TO 0 DO
    HeapifyStatus := Heapify(arr, n, i);
  END_FOR;

  WHILE NOT Done DO
    // Extract the largest element
    temp := arr[0];
    arr[0] := arr[n - 1];
    arr[n - 1] := temp;
    n := n - 1;

    // Restore the heap property
    SwapStatus := Heapify(arr, n, 0);

    // Check if sorting is complete
    IF n <= 1 THEN
      Done := TRUE;
    END_IF;
  END_WHILE;

  // Set status outputs
  Done := TRUE;
END_FUNCTION_BLOCK

// Helper function: Heapify
FUNCTION Heapify : BOOL
VAR_INPUT
  arr : ARRAY[0..MAX_ITERATIONS-1] OF INT;
  n   : INT;
  i   : INT;
END_VAR
VAR_OUTPUT
  HeapifyStatus : BOOL;
END_VAR
VAR
  left, right, largest, temp : INT;
BEGIN
  HeapifyStatus := FALSE;
  i := 0;
  left := 2 * i +

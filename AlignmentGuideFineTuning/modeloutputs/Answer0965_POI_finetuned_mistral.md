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
FUNCTION_BLOCK FB_QuickSort
VAR_INPUT
    InputArray : ARRAY[1..100] OF INT; // Input array to be sorted
    Execute : BOOL;                    // Trigger sorting on rising edge
END_VAR

VAR_OUTPUT
    SortedArray : ARRAY[1..100] OF INT; // Sorted array output
    Done : BOOL;                       // TRUE when sorting is complete
    Error : BOOL;                      // TRUE if an error occurs
    ErrorCode : DWORD;                 // 0: No error, 1: Invalid input, 2: Stack overflow
END_VAR

VAR
    Low : INT;                         // Low index of subarray
    High : INT;                        // High index of subarray
    Pivot : INT;                       // Pivot value
    i : INT;                           // Loop variable
    j : INT;                           // Loop variable
    Temp : INT;                        // Temporary variable for swapping
    Stack : ARRAY[1..10] OF INT;       // Stack for recursion
    StackTop : INT;                    // Top of the stack
    PartitionIndex : INT;              // Index of pivot position
    PartitionValue : INT;              // Value of pivot position
    PartitionLow : INT;                // Low index of left subarray
    PartitionHigh : INT;               // High index of right subarray
    IsStackEmpty : BOOL;               // TRUE if stack is empty
    RecursionCount : INT;              // Counts recursive calls
END_VAR

// Reset outputs on rising edge of Execute
IF Execute THEN
    Done := FALSE;
    Error := FALSE;
    ErrorCode := 0;
    RecursionCount := 0;
    StackTop := -1;
    FOR i := 1 TO 100 DO
        SortedArray[i] := InputArray[i];
    END_FOR;
END_IF;

// QuickSort Algorithm
IF Execute AND NOT Done AND NOT Error THEN
    // Initialize stack and recursion counter
    StackTop := -1;
    RecursionCount := 0;

    // Base

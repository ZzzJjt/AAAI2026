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
FUNCTION_BLOCK HeapSort
VAR_INPUT
    Enable : BOOL; // Enable sorting
    InputArray : ARRAY[1..100] OF INT; // Input array to sort
END_VAR

VAR_OUTPUT
    Done : BOOL; // Sorting completed
    Error : BOOL; // Sorting failed
    SortingProgress : INT; // Progress indicator (0-100)
END_VAR

VAR
    i, j, k, temp : INT;
    heapSize : INT;
    heap : ARRAY[1..100] OF INT; // Heap array
    heapIndex : ARRAY[1..100] OF INT; // Heap index array
END_VAR

// Initialize heap and heap index
heapSize := 100;
heap[1] := InputArray[1];
heapIndex[1] := 1;
FOR i := 2 TO heapSize DO
    heap[i] := 0;
    heapIndex[i] := 0;
END_FOR;

// Heapify the array
FOR i := 2 TO heapSize DO
    j := i;
    k := j / 2;
    WHILE j > 1 AND heap[k] < heap[j] DO
        temp := heap[k];
        heap[k] := heap[j];
        heap[j] := temp;
        j := j / 2;
        k := j;
    END_WHILE;
END_FOR;

// Sort the array
IF Enable THEN
    IF NOT Done THEN
        Done := FALSE;
        Error := FALSE;
        SortingProgress := 0;
        FOR i := 2 TO heapSize DO
            heap[1] := heap[i];
            heapIndex[1] := i;
            heapify(heap, heapIndex, heapSize);
            SortingProgress := SortingProgress + 10;
        END_FOR;
        Done := TRUE;
    END_IF;
END_IF;

// Sorting logic
FUNCTION_BLOCK Heapify
VAR_INPUT
    heap : ARRAY[1..100] OF INT; // Heap array
    heapIndex : ARRAY[1..100] OF INT; // Heap index array
    heapSize

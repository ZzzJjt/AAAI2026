### Intent:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text function block to iteratively perform heapsort on an integer array without recursion or `DOWNTO` loops, ensuring industrial PLC compatibility, in-place sorting, and clear documentation.  

*(Focus: Iterative heapsort, PLC constraints, reusability, and industrial deployment.)*

### Prompt:
**Heapsort:**
Implement a self-contained function block in IEC 61131-3 structured text to perform the heapsort algorithm on an array of integers without using recursion or the ‘DOWNTO’ keyword in loops. Ensure efficient heap construction and sorting.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

Sorting algorithms are essential for many automation tasks such as prioritization, scheduling, and sensor data organization. However, many traditional sorting routines rely on recursion or unsupported syntax like the DOWNTO keyword, which are not always practical or allowed in IEC 61131-3 Structured Text. Without a properly structured iterative approach, implementing heapsort—an efficient, in-place comparison-based sorting algorithm—can be complex, error-prone, and inefficient in a PLC environment.

⸻

🟩 A (After) – The Desired Outcome

Implement a self-contained function block in IEC 61131-3 Structured Text that performs the heapsort algorithm on an array of integers. The function block must:
	•	Avoid recursion entirely
	•	Avoid the use of DOWNTO loops for compatibility
	•	Build the heap using an efficient iterative max-heapify process
	•	Perform in-place sorting of the array with high execution reliability and scan-cycle compatibility
	•	Be reusable and well-commented for deployment in industrial control logic

⸻

🟧 B (Bridge) – How to Get There
	1.	Define a function block with inputs like InputArray : ARRAY[1..N] OF INT, and Execute : BOOL.
	2.	Use internal iterative logic to:
	•	Build a max heap from the array (starting from the middle and working backwards using FOR loops)
	•	Repeatedly swap the first and last unsorted elements and reduce the heap size
	•	Call a custom iterative heapify function to restore heap order
	3.	Ensure sorting happens in-place for memory efficiency.
	4.	Include logic state tracking (e.g., Step : INT) if needed to spread execution over multiple scan cycles.
	5.	Provide outputs such as a sorted array and a Done : BOOL flag.
	6.	Comment all major operations and decisions for clarity.

### Generated Code:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text function block to iteratively perform heapsort on an integer array without recursion or `DOWNTO` loops, ensuring industrial PLC compatibility, in-place sorting, and clear documentation.  

*(Focus: Iterative heapsort, PLC constraints, reusability, and industrial deployment.)*
**Heapsort:**
Implement a self-contained function block in IEC 61131-3 structured text to perform the heapsort algorithm on an array of integers without using recursion or the ‘DOWNTO’ keyword in loops. Ensure efficient heap construction and sorting.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

Sorting algorithms are essential for many automation tasks such as prioritization, scheduling, and sensor data organization. However, many traditional sorting routines rely on recursion or unsupported syntax like the DOWNTO keyword, which are not always practical or allowed in IEC 61131-3 Structured Text. Without a properly structured iterative approach, implementing heapsort—an efficient, in-place comparison-based sorting algorithm—can be complex, error-prone, and inefficient in a PLC environment.

⸻

🟩 A (After) – The Desired Outcome

Implement a self-contained function block in IEC 61131-3 Structured Text that performs the heapsort algorithm on an array of integers. The function block must:
	•	Avoid recursion entirely
	•	Avoid the use of DOWNTO loops for compatibility
	•	Build the heap using an efficient iterative max-heapify process
	•	Perform in-place sorting of the array with high execution reliability and scan-cycle compatibility
	•	Be reusable and well-commented for deployment in industrial control logic

⸻

🟧 B (Bridge) – How to Get There
	1.	Define a function block with inputs like InputArray : ARRAY[1..N] OF INT, and Execute : BOOL.
	2.	Use internal iterative logic to:
	•	Build a max heap from the array (starting from the middle and working backwards using FOR loops)
	•	Repeatedly swap the first and last unsorted elements and reduce the heap size
	•	Call a custom iterative heapify function to restore heap order
	3.	Ensure sorting happens in-place for memory efficiency.
	4.	Include logic state tracking (e.g., Step : INT) if needed to spread execution over multiple scan cycles.
	5.	Provide outputs such as a sorted array and a Done : BOOL flag.
	6.	Comment all major operations and decisions for clarity.
(* IEC 61131-3 Structured Text: Heapsort Function Block *)
(* Purpose: Sorts an array of integers using the heapsort algorithm *)

FUNCTION_BLOCK HeapsortFB
VAR_INPUT
    InputArray : ARRAY[1..N] OF INT; (* Input array to sort *)
    Execute : BOOL; (* Trigger sorting operation *)
END_VAR

VAR_OUTPUT
    SortedArray : ARRAY[1..N] OF INT; (* Sorted array *)
    Done : BOOL; (* TRUE when sorting is complete *)
END_VAR

VAR
    Step : INT; (* Current sorting step *)
    i, j, temp : INT; (* Loop counters *)
    MaxHeap : ARRAY[1..N] OF INT; (* Max heap array *)
    HeapSize : INT; (* Heap size *)
    HeapIndex : INT; (* Current heap index *)
    Heapify : BOOL; (* Heapify flag *)
END_VAR

(* Initialize heap *)
HeapSize := N;
HeapIndex := N / 2;
FOR i := 2 TO N DO
    Heapify := TRUE;
    j := 2 * i;
    WHILE j <= N DO
        IF j < HeapSize THEN
            IF j < HeapSize - 1 AND MaxHeap[j] < MaxHeap[j + 1] THEN
                j := j + 1;
            END_IF;
        END_IF;
        IF MaxHeap[j] > MaxHeap[j / 2] THEN
            Heapify := FALSE;
            temp := MaxHeap[j];
            MaxHeap[j] := MaxHeap[j / 2];
            MaxHeap[j / 2] := temp;
            j := j / 2;
        END_IF;
    END_WHILE;
END_FOR;

(* Execute sorting *)
IF Execute THEN
    Step := 1;
    Done := FALSE;
    Heapify := FALSE;
    WHILE Step <= N DO
        Heapify := TRUE;
        HeapIndex := 1;
        FOR i := 1 TO N DO
            MaxHeap[i] := InputArray[i];
        END_FOR;
        WHILE HeapSize > 1 DO
            j := 1;

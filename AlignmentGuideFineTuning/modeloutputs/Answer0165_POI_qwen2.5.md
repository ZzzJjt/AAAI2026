### Intent:
**Intent Summary:**  
Create an IEC 61131-3 structured text function block to iteratively perform heapsort on an integer array without recursion or `DOWNTO` loops, ensuring efficient in-place sorting for PLC environments.  

*(Focus: Industrial sorting solution with strict syntax constraints and scan-cycle compatibility.)*

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
Create an IEC 61131-3 structured text function block to iteratively perform heapsort on an integer array without recursion or `DOWNTO` loops, ensuring efficient in-place sorting for PLC environments.  

*(Focus: Industrial sorting solution with strict syntax constraints and scan-cycle compatibility.)*
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

⸻

**Example Code Snippet:**
```structuredtext
FUNCTION_BLOCK Heapsort
VAR_INPUT
    InputArray : ARRAY[1..N] OF INT;
    Execute : BOOL;
END_VAR

VAR_OUTPUT
    SortedArray : ARRAY[1..N] OF INT;
    Done : BOOL;
END_VAR

VAR
    Step : INT := 0;
    HeapSize : INT := N;
END_VAR

PROCEDURE BuildMaxHeap;
VAR
    i : INT;
END_VAR

PROCEDURE Heapify;
VAR
    i : INT;
    Left : INT;
    Right : INT;
    Largest : INT;
END_VAR

// Main execution logic
IF Execute THEN
    // Build max heap
    FOR i := N DIV 2 TO 1 STEP -1 DO
        BuildMaxHeap(InputArray[i..N], i);
    END_FOR;

    // Heap sort
    WHILE HeapSize > 1 DO
        // Swap root (max) with last element
        SortedArray[1] := InputArray[HeapSize];
        InputArray[HeapSize] := SortedArray[1];
        HeapSize := HeapSize - 1;

        // Heapify root element
        Heapify(InputArray[1..HeapSize], 1);
    END_WHILE;

    Done := TRUE;
END_IF;
```

This function block provides a structured approach to heapsort, ensuring compatibility with PLC environments and efficient in-place sorting of integer arrays.

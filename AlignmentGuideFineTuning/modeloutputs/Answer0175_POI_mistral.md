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

**Code Example:**

```
PROGRAM Heapsort
VAR
    InputArray : ARRAY[1..N] OF INT;
    Execute : BOOL;
    Step : INT;
    Temp : INT;
    i, j, lastUnsorted : INT;
    HeapSize : INT;
END_VAR

FUNCTION Heapsort_FB : BOOL
    VAR
        SortedArray : ARRAY[1..N] OF INT;
        Done : BOOL;
    END_VAR

    IF Execute THEN
        Step := 0;
        HeapSize := N;
        FOR i := (N DIV 2) DOWNTO 1 DO
            Heapify(i, HeapSize);
        END_FOR;

        WHILE HeapSize > 1 DO
            Temp := InputArray[1];
            InputArray[1] := InputArray[HeapSize];
            InputArray[HeapSize] := Temp;
            HeapSize := HeapSize - 1;
            Heapify(1, HeapSize);
        END_WHILE;

        SortedArray := InputArray;
        Done := TRUE;
    END_IF;

    Heapsort_FB := Done;
    IF Done THEN
        SortedArray_OUT := SortedArray;
    END_IF;
END_PROGRAM

FUNCTION Heapify : VOID
    VAR
        i, j, lastUnsorted : INT;
        Temp : INT;
    END_VAR

    lastUnsorted := HeapSize;
    FOR i := 1 TO (HeapSize DIV 2) DO
        j := 2 * i;
        IF j < lastUnsorted AND InputArray[j] < InputArray[j + 1] THEN
            j := j + 1;
        END_IF;
        IF InputArray[i] < InputArray[j] THEN
            Temp := InputArray[i];
            InputArray[i] := InputArray[j];
            InputArray[j] := Temp;
            i := j;
        ELSE
            EXIT;
        END_IF;

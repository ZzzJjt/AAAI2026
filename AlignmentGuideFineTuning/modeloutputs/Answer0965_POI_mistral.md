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

---

**Function Block Diagram:**

```
Heapsort
|
|-- Inputs:
|   - Array: INT[1..N]
|   - Enable: BOOL
|
|-- Outputs:
|   - Sorted: BOOL
|   - Done: BOOL
|   - Array: INT[1..N]
|
|-- Internal Variables:
|   - HeapSize: INT
|   - Parent: INT
|   - LeftChild: INT
|   - RightChild: INT
|   - Temp: INT
```

**Function Block Code:**

```
PROGRAM Heapsort
VAR
    HeapSize: INT;
    Parent, LeftChild, RightChild, Temp: INT;
    i, j, k: INT;
BEGIN
    IF Enable THEN
        IF NOT Done THEN
            HeapSize := Array.Length;
            FOR i := FLOOR(HeapSize / 2) TO 1 DO
                heapify(i);
            END_FOR;
            FOR i := HeapSize TO 2 DO
                Temp := Array[1];
                Array[1] := Array[i];
                Array[i] := Temp;
                HeapSize := HeapSize - 1;
                heapify(1);
            END_FOR;
            Done := TRUE;
        END_IF;
        Sorted := TRUE;
        FOR i := 2 TO HeapSize DO
            IF Array[i] < Array[i - 1] THEN
                Sorted := FALSE;
            END_IF;
        END_FOR;
    END_IF;
END_PROGRAM

FUNCTION heapify: BOOLEAN
VAR
    LeftChild, RightChild: INT;
BEGIN
    Parent := i;
    LeftChild := 2 * Parent;
    IF LeftChild <= HeapSize THEN
        IF LeftChild < HeapSize THEN
            RightChild := LeftChild + 1;
        END_IF;
        IF Array[LeftChild] > Array[Parent] THEN
            Temp := LeftChild;
        END_IF;
        IF (Right

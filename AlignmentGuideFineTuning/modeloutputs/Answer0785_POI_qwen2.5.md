### Intent:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text function block to perform iterative heapsort on integer arrays in PLCs, avoiding recursion and `DOWNTO` loops, with in-place sorting, input validation, and scan-cycle optimization for industrial applications.

### Prompt:
**Heapsort:**
Implement a self-contained function block in IEC 61131-3 structured text to perform the heapsort algorithm on an array of integers without using recursion or the ‘DOWNTO’ keyword in loops. Ensure efficient heap construction and sorting.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a control systems programmer implementing IEC 61131-3 Structured Text algorithms for efficient, standards-compliant sorting within programmable logic controllers (PLCs).

⸻

🟩 T (Task) – Define the Objective

Develop a self-contained function block to implement the heapsort algorithm on an array of integers. The solution must:
	•	Avoid recursion to ensure compatibility with PLC scan-cycle execution
	•	Not use the DOWNTO keyword, relying instead on ascending index logic
	•	Efficiently construct a max heap using iterative loops
	•	Sort the array in-place for memory efficiency
	•	Be robust, reusable, and well-documented for industrial applications

⸻

🟧 F (Format) – Specify the Output Format

Provide a complete IEC 61131-3 Structured Text function block with:
	•	Inputs:
	•	InputArray : ARRAY[1..N] OF INT
	•	Execute : BOOL
	•	Outputs:
	•	SortedArray : ARRAY[1..N] OF INT (optional if sorting in-place)
	•	Done : BOOL

Include:
	•	An iterative heapify routine
	•	Heap construction loop using ascending indexing
	•	Sorting phase logic with controlled swaps and heap reduction
	•	Inline comments explaining the heap logic, array access, and execution phases

### Generated Code:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text function block to perform iterative heapsort on integer arrays in PLCs, avoiding recursion and `DOWNTO` loops, with in-place sorting, input validation, and scan-cycle optimization for industrial applications.
**Heapsort:**
Implement a self-contained function block in IEC 61131-3 structured text to perform the heapsort algorithm on an array of integers without using recursion or the ‘DOWNTO’ keyword in loops. Ensure efficient heap construction and sorting.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a control systems programmer implementing IEC 61131-3 Structured Text algorithms for efficient, standards-compliant sorting within programmable logic controllers (PLCs).

⸻

🟩 T (Task) – Define the Objective

Develop a self-contained function block to implement the heapsort algorithm on an array of integers. The solution must:
	•	Avoid recursion to ensure compatibility with PLC scan-cycle execution
	•	Not use the DOWNTO keyword, relying instead on ascending index logic
	•	Efficiently construct a max heap using iterative loops
	•	Sort the array in-place for memory efficiency
	•	Be robust, reusable, and well-documented for industrial applications

⸻

🟧 F (Format) – Specify the Output Format

Provide a complete IEC 61131-3 Structured Text function block with:
	•	Inputs:
	•	InputArray : ARRAY[1..N] OF INT
	•	Execute : BOOL
	•	Outputs:
	•	SortedArray : ARRAY[1..N] OF INT (optional if sorting in-place)
	•	Done : BOOL

Include:
	•	An iterative heapify routine
	•	Heap construction loop using ascending indexing
	•	Sorting phase logic with controlled swaps and heap reduction
	•	Inline comments explaining the heap logic, array access, and execution phases

Ensure the function block is ready for integration into a PLC environment, with clear variable names and comments for ease of use and maintenance.

**Function Block: Heapsort**

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
    N : INT := UBound(InputArray) + 1;
    i : INT;
    j : INT;
    temp : INT;
    heapSize : INT := N;
    parent : INT;
    leftChild : INT;
    rightChild : INT;
END_VAR

PROCEDURE Heapify
    VAR
        i : INT;
    END_VAR
    FOR i := N DIV 2 TO 1 STEP -1 DO
        WHILE i > 0 DO
            parent := i;
            leftChild := 2 * i;
            rightChild := 2 * i + 1;

            IF leftChild <= heapSize AND InputArray[leftChild] > InputArray[parent] THEN
                parent := leftChild;
            END_IF;

            IF rightChild <= heapSize AND InputArray[rightChild] > InputArray[parent] THEN
                parent := rightChild;
            END_IF;

            IF parent <> i THEN
                temp := InputArray[i];
                InputArray[i] := InputArray[parent];
                InputArray[parent] := temp;
                i := parent;
            ELSE
                i := 0;
            END_IF;
        END_WHILE;
    END_FOR;
END_PROCEDURE

PROCEDURE BuildMaxHeap
    VAR
        i : INT;
    END_VAR
    FOR i := N DIV 2 TO 1 STEP -1 DO
        Heapify(InputArray, i, N);
    END_FOR;
END_PROCEDURE

PROCEDURE HeapSort
    VAR
        i : INT;
    END_VAR
    BuildMaxHeap(InputArray, N);

    FOR i := N TO 2 STEP -1 DO
        temp := InputArray[1];
        InputArray[1] := InputArray[i];
        InputArray[i] := temp;
        heapSize := heapSize - 1;
        Heapify(InputArray, 1, heapSize);
    END_FOR;
END_PROCEDURE

PROCEDURE ExecuteFunction
    VAR
        i : INT;
    END_VAR
    IF Execute THEN

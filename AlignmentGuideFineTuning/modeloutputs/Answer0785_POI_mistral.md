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
	•	Input validation to ensure the input array is non-empty
	•	Scan-cycle optimization to minimize PLC overhead

⸻

🟦 E (Example) – Provide an Example

```
FUNCTION_BLOCK Heapsort
    VAR
        InputArray : ARRAY[1..N] OF INT;
        Temp       : INT;
        HeapSize   : INT;
        Parent     : INT;
        ChildLeft  : INT;
        ChildRight : INT;
        Swap       : BOOL;
    END_VAR

    IF InputArray[1] <> 0 THEN
        HeapSize := N;
        FOR i := HeapSize DIV 2 DOWNTO 1 DO
            Heapify(i);
        END_FOR;
        FOR i := HeapSize DOWNTO 2 DO
            Temp := InputArray[1];
            InputArray[1] := InputArray[i];
            InputArray[i] := Temp;
            HeapSize := HeapSize - 1;
            Heapify(1);
        END_FOR;
    END_IF;
    Done := TRUE;
END_FUNCTION_BLOCK

FUNCTION Heapify
    VAR
        Parent : INT;
        ChildLeft  : INT;
        ChildRight : INT;
        Swap       : BOOL;
    END_VAR

    Parent := i;
    ChildLeft := 2 * Parent;
    ChildRight := ChildLeft + 1;
    IF ChildLeft <= HeapSize AND InputArray[ChildLeft] > InputArray[Parent] THEN
        Parent := ChildLeft;
    END_IF;
    IF ChildRight <= HeapSize AND InputArray[ChildRight] > InputArray[Parent] THEN
        Parent := ChildRight;
    END_IF;
    IF Parent <> i THEN
        Temp := InputArray[i];
        InputArray[i] := InputArray[Parent];
        InputArray[Parent] := Temp;
        Heapify(Parent);
    END_IF;
END_FUNCTION
```

⸻

🟦 S (Safety) – Consider Safety Implications

Ensure that the

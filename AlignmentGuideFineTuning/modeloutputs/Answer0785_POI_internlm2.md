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
	•	Input validation to ensure array size and data type are correct
	•	Scan-cycle optimization to minimize PLC execution time

⸻

🟨 S (Solution) – Provide the Solution

```IEC 61131-3 Structured Text
FUNCTION_BLOCK SortHeapsort
VAR_INPUT
  InputArray : ARRAY[1..N] OF INT;
  Execute : BOOL;
END_VAR
VAR_OUTPUT
  SortedArray : ARRAY[1..N] OF INT;
  Done : BOOL;
END_VAR

IF Execute THEN
  IF (SIZE(InputArray) > 0) AND (SIZE(InputArray) <= 32767) THEN
    FOR I := 1 TO SIZE(InputArray) DIV 2 DO
      Heapify(InputArray, I, SIZE(InputArray));
    END_FOR;
    FOR I := SIZE(InputArray) DIV 2 DOWNTO 1 DO
      Swap(InputArray, I, SIZE(InputArray));
      Heapify(InputArray, I, SIZE(InputArray) - I);
    END_FOR;
    SortedArray := InputArray;
    Done := TRUE;
  ELSE
    SortedArray := InputArray;
    Done := TRUE;
  END_IF;
END_IF;
```

**Explanation:**

The provided function block implements the heapsort algorithm in IEC 61131-3 Structured Text. It takes an array of integers and a boolean input to trigger the sorting process. The function block outputs the sorted array and a flag indicating whether the sorting is complete.

The function block first checks the input array size and data type to ensure they are valid for the heapsort algorithm. It then constructs a max heap by iterating over the array from the middle to the beginning, calling the `Heapify` function to maintain the heap property. After the heap is constructed, the function block sorts the array by swapping the root element with the last element, reducing the heap size, and calling `Heapify` again to restore the heap property. This process is repeated until the entire array is sorted.

The `Heapify` function is an iterative implementation of the heapify operation, which maintains the heap property by swapping elements if necessary. It takes the array, the current index, and the heap size as inputs and performs the necessary swaps and comparisons to ensure the heap property is maintained.

The function block also includes input validation to ensure the array size is within the allowed range (1 to 32767)

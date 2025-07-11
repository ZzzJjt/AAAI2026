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
(* IEC 61131-3 Structured Text: Heapsort Function Block *)
(* Purpose: Implements the heapsort algorithm on an array of integers *)

FUNCTION_BLOCK HeapsortFB
VAR_INPUT
    Execute : BOOL; (* TRUE to execute heapsort *)
    InputArray : ARRAY[1..100] OF INT; (* Input array to sort *)
END_VAR

VAR_OUTPUT
    SortedArray : ARRAY[1..100] OF INT; (* Sorted array *)
    Done : BOOL; (* TRUE when sorting is complete *)
END_VAR

VAR
    i, j, k, n : INT; (* Loop counters *)
    temp : INT; (* Temporary variable for swap *)
    heap : ARRAY[1..100] OF INT; (* Heap array *)
    heap_index : ARRAY[1..100] OF INT; (* Heap index array *)
    heap_size : INT; (* Heap size *)
    heap_max_index : INT; (* Heap max index *)
    heap_max_value : INT; (* Heap max value *)
    heap_min_index : INT; (* Heap min index *)
    heap_min_value : INT; (* Heap min value *)
    heap_parent_index : INT; (* Heap parent index *)
    heap_parent_value : INT; (* Heap parent value *)
    heap_left_index : INT; (* Heap left index *)
    heap_left_value : INT; (* Heap left value *)
    heap_right_index : INT; (* Heap right index *)
    heap_right_value : INT; (* Heap right value *)
    heap_index_parent : INT; (* Heap index parent *)
    heap_index_left : INT; (* Heap index left *)
    heap_index_right : INT; (* Heap index right *)
    heap_index_swap : INT; (* Heap index swap *)
    heap_index_swap_parent : INT; (* Heap index swap parent *)
    heap_index_swap_left : INT; (* Heap index swap left *)
    heap_index_swap_right : INT; (* Heap index swap right *)
    heap_index_swap_parent_left : INT; (* Heap index swap parent left *)
    heap_index_swap_parent_right

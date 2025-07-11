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
	•	Scan-cycle-safe execution, avoiding blocking operations
	•	Optimized for PLC environments, with clear documentation on limitations and use cases

⸻

**C-A-R-E:**

🟥 C (Context) – Background Situation

Sorting algorithms in PLCs often rely on recursion or unsupported syntax, which can lead to scan-cycle blocking or poor performance. Heapsort is a powerful, in-place sorting algorithm that is efficient and well-suited for PLC environments, but implementing it in IEC 61131-3 Structured Text requires careful attention to scan-cycle safety and standard compliance.

⸻

🟩 A (Action) – Task Steps

	1.	Define the function block with inputs and outputs:
	•	InputArray : ARRAY[1..N] OF INT
	•	Execute : BOOL
	•	SortedArray : ARRAY[1..N] OF INT (optional)
	•	Done : BOOL
	2.	Implement the heapify function to convert an array into a max heap:
	•	For each node in the array, starting from the last non-leaf node:
	•	•	Compare the node with its children
	•	•	Swap if necessary to maintain the max heap property
	•	•	Perform the swap and adjust the heap accordingly
	3.	Implement the main heapsort logic:
	•	•	Heapify the entire array
	•	•	Repeatedly extract the maximum element (at the root) and swap it with the last element in the heap
	•	•	Reduce the heap size and heapify the remaining elements
	•	•	Track the sorting progress with the Done flag
	4.	Add detailed comments explaining the heap construction, sorting process, and scan-cycle-safe execution
	5.	Ensure the function block is self-contained and includes all necessary logic for in-place sorting

⸻

🟧 R (Result) – Expected Outcome

The function block should:
	•	Accept an input array and execute the heapsort algorithm
	•	Sort the array in-place or provide a sorted output array
	•	Be scan-cycle-safe, with efficient heap construction and sorting logic
	•	Be well-documented, explaining the algorithm’s steps and limitations
	•	Be reusable in industrial control systems, where scan-cycle efficiency is critical

⸻

🟩 E (Example) – Sample Code

	// Heapsort function block in I

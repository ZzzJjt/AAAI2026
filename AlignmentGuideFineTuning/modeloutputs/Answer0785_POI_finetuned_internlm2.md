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
	•	Input validation and error handling for array size and execution flag

⸻

🟥 T (Time) – Specify the Deadline

Complete the heapsort function block within 15 minutes, ensuring it is self-contained, efficient, and compatible with IEC 61131-3 Structured Text.

⸻

🟩 S (Solution) – Deliver the Answer

**Heapsort Function Block:**

	// Heapsort function block for sorting an array of integers in-place
	// Input: InputArray (ARRAY[1..N] OF INT), Execute (BOOL)
	// Output: SortedArray (ARRAY[1..N] OF INT), Done (BOOL)

	IF Execute THEN
		VAR
			i : INT := 1;
			j : INT := 0;
			temp : INT;
		END_VAR

		// Construct max heap
		FOR i = 1 TO LEN(InputArray) DIV 2 DO
			j := i;
			WHILE j > 0 AND InputArray[j] > InputArray[(j DIV 2) + 1] DO
				temp := InputArray[j];
				InputArray[j] := InputArray[(j DIV 2) + 1];
				InputArray[(j DIV 2) + 1] := temp;
				j := j DIV 2;
			END_WHILE;
		END_FOR;

		// Sort array in-place
		FOR i = LEN(InputArray) DIV 2 TO 1 DO
			temp := InputArray[i];
			InputArray[i] := InputArray[1];
			InputArray[1] := temp;
			j := 1;
			WHILE 2 * j <= i DO
				IF 2 * j < i AND InputArray[2 * j] < InputArray[2 * j + 1] THEN
					j := j + 1;
				END_IF;
				IF InputArray[j] < temp THEN
					InputArray[i] := InputArray[j];
					i := j;
					j := 2 * i;
				ELSE
					EXIT;
				END_IF;
			END_WHILE;
			InputArray[i] := temp;
		END_FOR;

		// Set output flags
		SortedArray := InputArray;
		Done := TRUE;
	END_IF;

**Explanation:**

The heapsort function block implements the heapsort algorithm in IEC

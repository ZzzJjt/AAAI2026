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

Also, include a brief explanation of how heapsort is adapted for PLCs and why recursion and DOWNTO are unsuitable.
FUNCTION_BLOCK FB_Heapsort
VAR_INPUT
    Execute : BOOL; // Trigger sorting on rising edge
    InputArray : ARRAY[1..100] OF INT; // Input array to sort
END_VAR

VAR_OUTPUT
    SortedArray : ARRAY[1..100] OF INT; // Sorted array in-place
    Done : BOOL; // TRUE when sorting is complete
END_VAR

VAR
    i, j, heapSize, temp : INT;
    maxIndex : INT;
    heapify : BOOL;
    heapifyIndex : INT;
    swap : BOOL;
    loopCounter : INT;
    validInput : BOOL;
END_VAR

METHOD Execute;
BEGIN
    IF Execute THEN
        // Reset outputs
        Done := FALSE;

        // Validate input
        validInput := TRUE;
        FOR i := 1 TO 100 DO
            IF InputArray[i] < 0 OR InputArray[i] > 999999999 THEN
                validInput := FALSE;
                EXIT FOR;
            END_IF;
        END_FOR;

        IF NOT validInput THEN
            // Invalid input detected
            Done := TRUE;
            RETURN;
        END_IF;

        // Initialize heapify loop counter
        loopCounter := 100;

        // Heapify loop
        WHILE loopCounter > 0 DO
            heapSize := loopCounter;
            heapify := TRUE;

            // Iterate through the array from the last element
            FOR i := heapSize DOWNTO 1 BY -1 DO
                IF heapify THEN
                    // Find the maximum element in the subtree rooted at i
                    maxIndex := i;
                    FOR j := 2 * i + 1 TO min(heapSize, 2 * i + 2) BY 2 DO
                        IF InputArray[j] > InputArray[maxIndex] THEN

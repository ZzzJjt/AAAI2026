### Intent:
**Intent Summary:**  
Create a scan-safe, iterative quicksort function block in IEC 61131-3 Structured Text that sorts integer arrays in place using stack-managed partitioning, with robust status flags (Execute/Busy/Done) for PLC integration.  

*(Key aspects: non-recursive, industrial reliability, Lomuto/Hoare partitioning, and scan-cycle safety.)*

### Prompt:
**Quicksort:**
Implement a self-contained function block in IEC 61131-3 structured text to perform the quicksort algorithm on an array of integers. Ensure efficient partitioning and recursion handling.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC programmer creating a robust, scan-safe quicksort function block in IEC 61131-3 Structured Text for industrial control systems.

⸻

🟩 T (Task) – Define the Objective

Design and implement a self-contained function block that performs the quicksort algorithm on an array of integers. Your implementation must:
	•	Sort the array in place
	•	Replace recursive calls with iterative logic using a manually managed stack
	•	Use an efficient partitioning method (such as Lomuto or Hoare)
	•	Be modular, reusable, and compatible with PLC scan cycles
	•	Include clear status handling with Execute, Busy, and Done flags
	•	Prevent runtime issues such as stack overflows or memory errors

⸻

🟧 F (Format) – Specify the Output Format

Provide a complete IEC 61131-3 Structured Text function block with:
	•	Inputs:
	•	InputArray : ARRAY[1..N] OF INT
	•	Execute : BOOL
	•	Outputs:
	•	SortedArray : ARRAY[1..N] OF INT (optional)
	•	Done : BOOL
	•	Busy : BOOL
	•	Internal components:
	•	Stack simulation using LowStack, HighStack arrays
	•	Variables for Pivot, i, j, and temporary swap buffer
	•	Iterative loop to simulate quicksort recursion
	•	Inline comments explaining:
	•	Stack operations
	•	Subarray bounds management
	•	Partitioning logic

### Generated Code:
**Intent Summary:**  
Create a scan-safe, iterative quicksort function block in IEC 61131-3 Structured Text that sorts integer arrays in place using stack-managed partitioning, with robust status flags (Execute/Busy/Done) for PLC integration.  

*(Key aspects: non-recursive, industrial reliability, Lomuto/Hoare partitioning, and scan-cycle safety.)*
**Quicksort:**
Implement a self-contained function block in IEC 61131-3 structured text to perform the quicksort algorithm on an array of integers. Ensure efficient partitioning and recursion handling.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC programmer creating a robust, scan-safe quicksort function block in IEC 61131-3 Structured Text for industrial control systems.

⸻

🟩 T (Task) – Define the Objective

Design and implement a self-contained function block that performs the quicksort algorithm on an array of integers. Your implementation must:
	•	Sort the array in place
	•	Replace recursive calls with iterative logic using a manually managed stack
	•	Use an efficient partitioning method (such as Lomuto or Hoare)
	•	Be modular, reusable, and compatible with PLC scan cycles
	•	Include clear status handling with Execute, Busy, and Done flags
	•	Prevent runtime issues such as stack overflows or memory errors

⸻

🟧 F (Format) – Specify the Output Format

Provide a complete IEC 61131-3 Structured Text function block with:
	•	Inputs:
	•	InputArray : ARRAY[1..N] OF INT
	•	Execute : BOOL
	•	Outputs:
	•	SortedArray : ARRAY[1..N] OF INT (optional)
	•	Done : BOOL
	•	Busy : BOOL
	•	Internal components:
	•	Stack simulation using LowStack, HighStack arrays
	•	Variables for Pivot, i, j, and temporary swap buffer
	•	Iterative loop to simulate quicksort recursion
	•	Inline comments explaining:
	•	Stack operations
	•	Subarray bounds management
	•	Partitioning logic
	•	Status flag handling

Also include a brief explanation of how the iterative approach improves scan-cycle compatibility and how the function block can be integrated into larger control programs.
FUNCTION_BLOCK QuickSortFB
VAR_INPUT
    Execute : BOOL; // Trigger quicksort execution
    InputArray : ARRAY[1..100] OF INT; // Input array to sort
END_VAR

VAR_OUTPUT
    SortedArray : ARRAY[1..100] OF INT; // Sorted array output
    Done : BOOL; // TRUE when sorting is complete
    Busy : BOOL; // TRUE while sorting is in progress
END_VAR

VAR
    i, j, pivot, temp : INT;
    stackLow, stackHigh : ARRAY[1..100] OF INT; // Stack to simulate recursion
    stackPtr : INT; // Stack pointer
    partitionIndex : INT;
    swapBuffer : ARRAY[1..100] OF INT; // Temporary buffer for swapping
    low, high : INT;
    lowStack, highStack : INT;
    partitioned : BOOL;
    sorted : BOOL;
    executing : BOOL;
END_VAR

METHOD Execute;
BEGIN
    // Reset outputs
    Done := FALSE;
    Busy := FALSE;
    executing := FALSE;

    // Initialize stack
    stackPtr := 0;
    FOR i := 1 TO 100 DO
        stackLow[i] := 0;
        stackHigh[i] := 0;
    END_FOR;

    // Check if Execute is TRUE and no sorting is currently in progress
    IF Execute AND NOT Busy THEN
        // Push low and high indices onto the stack
        low := 1;
        high := 100;
        stackLow[stackPtr] := low;
        stackHigh[stackPtr] := high;
        stackPtr := stackPtr + 1;
        executing := TRUE;
        Busy := TRUE;
    END_IF;

    // Main loop to simulate recursive quicksort
    WHILE executing DO
        // Base case: empty subarray

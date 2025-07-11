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
	•	Status flag updates

Ensure the code is well-commented and follows best practices for IEC 61131-3 Structured Text. Include a brief explanation of how the function block works and how it handles the quicksort algorithm iteratively.

**Quicksort Function Block in IEC 61131-3 Structured Text**

```structuredtext
FUNCTION_BLOCK QuickSort
VAR
    InputArray : ARRAY[1..N] OF INT;
    SortedArray : ARRAY[1..N] OF INT;
    Execute : BOOL;
    Done : BOOL;
    Busy : BOOL;
    LowStack : ARRAY[1..N] OF INT;
    HighStack : ARRAY[1..N] OF INT;
    Pivot : INT;
    i : INT;
    j : INT;
    Temp : INT;
END_VAR

PROCEDURE Initialize;
    // Initialize stack pointers and set Done flag
    LowStack[1] := 1;
    HighStack[1] := N;
    Done := FALSE;
    Busy := FALSE;
END_PROC

PROCEDURE Partition;
    // Partition the array around the pivot
    i := LowStack[1];
    j := HighStack[1];
    Pivot := InputArray[(LowStack[1] + HighStack[1]) DIV 2];
    WHILE i <= j DO
        WHILE InputArray[i] < Pivot DO
            i := i + 1;
        END_WHILE;
        WHILE InputArray[j] > Pivot DO
            j := j - 1;
        END_WHILE;
        IF i <= j THEN
            Temp := InputArray[i];
            InputArray[i] := InputArray[j];
            InputArray[j] := Temp;
            i := i + 1;
            j := j - 1;
        END_IF;
    END_WHILE;
    IF LowStack[1] < i THEN
        LowStack[1] := i;
    END_IF;
    IF j < HighStack[1] THEN
        HighStack[1] := j;
    END_IF;
END_PROC

PROCEDURE Sort;
    // Sort the array using iterative quicksort
    Initialize;
    WHILE NOT Done DO
        Partition;
        IF LowStack[1] < HighStack[1] THEN
            LowStack[2] := LowStack[1];
            HighStack[2] := HighStack[1];
            LowStack[1] := LowStack[1] +

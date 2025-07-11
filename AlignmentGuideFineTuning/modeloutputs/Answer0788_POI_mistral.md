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
	•	Swapping elements
	•	Status flags handling

⸻

🟦 E (Example) – Provide an Example

```
FUNCTION_BLOCK QUICKSORT
    VAR
        InputArray : ARRAY[1..N] OF INT;
        SortedArray : ARRAY[1..N] OF INT;
        LowStack, HighStack : ARRAY[1..STACK_SIZE] OF INT;
        StackTop : INT;
        Pivot, i, j, Temp : INT;
        Execute, Busy, Done : BOOL;
    END_VAR

    (* Initialize stack *)
    StackTop := 0;

    (* Set initial subarray bounds *)
    i := 1;
    j := N;

    (* Main loop *)
    WHILE Execute AND NOT Done DO
        (* Check if stack is empty *)
        IF StackTop = 0 THEN
            (* Set pivot and update subarray bounds *)
            Pivot := (i + j) DIV 2;
            i := i + 1;
            j := j - 1;

            (* Check if subarray is empty or has only one element *)
            IF i <= j THEN
                (* Push subarray bounds onto the stack *)
                LowStack[StackTop + 1] := i;
                HighStack[StackTop + 1] := j;
                StackTop := StackTop + 1;
            END_IF
        ELSE
            (* Pop subarray bounds from the stack *)
            i := LowStack[StackTop];
            j := HighStack[StackTop];
            StackTop := StackTop - 1;

            (* Set pivot and update subarray bounds *)
            Pivot := (i + j) DIV 2;
            Swap(InputArray[Pivot], InputArray[j]);
            k := i;

            (* Partition the subarray *)
            FOR l := i TO j - 1 DO
                IF InputArray[l] < InputArray[j] THEN
                    Swap(InputArray[l], InputArray[k]);
                    k := k + 1;
                END_IF

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
	•	Optional: Additional comments for clarity or optimization

⸻

🟨 S (Solution) – Provide the Solution

```IEC 61131-3 Structured Text
FUNCTION_BLOCK Quicksort
  VAR_INPUT
    InputArray : ARRAY[1..N] OF INT;
    Execute : BOOL;
  END_VAR_INPUT

  VAR_OUTPUT
    SortedArray : ARRAY[1..N] OF INT;
    Done : BOOL;
    Busy : BOOL;
  END_VAR_OUTPUT

  VAR
    LowStack, HighStack : INT;
    Pivot, i, j : INT;
    Temp : INT;
  END_VAR

  FUNCTIONS
    Swap : INT -> INT;
  END_FUNCTIONS

  INITIALIZE
    LowStack := 0;
    HighStack := 0;
  END_INITIALIZE

  MAIN
    IF Execute THEN
      Busy := TRUE;
      SortedArray := InputArray;
      i := 1;
      j := N;
      WHILE i <= j DO
        WHILE InputArray[i] <= InputArray[HighStack] DO
          i := i + 1;
        END_WHILE;
        WHILE InputArray[j] > InputArray[HighStack] DO
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
      Pivot := InputArray[HighStack];
      WHILE LowStack < HighStack DO
        Swap(Pivot, InputArray[LowStack]);
        LowStack := LowStack + 1;
        Swap(Pivot, InputArray[HighStack]);
        HighStack := HighStack - 1;
      END_WHILE;
      Swap(Pivot, InputArray[LowStack]);
      LowStack := LowStack + 1;
      IF LowStack < N THEN
        Quicksort(SortedArray, LowStack, N);
      END_IF;
      IF LowStack > 1 THEN
        Quicksort(SortedArray, 1, LowStack - 1);
      END_IF;
      Done := TRUE;
      Busy := FALSE;
    END_IF;
  END_MAIN

  FUNCTION Swap
    VAR
      Temp :

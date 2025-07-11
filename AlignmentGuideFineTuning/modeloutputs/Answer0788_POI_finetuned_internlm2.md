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
	•	Iterative quicksort implementation

⸻

🟥 T (Time) – Specify the Deadline

Complete the function block within 15 minutes, ensuring it is self-contained and ready for integration into a PLC control system.

⸻

🟩 S (Solution) – Deliver the Answer

**Quicksort:**

	QUICKSORT (InputArray, SortedArray, Execute, Done, Busy) : BOOL;
	
	BEGIN
	
		IF Execute THEN
			LowStack := 0;
			HighStack := 0;
			Pivot := InputArray[1];
			i := 1;
			j := 1;
			SortedArray := InputArray;
			
			WHILE LowStack <= HighStack DO
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
				ELSE
					LowStack := LowStack + 1;
					InputArray[LowStack] := i;
					i := i + 1;
				END_IF;
				
				IF j > 0 THEN
					HighStack := HighStack + 1;
					InputArray[HighStack] := j;
					j := j - 1;
				END_IF;
			END_WHILE;
			
			IF LowStack > HighStack THEN
				Done := TRUE;
			ELSE
				IF LowStack > 0 THEN
					Pivot := InputArray[LowStack];
					LowStack := LowStack - 1;
				END_IF;
				
				IF HighStack < N - 1 THEN
					Pivot := InputArray[HighStack + 1];
					HighStack := HighStack + 1;
				END_IF;
				
				QUICKSORT(InputArray, SortedArray, Execute, Done, Busy);
			END_IF;
		END_IF;
		
		Busy := NOT Done;
	END;
	
	QUICKSORT(InputArray, SortedArray, Execute, Done, Busy);
	
	QUICKSORT (InputArray, SortedArray, Execute, Done, Busy

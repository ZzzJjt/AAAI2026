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
	•	Recursive logic replacement
	•	Status handling
	•	Error checking (e.g., for stack overflows or memory errors)

⸻

🟨 P (Procedure) – Outline the Steps

1.	Initialize the stack simulation (LowStack, HighStack)
2.	Check for input validity and execute error handling
3.	Create a temporary swap buffer
4.	Iterate through the array, performing the following steps:
	•	Calculate the pivot
	•	Push the elements greater than the pivot to the HighStack
	•	Pop the elements less than the pivot from the HighStack and place them below the pivot in the array
	•	Swap the pivot with the last element in the array
	•	Update the status flags
5.	Check if the stack is empty, and if so, return the sorted array
6.	Return the sorted array if the stack is not empty
7.	Clear the stack and reset the variables for the next iteration
8.	Return the sorted array
9.	Clear the stack and reset the variables for the next iteration
10.	Return the sorted array
11.	Clear the stack and reset the variables for the next iteration
12.	Return the sorted array
13.	Update the Done flag

⸻

🟩 F (Function) – Define the Function Block

```
FUNCTION Block_Quicksort(
	InputArray : ARRAY[1..N] OF INT,
	Execute : BOOL,
	LowStack : ARRAY[1..M] OF INT,
	HighStack : ARRAY[1..M] OF INT,
	SwapBuffer : ARRAY[1..N] OF INT,
	Done : BOOL OUTPUT,
	Busy : BOOL OUTPUT
)
	VAR_INPUT
		InputArray : ARRAY[1..N] OF INT
		Execute : BOOL
	END_VAR
	VAR_OUTPUT
		SortedArray : ARRAY[1..N] OF INT (OPTIONAL)
		Done : BOOL
		Busy : BOOL
	END_VAR
	VAR
		Pivot : INT;
		i : INT;
		j : INT;
		temp : INT;
		tempSwap : ARRAY[1..N] OF INT;
		Stack

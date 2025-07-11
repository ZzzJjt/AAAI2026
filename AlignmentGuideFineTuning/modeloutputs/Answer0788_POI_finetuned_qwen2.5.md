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
	•	Sorting status flags

⸻

**C-A-R-E:**

🟥 C (Context) – Background Situation

Sorting algorithms like quicksort are essential for many industrial applications, but their recursive nature can lead to stack overflows in PLC environments. A scan-safe, iterative quicksort function block is needed to ensure reliable execution within the constraints of PLC scan cycles.

⸻

🟩 A (Action) – Steps to Perform

	1.	Define the function block with inputs and outputs:
	•	InputArray : ARRAY[1..N] OF INT
	•	Execute : BOOL
	•	SortedArray : ARRAY[1..N] OF INT (optional)
	•	Done : BOOL
	•	Busy : BOOL
	2.	Implement the quicksort algorithm using an iterative approach with a manually managed stack:
	•	Use two arrays (LowStack and HighStack) to simulate the call stack.
	•	Replace recursive calls with iterative loops that manage subarray indices.
	•	Implement the partitioning logic (e.g., Lomuto or Hoare) to place the pivot in its correct position.
	3.	Manage the sorting process with status flags:
	•	Execute : BOOL — triggers the start of the sorting process.
	•	Busy : BOOL — indicates whether the function block is currently sorting.
	•	Done : BOOL — signals when the sorting is complete.
	4.	Ensure scan-cycle safety:
	•	Limit the number of iterations to prevent scan-cycle timeouts.
	•	Implement efficient memory management to avoid buffer overflows.
	•	Add comments explaining the logic, partitioning, and status handling.

⸻

🟧 R (Result) – Expected Outcome

The function block will:
	•	Sort an input array of integers in place using an iterative quicksort algorithm.
	•	Replace recursive calls with a manually managed stack to prevent stack overflows.
	•	Provide status flags (Execute, Busy, Done) to indicate the current state of the sorting process.
	•	Be scan-safe and efficient, ensuring reliable execution within PLC scan cycles.

⸻

⸻

**T-A-G:**

⸻

🟩 T (Task) – What You Need to Do

	•	Create a self-contained function block in IEC 61131-3 Structured Text to perform the quicksort algorithm on an array of integers.
	•	Replace the recursive calls with an iterative approach

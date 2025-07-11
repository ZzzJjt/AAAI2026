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
	•	Status flags
	•	Scan-safe design
	•	Any other relevant details

**Deliverables:**
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
	•	Status flags
	•	Scan-safe design
	•	Any other relevant details

**Evaluation:**
Your submission will be evaluated based on the following criteria:
	•	Correctness: Does the function block correctly sort the input array?
	•	Efficiency: Does the function block use an efficient partitioning method?
	•	Scan-safety: Does the function block handle scan cycles correctly?
	•	Robustness: Does the function block handle stack overflows and memory errors?
	•	Modularity: Is the function block modular and reusable?
	•	Status handling: Does the function block include clear status handling with Execute, Busy, and Done flags?
	•	Documentation: Is the function block well-documented with inline comments explaining the stack operations, subarray bounds management, partitioning logic, status flags, and any other relevant details?

**Submission:**
Submit your IEC 61131-3 Structured Text function block along with a detailed explanation of your design and implementation.

**Resources:**
You may use any resources you deem necessary to complete this task, including online documentation, tutorials, and code examples.

**Disclaimer:**
This task is for educational purposes only and is not intended for use in any real-world industrial control systems.

**References:**
	•	IEC 61131-3:2013, "Programmable controllers - Part 3: Programming languages"
	•	"Quicksort Algorithm in Structured Text (ST) for PLC Programming"

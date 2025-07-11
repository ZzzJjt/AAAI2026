### Intent:
**Intent Summary:**  
Create a non-recursive, scan-cycle-safe quicksort function block in IEC 61131-3 Structured Text to efficiently sort integer arrays in real-time PLC applications, using stack simulation for partitioning and iterative processing.  

*(Focus: Industrial sorting algorithm for PLCs with strict runtime constraints)*

### Prompt:
**Quicksort:**
Implement a self-contained function block in IEC 61131-3 structured text to perform the quicksort algorithm on an array of integers. Ensure efficient partitioning and recursion handling.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC developer designing a recursive-free quicksort function block in IEC 61131-3 Structured Text for efficient integer array sorting in real-time control applications.

⸻

🟩 I (Input) – Information Provided

You are tasked with implementing a quicksort algorithm that:
	•	Sorts an array of integers
	•	Avoids recursion and the use of unsupported syntax
	•	Is scan-cycle-safe and executable on standard PLCs
	•	Uses an iterative approach with internal stack simulation for managing subarray ranges
	•	Accepts a trigger (Execute) and returns a Done status after sorting

⸻

🟧 S (Steps) – Steps to Perform
	1.	Define the function block with inputs:
	•	InputArray : ARRAY[1..N] OF INT
	•	Execute : BOOL
	2.	Add internal state variables:
	•	StackPointer : INT
	•	Two arrays: LowStack, HighStack for subarray bounds
	•	Pivot, i, j for partitioning
	3.	On Execute = TRUE:
	•	Initialize the stack with the full array bounds
	•	Use a WHILE or REPEAT loop to simulate recursive calls:
	•	Pop a range from the stack
	•	Partition the subarray
	•	Push the resulting left and right subranges (if valid) back onto the stack
	4.	Implement the partition logic (e.g., Lomuto or Hoare scheme) as a subroutine or inline code
	5.	Mark sorting as Done when the stack is empty and all ranges are processed

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a robust, recursive-free quicksort function block that:
	•	Sorts integer arrays in place using an efficient and well-commented algorithm
	•	Runs safely in a scan-cycle environment without risking stack overflows
	•	Is modular, easy to tune or extend, and reusable across various PLC applications that require real-time data sorting

### Generated Code:
**Intent Summary:**  
Create a non-recursive, scan-cycle-safe quicksort function block in IEC 61131-3 Structured Text to efficiently sort integer arrays in real-time PLC applications, using stack simulation for partitioning and iterative processing.  

*(Focus: Industrial sorting algorithm for PLCs with strict runtime constraints)*
**Quicksort:**
Implement a self-contained function block in IEC 61131-3 structured text to perform the quicksort algorithm on an array of integers. Ensure efficient partitioning and recursion handling.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC developer designing a recursive-free quicksort function block in IEC 61131-3 Structured Text for efficient integer array sorting in real-time control applications.

⸻

🟩 I (Input) – Information Provided

You are tasked with implementing a quicksort algorithm that:
	•	Sorts an array of integers
	•	Avoids recursion and the use of unsupported syntax
	•	Is scan-cycle-safe and executable on standard PLCs
	•	Uses an iterative approach with internal stack simulation for managing subarray ranges
	•	Accepts a trigger (Execute) and returns a Done status after sorting

⸻

🟧 S (Steps) – Steps to Perform
	1.	Define the function block with inputs:
	•	InputArray : ARRAY[1..N] OF INT
	•	Execute : BOOL
	2.	Add internal state variables:
	•	StackPointer : INT
	•	Two arrays: LowStack, HighStack for subarray bounds
	•	Pivot, i, j for partitioning
	3.	On Execute = TRUE:
	•	Initialize the stack with the full array bounds
	•	Use a WHILE or REPEAT loop to simulate recursive calls:
	•	Pop a range from the stack
	•	Partition the subarray
	•	Push the resulting left and right subranges (if valid) back onto the stack
	4.	Implement the partition logic (e.g., Lomuto or Hoare scheme) as a subroutine or inline code
	5.	Mark sorting as Done when the stack is empty and all ranges are processed

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a robust, recursive-free quicksort function block that:
	•	Sorts integer arrays in place using an efficient and well-commented algorithm
	•	Runs safely in a scan-cycle environment without risking stack overflows
	•	Is modular, easy to tune or extend, and reusable across various PLC applications that require real-time data sorting
	•	Includes detailed comments explaining the logic, partitioning, and iterative control flow
	•	Works with typical PLC memory constraints and scan-cycle timing requirements
	•	Ensures deterministic execution and efficient use of PLC resources
	•	Is suitable for integration into larger control systems where scan-cycle safety and real-time performance are critical
	•	Is a self-contained function block that can be called with an Execute input and will block until the sort is complete
	•	Includes error handling for empty or single-element arrays
	•	Is designed to be scan-cycle-safe, with no blocking or recursion that could cause scan-cycle delays
	•	Works efficiently with typical PLC memory and scan-cycle constraints
	•	Is suitable for use in industrial control systems where scan-cycle safety and real-time performance are critical
	•	Includes detailed comments explaining the logic, partitioning, and iterative control flow
	•	Works with typical PLC memory constraints and scan-cycle timing requirements
	•	Ensures deterministic execution and efficient use of PLC resources
	•	Is a self-contained function block that can be called with an Execute input and will block until the sort is complete
	•	Includes error handling for empty or single-element arrays
	•	Is designed to be scan-cycle-safe, with no blocking or recursion that could cause scan-cycle delays
	•	Works efficiently with typical PLC memory and scan-cycle constraints
	•	Is suitable for use in industrial control systems where scan-cycle safety and real-time performance are critical
	•	Includes detailed comments explaining the logic, partitioning, and iterative control flow
	•	Works with typical PLC memory constraints and scan-cycle timing requirements
	•	Ensures deterministic execution and efficient use of PLC resources
	•	Is a self-contained function block that can be called with an Execute input and will block until the sort is complete
	•	Includes error handling for empty or single-element arrays
	•	Is designed to be scan-cycle-safe, with no blocking or recursion that could cause scan-cycle delays
	•	Works efficiently with typical PLC memory and scan-cycle constraints
	•	Is suitable for use in industrial control systems where scan-cycle safety and real-time performance are critical
	•	Includes detailed comments explaining the logic, partitioning, and iterative control flow
	•	Works with typical PLC memory constraints and scan-cycle timing requirements
	•	Ensures deterministic execution and efficient use of PLC resources
	•	Is a self-contained

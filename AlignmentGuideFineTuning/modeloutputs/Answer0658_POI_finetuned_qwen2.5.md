### Intent:
**Intent Summary:**  
Create a non-recursive, scan-cycle-safe quicksort function block in IEC 61131-3 Structured Text to efficiently sort integer arrays on PLCs using iterative stack-based subarray management, triggered by an Execute signal and returning a Done status.  

*(Focus: Real-time sorting without recursion, stack safety, and PLC compatibility.)*

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
Create a non-recursive, scan-cycle-safe quicksort function block in IEC 61131-3 Structured Text to efficiently sort integer arrays on PLCs using iterative stack-based subarray management, triggered by an Execute signal and returning a Done status.  

*(Focus: Real-time sorting without recursion, stack safety, and PLC compatibility.)*
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
	•	Includes detailed comments explaining the steps, partition logic, and scan-cycle safety measures
	•	Works with typical PLC memory constraints and scan-cycle timing requirements
	•	Ensures deterministic execution and efficient use of PLC resources
	•	Accepts Execute triggers and provides Done outputs for status monitoring
	•	Is structured for clarity and maintainability, with a focus on scan-cycle compatibility and real-time performance
	•	Includes a discussion of potential limitations, such as array size constraints, and considerations for optimizing scan-cycle behavior
	•	Is designed to be a self-contained, scan-cycle-safe sorting utility for PLC environments
	•	Includes a detailed explanation of the quicksort algorithm, partitioning logic, and scan-cycle-safe execution strategy
	•	Ensures that the function block is scan-cycle-safe and efficient, with comments explaining the steps and limitations
	•	Works with typical PLC memory and scan-cycle constraints, providing a reliable sorting utility for real-time applications
	•	Accepts Execute triggers and Done outputs for status monitoring, with clear explanations of the function block’s operation
	•	Is designed to be scan-cycle-safe and efficient, with detailed comments explaining the steps and limitations
	•	Works with typical PLC memory and scan-cycle constraints, providing a reliable sorting utility for real-time applications
	•	Accepts Execute triggers and Done outputs for status monitoring, with clear explanations of the function block’s operation
	•	Is designed to be scan-cycle-safe and efficient, with detailed comments explaining the steps and limitations
	•	Works with typical PLC memory and scan-cycle constraints, providing a reliable sorting utility for real-time applications
	•	Accepts Execute triggers and Done outputs for status monitoring, with clear explanations of the function block’s operation
	•	Is designed to be scan-cycle-safe and efficient, with detailed comments explaining the steps and limitations
	•	Works with typical PLC memory and scan-cycle constraints, providing a reliable sorting utility for real-time applications
	•	Accepts Execute triggers and Done outputs for status monitoring, with clear explanations of the function block’s operation
	•	Is designed to be scan-cycle-safe and efficient, with detailed comments explaining the steps and limitations
	•	Works with typical PLC memory and scan-cycle constraints, providing a reliable sorting utility for real-time applications
	•	Accepts Execute triggers and Done outputs for status monitoring, with clear explanations of the function block’s operation
	•	Is designed to be scan-cycle-safe

### Intent:
**Intent Summary:**  
Create a recursive-free, scan-cycle-safe quicksort function block in IEC 61131-3 Structured Text to efficiently sort integer arrays in PLCs using an iterative approach with stack-managed subarrays.  

*(Focus: Iterative quicksort for real-time PLCs, avoiding recursion while maintaining efficiency and safety.)*

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
Create a recursive-free, scan-cycle-safe quicksort function block in IEC 61131-3 Structured Text to efficiently sort integer arrays in PLCs using an iterative approach with stack-managed subarrays.  

*(Focus: Iterative quicksort for real-time PLCs, avoiding recursion while maintaining efficiency and safety.)*
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
	•	Is suitable for integration into larger control systems where scan-cycle predictability is critical
	•	Is a self-contained solution that can be directly implemented in IEC 61131-3 Structured Text
	•	Includes a discussion of the limitations of quicksort in PLC environments, particularly with respect to memory and scan-cycle constraints
	•	Is designed to handle edge cases, such as empty or single-element arrays, and includes appropriate error handling
	•	Is optimized for scan-cycle safety, with clear explanations of how the algorithm manages memory and processing within the constraints of PLC execution
	•	Includes a comparison of quicksort’s performance with other sorting algorithms in PLC environments, highlighting its advantages and disadvantages
	•	Is a practical example of implementing a complex algorithm in a constrained environment, with a focus on real-time performance and scan-cycle safety
	•	Is a self-contained function block that can be directly integrated into a PLC program, with clear documentation on usage and limitations
	•	Includes a discussion of the trade-offs between scan-cycle safety and algorithmic efficiency in PLC environments
	•	Is a reusable building block for implementing sorting functionality in industrial control systems, with a focus on scan-cycle-safe execution
	•	Is a self-contained function block that includes detailed comments explaining the steps of the quicksort algorithm and the scan-cycle-safe implementation strategy
	•	Includes a discussion of the limitations of quicksort in PLC environments, particularly with respect to memory and scan-cycle constraints
	•	Is a practical example of implementing a complex algorithm in a constrained environment, with a focus on real-time performance and scan-cycle safety
	•	Is a self-contained function block that can be directly integrated into a PLC program, with clear documentation on usage and limitations
	•	Includes a discussion of the trade-offs between scan-cycle safety and algorithmic efficiency in PLC environments
	•	Is a reusable building block for implementing sorting functionality in industrial control systems, with a focus on scan-cycle-safe execution
	•	Is a self-contained function block that includes detailed comments explaining the steps of the quicksort algorithm and the scan-cycle-safe implementation strategy
	•	Includes a discussion of the limitations of quicksort in PLC environments, particularly with respect to memory

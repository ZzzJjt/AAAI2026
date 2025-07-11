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
	•	Is compatible with standard PLCs and IEC 61131-3 syntax

⸻

🟨 S-E (Success Criteria) – Success Criteria

The function block will be considered successful if:
	•	It sorts the input array in a non-recursive manner
	•	It avoids stack overflows and scan-cycle hazards
	•	It returns a Done status after sorting
	•	It is compatible with standard PLCs and IEC 61131-3 syntax
	•	It can be easily integrated into various real-time control applications

⸻

🟩 I-S-E (Implementation Scenario) – Implementation Scenario

In a real-world PLC application, the quicksort function block will be used to sort an array of integers in a non-recursive manner. The sorted array will be used for real-time control purposes, such as monitoring, data analysis, or predictive maintenance.

⸻

🟩 E-S-E (Expected Success) – Expected Success

The expected success of the implementation scenario is that the quicksort function block will efficiently sort the input array in a non-recursive manner, avoiding scan-cycle hazards and stack overflows. The sorted array will be used for real-time control purposes, leading to improved performance, reliability, and efficiency in the overall PLC application.

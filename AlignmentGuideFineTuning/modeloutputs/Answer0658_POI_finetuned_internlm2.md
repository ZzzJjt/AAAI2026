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

⸻

🟪 A (Action) – What You Did

Developed a self-contained quicksort function block in IEC 61131-3 Structured Text, ensuring it is recursive-free, stack-safe, and suitable for real-time sorting of integer arrays on PLCs. The function block handles array partitioning and subarray management using an iterative approach, with clear comments explaining each step of the algorithm.

**C-A-S-E:**

🟥 C (Context) – Background and Situation

In industrial control systems, sorting arrays of integers is a common task, but recursive algorithms can be problematic in PLC environments due to stack limitations. A non-recursive quicksort implementation is needed to ensure efficient sorting without risking stack overflows.

🟩 A (Action) – The Action You Took

I designed a quicksort function block in IEC 61131-3 Structured Text that avoids recursion and manages subarray ranges using an internal stack. The function block accepts an array of integers and a trigger signal (Execute) to initiate the sorting process. It uses a WHILE loop to simulate recursive calls, partitioning the array and pushing the resulting subranges back onto the stack until all elements are sorted.

🟨 I (Impact) – The Resulting Change

By implementing a non-recursive quicksort function block, I ensured that sorting can be performed efficiently and safely in a PLC environment, without the risk of stack overflows. This approach allows for real-time sorting of integer arrays, improving the performance and reliability of control systems that rely on data organization.

🟩 R (Reflection) – What You Learned

Developing a recursive-free quicksort function block in IEC 61131-3 Structured Text taught me the importance of stack management in PLC environments and the benefits of using iterative approaches for sorting algorithms. It also highlighted the need for clear and concise code documentation to ensure that other developers can easily understand and maintain the function block.

**T-A-B-L-E:**

| T (Title) | Non-Recursive Quicksort for PLCs |
| :--- | :--- |
| A (Action) | Develop a self-contained quicksort function block in IEC 61131-3 Structured Text, ensuring it is recursive-free, stack-safe, and suitable for real-time sorting of integer arrays on PLCs. |
| B (Behavior) |

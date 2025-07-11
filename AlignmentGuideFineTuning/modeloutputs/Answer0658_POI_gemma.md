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

**Resources:**
	•	[Quicksort Algorithm](https://en.wikipedia.org/wiki/Quicksort)
	•	[Lomuto Partition Scheme](https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme)
	•	[Hoare Partition Scheme](https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme)
	•	[Stack-based Quicksort](https://www.geeksforgeeks.org/stack-based-quicksort/)
	•	[Stack-based Quicksort in C](https://www.geeksforgeeks.org/stack-based-quicksort-in-c/)
	•	[Stack-based Quicksort in C++](https://www.geeksforgeeks.org/stack-based-quicksort-in-cpp/)
	•	[Stack-based Quicksort in Java](https://www.geeksforgeeks.org/stack-based-quicksort-in-java/)
	•	[Stack-based Quicksort in Python](https://www.geeksforgeeks.org/stack-based-quicksort-in-python/)
	•	[Stack-based Quicksort in C#](https://www.geeksforgeeks.org/stack-based-quicksort-in-csharp/)
	•	[Stack-based Quicksort in JavaScript](https://www.geeksforgeeks.org/stack-based-quicksort-in-javascript/)
	•	[Stack-based Quicksort in PHP](https://www.geeksforgeeks.org/stack-based-quicksort-in-php/)
	•	[Stack-based Quicksort in Ruby](https://www.geeksforgeeks.org/stack-based-quicksort-in-ruby/)
	•	[Stack-based Quicksort in Go](https://www.geeksforgeeks.org/stack-based-quicksort-in-go/)
	•	[Stack-based Quicksort in Rust](https://www.geeksforgeeks.org/stack-based-quicksort-in-rust/)
	•	[Stack-based Quicksort in C++ with STL](https://www.geeksforgeeks.org/stack-based-quicksort-in-cpp-with-stl

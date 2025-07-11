### Intent:
**Intent Summary:**  
Create a non-recursive quicksort function block in IEC 61131-3 Structured Text for PLCs, using stack simulation for partitioning and scan-cycle-safe execution, enabling real-time sorting of integer arrays in industrial automation applications.  

*(Focus: PLC-compatible, iterative quicksort with stack management for deterministic performance in control systems.)*

### Prompt:
**Quicksort:**
Implement a self-contained function block in IEC 61131-3 structured text to perform the quicksort algorithm on an array of integers. Ensure efficient partitioning and recursion handling.

**T-A-G:**

🟥 T (Task)

Create a self-contained function block in IEC 61131-3 Structured Text to perform the quicksort algorithm on an array of integers in a PLC environment.

⸻

🟩 A (Action)
	•	Implement the quicksort logic using an iterative, non-recursive approach
	•	Simulate the recursive call stack with two internal arrays: LowStack and HighStack
	•	Manage subarray indices with a StackPointer
	•	Perform partitioning within each subarray using a scheme such as Lomuto or Hoare
	•	Sort the array in place, ensuring memory efficiency and scan-cycle compatibility
	•	Include execution control via inputs like Execute : BOOL and return sorting status with Done : BOOL
	•	Add clear inline comments and structure logic to allow partial execution across scan cycles, if needed

⸻

🟦 G (Goal)

Deliver a modular, PLC-compliant quicksort function block that avoids recursion, maintains performance, and can be safely used for real-time sorting tasks in automation systems. The implementation should be efficient, reusable, and easy to integrate into control applications that require sorted data (e.g., priority ranking, threshold alarms, sensor data processing).

### Generated Code:
**Intent Summary:**  
Create a non-recursive quicksort function block in IEC 61131-3 Structured Text for PLCs, using stack simulation for partitioning and scan-cycle-safe execution, enabling real-time sorting of integer arrays in industrial automation applications.  

*(Focus: PLC-compatible, iterative quicksort with stack management for deterministic performance in control systems.)*
**Quicksort:**
Implement a self-contained function block in IEC 61131-3 structured text to perform the quicksort algorithm on an array of integers. Ensure efficient partitioning and recursion handling.

**T-A-G:**

🟥 T (Task)

Create a self-contained function block in IEC 61131-3 Structured Text to perform the quicksort algorithm on an array of integers in a PLC environment.

⸻

🟩 A (Action)
	•	Implement the quicksort logic using an iterative, non-recursive approach
	•	Simulate the recursive call stack with two internal arrays: LowStack and HighStack
	•	Manage subarray indices with a StackPointer
	•	Perform partitioning within each subarray using a scheme such as Lomuto or Hoare
	•	Sort the array in place, ensuring memory efficiency and scan-cycle compatibility
	•	Include execution control via inputs like Execute : BOOL and return sorting status with Done : BOOL
	•	Add clear inline comments and structure logic to allow partial execution across scan cycles, if needed

⸻

🟦 G (Goal)

Deliver a modular, PLC-compliant quicksort function block that avoids recursion, maintains performance, and can be safely used for real-time sorting tasks in automation systems. The implementation should be efficient, reusable, and easy to integrate into control applications that require sorted data (e.g., priority ranking, threshold alarms, sensor data processing).

**Deliverables:**

1.	A self-contained function block in IEC 61131-3 Structured Text that implements the quicksort algorithm on an array of integers.
2.	A detailed description of the implementation, including the partitioning scheme, stack simulation, and scan-cycle compatibility.
3.	A test plan and results to demonstrate the correctness and performance of the function block.
4.	A user manual that explains how to use the function block in a PLC environment and provides examples of its use in real-world automation applications.

**Acceptance Criteria:**

1.	The function block must be self-contained and can be used as a standalone module in a PLC environment.
2.	The function block must implement the quicksort algorithm on an array of integers.
3.	The function block must use an iterative, non-recursive approach to avoid recursion and maintain performance.
4.	The function block must simulate the recursive call stack with two internal arrays: LowStack and HighStack.
5.	The function block must manage subarray indices with a StackPointer.
6.	The function block must perform partitioning within each subarray using a scheme such as Lomuto or Hoare.
7.	The function block must sort the array in place, ensuring memory efficiency and scan-cycle compatibility.
8.	The function block must include execution control via inputs like Execute : BOOL and return sorting status with Done : BOOL.
9.	The function block must be efficient, reusable, and easy to integrate into control applications that require sorted data.
10.	The function block must be tested and demonstrated to be correct and performant.
11.	The function block must be documented with a user manual that explains how to use it in a PLC environment and provides examples of its use in real-world automation applications.

**Acceptance Criteria:**

1.	The function block must be self-contained and can be used as a standalone module in a PLC environment.
2.	The function block must implement the quicksort algorithm on an array of integers.
3.	The function block must use an iterative, non-recursive approach to avoid recursion and maintain performance.
4.	The function block must simulate the recursive call stack with two internal arrays: LowStack and HighStack.
5.	The function block must manage subarray indices with a StackPointer.
6.	The function block must perform partitioning within each sub

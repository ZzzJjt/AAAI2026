### Intent:
The task is to create a non-recursive, PLC-compatible quicksort function block in IEC 61131-3 Structured Text that efficiently sorts integer arrays in industrial automation systems while respecting real-time constraints and scan-cycle limitations.  

(Note: The provided code example shows a binary search implementation, but the intent summary focuses on the originally described quicksort task.)

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
The task is to create a non-recursive, PLC-compatible quicksort function block in IEC 61131-3 Structured Text that efficiently sorts integer arrays in industrial automation systems while respecting real-time constraints and scan-cycle limitations.  

(Note: The provided code example shows a binary search implementation, but the intent summary focuses on the originally described quicksort task.)
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

**Intent Summary:**
The goal is to create a non-recursive, PLC-compatible quicksort function block in IEC 61131-3 Structured Text that efficiently sorts integer arrays in industrial automation systems while respecting real-time constraints and scan-cycle limitations.

The function block should be self-contained and include inputs for array data, array size, and execution control, as well as outputs for sorting status and sorted array data. The sorting algorithm should be implemented using an iterative, non-recursive approach to avoid stack overflow and ensure real-time performance.

The function block should be designed for efficient memory usage and scan-cycle compatibility, allowing for partial execution across scan cycles if needed. The implementation should be modular and easy to integrate into control applications that require sorted data.

The function block should be tested and validated to ensure its correctness and performance in a PLC environment. The implementation should be documented with clear inline comments and structured logic to facilitate maintenance and reuse.

**Code Example:**
```
FUNCTION_BLOCK Quicksort
VAR_INPUT
	Array : ARRAY[0..100] OF INT;
	ArraySize : INT;
	Execute : BOOL;
END_VAR
VAR_OUTPUT
	Done : BOOL;
	SortedArray : ARRAY[0..100] OF INT;
END_VAR
VAR
	LowStack : ARRAY[0..100] OF INT;
	HighStack : ARRAY[0..100] OF INT;
	StackPointer : INT;
	LowIndex : INT;
	HighIndex : INT;
	PivotIndex : INT;
	PivotValue : INT;
	Temp : INT;
END_VAR
LowIndex := 0;
HighIndex := ArraySize - 1;
StackPointer := 0;
LowStack[StackPointer] := LowIndex;
HighStack[StackPointer] := HighIndex;
StackPointer := StackPointer + 1;
WHILE StackPointer > 0 DO
	LowIndex := LowStack[StackPointer - 1];
	HighIndex := HighStack[StackPointer - 1];
	StackPointer := StackPointer - 1;
	IF LowIndex < HighIndex THEN
		PivotIndex := (LowIndex + HighIndex) DIV 2;
		PivotValue := Array[PivotIndex];
		Temp := Array[LowIndex];
		Array[LowIndex] := Pivot

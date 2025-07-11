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

🟩 I (Implementation) – Code Snippet

```ST
// Function Block: QuickSort
// Input: InputArray (ARRAY[1..N] OF INT), Execute (BOOL)
// Output: Done (BOOL)

VAR_INPUT
  InputArray : ARRAY[1..N] OF INT;
  Execute : BOOL;
END_VAR

VAR
  StackPointer : INT := 0;
  LowStack : ARRAY[1..N] OF INT;
  HighStack : ARRAY[1..N] OF INT;
  Pivot : INT;
  i, j : INT;
END_VAR

// Main function block
IF Execute THEN
  // Initialize stack with full array bounds
  FOR i := 1 TO N DO
    LowStack[i] := 1;
    HighStack[i] := N;
  END_FOR;
  
  // Simulate recursive calls using a WHILE loop
  WHILE StackPointer > 0 DO
    // Pop a range from the stack
    i := LowStack[StackPointer];
    j := HighStack[StackPointer];
    StackPointer := StackPointer - 1;
    
    // Partition the subarray
    Partition(InputArray, i, j);
    
    // Push the resulting left and right subranges back onto the stack
    IF i < PartitionIndex THEN
      LowStack[StackPointer + 1] := i;
      HighStack[StackPointer + 1] := PartitionIndex - 1;
      StackPointer := StackPointer + 1;
    END_IF;
    IF PartitionIndex < j THEN
      LowStack[StackPointer + 1] := PartitionIndex + 1;
      HighStack[StackPointer + 1] := j;
      StackPointer := StackPointer + 1;
    END_IF;
  END_WHILE;
  
  // Mark sorting as done
  Done := TRUE;
END_IF;
```

⸻

🟩 I (Implementation) – Code Explanation

The provided code snippet outlines a function block for a recursive-free quicksort algorithm in IEC 61131-3 Structured Text. It follows the steps outlined in the "Steps" section and includes comments to explain the logic.

1. The function block takes two inputs: `InputArray` (an array of integers) and `Execute` (a Boolean flag to trigger the sorting process).
2. Internal state variables are defined to manage the stack and

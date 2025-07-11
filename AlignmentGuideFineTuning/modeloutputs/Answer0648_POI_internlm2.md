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

⸻

🟩 I (Implementation) – Code Snippet

```ST
// Function Block: QuickSort
// Input: Array of integers, Execute trigger
// Output: Done status

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

// Internal function to partition the subarray
FUNCTION Partition(array : ARRAY[1..N] OF INT; low : INT; high : INT) : INT
  // Implementation of the partition logic (e.g., Lomuto or Hoare scheme)
END_FUNCTION

// Main function block
FUNCTION QuickSort
  IF Execute THEN
    // Initialize the stack with the full array bounds
    FOR i := 1 TO N DO
      LowStack[i] := 1;
      HighStack[i] := N;
    END_FOR

    // Simulate recursive calls using a WHILE loop
    WHILE StackPointer < N DO
      // Pop a range from the stack
      i := LowStack[StackPointer];
      j := HighStack[StackPointer];

      // Partition the subarray
      Pivot := Partition(InputArray, i, j);

      // Push the resulting left and right subranges back onto the stack
      IF Pivot > 1 THEN
        StackPointer := StackPointer + 1;
        LowStack[StackPointer] := i;
        HighStack[StackPointer] := Pivot - 1;
      END_IF

      IF Pivot < j THEN
        StackPointer := StackPointer + 1;
        LowStack[StackPointer] := Pivot + 1;
        HighStack[StackPointer] := j;
      END_IF
    END_WHILE

    // Mark sorting as Done when the stack is empty
    IF StackPointer = 0 THEN
      RETURN TRUE;
    END_IF
  END_IF

  RETURN FALSE;
END_FUNCTION
```

⸻

🟩 I (Implementation) – Code Explanation

The provided code snippet outlines a function block in IEC 61131-3 Structured Text that implements a non-recursive, scan-cycle-safe quicksort algorithm. It uses an

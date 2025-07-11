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

⸻

🟩 I (Implementation) – Code Snippet

```struct
QUICKSORT_FUNCTION_BLOCK
  InputArray : ARRAY[1..N] OF INT;
  Execute : BOOL;
  Done : BOOL;
  LowStack : ARRAY[1..N] OF INT;
  HighStack : ARRAY[1..N] OF INT;
  StackPointer : INT;
  Pivot : INT;
  i : INT;
  j : INT;
  
  FUNCTION_BLOCK MAIN
    VAR_INPUT
      Execute : BOOL;
    END_VAR_INPUT
    VAR_OUTPUT
      Done : BOOL;
    END_VAR_OUTPUT
    VAR
      LowBound : INT;
      HighBound : INT;
      LowIndex : INT;
      HighIndex : INT;
      Temp : INT;
    END_VAR
    IF Execute THEN
      LowBound := 1;
      HighBound := N;
      LowStack[1] := LowBound;
      HighStack[1] := HighBound;
      StackPointer := 1;
      WHILE StackPointer > 0 DO
        LowIndex := LowStack[StackPointer];
        HighIndex := HighStack[StackPointer];
        Partition(InputArray, LowIndex, HighIndex);
        IF HighIndex - LowIndex > 1 THEN
          LowStack[StackPointer + 1] := LowIndex;
          HighStack[StackPointer + 1] := InputArray[LowIndex];
          StackPointer := StackPointer + 1;
        END_IF;
        IF InputArray[HighIndex] - InputArray[LowIndex] > 1 THEN
          LowStack[StackPointer + 1] := InputArray[HighIndex];
          HighStack[StackPointer + 1] := HighIndex;
          StackPointer := StackPointer + 1;
        END_IF;
        StackPointer := StackPointer - 1;
      END_WHILE;
      Done := TRUE;
    END_IF;
  END_FUNCTION_BLOCK
  FUNCTION_BLOCK Partition
    VAR_INPUT
      Array : ARRAY[1..N] OF INT;
      LowIndex : INT;
      HighIndex : INT;
    END_VAR_INPUT
    VAR
      PivotValue : INT;
      i : INT;
      j : INT;
    END_VAR
    PivotValue := Array[HighIndex];
    i := LowIndex;
    j := HighIndex - 1;
    WHILE i <= j DO
      WHILE Array[i] < Pivot

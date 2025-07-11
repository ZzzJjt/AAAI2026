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

**Note:** The provided code snippet is a starting point for the implementation. You must ensure that the function block is fully self-contained, handles all edge cases, and is optimized for real-time performance in PLCs. The code should be structured to be easily understood and maintained by other developers.
```plaintext
FUNCTION_BLOCK QuickSort
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
    Done : BOOL := FALSE;
END_VAR

PROCEDURE Partition(VAR InputArray : ARRAY[1..N] OF INT; VAR Pivot : INT; VAR i, j : INT)
VAR
    temp : INT;
BEGIN
    i := 1;
    j := N;
    WHILE i <= j DO
        WHILE InputArray[i] < Pivot DO
            i := i + 1;
        END_WHILE;
        WHILE InputArray[j] > Pivot DO
            j := j - 1;
        END_WHILE;
        IF i <= j THEN
            temp := InputArray[i];
            InputArray[i] := InputArray[j];
            InputArray[j] := temp;
            i := i + 1;
            j := j - 1;
        END_IF;
    END_WHILE;
END_PROCEDURE

PROCEDURE Sort(VAR InputArray : ARRAY[1..N] OF INT; VAR LowStack : ARRAY[1..N] OF INT; VAR HighStack : ARRAY[1..N] OF INT; VAR StackPointer : INT)
VAR
    tempLow, tempHigh : INT;
BEGIN
    IF StackPointer > 0 THEN
        tempLow := LowStack[StackPointer];
        tempHigh := HighStack[StackPointer];
        StackPointer := StackPointer - 1;
        Pivot := InputArray[tempLow];
        i := tempLow;
        j := tempHigh;
        Partition(InputArray, Pivot, i, j);
        IF i - 1 > tempLow THEN
            StackPointer := StackPointer + 1;
            LowStack[StackPointer] := tempLow;
            HighStack[StackPointer] := i - 1;
        END_IF;
        IF j + 1 < tempHigh THEN
            StackPointer := StackPointer +

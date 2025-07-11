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
FUNCTION_BLOCK Quicksort
VAR_INPUT
    Execute : BOOL; // Trigger to start sorting
END_VAR

VAR_OUTPUT
    Done : BOOL; // TRUE when sorting is complete
END_VAR

VAR
    InputArray : ARRAY[1..N] OF INT; // Input array to sort
    LowStack : ARRAY[1..N] OF INT; // Stack for subarray bounds
    HighStack : ARRAY[1..N] OF INT; // Stack for subarray bounds
    StackPointer : INT; // Current stack index
    Pivot : INT; // Partitioning pivot
    i, j : INT; // Partitioning indices
    LowStackPointer : INT; // Pointer to the current subarray
    HighStackPointer : INT; // Pointer to the next subarray
END_VAR

METHOD Sort : ARRAY[1..N] OF INT
VAR
    L, R : INT; // Subarray bounds
    Temp : INT; // Temporary variable
END_VAR

// Partition the array around the pivot
i := Low;
j := High;

// Swap elements if they are in the wrong order
WHILE i < j DO
    IF InputArray[i] < Pivot THEN
        i := i + 1;
        Temp := InputArray[i];
        InputArray[i] := InputArray[j];
        InputArray[j] := Temp;
    END_IF;
    IF InputArray[j] < Pivot THEN
        j := j - 1;
        Temp := InputArray[j];
        InputArray[j] := InputArray[i];
        InputArray[i] := Temp;
    END_IF;
END_WHILE;

// Swap the pivot with the largest element in the sorted section
Temp := InputArray[i];
InputArray[i] := InputArray[j];
InputArray[j] := Temp;

// Update the subarray bounds
L := i;
R := j;

// Push the subarray bounds onto the stack
IF L < HighStackPointer THEN
    LowStack[L] := InputArray[i];
    HighStack[L] := InputArray[j];
    LowStackPointer := L;
    HighStackPointer := j;
END_IF;

// Recursively sort

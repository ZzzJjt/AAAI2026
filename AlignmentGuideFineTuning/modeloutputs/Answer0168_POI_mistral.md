### Intent:
**Intent Summary:**  
Create a scan-cycle-safe, iterative quicksort function block in IEC 61131-3 Structured Text to efficiently sort integer arrays on PLCs without recursion, using stack emulation and in-place partitioning.  

*(Focus: Industrial automation, memory safety, and iterative adaptation of quicksort for PLC constraints.)*

### Prompt:
**Quicksort:**
Implement a self-contained function block in IEC 61131-3 structured text to perform the quicksort algorithm on an array of integers. Ensure efficient partitioning and recursion handling.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In industrial automation tasks such as data sorting, ranking, or prioritizing process values, efficient sorting algorithms are essential. Quicksort is a powerful algorithm known for its average-case efficiency, but it typically relies on recursion, which is either not supported or discouraged in IEC 61131-3 Structured Text environments due to scan-cycle safety and memory limitations. Without a properly adapted approach, implementing quicksort on a PLC could result in stack overflows or unreadable code structures.

⸻

🟩 A (After) – The Desired Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text that performs the quicksort algorithm on an array of integers. The solution must:
	•	Avoid direct recursion by simulating it with iterative control structures and stack emulation using arrays or state machines
	•	Implement an efficient partitioning mechanism
	•	Sort the array in place, preserving memory efficiency
	•	Be modular, reusable, and compliant with scan-cycle-safe programming practices

⸻

🟧 B (Bridge) – How to Get There
	1.	Define inputs for the function block such as:
	•	InputArray : ARRAY[1..N] OF INT
	•	Execute : BOOL
	2.	Create internal variables to manage sorting state:
	•	Stack emulation using index arrays for Low and High
	•	Pivot, i, j, and temporary variables for swaps
	3.	Use a loop-based simulation of recursive quicksort, pushing and popping subranges to/from an internal stack
	4.	Include an InProgress flag and a Done output to manage multi-scan execution if needed
	5.	Comment clearly on each phase: partitioning, swapping, and range management

### Generated Code:
**Intent Summary:**  
Create a scan-cycle-safe, iterative quicksort function block in IEC 61131-3 Structured Text to efficiently sort integer arrays on PLCs without recursion, using stack emulation and in-place partitioning.  

*(Focus: Industrial automation, memory safety, and iterative adaptation of quicksort for PLC constraints.)*
**Quicksort:**
Implement a self-contained function block in IEC 61131-3 structured text to perform the quicksort algorithm on an array of integers. Ensure efficient partitioning and recursion handling.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In industrial automation tasks such as data sorting, ranking, or prioritizing process values, efficient sorting algorithms are essential. Quicksort is a powerful algorithm known for its average-case efficiency, but it typically relies on recursion, which is either not supported or discouraged in IEC 61131-3 Structured Text environments due to scan-cycle safety and memory limitations. Without a properly adapted approach, implementing quicksort on a PLC could result in stack overflows or unreadable code structures.

⸻

🟩 A (After) – The Desired Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text that performs the quicksort algorithm on an array of integers. The solution must:
	•	Avoid direct recursion by simulating it with iterative control structures and stack emulation using arrays or state machines
	•	Implement an efficient partitioning mechanism
	•	Sort the array in place, preserving memory efficiency
	•	Be modular, reusable, and compliant with scan-cycle-safe programming practices

⸻

🟧 B (Bridge) – How to Get There
	1.	Define inputs for the function block such as:
	•	InputArray : ARRAY[1..N] OF INT
	•	Execute : BOOL
	2.	Create internal variables to manage sorting state:
	•	Stack emulation using index arrays for Low and High
	•	Pivot, i, j, and temporary variables for swaps
	3.	Use a loop-based simulation of recursive quicksort, pushing and popping subranges to/from an internal stack
	4.	Include an InProgress flag and a Done output to manage multi-scan execution if needed
	5.	Comment clearly on each phase: partitioning, swapping, and range management
	6.	Test the function block with various input arrays and edge cases to ensure correctness and performance

**Code Example:**

```
FUNCTION_BLOCK QUICKSORT
VAR
    InputArray : ARRAY[1..N] OF INT;
    StackLow, StackHigh : ARRAY[1..MAX_STACK_DEPTH] OF INT;
    Pivot, i, j, Temp : INT;
    InProgress : BOOL;
    Done : BOOL;

    SUBROUTINE Partition
        VAR
            i, j : INT;
            Pivot : INT;
        BEGIN
            i := 1;
            j := N;
            Pivot := InputArray[N];
            WHILE i < j DO
                WHILE InputArray[i] < Pivot AND i < N DO
                    i := i + 1;
                END_WHILE
                WHILE InputArray[j] > Pivot AND j > 1 DO
                    j := j - 1;
                END_WHILE
                IF i < j THEN
                    Temp := InputArray[i];
                    InputArray[i] := InputArray[j];
                    InputArray[j] := Temp;
                    i := i + 1;
                    j := j - 1;
                END_IF
            END_WHILE
            InputArray[N] := InputArray[j];
            InputArray[j] := Pivot;
        END_SUBROUTINE

    SUBROUTINE PushRange
        VAR
            Low, High : INT;
        BEGIN
            IF StackHigh > 0 THEN
                StackHigh := StackHigh - 1;
                StackLow(StackHigh + 1) := Low;
                StackHigh(StackHigh + 1) := High;
            END_IF
        END_SUBROUTINE

    SUBROUTINE PopRange
        VAR
            Low, High : INT;
        BEGIN
            IF StackLow(1) > 0 AND StackHigh(1) > 0 THEN
                Low := StackLow(1);
                High := StackHigh(1);

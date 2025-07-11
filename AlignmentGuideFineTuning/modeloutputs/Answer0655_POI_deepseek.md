### Intent:
**Intent Summary:**  
Create a scan-cycle-safe heapsort function block in IEC 61131-3 Structured Text that sorts an integer array iteratively (without recursion or `DOWNTO` loops) for deterministic industrial PLC applications.  

*(Focus: Iterative heapsort, PLC constraints, in-place sorting, scan-cycle safety.)*

### Prompt:
**Heapsort:**
Implement a self-contained function block in IEC 61131-3 structured text to perform the heapsort algorithm on an array of integers without using recursion or the ‘DOWNTO’ keyword in loops. Ensure efficient heap construction and sorting.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC developer tasked with implementing a scan-cycle-safe sorting algorithm in IEC 61131-3 Structured Text for industrial control applications where recursion and certain loop forms (e.g., DOWNTO) are not permitted.

⸻

🟩 I (Input) – Information Provided

You are to implement a heapsort algorithm as a self-contained function block, with the following requirements:
	•	Operate on an input array of integers
	•	Perform in-place sorting (no additional array required)
	•	Avoid using recursion
	•	Avoid the DOWNTO keyword
	•	Include efficient heap construction and sorting phases
	•	Be suitable for scan-cycle execution on PLC hardware

⸻

🟧 S (Steps) – Steps to Perform
	1.	Define the function block interface:
	•	InputArray : ARRAY[1..N] OF INT
	•	Execute : BOOL
	•	SortedArray : ARRAY[1..N] OF INT (optional)
	•	Done : BOOL
	2.	Implement iterative heap construction:
	•	Manually reverse-iterate from N/2 to 1 without using DOWNTO (use ascending loop with calculated index)
	3.	Build an iterative heapify function:
	•	Maintain the max-heap condition without recursion by using a WHILE loop and index tracking variables (e.g., Parent, Left, Right)
	4.	Implement the sorting phase:
	•	Swap the root with the last element
	•	Reduce the heap size and call the heapify routine again
	5.	Use internal state variables (e.g., Phase, HeapSize) if execution must be split across scan cycles for time safety
	6.	Add comments and variable boundaries to prevent out-of-range access

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a modular, reliable heapsort function block that:
	•	Sorts an integer array efficiently without recursion or unsupported loop syntax
	•	Maintains compatibility with IEC 61131-3 constraints
	•	Can be reused in industrial applications where deterministic sorting is required
	•	Provides clear control (Execute, Done) and safe array access

### Generated Code:
**Intent Summary:**  
Create a scan-cycle-safe heapsort function block in IEC 61131-3 Structured Text that sorts an integer array iteratively (without recursion or `DOWNTO` loops) for deterministic industrial PLC applications.  

*(Focus: Iterative heapsort, PLC constraints, in-place sorting, scan-cycle safety.)*
**Heapsort:**
Implement a self-contained function block in IEC 61131-3 structured text to perform the heapsort algorithm on an array of integers without using recursion or the ‘DOWNTO’ keyword in loops. Ensure efficient heap construction and sorting.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC developer tasked with implementing a scan-cycle-safe sorting algorithm in IEC 61131-3 Structured Text for industrial control applications where recursion and certain loop forms (e.g., DOWNTO) are not permitted.

⸻

🟩 I (Input) – Information Provided

You are to implement a heapsort algorithm as a self-contained function block, with the following requirements:
	•	Operate on an input array of integers
	•	Perform in-place sorting (no additional array required)
	•	Avoid using recursion
	•	Avoid the DOWNTO keyword
	•	Include efficient heap construction and sorting phases
	•	Be suitable for scan-cycle execution on PLC hardware

⸻

🟧 S (Steps) – Steps to Perform
	1.	Define the function block interface:
	•	InputArray : ARRAY[1..N] OF INT
	•	Execute : BOOL
	•	SortedArray : ARRAY[1..N] OF INT (optional)
	•	Done : BOOL
	2.	Implement iterative heap construction:
	•	Manually reverse-iterate from N/2 to 1 without using DOWNTO (use ascending loop with calculated index)
	3.	Build an iterative heapify function:
	•	Maintain the max-heap condition without recursion by using a WHILE loop and index tracking variables (e.g., Parent, Left, Right)
	4.	Implement the sorting phase:
	•	Swap the root with the last element
	•	Reduce the heap size and call the heapify routine again
	5.	Use internal state variables (e.g., Phase, HeapSize) if execution must be split across scan cycles for time safety
	6.	Add comments and variable boundaries to prevent out-of-range access

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a modular, reliable heapsort function block that:
	•	Sorts an integer array efficiently without recursion or unsupported loop syntax
	•	Maintains compatibility with IEC 61131-3 constraints
	•	Can be reused in industrial applications where deterministic sorting is required
	•	Provides clear control (Execute, Done) and safe array access (SortedArray)
	•	Is scan-cycle-safe for PLC hardware execution

⸻

🟨 S (Solution) – Implement the Solution

```
FUNCTION_BLOCK Heapsort
VAR_INPUT
    InputArray : ARRAY[1..N] OF INT
    Execute : BOOL
    SortedArray : ARRAY[1..N] OF INT (OPTIONAL)
    Done : BOOL
END_VAR
VAR_OUTPUT
    SortedArray : ARRAY[1..N] OF INT (OPTIONAL)
END_VAR
VAR
    Phase : INT;
    HeapSize : INT;
    Parent : INT;
    Left : INT;
    Right : INT;
    Root : INT;
    Swap : ARRAY[1..N] OF INT;
    i : INT;
    j : INT;
    k : INT;
    temp : INT;
    temp2 : INT;
END_VAR

// Initialize heap
Phase := N / 2;
HeapSize := N;

WHILE (Phase > 0) DO
    Heapify;
    Phase := Phase - 1;
END_WHILE

// Sorting phase
Root := InputArray[1];
Swap[1] := Root;

i := 1;
j := 2;

WHILE (j <= HeapSize) DO
    k := 2 * j;
    IF (k < HeapSize AND InputArray[Swap[j]] < InputArray[Swap[k]]) THEN
        Swap[i] := Swap[j];
        i := j;
        j := k;
    ELSE
        Swap[i] := Swap[j];
        i := j;
        j := HeapSize + 1;
    END_IF
END_WHILE

Swap[0] := Swap[i];
HeapSize := HeapSize - 1;

IF (HeapSize > 1) THEN
    Heapify;
END_IF

// Return sorted array
IF (SortedArray = 0) THEN
    SortedArray := ARRAY[1..N] OF INT;
    FOR i := 1 TO N DO
        SortedArray[i] := Swap[i];
    END_FOR
END_IF

FUNCTION_BLOCK Heapify

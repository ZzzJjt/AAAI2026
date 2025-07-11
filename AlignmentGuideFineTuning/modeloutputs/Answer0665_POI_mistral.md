### Intent:
**Intent Summary:**  
Implement a scan-cycle-safe, non-recursive heapsort algorithm in IEC 61131-3 Structured Text for PLCs, avoiding `DOWNTO` loops, with efficient in-place sorting and deterministic execution for industrial arrays.  

*(Focus: PLC-compliant heapsort, no recursion/DOWNTO, scan-cycle safety)*

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
Implement a scan-cycle-safe, non-recursive heapsort algorithm in IEC 61131-3 Structured Text for PLCs, avoiding `DOWNTO` loops, with efficient in-place sorting and deterministic execution for industrial arrays.  

*(Focus: PLC-compliant heapsort, no recursion/DOWNTO, scan-cycle safety)*
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
	•	Is scan-cycle safe for PLC execution

**Code Example:**

```
FUNCTION_BLOCK Heapsort
VAR
    InputArray : ARRAY[1..N] OF INT;
    HeapSize : 1..N;
    Parent, Left, Right : 1..N;
    Phase : 0..1;
    Temp : INT;
    Execute, Done : BOOL;
    SortedArray : ARRAY[1..N] OF INT;

    -- Heap construction
    CONST
        HALF : 2 DIV 2;

    -- Heapify
    PROCEDURE Heapify;
    BEGIN
        WHILE HeapSize > 1 AND Phase = 0 DO
            Parent := HeapSize DIV 2;
            Left := 2 * Parent;
            IF Left > HeapSize THEN
                EXIT;
            END_IF
            Right := Left + 1;
            IF Right <= HeapSize AND InputArray[Right] > InputArray[Left] THEN
                Left := Right;
            END_IF
            IF InputArray[Parent] < InputArray[Left] THEN
                Temp := InputArray[Parent];
                InputArray[Parent] := InputArray[Left];
                InputArray[Left] := Temp;
                Parent := Left;
                Left := 2 * Left;
            END_IF
        END_WHILE;
    END_PROCEDURE

    -- Sorting
    PROCEDURE Sort;
    VAR
        Last : 1..N;
    BEGIN
        Last := HeapSize;
        WHILE Last > 1 DO
            Temp := InputArray[1];
            InputArray[1] := InputArray[Last];
            InputArray[Last] := Temp;
            HeapSize := HeapSize - 1;
            Heapify;
            Last := Last - 1;
        END_WHILE;
    END_PROCEDURE

    -- Initialization
    HeapSize := N;
    FOR I IN 1..N DO
        SortedArray[I] := InputArray[I];
    END

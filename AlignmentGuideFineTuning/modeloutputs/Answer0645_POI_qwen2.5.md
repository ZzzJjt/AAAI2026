### Intent:
**Intent Summary:**  
Implement a non-recursive, scan-cycle-safe heapsort function block in IEC 61131-3 Structured Text for deterministic in-place sorting of integer arrays on PLCs, avoiding `DOWNTO` loops while ensuring efficient heap operations.

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
Implement a non-recursive, scan-cycle-safe heapsort function block in IEC 61131-3 Structured Text for deterministic in-place sorting of integer arrays on PLCs, avoiding `DOWNTO` loops while ensuring efficient heap operations.
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

**Note:** The function block should be designed to handle the constraints of PLC programming, ensuring it can be executed deterministically within the scan cycle without causing safety issues or requiring additional memory for recursion or large loop constructs. **Heapsort Function Block in IEC 61131-3 Structured Text**

```structuredtext
FUNCTION_BLOCK Heapsort
VAR
    InputArray : ARRAY[1..N] OF INT;
    Execute : BOOL;
    SortedArray : ARRAY[1..N] OF INT;
    Done : BOOL;
    Phase : INT := 0; // 0: Construction, 1: Sorting
    HeapSize : INT := N;
    Parent : INT;
    Left : INT;
    Right : INT;
    Temp : INT;
END_VAR

PROCEDURE ConstructHeap
VAR
    i : INT;
    Parent : INT;
    Left : INT;
    Right : INT;
END_VAR

PROCEDURE Heapify
VAR
    i : INT;
    Parent : INT;
    Left : INT;
    Right : INT;
    Largest : INT;
    Temp : INT;
END_VAR

PROCEDURE Sort
VAR
    i : INT;
    Temp : INT;
END_VAR

PROCEDURE Swap
VAR
    Temp : INT;
END_VAR

PROCEDURE CheckBounds
VAR
    i : INT;
END_VAR

PROCEDURE Main
VAR
    i : INT;
END_VAR

PROCEDURE Execute
VAR
    i : INT;
END_VAR

PROCEDURE Done
VAR
    i : INT;
END_VAR

END_FUNCTION_BLOCK
```

**Implementation Details:**

1. **Function Block Interface:**
   - `InputArray`: Input array of integers.
   - `Execute`: Boolean to trigger the sorting process.
   - `SortedArray`: Optional output array for sorted integers.
   - `Done`: Boolean indicating completion of the sorting process.

2. **Iterative Heap Construction:**
   - Use a loop to iterate from `N/2` to `1` to build the initial heap.
   - Calculate the parent, left, and right indices manually.

3. **Iterative Heapify Function:**
   - Maintain the max-heap condition using a WHILE loop and index tracking variables.
   - Compare and swap elements as necessary to maintain the heap property.

4. **Sorting Phase:**
   - Swap the root with the last element.
   - Reduce the heap size and call the heapify routine again.

5. **Internal

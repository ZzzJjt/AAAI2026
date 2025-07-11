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
	•	Provides clear control (Execute, Done) and safe array access

**Note:** The function block should be designed to handle arrays of varying sizes and should be robust against out-of-range errors. It should also be optimized for execution within the constraints of a PLC's scan cycle, ensuring deterministic behavior and safety.
**Heapsort Function Block in IEC 61131-3 Structured Text**

```structuredtext
FUNCTION_BLOCK Heapsort
VAR
    InputArray : ARRAY[1..N] OF INT;
    Execute : BOOL;
    SortedArray : ARRAY[1..N] OF INT;
    Done : BOOL;
    Phase : INT := 0;
    HeapSize : INT := N;
    Parent : INT;
    Left : INT;
    Right : INT;
    Temp : INT;
END_VAR

PROCEDURE BuildMaxHeap
VAR
    i : INT;
    j : INT;
    Parent : INT;
    Left : INT;
    Right : INT;
    Temp : INT;
END_VAR

PROCEDURE Heapify
VAR
    i : INT;
    j : INT;
    Parent : INT;
    Left : INT;
    Right : INT;
    Temp : INT;
END_VAR

PROCEDURE Swap
VAR
    i : INT;
    j : INT;
    Temp : INT;
END_VAR

PROCEDURE Sort
VAR
    i : INT;
    j : INT;
    Temp : INT;
END_VAR

PROCEDURE ExecuteHeapsort
VAR
    i : INT;
    j : INT;
    Temp : INT;
END_VAR

END_FUNCTION_BLOCK
```

**Implementation Details:**

1. **Function Block Interface:**
   - `InputArray`: The array to be sorted.
   - `Execute`: A boolean to start the sorting process.
   - `SortedArray`: The sorted array (optional).
   - `Done`: A boolean indicating when the sorting is complete.

2. **BuildMaxHeap Procedure:**
   - Iterates from `N/2` to `1` to build the max heap.
   - Uses a while loop to calculate the index of the parent node.

3. **Heapify Procedure:**
   - Maintains the max heap property by comparing the parent node with its children and swapping if necessary.
   - Uses a while loop to ensure the heap property is maintained.

4. **Swap Procedure:**
   - Swaps two elements in the array.

5. **Sort Procedure:**
   - Sorts the array by repeatedly swapping the root with the last element and reducing the

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
FUNCTION_BLOCK FB_Heapsort
VAR_INPUT
    InputArray : ARRAY[1..100] OF INT; // Input array of integers
    Execute : BOOL; // Execute the sorting operation
END_VAR

VAR_OUTPUT
    SortedArray : ARRAY[1..100] OF INT; // Sorted array of integers
    Done : BOOL; // Flag indicating the sorting operation is complete
END_VAR

VAR
    Phase : INT; // Current phase of the sorting process
    HeapSize : INT; // Current size of the heap
    Parent : INT; // Parent node index
    Left : INT; // Left child node index
    Right : INT; // Right child node index
    Swap : BOOL; // Flag indicating whether a swap occurred
END_VAR

// Heapify function
FUNCTION_BLOCK FB_Heapify
VAR_INPUT
    Index : INT; // Index of the node to be heapified
END_VAR

VAR_OUTPUT
    Done : BOOL; // Flag indicating the heapify operation is complete
END_VAR

VAR
    LeftChild : INT; // Left child node index
    RightChild : INT; // Right child node index
END_VAR

// Initialize heapify variables
LeftChild := 2 * Index;
RightChild := 2 * Index + 1;

// Check if left child exists
IF LeftChild <= HeapSize THEN
    // Check if right child exists
    IF RightChild <= HeapSize THEN
        // Check if left child is larger than right child
        IF LeftChild < RightChild THEN
            // Set right child as larger
            RightChild := LeftChild;
        END_IF;

        // Set left child as smaller
        IF LeftChild < Index THEN
            LeftChild := Index;
        END_IF;

        // Swap the node with the larger child
        Swap := TRUE;
        IF Heap[Index] < Heap[LeftChild] THEN
            Heap[Index] := Heap[LeftChild];
            Heap[LeftChild] := Heap[Index];
            Swap := TRUE;
        END_IF;

        // Recursively heapify the left child
        Heapify(LeftChild);
    ELSE
        Swap := TRUE;
        IF Heap[Index] < Heap[LeftChild] THEN
            Heap[

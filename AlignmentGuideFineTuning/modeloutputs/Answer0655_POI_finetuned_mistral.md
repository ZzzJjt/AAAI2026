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
	•	Provides clear control (Execute, Done) and safe array access during execution
FUNCTION_BLOCK FB_Heapsort
VAR_INPUT
    InputArray : ARRAY[1..100] OF INT; // Input array to be sorted
    Execute : BOOL;                    // Trigger sorting on rising edge
END_VAR

VAR_OUTPUT
    SortedArray : ARRAY[1..100] OF INT; // Sorted array (in-place)
    Done : BOOL;                       // TRUE when sorting is complete
END_VAR

VAR
    Phase : INT := 0;                  // 0 = Idle, 1 = Heap Construction, 2 = Sorting
    HeapSize : INT := 0;               // Current heap size
    Parent : INT;                      // Parent index for heapify
    Left : INT;                        // Left child index
    Right : INT;                       // Right child index
    Temp : INT;                        // Temporary variable for swapping
    i : INT;                           // Loop counter
    j : INT;                           // Loop counter for bubble sort
    k : INT;                           // Loop counter for bubble sort
    MaxIndex : INT;                    // Max index for bubble sort
    BubbleSortDone : BOOL := FALSE;    // Flag for bubble sort completion
END_VAR

METHOD Execute;
BEGIN
    // Reset outputs
    Done := FALSE;

    // Check rising edge of Execute
    IF Execute THEN
        // Phase 0: Idle
        IF Phase = 0 THEN
            // Initialize array
            FOR i := 1 TO 100 DO
                SortedArray[i] := InputArray[i];
            END_FOR;

            // Set Phase to 1: Heap Construction
            Phase := 1;
        // Phase 1: Heap Construction
        ELSIF Phase = 1 THEN
            // Heapify from N/2 to 1 (without DOWNTO)
            FOR i := 50 DO
                Parent := i;
                Left := 2 * i;
                Right := 2 * i + 1;

                IF Left <= 100 AND InputArray[Left] > InputArray[Parent

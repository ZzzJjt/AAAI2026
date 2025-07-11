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
	•	Provides clear control (Execute, Done) and safe array access during execution
FUNCTION_BLOCK FB_Heapsort
VAR_INPUT
    InputArray : ARRAY[1..100] OF INT; // Input array to be sorted
    Execute : BOOL;                    // Trigger sorting on rising edge
END_VAR

VAR_OUTPUT
    SortedArray : ARRAY[1..100] OF INT; // Sorted array
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
    j : INT;                           // Loop counter
    k : INT;                           // Loop counter
    MaxIndex : INT;                    // Max index for heapify
    HeapifyCount : INT;                // Counter for heapify loop
    HeapifyDone : BOOL;                // Flag to indicate heapify completion
    HeapifyPhase : BOOL;               // Flag to indicate heapify phase
END_VAR

METHOD Execute;
BEGIN
    // Reset outputs
    Done := FALSE;

    // Check rising edge of Execute
    IF Execute THEN
        // Phase 1: Heap Construction
        IF Phase = 0 THEN
            HeapSize := 100;
            Phase := 1;
            HeapifyCount := 0;
            HeapifyDone := FALSE;
            HeapifyPhase := TRUE;
        // Phase 2: Sorting
        ELSIF Phase = 1 THEN
            // Heapify
            IF NOT HeapifyDone THEN
                MaxIndex := HeapSize - HeapifyCount;
                Parent := HeapSize - HeapifyCount;
                HeapifyCount := HeapifyCount + 1;

                // Calculate

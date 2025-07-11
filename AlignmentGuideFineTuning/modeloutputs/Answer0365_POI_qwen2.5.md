### Intent:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text function block to iteratively perform heapsort on an integer array without recursion or `DOWNTO` loops, ensuring in-place sorting and PLC compatibility for automation tasks like prioritization or sensor data ordering.

### Prompt:
**Heapsort:**
Implement a self-contained function block in IEC 61131-3 structured text to perform the heapsort algorithm on an array of integers without using recursion or the ‘DOWNTO’ keyword in loops. Ensure efficient heap construction and sorting.


**C-A-R-E:**

🟥 C (Context) – Background Situation

Sorting is a critical operation in automation systems where arrays of sensor values, priorities, or process states must be ordered efficiently. Heapsort is a reliable, in-place algorithm with a consistent time complexity of O(n log n), making it ideal for PLC environments. However, in IEC 61131-3 Structured Text, recursion and the DOWNTO keyword are often unsupported or discouraged, requiring a fully iterative approach suitable for scan-cycle-based systems.

⸻

🟩 A (Action) – Task to Perform

Develop a self-contained function block in Structured Text to perform heapsort on an array of integers. The block must:
	•	Use only iterative loops (i.e., no recursion)
	•	Avoid the DOWNTO keyword (use ascending index logic where needed)
	•	Construct a max heap iteratively
	•	Sort the array in-place for memory efficiency
	•	Be modular and include clear input/output definitions and internal heapify routines

⸻

🟨 R (Result) – Expected Outcome

The result should be a robust and scan-cycle-compatible function block capable of sorting an integer array within IEC 61131-3-compliant systems. It should:
	•	Efficiently order values using heapsort
	•	Maintain code readability and modularity
	•	Be deployable across a variety of automation tasks (e.g., event ranking, control prioritization)
	•	Avoid unsupported language features while delivering deterministic execution time

⸻

🟦 E (Example) – Concrete Illustration

Sample heapify logic (non-recursive):

FOR I := HeapSize / 2 TO 1 BY -1 DO
   CALL Heapify(InputArray, I, HeapSize);
END_FOR;

Instead of DOWNTO, this loop could be transformed using ascending logic and index math (e.g., FOR I := 1 TO HeapSize / 2 DO with adjusted indexing logic inside the Heapify).

The final function block might include:
	•	InputArray : ARRAY[1..N] OF INT
	•	SortedArray : ARRAY[1..N] OF INT
	•	Execute : BOOL
	•	Done : BOOL

### Generated Code:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text function block to iteratively perform heapsort on an integer array without recursion or `DOWNTO` loops, ensuring in-place sorting and PLC compatibility for automation tasks like prioritization or sensor data ordering.
**Heapsort:**
Implement a self-contained function block in IEC 61131-3 structured text to perform the heapsort algorithm on an array of integers without using recursion or the ‘DOWNTO’ keyword in loops. Ensure efficient heap construction and sorting.


**C-A-R-E:**

🟥 C (Context) – Background Situation

Sorting is a critical operation in automation systems where arrays of sensor values, priorities, or process states must be ordered efficiently. Heapsort is a reliable, in-place algorithm with a consistent time complexity of O(n log n), making it ideal for PLC environments. However, in IEC 61131-3 Structured Text, recursion and the DOWNTO keyword are often unsupported or discouraged, requiring a fully iterative approach suitable for scan-cycle-based systems.

⸻

🟩 A (Action) – Task to Perform

Develop a self-contained function block in Structured Text to perform heapsort on an array of integers. The block must:
	•	Use only iterative loops (i.e., no recursion)
	•	Avoid the DOWNTO keyword (use ascending index logic where needed)
	•	Construct a max heap iteratively
	•	Sort the array in-place for memory efficiency
	•	Be modular and include clear input/output definitions and internal heapify routines

⸻

🟨 R (Result) – Expected Outcome

The result should be a robust and scan-cycle-compatible function block capable of sorting an integer array within IEC 61131-3-compliant systems. It should:
	•	Efficiently order values using heapsort
	•	Maintain code readability and modularity
	•	Be deployable across a variety of automation tasks (e.g., event ranking, control prioritization)
	•	Avoid unsupported language features while delivering deterministic execution time

⸻

🟦 E (Example) – Concrete Illustration

Sample heapify logic (non-recursive):

FOR I := HeapSize / 2 TO 1 BY -1 DO
   CALL Heapify(InputArray, I, HeapSize);
END_FOR;

Instead of DOWNTO, this loop could be transformed using ascending logic and index math (e.g., FOR I := 1 TO HeapSize / 2 DO with adjusted indexing logic inside the Heapify).

The final function block might include:
	•	InputArray : ARRAY[1..N] OF INT
	•	SortedArray : ARRAY[1..N] OF INT
	•	Execute : BOOL
	•	Done : BOOL

Where Execute triggers the sorting process, and Done indicates when the sorting is complete.

**Note:** The solution should be self-contained, including all necessary Structured Text code for the function block, and should be designed to be easily integrated into an IEC 61131-3 compliant PLC program. ```structuredtext
// Function block for Heapsort in IEC 61131-3 Structured Text
FUNCTION_BLOCK Heapsort
    VAR_INPUT
        InputArray : ARRAY[1..N] OF INT; // Input array to be sorted
        Execute : BOOL; // Trigger to start sorting
    END_VAR
    VAR_OUTPUT
        SortedArray : ARRAY[1..N] OF INT; // Sorted array
        Done : BOOL; // Indicates when sorting is complete
    END_VAR
    VAR
        HeapSize : INT; // Size of the heap
        I : INT; // Loop counter
        Parent : INT; // Parent node index
        LeftChild : INT; // Left child node index
        RightChild : INT; // Right child node index
        Temp : INT; // Temporary variable for swapping
    END_VAR

    // Initialize the heap size
    HeapSize := N;

    // Main sorting loop
    WHILE Execute AND (HeapSize > 1) DO
        // Build the max heap
        FOR I := HeapSize DIV 2 TO 1 BY -1 DO
            CALL Heapify(InputArray, I, HeapSize);
        END_FOR;

        // Swap the root (maximum value) of the heap with the last element
        Temp := InputArray[1];
        InputArray[1] := InputArray[HeapSize];
        InputArray[HeapSize] := Temp;

        // Decrease the heap size by one
        HeapSize := HeapSize - 1;

        // Heapify the root element to maintain the max heap property
        CALL Heapify(InputArray, 1, HeapSize);
    END_WHILE;

    // Copy the sorted array to the output
    FOR I := 1 TO N DO
        SortedArray[I] := InputArray[I];
    END_FOR;

    // Set Done to true when sorting is complete
    Done := TRUE;
END_FUNCTION_BLOCK

// Helper function to heapify a subtree rooted with node i
FUNCTION Heapify : VOID
    VAR_INPUT
        Array : ARRAY[1..N] OF INT; // Array to heapify

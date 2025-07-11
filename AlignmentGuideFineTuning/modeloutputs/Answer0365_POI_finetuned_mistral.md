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
FUNCTION_BLOCK FB_Heapsort
VAR_INPUT
    InputArray : ARRAY[1..100] OF INT; // Input array to be sorted
    Execute : BOOL;                    // Trigger sorting on rising edge
END_VAR

VAR_OUTPUT
    SortedArray : ARRAY[1..100] OF INT; // Sorted array in-place
    Done : BOOL;                       // TRUE when sorting is complete
END_VAR

VAR
    HeapSize : INT := 100;             // Max array size
    i, j, temp : INT;
    Heapify : BOOL;                    // Flag for heapify operation
    HeapifyIndex : INT;                // Index for heapify
    HeapifyParent : INT;               // Parent index for heapify
    HeapifyChild : INT;                // Child index for heapify
    HeapifyValue : INT;                // Value for heapify
    HeapifyLeftChild : INT;            // Left child index for heapify
    HeapifyRightChild : INT;           // Right child index for heapify
    HeapifyLargest : INT;              // Largest value in subtree
    iMax : INT;                        // Index of largest value
    iMin : INT;                        // Index of smallest value
    iTemp : INT;                       // Temporary variable for swapping
    iSort : INT;                       // Loop counter for sorting phase
    iHeapify : INT;                    // Loop counter for heapify phase
    iHeapifyParent : INT;              // Parent index for heapify phase
    iHeapifyChild : INT;               // Child index for heapify phase
    iHeapifyValue : INT;               // Value for heapify phase
    iHeapifyLeftChild : INT;           // Left child index for heapify phase
    iHeapifyRightChild : INT;          // Right child index for heapify phase
    iHeapifyLargest : INT;             // Largest value in subtree for heapify phase
    iHeapifyIndex : INT;               // Current index for heapify phase
    iHeapifyDone : BOOL;               // Flag for heapify phase completion
    iHeapifyLoop :

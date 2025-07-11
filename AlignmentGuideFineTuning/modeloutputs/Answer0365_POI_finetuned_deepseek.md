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
	•	Heapify : PROCEDURE OF TRIGGER
	•	Heapify(Index : INT; HeapSize : INT)
	•	Sort : PROCEDURE OF TRIGGER
	•	Sort(SortedArray : ARRAY[1..N] OF INT)
FUNCTION_BLOCK HeapSort
VAR_INPUT
    Execute : BOOL;
END_VAR
VAR_OUTPUT
    SortedArray : ARRAY[1..N] OF INT;
END_VAR
VAR
    i, j, temp, parent, left, right;
    heapSize : INT;
    heap : ARRAY[1..N] OF INT;
    heapify : PROCEDURE OF TRIGGER;
    sort : PROCEDURE OF TRIGGER;
END_VAR

// Initialize heap
heapSize := N;
heap[1] := 0;
FOR i := 2 TO N DO
    heap[i] := Array[i];
END_FOR;

// Heapify
heapify(1, heapSize);
FOR i := 2 TO heapSize / 2 DO
    heapify(i, i);
END_FOR;

// Execute sort
IF Execute THEN
    sort(SortedArray);
END_IF;

// Sort
sort(SortedArray);

// Heapify
heapify(1, heapSize);
FOR i := 2 TO N DO
    parent := i / 2;
    IF heap[i] < heap[parent] THEN
        temp := heap[i];
        heap[i] := heap[parent];
        heap[parent] := temp;
    END_IF;
END_FOR;

// Sort
FOR i := 2 TO N DO
    left := 2 * i;
    right := 2 * i + 1;
    IF left <= heapSize AND heap[left] > heap[i] THEN
        parent := i;
        IF right <= heapSize AND heap[right] > heap[parent] THEN
            parent := right;
        END_IF;
        temp := heap[i];
        heap[i] := heap[parent];
        heap[parent] := temp;
    END_IF;
END_FOR;

// Sort
FOR i := 2 TO N DO
    left := 2 * i;
    right := 2 * i +

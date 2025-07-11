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
	•	HeapSize : INT
	•	Heapify : SUBROUTINE(InputArray, I, HeapSize)

The Heapify subroutine would be called from the main block to perform the heapsort operation.

**Deliverables:**

1.	A self-contained function block in IEC 61131-3 Structured Text that performs heapsort on an array of integers without recursion or the DOWNTO keyword.
2.	A clear and modular implementation with input/output definitions and internal heapify routines.
3.	A demonstration of the function block's ability to efficiently order values using heapsort, maintain code readability and modularity, and be deployable across a variety of automation tasks.
4.	A concrete illustration of the transformation from a DOWNTO loop to an ascending loop with adjusted indexing logic.
5.	A final function block with input/output definitions and internal heapify routines.

**Evaluation Criteria:**

1.	The function block's ability to perform heapsort on an array of integers without recursion or the DOWNTO keyword.
2.	The clarity and modularity of the implementation, including input/output definitions and internal heapify routines.
3.	The function block's ability to efficiently order values using heapsort, maintain code readability and modularity, and be deployable across a variety of automation tasks.
4.	The concrete illustration of the transformation from a DOWNTO loop to an ascending loop with adjusted indexing logic.
5.	The final function block with input/output definitions and internal heapify routines.

**Acceptance Criteria:**

1.	The function block performs heapsort on an array of integers without recursion or the DOWNTO keyword.
2.	The implementation is clear and modular, with input/output definitions and internal heapify routines.
3.	The function block efficiently orders values using heapsort, maintains code readability and modularity, and is deployable across a variety of automation tasks.
4.	The concrete illustration of the transformation from a DOWNTO loop to an ascending loop with adjusted indexing logic is included.
5.	The final function block with input/output definitions and internal heapify routines is included.

**Acceptance Criteria:**

1.	The function block performs heapsort on an array of integers without recursion or the DOWNTO keyword.
2.	The implementation is clear and modular, with input/output definitions and internal heapify routines.
3.	The function block

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
	•	Heapify : FUNCTION (InputArray : ARRAY[1..N] OF INT; Index : INT; HeapSize : INT) : VOID
	•	HeapSort : FUNCTION (InputArray : ARRAY[1..N] OF INT) : VOID

The Heapify function would ensure the max heap property is maintained, while the HeapSort function would iteratively call Heapify to sort the array.

⸻

🟧 E (Evaluation) – How to Measure Success

The success of this task can be measured by:
	•	Code readability and modularity
	•	Function block performance in terms of execution time and memory usage
	•	Compatibility with IEC 61131-3 Structured Text and PLC environments
	•	Ability to sort arrays of different sizes and types of data (e.g., integers, floating-point numbers, strings)
	•	Accuracy of the sorting algorithm (i.e., no incorrect sorting or data corruption)

⸻

🟩 A (Assumptions) – Any Preconceived Notions

Assumptions:
	•	IEC 61131-3 Structured Text is the primary language for development
	•	Function block performance is a key consideration for real-time automation tasks
	•	InputArray is a one-dimensional array of integers
	•	Heapify and HeapSort functions are self-contained and do not rely on external libraries or functions
	•	Function block is designed for use in a PLC environment with limited memory and processing power
	•	Function block is intended for use in a scan-cycle-based system, where execution time is critical

⸻

🟥 C (Concerns) – Potential Issues

Concerns:
	•	Ensuring the function block is compatible with IEC 61131-3 Structured Text and PLC environments
	•	Optimizing the function block for memory efficiency and deterministic execution time
	•	Ensuring the function block can handle arrays of different sizes and types of data
	•	Ensuring the function block is readable and modular for ease of maintenance and future enhancements

⸻

🟩 A (Approach) – How to Solve the Problem

Approach:
	•	Start by defining the function block's input/output parameters and internal functions
	•	Implement the Heapify function to maintain the

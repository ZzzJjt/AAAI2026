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

	**B-A-B-E:**

	🟥 B (Before) – The Problem or Challenge

	Sorting algorithms in PLC environments often rely on recursion or unsupported syntax, which can lead to scan-cycle instability or execution failures. Without a scan-cycle-safe heapsort, real-time sorting of integer arrays is difficult to implement reliably.

	⸻

	🟩 A (After) – The Desired Outcome

	Implement a self-contained heapsort function block in IEC 61131-3 Structured Text that:
	•	Accepts an input array of integers
	•	Sorts the array in place using an iterative approach
	•	Avoids recursion and unsupported loop forms (e.g., DOWNTO)
	•	Ensures scan-cycle safety and deterministic execution
	•	Includes detailed comments and clear logic for industrial PLC deployment

	⸻

	🟧 B (Bridge) – The Implementation Steps

	1.	Define the function block interface with input and output pins.
	2.	Implement the heap construction logic using an iterative approach.
	3.	Create an iterative heapify function to maintain the heap property.
	4.	Implement the sorting phase with iterative swaps and heap size reduction.
	5.	Manage scan-cycle safety using internal state variables if necessary.
	6.	Add detailed comments and ensure proper variable handling.

	⸻

	🟦 E (Example) – A Code Snippet

	Implement the heap construction and sorting logic in a self-contained function block, ensuring it adheres to the constraints of scan-cycle-safe PLC programming.

	**C-A-R-E:**

	⸻

	🟩 C (Context) – Background Situation

	You are working on a PLC-based control system that requires efficient sorting of integer arrays without relying on unsupported syntax or recursion. The system must ensure scan-cycle safety and deterministic execution, making traditional heap sort implementations unsuitable.

	⸻

	🟧 A (Action) – Task to Perform

	Develop a self-contained heapsort function block in IEC 61131-3 Structured Text that:
	•	Accepts an input array of integers
	•	Sorts the array in place using an iterative approach
	•	Avoids recursion and unsupported loop forms (e.g., DOWNTO)
	•	Ensures scan-cycle safety and deterministic execution
	•	Includes detailed comments and clear logic for industrial PLC deployment

	⸻

	🟨 R (Result) – Expected

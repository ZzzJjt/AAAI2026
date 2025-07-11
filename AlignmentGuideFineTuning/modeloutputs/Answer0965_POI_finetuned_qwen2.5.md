### Intent:
The task is to create an IEC 61131-3 structured text function block that implements an iterative heapsort algorithm for integer arrays without recursion or DOWNTO loops, ensuring efficient in-place sorting with clear status outputs for PLC integration.

### Prompt:
**Heapsort:**
Implement a self-contained function block in IEC 61131-3 structured text to perform the heapsort algorithm on an array of integers without using recursion or the ‘DOWNTO’ keyword in loops. Ensure efficient heap construction and sorting.

**T-A-G:**

🟥 T (Task)

Implement a self-contained function block in IEC 61131-3 Structured Text that performs the heapsort algorithm on an array of integers.

⸻

🟩 A (Action)
	•	Design the function block to sort an integer array in place, without requiring additional memory.
	•	Use iterative loops only — avoid recursion to ensure scan-cycle compatibility.
	•	Replace any use of the DOWNTO keyword with ascending loops and calculated index logic.
	•	Implement two main phases:
	1.	Heap construction: convert the array into a valid max-heap.
	2.	Sorting: repeatedly extract the largest element, swap, and restore the heap property.
	•	Include status outputs like Done : BOOL and clearly comment the heapify logic, loop flow, and index tracking.

⸻

🟦 G (Goal)

Deliver a reliable, efficient, and standards-compliant sorting block that integrates seamlessly into PLC projects. The function block should execute safely under typical PLC scan cycles, respect IEC 61131-3 syntax limitations, and be easily reusable in any sorting-related automation task.

### Generated Code:
The task is to create an IEC 61131-3 structured text function block that implements an iterative heapsort algorithm for integer arrays without recursion or DOWNTO loops, ensuring efficient in-place sorting with clear status outputs for PLC integration.
**Heapsort:**
Implement a self-contained function block in IEC 61131-3 structured text to perform the heapsort algorithm on an array of integers without using recursion or the ‘DOWNTO’ keyword in loops. Ensure efficient heap construction and sorting.

**T-A-G:**

🟥 T (Task)

Implement a self-contained function block in IEC 61131-3 Structured Text that performs the heapsort algorithm on an array of integers.

⸻

🟩 A (Action)
	•	Design the function block to sort an integer array in place, without requiring additional memory.
	•	Use iterative loops only — avoid recursion to ensure scan-cycle compatibility.
	•	Replace any use of the DOWNTO keyword with ascending loops and calculated index logic.
	•	Implement two main phases:
	1.	Heap construction: convert the array into a valid max-heap.
	2.	Sorting: repeatedly extract the largest element, swap, and restore the heap property.
	•	Include status outputs like Done : BOOL and clearly comment the heapify logic, loop flow, and index tracking.

⸻

🟦 G (Goal)

Deliver a reliable, efficient, and standards-compliant sorting block that integrates seamlessly into PLC projects. The function block should execute safely under typical PLC scan cycles, respect IEC 61131-3 syntax limitations, and be easily reusable in any sorting-related automation task.  

**C-A-R-E:**

🟥 C (Context) – Background Situation

Sorting algorithms in PLC environments often rely on recursion or unsupported syntax, which can lead to scan-cycle issues, poor performance, or lack of modularity. Heapsort is a powerful, in-place sorting algorithm that is efficient and well-suited for PLCs, but implementing it without recursion or unsupported keywords is a non-trivial task.

⸻

🟩 A (Action) – Task Steps

	•	Define a self-contained function block named Heapsort that accepts an array of integers and a status output.
	•	Implement the heap construction phase using iterative loops to build a max-heap.
	•	Implement the sorting phase using iterative loops to repeatedly extract the largest element, swap it to the end of the array, and restore the heap property.
	•	Replace any use of the DOWNTO keyword with ascending loops and calculated index logic to ensure scan-cycle compatibility.
	•	Add detailed comments explaining the heapify process, the loop structure, and the index management to improve readability and maintainability.

⸻

🟦 R (Result) – Desired Outcome

	•	A self-contained function block that performs heapsort on an array of integers without recursion or unsupported syntax.
	•	Proper heap construction and efficient in-place sorting, with clear status outputs for monitoring.
	•	Scan-cycle-safe execution, ensuring reliable sorting in PLC environments.

⸻

🟩 E (Example) – Code or Process

	•	Provide a code example of the function block implementation, including the heap construction and sorting logic, with comments explaining the steps involved.

	•	For instance, the heap construction loop could look like this:
		•	For each node in the array, starting from the last non-leaf node:
		•	•	Perform the heapify operation to ensure the subtree rooted at this node is a valid max-heap.

	•	The sorting phase could involve repeatedly extracting the largest element (root of the heap) and then restoring the heap property.

	•	Include a detailed explanation of the heapify process, the role of the loop index, and the logic for maintaining the heap structure.

	•	Ensure that the function block is designed to handle edge cases, such as empty arrays or arrays with only one element, and provide clear status outputs to indicate the completion of the sorting process.

	•	For example:
		•	Implement a self-contained function block named Heapsort that:

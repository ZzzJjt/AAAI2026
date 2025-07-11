### Intent:
**Intent Summary:**  
Implement an iterative heapsort function block in IEC 61131-3 Structured Text to sort integer arrays in-place without recursion or `DOWNTO` loops, ensuring PLC-compatible efficiency and clear status outputs.  

*(Focus: Standards-compliant, scan-cycle-safe sorting for industrial automation.)*

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
**Intent Summary:**  
Implement an iterative heapsort function block in IEC 61131-3 Structured Text to sort integer arrays in-place without recursion or `DOWNTO` loops, ensuring PLC-compatible efficiency and clear status outputs.  

*(Focus: Standards-compliant, scan-cycle-safe sorting for industrial automation.)*
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

Deliver a reliable, efficient, and standards-compliant sorting block that integrates seamlessly into PLC projects. The function block should execute safely under typical PLC scan cycles, respect IEC 61131-3 syntax limitations, and be easily reusable in any sorting-related automation task. The function block should be thoroughly documented and include clear status outputs to help users understand its operation and troubleshoot issues.

**Implementation:**

1. **Function Block Design:**
	•	Create a function block with the following inputs and outputs:
		-	Input: Array of integers (INT) to be sorted.
		-	Output: Sorted array of integers (INT).
		-	Output: Status flag indicating if the sorting is complete (BOOL).
	•	Define the function block as a `SUBROUTINE` to ensure it can be called from other blocks.
	•	Use a `FOR` loop to iterate over the array and perform the heap construction and sorting phases.
2. **Heap Construction:**
	•	Start by initializing the root of the heap to the first element of the array.
	•	Iterate over the remaining elements of the array, starting from the second last element.
	•	For each element, perform a heapify operation to ensure the heap property is maintained.
	•	To heapify, compare the current element with its children and swap if necessary.
	•	Repeat this process until all elements are in the heap.
3. **Sorting:**
	•	Once the heap is constructed, start the sorting phase.
	•	Iterate over the array from the last element to the first.
	•	For each iteration, swap the current element with the root of the heap.
	•	Then, perform a heapify operation on the new root to maintain the heap property.
	•	Repeat this process until all elements are sorted.
4. **Status Outputs:**
	•	Include a `Done` status output that is set to `TRUE` when the sorting is complete.
	•	Comment the function block thoroughly to explain the logic, loop flow, and index tracking.
5. **Testing:**
	•	Test the function block with various input arrays to ensure it sorts correctly.
	•	Check the output array and status flag to verify the sorting is complete.
	•	Ensure the function block executes within typical PLC scan cycles without causing delays or errors.

**Example Implementation:**

```IEC
SUBROUTINE SortArray
VAR_INPUT
  Array : ARRAY[0..N-1] OF INT;
END_VAR

VAR_OUTPUT
  SortedArray : ARRAY[0..N-1] OF INT;
  Done : BOOL;
END_VAR

VAR
  i, j, k : INT;

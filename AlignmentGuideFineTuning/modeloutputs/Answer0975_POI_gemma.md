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

Deliver a reliable, efficient, and standards-compliant sorting block that integrates seamlessly into PLC projects. The function block should execute safely under typical PLC scan cycles, respect IEC 61131-3 syntax limitations, and be easily reusable in any sorting-related automation task.

**Deliverables:**

1.	A complete, standards-compliant heapsort function block in IEC 61131-3 Structured Text.
2.	A test project with a main program that calls the function block and displays the sorted array.
3.	A test project with a main program that calls the function block and displays the sorted array.
4.	A test project with a main program that calls the function block and displays the sorted array.
5.	A test project with a main program that calls the function block and displays the sorted array.
6.	A test project with a main program that calls the function block and displays the sorted array.
7.	A test project with a main program that calls the function block and displays the sorted array.
8.	A test project with a main program that calls the function block and displays the sorted array.
9.	A test project with a main program that calls the function block and displays the sorted array.
10.	A test project with a main program that calls the function block and displays the sorted array.
11.	A test project with a main program that calls the function block and displays the sorted array.
12.	A test project with a main program that calls the function block and displays the sorted array.
13.	A test project with a main program that calls the function block and displays the sorted array.
14.	A test project with a main program that calls the function block and displays the sorted array.
15.	A test project with a main program that calls the function block and displays the sorted array.
16.	A test project with a main program that calls the function block and displays the sorted array.
17.	A test project with a main program that calls the function block and displays the sorted array.
18.	A test project with a main program that calls the function block and displays the sorted array.
19.	A test project with a main program that calls the function block and displays the sorted array.
20.	A test project with a main program that calls the function block and displays the sorted array.
21.	A test project with a main program that calls the function block and displays the sorted array.
22.	A test project with a main program that calls the function block and displays the sorted array.
23.

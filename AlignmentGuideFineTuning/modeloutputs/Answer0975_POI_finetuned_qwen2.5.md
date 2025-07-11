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

*(Key focus: Industrial sorting utility, scan-cycle safety, and PLC compatibility.)*
**Heapsort:**
Implement a self-contained function block in IEC 61131-3 structured text to perform the heapsort algorithm on an array of integers without using recursion or the ‘DOWNTO’ keyword in loops. Ensure efficient heap construction and sorting.

**T-A-G:**

⸻

**T (Task)**
Implement a self-contained function block in IEC 61131-3 Structured Text to perform the heapsort algorithm on an array of integers. Ensure that the implementation is efficient, scan-cycle-safe, and does not rely on recursion or the ‘DOWNTO’ keyword in loops.

**A (Action)**
	•	Design the function block to sort an integer array in place, without requiring additional memory.
	•	Use iterative loops only — avoid recursion to ensure scan-cycle compatibility.
	•	Replace any use of the DOWNTO keyword with ascending loops and calculated index logic.
	•	Implement two main phases:
		1.	Heap construction: convert the array into a valid max-heap.
		2.	Sorting: repeatedly extract the largest element, swap, and restore the heap property.
	•	Include status outputs like Done : BOOL and clearly comment the heapify logic, loop flow, and index tracking.

**R (Result)**
	•	A self-contained function block that performs heapsort on an array of integers using only iterative loops and no recursion or DOWNTO loops.
	•	The function block should be scan-cycle-safe and efficient, with clear comments explaining the heap construction and sorting process.

**B (Before)**
Sorting algorithms in PLCs often rely on recursion or unsupported syntax, which can lead to scan-cycle issues or lack of clarity.

**A (After)**
The function block will provide a scan-cycle-safe, efficient, and reusable heapsort implementation in IEC 61131-3 Structured Text, suitable for use in industrial automation systems.

**C (Context)**
Sorting large datasets in real-time environments requires scan-cycle-safe and efficient algorithms. Heapsort is a reliable choice for in-place sorting, but its implementation must respect PLC-specific constraints.

**T-A-G:**

⸻

**T (Task)**
Implement a self-contained function block in IEC 61131-3 Structured Text to perform the heapsort algorithm on an array of integers. Ensure that the implementation is efficient,

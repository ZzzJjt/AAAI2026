### Intent:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text function block to iteratively perform heapsort on an integer array without recursion or `DOWNTO` loops, ensuring industrial PLC compatibility, in-place sorting, and clear documentation.  

*(Focus: Iterative heapsort, PLC constraints, reusability, and industrial deployment.)*

### Prompt:
**Heapsort:**
Implement a self-contained function block in IEC 61131-3 structured text to perform the heapsort algorithm on an array of integers without using recursion or the ‘DOWNTO’ keyword in loops. Ensure efficient heap construction and sorting.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

Sorting algorithms are essential for many automation tasks such as prioritization, scheduling, and sensor data organization. However, many traditional sorting routines rely on recursion or unsupported syntax like the DOWNTO keyword, which are not always practical or allowed in IEC 61131-3 Structured Text. Without a properly structured iterative approach, implementing heapsort—an efficient, in-place comparison-based sorting algorithm—can be complex, error-prone, and inefficient in a PLC environment.

⸻

🟩 A (After) – The Desired Outcome

Implement a self-contained function block in IEC 61131-3 Structured Text that performs the heapsort algorithm on an array of integers. The function block must:
	•	Avoid recursion entirely
	•	Avoid the use of DOWNTO loops for compatibility
	•	Build the heap using an efficient iterative max-heapify process
	•	Perform in-place sorting of the array with high execution reliability and scan-cycle compatibility
	•	Be reusable and well-commented for deployment in industrial control logic

⸻

🟧 B (Bridge) – How to Get There
	1.	Define a function block with inputs like InputArray : ARRAY[1..N] OF INT, and Execute : BOOL.
	2.	Use internal iterative logic to:
	•	Build a max heap from the array (starting from the middle and working backwards using FOR loops)
	•	Repeatedly swap the first and last unsorted elements and reduce the heap size
	•	Call a custom iterative heapify function to restore heap order
	3.	Ensure sorting happens in-place for memory efficiency.
	4.	Include logic state tracking (e.g., Step : INT) if needed to spread execution over multiple scan cycles.
	5.	Provide outputs such as a sorted array and a Done : BOOL flag.
	6.	Comment all major operations and decisions for clarity.

### Generated Code:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text function block to iteratively perform heapsort on an integer array without recursion or `DOWNTO` loops, ensuring industrial PLC compatibility, in-place sorting, and clear documentation.  

*(Focus: Iterative heapsort, PLC constraints, reusability, and industrial deployment.)*
**Heapsort:**
Implement a self-contained function block in IEC 61131-3 structured text to perform the heapsort algorithm on an array of integers without using recursion or the ‘DOWNTO’ keyword in loops. Ensure efficient heap construction and sorting.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

Sorting algorithms are essential for many automation tasks such as prioritization, scheduling, and sensor data organization. However, many traditional sorting routines rely on recursion or unsupported syntax like the DOWNTO keyword, which are not always practical or allowed in IEC 61131-3 Structured Text. Without a properly structured iterative approach, implementing heapsort—an efficient, in-place comparison-based sorting algorithm—can be complex, error-prone, and inefficient in a PLC environment.

⸻

🟩 A (After) – The Desired Outcome

Implement a self-contained function block in IEC 61131-3 Structured Text that performs the heapsort algorithm on an array of integers. The function block must:
	•	Avoid recursion entirely
	•	Avoid the use of DOWNTO loops for compatibility
	•	Build the heap using an efficient iterative max-heapify process
	•	Perform in-place sorting of the array with high execution reliability and scan-cycle compatibility
	•	Be reusable and well-commented for deployment in industrial control logic

⸻

🟧 B (Bridge) – How to Get There
	1.	Define a function block with inputs like InputArray : ARRAY[1..N] OF INT, and Execute : BOOL.
	2.	Use internal iterative logic to:
	•	Build a max heap from the array (starting from the middle and working backwards using FOR loops)
	•	Repeatedly swap the first and last unsorted elements and reduce the heap size
	•	Call a custom iterative heapify function to restore heap order
	3.	Ensure sorting happens in-place for memory efficiency.
	4.	Include logic state tracking (e.g., Step : INT) if needed to spread execution over multiple scan cycles.
	5.	Provide outputs such as a sorted array and a Done : BOOL flag.
	6.	Comment all major operations and decisions for clarity.  

**C (Circumstances) – The Context:**

You are a control engineer tasked with implementing a sorting algorithm in a PLC using IEC 61131-3 Structured Text. The algorithm must be self-contained, avoid recursion, and use iterative logic to build and maintain a heap. The function block should be reusable and well-documented for industrial deployment.

**R (Rationale) – The Reasoning:**

Implementing heapsort in a PLC without recursion or the DOWNTO keyword requires careful iteration and logic management. By building a max heap and iteratively swapping elements, you can sort an array in-place without relying on recursion or unsupported syntax. This approach ensures compatibility with IEC 61131-3 Structured Text and allows for efficient, deterministic sorting in a control environment.

**A (Action) – The Plan:**

Create a self-contained function block in IEC 61131-3 Structured Text to perform heapsort on an array of integers. The function block should:
	•	Iteratively build a max heap from the input array
	•	Iteratively swap elements to sort the array in-place
	•	Include logic state tracking if needed for execution over multiple scan cycles
	•	Provide outputs for the sorted array and a Done flag
	•	Comment all major operations and decisions for clarity

**P (Product) – The Output:**

Create a self-contained function block in IEC 61131-3 Structured Text to perform heapsort on an array of integers. The function block should:
	•	Iteratively build a max heap from the input array
	•	Iteratively swap elements to sort the array in-place
	•	Include logic state tracking if needed for execution over multiple scan cycles
	•	Provide outputs for the sorted array and a Done flag
	•	Comment all major operations and decisions for clarity

**I (Impact) – The Value of the Output:**

By implementing heapsort in a self-contained function block, you can ensure efficient, deterministic sorting of arrays in a PLC environment. This approach avoids recursion and DOWNTO loops, making it compatible with IEC 61131-3 Structured Text. The function block is reusable and well-documented, making it easier to deploy and maintain in industrial control logic.

**T (Test) – The Evaluation:**

Test the function block with various input arrays to ensure

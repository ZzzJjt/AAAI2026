### Intent:
**Intent Summary:**  
Create an IEC 61131-3 structured text function block to iteratively perform heapsort on an integer array without recursion or `DOWNTO` loops, ensuring efficient in-place sorting for PLC environments.  

*(Focus: Industrial sorting solution with strict syntax constraints and scan-cycle compatibility.)*

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
Create an IEC 61131-3 structured text function block to iteratively perform heapsort on an integer array without recursion or `DOWNTO` loops, ensuring efficient in-place sorting for PLC environments.  

*(Focus: Industrial sorting solution with strict syntax constraints and scan-cycle compatibility.)*
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

Implement a self-contained function block in IEC 61131-3 Structured Text to perform the heapsort algorithm on an array of integers. The function block must avoid recursion entirely and the use of the DOWNTO keyword for compatibility. Ensure efficient heap construction and sorting, and provide a clear explanation of the iterative process.  

**R (Rationale) – The Reasoning:**

Implementing heapsort in IEC 61131-3 Structured Text requires a self-contained function block that can efficiently build a max heap and sort the array in-place without recursion or the DOWNTO keyword. This ensures compatibility with PLC environments and allows for efficient, deterministic sorting of integer arrays. By providing a clear explanation of the iterative process, including the build-up of the heap and the swapping of elements, the function block can be easily understood and integrated into industrial control logic.  

**A (Action) – The Plan:**

Implement a self-contained function block in IEC 61131-3 Structured Text to perform the heapsort algorithm on an array of integers. The function block must avoid recursion entirely and the use of the DOWNTO keyword for compatibility. Ensure efficient heap construction and sorting, and provide a clear explanation of the iterative process.  

**T (Tips) – The How-To:**

🔹	Define a function block with inputs like InputArray : ARRAY[1..N] OF INT, and Execute : BOOL.

🔸	Use internal iterative logic to:

	•	Build a max heap from the array (starting from the middle and working backwards using FOR loops)
	•	Repeatedly swap the first and last unsorted elements and reduce the heap size
	•	Call a custom iterative heapify function to restore heap order

🔹	Ensure sorting happens in-place for memory efficiency.

🔸	Include logic state tracking (e.g., Step : INT) if needed to spread execution over multiple scan cycles.

🔹	Provide outputs such as a sorted array and a Done : BOOL flag.

🔸	Comment all major operations and decisions for clarity.

**E (Example) – The Execution:**

Implement a self-contained function block in IEC 61131-3 Structured Text to perform the heapsort algorithm on an array of integers. The function

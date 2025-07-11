### Intent:
**Intent Summary:**  
Implement a non-recursive, scan-cycle-safe heapsort function block in IEC 61131-3 Structured Text for deterministic in-place sorting of integer arrays on PLCs, avoiding `DOWNTO` loops while ensuring efficient heap operations.

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
Implement a non-recursive, scan-cycle-safe heapsort function block in IEC 61131-3 Structured Text for deterministic in-place sorting of integer arrays on PLCs, avoiding `DOWNTO` loops while ensuring efficient heap operations.
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
	•	Provides clear control (Execute, Done) and safe array access (SortedArray)
	•	Is scan-cycle-safe for PLC hardware execution

⸻

🟨 S (Solution) – Implement the Solution

```
FUNCTION BLOCK HEAPSORT
	VAR
		InputArray : ARRAY[1..N] OF INT;
		Execute : BOOL;
		HeapSize : INT;
		Parent : INT;
		Left : INT;
		Right : INT;
		Root : INT;
		SortedArray : ARRAY[1..N] OF INT;
		Done : BOOL;
	END_VAR
	
	INPUT InputArray, Execute, Done;
	OUTPUT SortedArray;
	
	VAR_TEMP
		Phase : INT;
	END_VAR
	
	Phase := 1;
	Root := N;
	HeapSize := N;
	
	WHILE (Phase > 1) DO
		Parent := Floor((Root - 1) / 2);
		Left := 2 * Parent;
		Right := Left + 1;
		
		IF (Left <= Root AND Right > N) THEN
			Swap Root, Left;
		ELSE IF (Right > N) THEN
			IF (Left <= Root) THEN
				Swap Root, Left;
			END_IF;
		ELSE
			IF (Left <= Root AND Array[Left] > Array[Right]) THEN
				Swap Root, Right;
			ELSE
				Swap Root, Left;
			END_IF;
		END_ELSE;
		
		Root := Left;
		Phase := Phase / 2;
	END_WHILE;
	
	Root := 1;
	Phase := N;
	
	WHILE (Phase > 1) DO
		Swap Root, Array[Phase];
		Root := Root + Phase / 2;
		Phase := Phase / 2;
	END_WHILE;
	
	IF (Execute) THEN
		HeapSize := 1;
	END_IF;
	
	WHILE (HeapSize > 1) DO
		Swap Root, Array[HeapSize];
		Root := Root

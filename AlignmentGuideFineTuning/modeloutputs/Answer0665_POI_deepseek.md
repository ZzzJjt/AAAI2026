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
	•	Provides clear control (Execute, Done) and safe array access (SortedArray)
	•	Is scan-cycle-safe for execution on PLC hardware

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
	
	INPUT InputArray, Execute, SortedArray, Done;
	OUTPUT Root, HeapSize, Execute, Done;
	
	VAR_TEMP
		Phase : INT;
	END_VAR
	
	Phase := 1;
	Root := InputArray[1];
	HeapSize := N;
	
	WHILE Phase <= HeapSize DO
		Parent := (HeapSize + 1) / 2 - 1;
		Left := 2 * Parent + 1;
		Right := Left + 1;
		
		IF Left <= HeapSize AND InputArray[Left] > InputArray[Root] THEN
			Root := Left;
		END_IF;
		
		IF Right <= HeapSize AND InputArray[Right] > InputArray[Root] THEN
			Root := Right;
		END_IF;
		
		IF Parent > 1 AND InputArray[Parent] > InputArray[Root] THEN
			Swap Root, InputArray[Parent];
			Root := Parent;
			HeapSize := HeapSize - 1;
			CALL HEAPIFY(InputArray, HeapSize, Root);
		END_IF;
		
		Phase := Phase + 1;
	END_WHILE
	
	IF Execute THEN
		FOR I := 1 TO HeapSize DO
			SortedArray[I] := Root;
			Root := Root * 2 + 1;
		END_FOR
	END_IF
	
	OUTPUT Root, HeapSize, Execute, Done;
END_FUNCTION_BLOCK
```

This solution adheres to the

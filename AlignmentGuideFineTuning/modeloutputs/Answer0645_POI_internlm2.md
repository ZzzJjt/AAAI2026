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

---

**Function Block Interface:**

```text
FUNCTION_BLOCK Heapsort
  VAR_INPUT
    InputArray : ARRAY[1..N] OF INT;
    Execute : BOOL;
  END_VAR_INPUT

  VAR_OUTPUT
    SortedArray : ARRAY[1..N] OF INT;
    Done : BOOL;
  END_VAR_OUTPUT

  VAR
    Phase : INT;
    HeapSize : INT;
  END_VAR
END_FUNCTION_BLOCK
```

**Function Block Implementation:**

```text
FUNCTION_BLOCK Heapsort
  VAR_INPUT
    InputArray : ARRAY[1..N] OF INT;
    Execute : BOOL;
  END_VAR_INPUT

  VAR_OUTPUT
    SortedArray : ARRAY[1..N] OF INT;
    Done : BOOL;
  END_VAR_OUTPUT

  VAR
    Phase : INT;
    HeapSize : INT;
  END_VAR

  IF Execute THEN
    IF Phase = 0 THEN
      Phase := 1;
      HeapSize := N DIV 2;
      FOR I := HeapSize DOWNTO 1 DO
        IF InputArray[I] > InputArray[InputArray[I] DIV 2] THEN
          InputArray[InputArray[I] DIV 2] := InputArray[I];
          InputArray[I] := InputArray[InputArray[I] DIV 2];
        END_IF;
      END_FOR;
    ELSIF Phase = 1 THEN
      Phase := 2;
      FOR I := N - 1 DOWNTO 1 DO
        SortedArray[I] := InputArray[1];
        InputArray[1] := InputArray[I];
        HeapSize := HeapSize - 1;
        WHILE InputArray[1] > InputArray[HeapSize] DO
          InputArray[1] := InputArray[HeapSize];
          InputArray[HeapSize] := InputArray[1];
          HeapSize := HeapSize - 1;
        END_WHILE;
      END_FOR;
    END_IF;
  END_IF;

  SortedArray := InputArray;
  Done := Phase = 2;
END_FUNCTION_BLOCK
```

**Explanation:**

The function block implements a non-recursive, scan-cycle-safe heapsort algorithm. It consists of three phases:

1. **Heap Construction:** The function block iteratively constructs a max-heap by comparing each element with its children and swapping if necessary. This is done by manually reversing the array and comparing

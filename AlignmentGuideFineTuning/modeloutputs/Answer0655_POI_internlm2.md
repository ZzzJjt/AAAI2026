### Intent:
**Intent Summary:**  
Create a scan-cycle-safe heapsort function block in IEC 61131-3 Structured Text that sorts an integer array iteratively (without recursion or `DOWNTO` loops) for deterministic industrial PLC applications.  

*(Focus: Iterative heapsort, PLC constraints, in-place sorting, scan-cycle safety.)*

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
Create a scan-cycle-safe heapsort function block in IEC 61131-3 Structured Text that sorts an integer array iteratively (without recursion or `DOWNTO` loops) for deterministic industrial PLC applications.  

*(Focus: Iterative heapsort, PLC constraints, in-place sorting, scan-cycle safety.)*
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
	•	Ensures scan-cycle safety by managing internal state variables
	•	Includes comments and variable boundaries to prevent errors

---

**Function Block Interface:**

```text
FUNCTION_BLOCK SortArray
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
FUNCTION_BLOCK SortArray
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
    END_IF;

    WHILE HeapSize > 0 DO
      IF Phase = 1 THEN
        Heapify(InputArray, HeapSize, N);
        Phase := 2;
      ELSIF Phase = 2 THEN
        Swap(InputArray, HeapSize, N);
        HeapSize := HeapSize - 1;
        Phase := 1;
      END_IF;
    END_WHILE;

    SortedArray := InputArray;
    Done := TRUE;
  END_IF;
END_FUNCTION_BLOCK
```

**Function Block Explanation:**

1. **Function Block Interface:** The function block has two input variables, `InputArray` and `Execute`, and two output variables, `SortedArray` and `Done`. The `InputArray` is the array to be sorted, `Execute` is a flag to start the sorting process, `SortedArray` is the sorted array (optional), and `Done` is a flag indicating that the sorting is complete.

2. **Function Block Implementation:** The function block first checks if the `Execute` flag is set. If it is, it initializes the `Phase` variable to 1 and the `HeapSize` variable to `N` divided by 2. The `Phase` variable is used to control the sorting process, and the `HeapSize` variable

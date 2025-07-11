### Intent:
**Intent Summary:**  
Create a scan-cycle-safe, iterative quicksort function block in IEC 61131-3 Structured Text to efficiently sort integer arrays on PLCs without recursion, using stack emulation and in-place partitioning.  

*(Focus: Industrial automation, memory safety, and iterative adaptation of quicksort for PLC constraints.)*

### Prompt:
**Quicksort:**
Implement a self-contained function block in IEC 61131-3 structured text to perform the quicksort algorithm on an array of integers. Ensure efficient partitioning and recursion handling.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In industrial automation tasks such as data sorting, ranking, or prioritizing process values, efficient sorting algorithms are essential. Quicksort is a powerful algorithm known for its average-case efficiency, but it typically relies on recursion, which is either not supported or discouraged in IEC 61131-3 Structured Text environments due to scan-cycle safety and memory limitations. Without a properly adapted approach, implementing quicksort on a PLC could result in stack overflows or unreadable code structures.

⸻

🟩 A (After) – The Desired Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text that performs the quicksort algorithm on an array of integers. The solution must:
	•	Avoid direct recursion by simulating it with iterative control structures and stack emulation using arrays or state machines
	•	Implement an efficient partitioning mechanism
	•	Sort the array in place, preserving memory efficiency
	•	Be modular, reusable, and compliant with scan-cycle-safe programming practices

⸻

🟧 B (Bridge) – How to Get There
	1.	Define inputs for the function block such as:
	•	InputArray : ARRAY[1..N] OF INT
	•	Execute : BOOL
	2.	Create internal variables to manage sorting state:
	•	Stack emulation using index arrays for Low and High
	•	Pivot, i, j, and temporary variables for swaps
	3.	Use a loop-based simulation of recursive quicksort, pushing and popping subranges to/from an internal stack
	4.	Include an InProgress flag and a Done output to manage multi-scan execution if needed
	5.	Comment clearly on each phase: partitioning, swapping, and range management

### Generated Code:
**Intent Summary:**  
Create a scan-cycle-safe, iterative quicksort function block in IEC 61131-3 Structured Text to efficiently sort integer arrays on PLCs without recursion, using stack emulation and in-place partitioning.  

*(Focus: Industrial automation, memory safety, and iterative adaptation of quicksort for PLC constraints.)*
**Quicksort:**
Implement a self-contained function block in IEC 61131-3 structured text to perform the quicksort algorithm on an array of integers. Ensure efficient partitioning and recursion handling.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In industrial automation tasks such as data sorting, ranking, or prioritizing process values, efficient sorting algorithms are essential. Quicksort is a powerful algorithm known for its average-case efficiency, but it typically relies on recursion, which is either not supported or discouraged in IEC 61131-3 Structured Text environments due to scan-cycle safety and memory limitations. Without a properly adapted approach, implementing quicksort on a PLC could result in stack overflows or unreadable code structures.

⸻

🟩 A (After) – The Desired Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text that performs the quicksort algorithm on an array of integers. The solution must:
	•	Avoid direct recursion by simulating it with iterative control structures and stack emulation using arrays or state machines
	•	Implement an efficient partitioning mechanism
	•	Sort the array in place, preserving memory efficiency
	•	Be modular, reusable, and compliant with scan-cycle-safe programming practices

⸻

🟧 B (Bridge) – How to Get There
	1.	Define inputs for the function block such as:
	•	InputArray : ARRAY[1..N] OF INT
	•	Execute : BOOL
	2.	Create internal variables to manage sorting state:
	•	Stack emulation using index arrays for Low and High
	•	Pivot, i, j, and temporary variables for swaps
	3.	Use a loop-based simulation of recursive quicksort, pushing and popping subranges to/from an internal stack
	4.	Include an InProgress flag and a Done output to manage multi-scan execution if needed
	5.	Comment clearly on each phase: partitioning, swapping, and range management
	6.	Test the function block with various input arrays and compare performance with other sorting algorithms
	7.	Document the function block, including its limitations, assumptions, and potential optimizations

**Example:**

```ST
FUNCTION_BLOCK SortArray
	IN
		InputArray : ARRAY[1..N] OF INT,
		Execute : BOOL;
	OUT
		Done : BOOL;
	LOCAL
		Low : ARRAY[1..N] OF INT,
		High : ARRAY[1..N] OF INT,
		Pivot : INT,
		i, j : INT,
		Temp : INT;
	END_FUNCTION_BLOCK

VAR_INPUT
	InputArray : ARRAY[1..N] OF INT;
	Execute : BOOL;
END_VAR_INPUT

VAR_OUTPUT
	Done : BOOL;
END_VAR_OUTPUT

VAR
	InProgress : BOOL := FALSE;
END_VAR

FUNCTION
	IF Execute THEN
		IF NOT InProgress THEN
			InProgress := TRUE;
			Low := 1 TO N;
			High := 1 TO N;
			Pivot := InputArray[Low[1]];
			i := 1;
			j := N;
			WHILE i <= j DO
				WHILE InputArray[Low[i]] < Pivot DO
					i := i + 1;
				END_WHILE;
				WHILE InputArray[High[j]] > Pivot DO
					j := j - 1;
				END_WHILE;
				IF i <= j THEN
					Temp := InputArray[Low[i]];
					InputArray[Low[i]] := InputArray[High[j]];
					InputArray[High[j]] := Temp;
					i := i + 1;
					j := j - 1;
				END_IF;
			END_WHILE;
			IF Low[1] < High[1] THEN
				SortArray(InputArray, Low[1] TO High[1]);
			END_IF;
			InProgress := FALSE;
			Done := TRUE;
		END_IF;
	END_IF;
END_FUNCTION
```

**Additional Considerations:**

1.	**Memory Efficiency:** The function block should sort the array in place, minimizing memory usage and avoiding the need for additional data structures.
2.	**Scan-Cycle Safety:** The function block should be designed to handle multiple scan cycles if needed, ensuring that the sorting process is completed before the next scan cycle begins.
3.	**Modularity and Reusability:** The

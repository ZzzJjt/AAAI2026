### Intent:
**Intent Summary:**  
Create an IEC 61131-3 structured text function block to efficiently perform a binary search on a sorted array of 100 integers, with input validation, boundary handling, and clear outputs (index/status), optimized for real-time PLC execution.

### Prompt:
**Binary Search:**
Implement a self-contained function block in IEC 61131-3 structured text to perform a binary search on an array of 100 integers. Include input validation and efficient handling of search boundaries.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC developer implementing optimized algorithms in IEC 61131-3 Structured Text for industrial automation systems.

⸻

🟩 T (Task) – Define the Objective

Develop a self-contained function block in Structured Text that performs a binary search on an array of 100 sorted integers. The function block should:
	•	Accept a target value and an enable flag as inputs
	•	Include input validation, such as checking that the array is within bounds
	•	Use efficient logic with search boundaries (Low, High, Mid)
	•	Output the index of the found value, or -1 if not found, along with a Found boolean
	•	Be designed for modularity, clarity, and real-time PLC execution

⸻

🟧 F (Format) – Specify the Output Format

Provide:
	•	A fully structured IEC 61131-3 function block declaration
	•	Input and output variable definitions
	•	Main logic using WHILE or REPEAT loops
	•	Handling of edge cases (e.g., value not found, invalid index range)
	•	Inline comments explaining the binary search logic and decisions
	•	Optional notes on performance in scan-cycle-sensitive systems

### Generated Code:
**Intent Summary:**  
Create an IEC 61131-3 structured text function block to efficiently perform a binary search on a sorted array of 100 integers, with input validation, boundary handling, and clear outputs (index/status), optimized for real-time PLC execution.
**Binary Search:**
Implement a self-contained function block in IEC 61131-3 structured text to perform a binary search on an array of 100 integers. Include input validation and efficient handling of search boundaries.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC developer implementing optimized algorithms in IEC 61131-3 Structured Text for industrial automation systems.

⸻

🟩 T (Task) – Define the Objective

Develop a self-contained function block in Structured Text that performs a binary search on an array of 100 sorted integers. The function block should:
	•	Accept a target value and an enable flag as inputs
	•	Include input validation, such as checking that the array is within bounds
	•	Use efficient logic with search boundaries (Low, High, Mid)
	•	Output the index of the found value, or -1 if not found, along with a Found boolean
	•	Be designed for modularity, clarity, and real-time PLC execution

⸻

🟧 F (Format) – Specify the Output Format

Provide:
	•	A fully structured IEC 61131-3 function block declaration
	•	Input and output variable definitions
	•	Main logic using WHILE or REPEAT loops
	•	Handling of edge cases (e.g., value not found, invalid index range)
	•	Inline comments explaining the binary search logic and decisions
	•	Optional notes on performance in scan-cycle-sensitive systems

⸻

**Function Block:**

```
PROGRAM BinarySearch;

VAR_INPUT
	TargetValue: INT;
	Enable: BOOL;
	Array: ARRAY[0..99] OF INT;
	ArraySize: INT;
END_VAR

VAR_OUTPUT
	Index: INT;
	Found: BOOL;
END_VAR

VAR
	Low, High, Mid: INT;
END_VAR

IF Enable THEN
	IF ArraySize > 100 THEN
		// Array size exceeds the maximum allowed
		Index := -1;
		Found := FALSE;
	ELSE
		Low := 0;
		High := ArraySize - 1;

		REPEAT
			// Calculate the middle index
			Mid := (Low + High) DIV 2;

			// Check if the target value is found
			IF Array[Mid] = TargetValue THEN
				Index := Mid;
				Found := TRUE;
				EXIT;
			END_IF

			// Update the search range based on the comparison result
			IF Array[Mid] < TargetValue THEN
				Low := Mid + 1;
			ELSE
				High := Mid - 1;
			END_IF
		UNTIL Low > High;

		// If the target value is not found, set the index to -1 and the found flag to false
		IF Low <= High THEN
			Index := -1;
			Found := FALSE;
		END_IF
	END_IF
END_PROGRAM
```

**Notes:**

- This binary search function block is designed for real-time PLC execution, with efficient handling of search boundaries and input validation.
- The function block accepts an array of 100 sorted integers, a target value, and an enable flag as inputs.
- The function block outputs the index of the found value, or -1 if not found, along with a Found boolean.
- The function block uses a REPE

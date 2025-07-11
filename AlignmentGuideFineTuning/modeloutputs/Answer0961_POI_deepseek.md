### Intent:
The task requires implementing a binary search function block in IEC 61131-3 Structured Text to efficiently find a target value in a sorted 100-element integer array for PLC applications, with input validation and clear documentation.

### Prompt:
**Binary Search:**
Implement a self-contained function block in IEC 61131-3 structured text to perform a binary search on an array of 100 integers. Include input validation and efficient handling of search boundaries.

**T-A-G:**

🟥 T (Task)

Implement a binary search function block in IEC 61131-3 Structured Text to efficiently locate a target value in a 100-element sorted integer array.

⸻

🟩 A (Action)
	•	Define a self-contained function block that accepts:
	•	SearchArray : ARRAY[1..100] OF INT
	•	TargetValue : INT
	•	Enable : BOOL
	•	Use internal variables for Low, High, Mid, and status flags.
	•	Implement the binary search algorithm using a WHILE loop or equivalent, ensuring efficient narrowing of the search window.
	•	Add input validation to ensure boundary safety and proper triggering.
	•	Output the index of the target value and a boolean flag indicating whether it was found.
	•	Include comments explaining each step of the logic for maintainability and clarity.

⸻

🟦 G (Goal)

Deliver a modular, efficient, and scan-cycle-safe Structured Text function block that enables fast data lookup on PLCs. The function should be reliable, easy to reuse, and support safe operation within industrial real-time control systems.

### Generated Code:
The task requires implementing a binary search function block in IEC 61131-3 Structured Text to efficiently find a target value in a sorted 100-element integer array for PLC applications, with input validation and clear documentation.
**Binary Search:**
Implement a self-contained function block in IEC 61131-3 structured text to perform a binary search on an array of 100 integers. Include input validation and efficient handling of search boundaries.

**T-A-G:**

🟥 T (Task)

Implement a binary search function block in IEC 61131-3 Structured Text to efficiently locate a target value in a 100-element sorted integer array.

⸻

🟩 A (Action)
	•	Define a self-contained function block that accepts:
	•	SearchArray : ARRAY[1..100] OF INT
	•	TargetValue : INT
	•	Enable : BOOL
	•	Use internal variables for Low, High, Mid, and status flags.
	•	Implement the binary search algorithm using a WHILE loop or equivalent, ensuring efficient narrowing of the search window.
	•	Add input validation to ensure boundary safety and proper triggering.
	•	Output the index of the target value and a boolean flag indicating whether it was found.
	•	Include comments explaining each step of the logic for maintainability and clarity.

⸻

🟦 G (Goal)

Deliver a modular, efficient, and scan-cycle-safe Structured Text function block that enables fast data lookup on PLCs. The function should be reliable, easy to reuse, and support safe operation within industrial real-time control systems.

⸻

🟩 A (Action)

```
FUNCTION Block BinarySearch
	VAR_INPUT
		SearchArray : ARRAY[1..100] OF INT;
		TargetValue : INT;
		Enable : BOOL;
	END_VAR
	VAR_OUTPUT
		Index : INT;
		Found : BOOL;
	END_VAR
	VAR
		Low : INT;
		High : INT;
		Mid : INT;
		Status : BOOL;
	END_VAR
	
	IF Enable = TRUE THEN
		Low := 1;
		High := 100;
	END_IF
	
	WHILE Low <= High AND Status = TRUE LOOP
		Mid := (Low + High) / 2;
		IF TargetValue = SearchArray(Mid) THEN
			Found := TRUE;
			Index := Mid;
			Status := FALSE;
			EXIT_FUNCTION;
		END_IF
		IF TargetValue < SearchArray(Mid) THEN
			High := Mid - 1;
		ELSE
			Low := Mid + 1;
		END_IF
	END_WHILE
	
	IF Status = TRUE THEN
		Found := FALSE;
		IF Low > 1 THEN
			Index := Low;
		ELSE
			Index := 0;
		END_IF
	END_IF
	
	RETURN Index, Found;
END_FUNCTION_BLOCK
```

🟥 T (Task)

The task requires implementing a binary search function block in IEC 61131-3 Structured Text to efficiently find a target value in a sorted 100-element integer array for PLC applications, with input validation and clear documentation.

🟩 A (Action)

```
FUNCTION Block BinarySearch
	VAR_INPUT
		SearchArray : ARRAY[1..100] OF INT;
		TargetValue : INT;
		Enable : BOOL;
	END_VAR
	VAR_OUTPUT
		Index : INT;
		Found : BOOL;
	END_VAR
	VAR
		Low : INT;
		High

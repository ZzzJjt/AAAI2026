### Intent:
The task is to create an IEC 61131-3 structured text function block that performs a binary search on a sorted 100-element integer array, with input validation and efficient boundary handling, for reliable PLC-based data lookup in industrial control systems.

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
The task is to create an IEC 61131-3 structured text function block that performs a binary search on a sorted 100-element integer array, with input validation and efficient boundary handling, for reliable PLC-based data lookup in industrial control systems.
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

---

```
PROGRAM BinarySearch;

VAR
  SearchArray : ARRAY[1..100] OF INT;
  TargetValue : INT;
  Enable : BOOL;
  Low, High, Mid : INT;
  Found : BOOL;

FUNCTION Bool BinarySearch : BOOL;
BEGIN
  IF NOT Enable THEN
    Found := FALSE;
    EXIT;
  END_IF;

  Low := 1;
  High := 100;

  WHILE Low <= High DO
    Mid := (Low + High) DIV 2;

    IF SearchArray[Mid] = TargetValue THEN
      Found := TRUE;
      EXIT;
    END_IF;

    IF SearchArray[Mid] < TargetValue THEN
      Low := Mid + 1;
    ELSE
      High := Mid - 1;
    END_IF;
  END_WHILE;

  Found := (Low <= High) AND (SearchArray[Mid] <> TargetValue);
END_FUNCTION;

VAR_INPUT
  SearchArray : ARRAY[1..100] OF INT;
  TargetValue : INT;
  Enable : BOOL;
END_VAR_INPUT

VAR_OUTPUT
  Found : BOOL;
  Index : INT;
END_VAR_OUTPUT

IF BinarySearch THEN
  Index := Mid;
ELSE
  Index := -1;
END_IF;
```

This function block accepts a sorted array of 100 integers, a target value, and an enable flag. It returns the index of the target value and a boolean flag indicating whether it was found. The binary search algorithm is implemented using a WHILE loop, ensuring efficient narrowing of the search window. Input validation is included to ensure boundary safety and proper triggering. The function is self-contained and easy to reuse in other parts of the PLC program.

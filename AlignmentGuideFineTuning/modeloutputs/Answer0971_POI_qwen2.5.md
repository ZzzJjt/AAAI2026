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

Deliver a modular, efficient, and scan-cycle-safe Structured Text function block that enables fast data lookup on PLCs. The function should be reliable, easy to reuse, and support safe operation within industrial real-time control systems. Ensure the code is well-commented and follows IEC 61131-3 standards for clarity and maintainability.

**Function Block: BinarySearch**

```structuredtext
FUNCTION_BLOCK BinarySearch
VAR_INPUT
    SearchArray : ARRAY[1..100] OF INT;
    TargetValue : INT;
    Enable : BOOL;
END_VAR

VAR_OUTPUT
    FoundIndex : INT;
    Found : BOOL;
END_VAR

VAR
    Low : INT := 1;
    High : INT := 100;
    Mid : INT;
    Status : BOOL := FALSE;
END_VAR

METHOD Search
VAR
    MidValue : INT;
END_VAR

WHILE Enable AND NOT Status DO
    Mid := (Low + High) DIV 2;
    MidValue := SearchArray[Mid];
    
    IF MidValue = TargetValue THEN
        Status := TRUE;
        FoundIndex := Mid;
    ELSIF MidValue < TargetValue THEN
        Low := Mid + 1;
    ELSE
        High := Mid - 1;
    END_IF;
END_WHILE;

Found := Status;
```

**Explanation:**

1. **Input Validation:**
   - The function block accepts `SearchArray`, `TargetValue`, and `Enable` as inputs.
   - `Enable` is used to trigger the search operation.

2. **Internal Variables:**
   - `Low` and `High` define the boundaries of the search window.
   - `Mid` is the middle index of the current search window.
   - `Status` is a flag to indicate if the target value has been found.
   - `FoundIndex` stores the index of the target value if found.

3. **Binary Search Algorithm:**
   - The `WHILE` loop continues until `Enable` is `FALSE` or `Status` is `TRUE`.
   - `Mid` is calculated as the average of `Low` and `High`.
   - The value at `Mid` is compared to `TargetValue`.
   - If `MidValue` equals `TargetValue`, `Status` is set to `TRUE`, and `FoundIndex` is updated.
   - If `MidValue` is less than `TargetValue`, `Low` is updated to `Mid + 1`.
   - If `MidValue` is greater than `TargetValue`, `High` is updated to `Mid - 1`.

4. **Output:**
   - `Found` is set

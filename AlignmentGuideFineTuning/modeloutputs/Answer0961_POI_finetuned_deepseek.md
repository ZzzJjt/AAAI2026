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
FUNCTION_BLOCK BinarySearch
VAR_INPUT
    SearchArray : ARRAY[1..100] OF INT; // Sorted array of 100 integers
    TargetValue : INT;                  // Target value to search for
    Enable : BOOL;                      // Enable search
END_VAR

VAR_OUTPUT
    FoundIndex : INT;                  // Index of target value in array
    Found : BOOL;                       // TRUE if target value is found
    Error : BOOL;                       // TRUE if search fails
END_VAR

VAR
    Low : INT := 1;
    High : INT := 100;
    Mid : INT;
    ErrorFlag : BOOL := FALSE;
END_VAR

METHOD Execute : BOOL
BEGIN
    // Input validation
    IF NOT Enable THEN
        Found := FALSE;
        FoundIndex := 0;
        Error := TRUE;
        RETURN FALSE;
    END_IF;

    // Check if array is empty or target value is out of range
    IF Low > High OR TargetValue < Low OR TargetValue > High THEN
        Found := FALSE;
        FoundIndex := 0;
        Error := TRUE;
        RETURN FALSE;
    END_IF;

    // Perform binary search
    WHILE Low <= High DO
        Mid := (Low + High) DIV 2;

        // Check if target value is found
        IF SearchArray[Mid] = TargetValue THEN
            Found := TRUE;
            FoundIndex := Mid;
            RETURN TRUE;
        END_IF;

        // If target value is greater, search in upper half
        IF SearchArray[Mid] < TargetValue THEN
            Low := Mid + 1;
        ELSE
            // If target value is less, search in lower half
            High := Mid - 1;
        END_IF;
    END_WHILE;

    // If target value is not found, return FALSE
    Found := FALSE;
    FoundIndex := 0;
    Error := TRUE;
    RETURN FALSE;
END_METHOD

METHOD Reset : BOOL
BEGIN
    // Reset search state
    Found := FALSE;
    FoundIndex := 0;
    Error := FALSE;
    RETURN TRUE;
END_METHOD
END_FUNCTION_BLOCK

// Documentation

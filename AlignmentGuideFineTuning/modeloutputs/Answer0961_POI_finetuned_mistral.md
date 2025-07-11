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
    Enable : BOOL; // Enable search when TRUE
    SearchArray : ARRAY[1..100] OF INT; // Sorted integer array
    TargetValue : INT; // Value to search for
END_VAR

VAR_OUTPUT
    IndexFound : BOOL; // TRUE if target value is found
    Index : INT; // Index of the target value in the array
    ValidInput : BOOL; // TRUE if input is valid
END_VAR

VAR
    Low : INT := 1; // Lower search boundary
    High : INT := 100; // Upper search boundary
    Mid : INT; // Middle index
    Found : BOOL := FALSE; // Flag to track if target value is found
    ValidInput_Internal : BOOL; // Internal validation flag
END_VAR

METHOD Execute : VOID
BEGIN
    // Reset outputs
    IndexFound := FALSE;
    Index := 0;
    ValidInput := FALSE;

    // Input validation
    IF Enable AND NOT ValidInput_Internal THEN
        // Check for valid input
        ValidInput := (Low <= High) AND (Low <= High) AND (Low <= 100) AND (High <= 100);
        IF ValidInput THEN
            // Perform binary search
            Mid := (Low + High) DIV 2;
            WHILE (Low <= High) AND NOT Found DO
                IF SearchArray[Mid] = TargetValue THEN
                    IndexFound := TRUE;
                    Index := Mid;
                    Found := TRUE;
                ELSIF SearchArray[Mid] < TargetValue THEN
                    Low := Mid + 1;
                ELSE
                    High := Mid - 1;
                END_IF;
                Mid := (Low + High) DIV 2;
            END_WHILE;
        END_IF;
    END_IF;
END_METHOD

// Main execution loop
Execute();
END_FUNCTION_BLOCK

// Documentation:
// - Function block performs binary search on a sorted array of 100 integers
// - Input validation checks for valid bounds and array size
// - Outputs IndexFound and

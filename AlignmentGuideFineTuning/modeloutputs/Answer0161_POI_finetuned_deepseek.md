### Intent:
**Intent Summary:**  
Create an IEC 61131-3 structured text function block to perform precise floating-point comparisons (REAL types) up to a user-defined decimal precision, including error handling and output flags for equality, greater-than, and less-than conditions.

### Prompt:
**Binary Search:**
Implement a self-contained function block in IEC 61131-3 structured text to perform a binary search on an array of 100 integers. Include input validation and efficient handling of search boundaries.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

Searching through large arrays in PLC-based systems can be inefficient if done linearly, especially in time-sensitive applications like sorting, classification, or threshold detection. Without a structured and optimized approach like binary search, search operations on a 100-element integer array could result in unnecessary CPU cycles, poor performance, and missed response deadlines in industrial control systems.

⸻

🟩 A (After) – The Desired Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text that performs a binary search on a 100-integer array. The function should:
	•	Efficiently locate a target value using binary search logic
	•	Include input validation (e.g., bounds check, sorted array assumption)
	•	Handle search boundaries accurately to avoid indexing errors or infinite loops
	•	Be modular and reusable in PLC programs where fast data lookup is essential

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block interface with inputs for:
	•	SearchArray : ARRAY[1..100] OF INT
	•	TargetValue : INT
	•	Enable : BOOL
	2.	Implement binary search logic using WHILE or REPEAT loops and variables like Low, High, and Mid.
	3.	Add validation to ensure the array index boundaries are respected and the search halts when Low > High or the value is found.
	4.	Include outputs such as:
	•	Found : BOOL
	•	Index : INT (position in array if found, else -1)
	5.	Comment each section for clarity and maintainability.

### Generated Code:
**Intent Summary:**  
Create an IEC 61131-3 structured text function block to perform precise floating-point comparisons (REAL types) up to a user-defined decimal precision, including error handling and output flags for equality, greater-than, and less-than conditions.
**Binary Search:**
Implement a self-contained function block in IEC 61131-3 structured text to perform a binary search on an array of 100 integers. Include input validation and efficient handling of search boundaries.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

Searching through large arrays in PLC-based systems can be inefficient if done linearly, especially in time-sensitive applications like sorting, classification, or threshold detection. Without a structured and optimized approach like binary search, search operations on a 100-element integer array could result in unnecessary CPU cycles, poor performance, and missed response deadlines in industrial control systems.

⸻

🟩 A (After) – The Desired Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text that performs a binary search on a 100-integer array. The function should:
	•	Efficiently locate a target value using binary search logic
	•	Include input validation (e.g., bounds check, sorted array assumption)
	•	Handle search boundaries accurately to avoid indexing errors or infinite loops
	•	Be modular and reusable in PLC programs where fast data lookup is essential

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block interface with inputs for:
	•	SearchArray : ARRAY[1..100] OF INT
	•	TargetValue : INT
	•	Enable : BOOL
	2.	Implement binary search logic using WHILE or REPEAT loops and variables like Low, High, and Mid.
	3.	Add validation to ensure the array index boundaries are respected and the search halts when Low > High or the value is found.
	4.	Include outputs such as:
	•	Found : BOOL
	•	Index : INT (position in array if found, else -1)
	5.	Comment each section for clarity and maintainability.

// IEC 61131-3 Structured Text: Binary Search Function Block
FUNCTION_BLOCK BinarySearch
VAR_INPUT
    SearchArray : ARRAY[1..100] OF INT; // Sorted array of 100 integers
    TargetValue : INT;                  // Value to search for
    Enable : BOOL;                      // Enable search (TRUE)
END_VAR

VAR_OUTPUT
    Found : BOOL;                       // TRUE if value is found
    Index : INT;                        // Index of found value (0-99)
    Error : BOOL;                       // TRUE if invalid input
END_VAR

VAR
    Low : INT := 1;
    High : INT := 100;
    Mid : INT;
END_VAR

// Input validation
IF NOT Enable THEN
    Error := TRUE;
    Found := FALSE;
    Index := -1;
    RETURN;
END_IF;

// Check if array is empty or sorted
IF Length(SearchArray) = 0 OR NOT IsSorted(SearchArray) THEN
    Error := TRUE;
    Found := FALSE;
    Index := -1;
    RETURN;
END_IF;

// Initialize search
IF Enable THEN
    Low := 1;
    High := 100;
    Found := FALSE;
    Index := -1;
END_IF;

// Perform binary search
WHILE Low <= High DO
    Mid := (Low + High) / 2;

    // Check if target is found
    IF SearchArray[Mid] = TargetValue THEN
        Found := TRUE;
        Index := Mid;
        RETURN;
    END_IF;

    // Check if target is greater than current value
    IF SearchArray[Mid] < TargetValue THEN
        Low := Mid + 1;
    ELSE
        High := Mid - 1;
    END_IF;
END_WHILE;

// If search fails, return error
IF NOT Found THEN
    Error := TRUE;
    Index := -1;
END_IF;
END_FUNCTION_BLOCK

// Sample usage:
//   Enable := TRUE;
//   TargetValue := 50;
//   SearchArray[1..10] := [10,

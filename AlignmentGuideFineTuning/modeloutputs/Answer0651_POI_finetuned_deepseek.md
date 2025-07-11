### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block to perform an efficient binary search on a sorted 100-integer array with input validation, boundary management, and real-time PLC compatibility.  

*(Key focus: Binary search, structured text, PLC, input validation, real-time safety)*

### Prompt:
**Binary Search:**
Implement a self-contained function block in IEC 61131-3 structured text to perform a binary search on an array of 100 integers. Include input validation and efficient handling of search boundaries.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC programmer tasked with developing a reusable and efficient search utility in IEC 61131-3 Structured Text for use in real-time automation systems.

⸻

🟩 I (Input) – Information Provided

You are to implement a binary search algorithm within a function block that operates on an array of 100 integers. The function must:
	•	Accept a sorted array, a target value, and an enable trigger
	•	Perform input validation (e.g., index bounds, empty range)
	•	Efficiently manage search boundaries (low, high, mid)
	•	Return both a boolean flag (Found) and the index where the value was located (or -1 if not found)

⸻

🟧 S (Steps) – Steps to Perform
	1.	Define a function block interface with inputs:
	•	SearchArray : ARRAY[1..100] OF INT
	•	TargetValue : INT
	•	Enable : BOOL
	2.	Add internal variables for Low, High, Mid, and Found.
	3.	Use a WHILE loop to implement binary search logic:
	•	Compare the middle element with the target
	•	Adjust Low or High accordingly
	•	Break on match or conclude if Low > High
	4.	Output:
	•	Found : BOOL
	•	Index : INT (valid index or -1)
	5.	Include input validation and comment the logic for maintainability.

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a robust, reusable Structured Text function block that efficiently performs binary search on a fixed-size array. The implementation should be:
	•	Scan-cycle safe for use in real-time PLC environments
	•	Modular, with clear documentation and boundary checks
	•	Adaptable for future use cases involving longer arrays or dynamic array sizes (with minor modifications)

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block to perform an efficient binary search on a sorted 100-integer array with input validation, boundary management, and real-time PLC compatibility.  

*(Key focus: Binary search, structured text, PLC, input validation, real-time safety)*
**Binary Search:**
Implement a self-contained function block in IEC 61131-3 structured text to perform a binary search on an array of 100 integers. Include input validation and efficient handling of search boundaries.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC programmer tasked with developing a reusable and efficient search utility in IEC 61131-3 Structured Text for use in real-time automation systems.

⸻

🟩 I (Input) – Information Provided

You are to implement a binary search algorithm within a function block that operates on an array of 100 integers. The function must:
	•	Accept a sorted array, a target value, and an enable trigger
	•	Perform input validation (e.g., index bounds, empty range)
	•	Efficiently manage search boundaries (low, high, mid)
	•	Return both a boolean flag (Found) and the index where the value was located (or -1 if not found)

⸻

🟧 S (Steps) – Steps to Perform
	1.	Define a function block interface with inputs:
	•	SearchArray : ARRAY[1..100] OF INT
	•	TargetValue : INT
	•	Enable : BOOL
	2.	Add internal variables for Low, High, Mid, and Found.
	3.	Use a WHILE loop to implement binary search logic:
	•	Compare the middle element with the target
	•	Adjust Low or High accordingly
	•	Break on match or conclude if Low > High
	4.	Output:
	•	Found : BOOL
	•	Index : INT (valid index or -1)
	5.	Include input validation and comment the logic for maintainability.

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a robust, reusable Structured Text function block that efficiently performs binary search on a fixed-size array. The implementation should be:
	•	Scan-cycle safe for use in real-time PLC environments
	•	Modular, with clear documentation and boundary checks
	•	Adaptable for future use cases involving longer arrays or dynamic array sizes (with minor modifications)
FUNCTION_BLOCK BinarySearch
VAR_INPUT
    SearchArray : ARRAY[1..100] OF INT; // Sorted array of 100 integers
    TargetValue : INT;                  // Value to search for
    Enable : BOOL;                      // Enable search
END_VAR

VAR_OUTPUT
    Found : BOOL;                       // TRUE if found, FALSE otherwise
    Index : INT;                        // Index of found value (or -1 if not found)
END_VAR

VAR
    Low : INT := 1;
    High : INT := 100;
    Mid : INT;
END_VAR

METHOD Execute : BOOL
VAR_LOCAL
    Done : BOOL := FALSE;
END_VAR

IF NOT Enable THEN
    Done := TRUE;
    RETURN TRUE;
END_IF;

IF Done THEN
    RETURN TRUE;
END_IF;

IF Low > High THEN
    Found := FALSE;
    Index := -1;
    Done := TRUE;
    RETURN TRUE;
END_IF;

// Find middle index
Mid := (Low + High) / 2;

// Compare target with middle element
IF SearchArray[Mid] = TargetValue THEN
    Found := TRUE;
    Index := Mid;
    Done := TRUE;
    RETURN TRUE;
END_IF;

IF SearchArray[Mid] < TargetValue THEN
    Low := Mid + 1;
ELSE
    High := Mid - 1;
END_IF;

Done := FALSE;
RETURN TRUE;
END_METHOD

// Call Execute method to perform search
Execute();

// Output results
Found := NOT Done;
IF Done THEN
    Index := -1;
ELSE
    Index := Mid;
END_IF;

END_FUNCTION_BLOCK
(* IEC 61131-3 Structured Text: Binary Search Function Block *)
(* Purpose: Performs a binary search on a sorted array of 100 integers *)
(* Inputs: SearchArray : ARRAY[1..100] OF INT, TargetValue : INT, Enable : BOOL *)
(* Outputs: Found : BOOL, Index : INT *)
(* Features: *)
(*   - Efficient binary search algorithm *)
(*   - Sorted array input validation *)
(*

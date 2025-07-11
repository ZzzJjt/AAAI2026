### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block to perform a binary search on a sorted array of 100 integers, ensuring input validation, efficient boundary handling, and clear outputs (found index or -1).  

*(Focus: Modular, real-time PLC lookup for industrial automation.)*

### Prompt:
**Binary Search:**
Implement a self-contained function block in IEC 61131-3 structured text to perform a binary search on an array of 100 integers. Include input validation and efficient handling of search boundaries.

**C-A-R-E:**

🟥 C (Context) – Background Situation

In industrial automation systems, it’s common to work with arrays of sensor readings, setpoints, or index values. Efficient data retrieval is essential, especially when scanning large arrays. A binary search algorithm is optimal for sorted integer arrays, offering logarithmic-time performance compared to linear search. Implementing such logic in IEC 61131-3 Structured Text allows for modular, real-time lookup operations on PLCs.

⸻

🟩 A (Action) – Task to Perform

Create a self-contained function block in Structured Text to perform a binary search on an array of 100 integers. Your implementation should:
	•	Take as input a sorted array, the target value, and an enable flag
	•	Use Low, High, and Mid pointers to narrow the search space
	•	Validate input conditions such as array bounds and search preconditions
	•	Handle edge cases like an empty range or out-of-bounds indices
	•	Output the index of the found value (or -1 if not found), and a boolean flag indicating success

⸻

🟨 R (Result) – Expected Outcome

The result should be a modular, reliable, and reusable binary search function block that runs efficiently on PLC hardware. It should minimize scan time for data lookups and be easily integrated into structured control applications that require high-speed decision-making or condition detection.

⸻

🟦 E (Example) – Concrete Illustration

Here’s an excerpt of what the Structured Text logic might look like:

IF Enable THEN
   Low := 1;
   High := 100;
   Found := FALSE;

   WHILE (Low <= High) AND NOT Found DO
      Mid := (Low + High) / 2;
      IF SearchArray[Mid] = TargetValue THEN
         Index := Mid;
         Found := TRUE;
      ELSIF SearchArray[Mid] > TargetValue THEN
         High := Mid - 1;
      ELSE
         Low := Mid + 1;
      END_IF;
   END_WHILE;

   IF NOT Found THEN
      Index := -1;
   END_IF;
END_IF;

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block to perform a binary search on a sorted array of 100 integers, ensuring input validation, efficient boundary handling, and clear outputs (found index or -1).  

*(Focus: Modular, real-time PLC lookup for industrial automation.)*
**Binary Search:**
Implement a self-contained function block in IEC 61131-3 structured text to perform a binary search on an array of 100 integers. Include input validation and efficient handling of search boundaries.

**C-A-R-E:**

🟥 C (Context) – Background Situation

In industrial automation systems, it’s common to work with arrays of sensor readings, setpoints, or index values. Efficient data retrieval is essential, especially when scanning large arrays. A binary search algorithm is optimal for sorted integer arrays, offering logarithmic-time performance compared to linear search. Implementing such logic in IEC 61131-3 Structured Text allows for modular, real-time lookup operations on PLCs.

⸻

🟩 A (Action) – Task to Perform

Create a self-contained function block in Structured Text to perform a binary search on an array of 100 integers. Your implementation should:
	•	Take as input a sorted array, the target value, and an enable flag
	•	Use Low, High, and Mid pointers to narrow the search space
	•	Validate input conditions such as array bounds and search preconditions
	•	Handle edge cases like an empty range or out-of-bounds indices
	•	Output the index of the found value (or -1 if not found), and a boolean flag indicating success

⸻

🟨 R (Result) – Expected Outcome

The result should be a modular, reliable, and reusable binary search function block that runs efficiently on PLC hardware. It should minimize scan time for data lookups and be easily integrated into structured control applications that require high-speed decision-making or condition detection.

⸻

🟦 E (Example) – Concrete Illustration

Here’s an excerpt of what the Structured Text logic might look like:

IF Enable THEN
   Low := 1;
   High := 100;
   Found := FALSE;

   WHILE (Low <= High) AND NOT Found DO
      Mid := (Low + High) / 2;
      IF SearchArray[Mid] = TargetValue THEN
         Index := Mid;
         Found := TRUE;
      ELSIF SearchArray[Mid] > TargetValue THEN
         High := Mid - 1;
      ELSE
         Low := Mid + 1;
      END_IF;
   END_WHILE;

   IF NOT Found THEN
      Index := -1;
   END_IF;
END_IF;
FUNCTION_BLOCK BinarySearch
VAR_INPUT
    Enable : BOOL; // Enable the search
    SearchArray : ARRAY[1..100] OF INT; // Sorted array of integers
    TargetValue : INT; // Value to search for
END_VAR

VAR_OUTPUT
    Index : INT; // Index of the found value or -1 if not found
    Found : BOOL; // TRUE if the value was found
END_VAR

VAR
    Low : INT; // Lower search boundary
    High : INT; // Upper search boundary
    Mid : INT; // Middle search index
    Found : BOOL; // Flag indicating whether the value was found
END_VAR

METHOD Execute : BOOL
BEGIN
    // Validate inputs
    IF NOT Enable OR NOT SearchArray[1..100] THEN
        Index := -1;
        Found := FALSE;
        RETURN FALSE;
    END_IF;

    // Initialize search variables
    Low := 1;
    High := 100;
    Found := FALSE;

    // Perform binary search
    WHILE (Low <= High) AND NOT Found DO
        Mid := (Low + High) / 2;
        IF SearchArray[Mid] = TargetValue THEN
            Index := Mid;
            Found := TRUE;
        ELSIF SearchArray[Mid] > TargetValue THEN
            High := Mid - 1;
        ELSE
            Low := Mid + 1;
        END_IF;
    END_WHILE;

    // Return results
    IF NOT Found THEN
        Index := -1;
    END_IF;

    RETURN TRUE;
END_METHOD
END_FUNCTION_BLOCK
# IEC 61131-3 Structured Text: Binary Search Function Block
# Purpose: Performs a binary search on a sorted array of 100 integers
#          Returns the index of the target value or -1 if not found

FUNCTION_BLOCK BinarySearch
VAR_INPUT
    Enable : BOOL; // TRUE to enable the search
    SearchArray : ARRAY[1..100] OF INT; // Sorted array of integers
    TargetValue : INT; // Value to search for
END_VAR

VAR_OUTPUT
    Index : INT; // Index of the found value or -1

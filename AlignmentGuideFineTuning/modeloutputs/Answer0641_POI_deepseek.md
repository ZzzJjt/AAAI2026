### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block to perform a precise floating-point comparison (with configurable decimal precision) for real-time PLC applications, including input validation and clear output flags.

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
Create a reusable IEC 61131-3 Structured Text function block to perform a precise floating-point comparison (with configurable decimal precision) for real-time PLC applications, including input validation and clear output flags.
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

⸻

🟨 I (Implementation) – Implement the Function Block

1.	Define a function block interface with inputs:
```
FUNCTION_BLOCK BinarySearch
VAR_INPUT
    SearchArray : ARRAY[1..100] OF INT
    TargetValue : INT
    Enable : BOOL
END_VAR
VAR_OUTPUT
    Found : BOOL
    Index : INT
END_VAR
```
2.	Add internal variables for Low, High, Mid, and Found.
```
VAR_INTERNAL
    Low : INT;
    High : INT;
    Mid : INT;
    Found : BOOL;
END_VAR
```
3.	Use a WHILE loop to implement binary search logic:
```
WHILE NOT Found AND (Low <= High) DO
    Mid := (Low + High) / 2;
    IF SearchArray(Mid) = TargetValue THEN
        Found := TRUE;
        Index := Mid;
    ELSE IF SearchArray(Mid) < TargetValue THEN
        Low := Mid + 1;
    ELSE
        High := Mid - 1;
    END_IF
ENDWHILE
```
4.	Output:
```
Found : BOOL;
Index : INT (valid index or -1);
```
5.	Include input validation and comment the logic for maintainability.
```
// Input validation
IF Low > 100 OR High < 1 OR SearchArray(Low) > SearchArray(High) THEN
    Found := FALSE;
    Index := -1;
    OUTPUT("Invalid input range. Please check the array bounds and target value.");
END_IF
```
🟩 I (Information) – Information Provided

The function block is now ready for use in real-time PLC applications. It can efficiently perform binary search on a fixed-size array, with input validation and clear output flags. The function block can be easily adapted for use with larger arrays or dynamic array sizes by adjusting the input parameters.

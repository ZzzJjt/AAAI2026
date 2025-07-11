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
FUNCTION_BLOCK FloatingPointCompare
VAR_INPUT
    Value1 : REAL; // First floating-point value to compare
    Value2 : REAL; // Second floating-point value to compare
    Precision : INT := 4; // Number of decimal places to compare
END_VAR

VAR_OUTPUT
    Equal : BOOL; // TRUE if values are equal within the specified precision
    Greater : BOOL; // TRUE if Value1 > Value2 within the specified precision
    Less : BOOL; // TRUE if Value1 < Value2 within the specified precision
END_VAR

VAR
    Diff : REAL; // Difference between the two values
    Power : INT; // Exponent for scaling
    ScaledDiff : REAL; // Scaled difference for comparison
END_VAR

// Initialize outputs to FALSE
Equal := FALSE;
Greater := FALSE;
Less := FALSE;

// Validate inputs
IF Precision < 0 OR Precision > 10 THEN
    Equal := FALSE;
    Greater := FALSE;
    Less := FALSE;
    RETURN;
END_IF;

// Normalize inputs to the same scale
Power := CEIL(LOG10(ABS(Value1)) + LOG10(ABS(Value2)));
Value1 := Value1 * 10.0**Power;
Value2 := Value2 * 10.0**Power;

// Compute the difference
Diff := Value1 - Value2;

// Scale the difference to the specified precision
ScaledDiff := Diff * 10.0**(-Precision);

// Compare the scaled difference
IF ABS(ScaledDiff) < 0.0001 THEN
    Equal := TRUE;
    Greater := FALSE;
    Less := FALSE;
ELSIF ScaledDiff > 0.0001 THEN
    Greater := TRUE;
    Less := FALSE;
ELSE
    Less := TRUE;
    Greater := FALSE;
END_IF;

// Reset outputs if the inputs change
IF (Value1 <> OldValue1 OR Value2 <> OldValue2) THEN
    Equal := FALSE;
    Greater := FALSE;
    Less := FALSE

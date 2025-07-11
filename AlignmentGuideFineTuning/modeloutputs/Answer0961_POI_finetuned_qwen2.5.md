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

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC programmer or automation engineer responsible for implementing efficient search algorithms in IEC 61131-3 Structured Text for use in industrial control systems.

⸻

🟩 I (Input) – What You’re Given

You are tasked with implementing a binary search algorithm to find a target value in a sorted array of 100 integers. The input includes:
	•	An array of 100 integers (SearchArray)
	•	A target value to search for (TargetValue)
	•	A boolean flag to enable the search process (Enable)
	•	You need to ensure that the implementation is scan-cycle-safe, efficient, and includes proper input validation.

⸻

🟧 S (Steps) – How to Do It

	1.	Define a self-contained function block named BinarySearch that accepts the required inputs:
	•	SearchArray : ARRAY[1..100] OF INT
	•	TargetValue : INT
	•	Enable : BOOL
	2.	Implement the binary search algorithm using a WHILE loop or equivalent, ensuring efficient narrowing of the search window:
	•	Define internal variables for Low, High, Mid, and status flags.
	•	Perform input validation to ensure that the search boundaries are within the valid range of the array.
	•	Implement the binary search logic, adjusting the search window based on comparisons between the target value and the middle element of the current window.
	•	Track the status of the search (found/not found) and provide an output flag to indicate the result.
	3.	Add comments to explain the logic of the binary search algorithm, including the steps involved in narrowing the search window and the conditions for continuing or stopping the search.
	4.	Ensure that the function block is scan-cycle-safe and efficient, with comments explaining the scan-cycle-safe implementation of the search algorithm.

⸻

🟦 E (Example) – What It Should Look Like

	•	Implement a self-contained function block named BinarySearch that:
	•	Accepts an array of 100 integers and a target value to search for.
	•	Includes input validation to ensure the search boundaries are within the valid range of the array.
	•	Uses a binary search algorithm to efficiently locate the target value within the array.
	•	Outputs the index of the target value if found, or a flag indicating that the

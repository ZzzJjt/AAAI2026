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

	Ensure the function block is well-documented and includes comments explaining the search process, edge cases, and limitations.

**C-A-R-E:**

⸻

⸻

🟥 C (Context) – Background Situation

In industrial automation, efficient search algorithms are essential for processing sensor data, managing inventory, or optimizing control logic. However, many PLC environments lack built-in search utilities, and implementing such functionality requires a structured, scan-cycle-safe approach using IEC 61131-3 Structured Text.

⸻

🟩 A (Action) – Task to Perform

Develop a self-contained function block in IEC 61131-3 Structured Text that performs a binary search on a fixed-size array of 100 integers. Ensure the function block:
	•	Accepts a sorted array, a target value, and an enable trigger
	•	Includes input validation to handle edge cases (e.g., empty range, index bounds)
	•	Uses efficient binary search logic with clear comments
	•	Returns both a boolean flag indicating whether the value was found and the index of the value
	•	Is designed for scan-cycle-safe execution in real-time PLC environments
	•	Includes detailed comments explaining the algorithm, search boundaries, and limitations

⸻

🟧 R (Result) – Desired Outcome

The result should be a reusable function block that:
	•	Works efficiently within the constraints of IEC 61131-3 Structured Text
	•	Is scan-cycle-safe and suitable for use in real-time PLC applications
	•	Includes input validation and clear comments for maintainability
	•	Performs binary search on a fixed-size array of 100 integers
	•	Returns both a boolean and an index, with appropriate handling for not-found cases
	•	Is designed to be extended or adapted for use with larger arrays or dynamic data structures

⸻

⸻
**Binary Search:**
Implement a self-contained function block in IEC 61131-3 structured text to perform a binary search on an array of 100 integers. Include input validation and efficient handling of search boundaries.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC programmer tasked with developing a reusable and efficient search utility in IEC 61131-3 Structured Text for use in real-time automation systems.

⸻

🟩

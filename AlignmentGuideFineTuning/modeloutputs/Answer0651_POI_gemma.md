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

**Submission Format:**
Submit a single .st file containing the function block implementation.

**Evaluation Criteria:**
The evaluation will be based on the following criteria:
	•	Correctness: The function block should correctly perform a binary search on a sorted array of 100 integers.
	•	Efficiency: The function block should be efficient in terms of scan time and memory usage.
	•	Input Validation: The function block should perform input validation to ensure that the input array is sorted and that the target value is within the range of the array.
	•	Real-Time Safety: The function block should be scan-cycle safe for use in real-time PLC environments.
	•	Modularity: The function block should be modular, with clear documentation and boundary checks.
	•	Adaptability: The function block should be adaptable for future use cases involving longer arrays or dynamic array sizes (with minor modifications).

**Resources:**
	•	IEC 61131-3 Standard: https://www.iec.ch/standards/iec61131-3
	•	Binary Search Algorithm: https://en.wikipedia.org/wiki/Binary_search_algorithm
	•	Structured Text Programming: https://www.plctalk.net/downloads/Structured_Text_Programming.pdf
	•	Real-Time PLC Programming: https://www.plctalk.net/downloads/Real-Time_PLC_Programming.pdf
	•	Input Validation: https://www.plctalk.net/downloads/Input_Validation.pdf
	•	Boundary Management: https://www.plctalk.net/downloads/Boundary_Management.pdf
	•	Real-Time Safety: https://www.plctalk.net/downloads/Real-Time_Safety.pdf
	•	Modularity: https://www.plctalk.net/downloads/Modularity.pdf
	•	Adaptability: https://www.plctalk.net/downloads/Adaptability.pdf

**Submission Deadline:**
The submission deadline is 11:59 PM on 12/31/2022.

**Submission Instructions:**
Submit your solution as a single .st file to the submission link provided.

**Evaluation Process:**
The evaluation process will be conducted by a panel of experts in the field of PLC programming. The panel will

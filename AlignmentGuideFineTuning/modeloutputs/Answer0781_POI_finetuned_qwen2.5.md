### Intent:
**Intent Summary:**  
Create an IEC 61131-3 structured text function block to efficiently perform a binary search on a sorted array of 100 integers, with input validation, boundary handling, and clear outputs (index/status), optimized for real-time PLC execution.

### Prompt:
**Binary Search:**
Implement a self-contained function block in IEC 61131-3 structured text to perform a binary search on an array of 100 integers. Include input validation and efficient handling of search boundaries.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC developer implementing optimized algorithms in IEC 61131-3 Structured Text for industrial automation systems.

⸻

🟩 T (Task) – Define the Objective

Develop a self-contained function block in Structured Text that performs a binary search on an array of 100 sorted integers. The function block should:
	•	Accept a target value and an enable flag as inputs
	•	Include input validation, such as checking that the array is within bounds
	•	Use efficient logic with search boundaries (Low, High, Mid)
	•	Output the index of the found value, or -1 if not found, along with a Found boolean
	•	Be designed for modularity, clarity, and real-time PLC execution

⸻

🟧 F (Format) – Specify the Output Format

Provide:
	•	A fully structured IEC 61131-3 function block declaration
	•	Input and output variable definitions
	•	Main logic using WHILE or REPEAT loops
	•	Handling of edge cases (e.g., value not found, invalid index range)
	•	Inline comments explaining the binary search logic and decisions
	•	Optional notes on performance in scan-cycle-sensitive systems

### Generated Code:
**Intent Summary:**  
Create an IEC 61131-3 structured text function block to efficiently perform a binary search on a sorted array of 100 integers, with input validation, boundary handling, and clear outputs (index/status), optimized for real-time PLC execution.
**Binary Search:**
Implement a self-contained function block in IEC 61131-3 structured text to perform a binary search on an array of 100 integers. Include input validation and efficient handling of search boundaries.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC developer implementing optimized algorithms in IEC 61131-3 Structured Text for industrial automation systems.

⸻

🟩 T (Task) – Define the Objective

Develop a self-contained function block in Structured Text that performs a binary search on an array of 100 sorted integers. The function block should:
	•	Accept a target value and an enable flag as inputs
	•	Include input validation, such as checking that the array is within bounds
	•	Use efficient logic with search boundaries (Low, High, Mid)
	•	Output the index of the found value, or -1 if not found, along with a Found boolean
	•	Be designed for modularity, clarity, and real-time PLC execution

⸻

🟧 F (Format) – Specify the Output Format

Provide:
	•	A fully structured IEC 61131-3 function block declaration
	•	Input and output variable definitions
	•	Main logic using WHILE or REPEAT loops
	•	Handling of edge cases (e.g., value not found, invalid index range)
	•	Inline comments explaining the binary search logic and decisions
	•	Optional notes on performance in scan-cycle-sensitive systems

⸻

**C-A-R-E:**

🟥 C (Context) – Background Situation

In industrial automation, efficient search algorithms like binary search are essential for quickly locating data within arrays, especially when scanning large amounts of sensor or control data. However, implementing such algorithms in IEC 61131-3 Structured Text requires careful attention to scan-cycle efficiency, memory usage, and real-time constraints.

⸻

🟩 A (Action) – Task Steps

	1.	Define the function block with inputs:
	•	Enable: BOOL — triggers the search process
	•	TargetValue: INT — the value to be found
	•	SearchArray: ARRAY[1..100] OF INT — the array to be searched
	•	Found: BOOL — output to indicate whether the value was found
	•	FoundValue: INT — output to store the index of the found value or -1 if not found
	2.	Implement input validation:
	•	Ensure the searchArray is within the specified bounds (1..100)
	•	Reject invalid inputs to prevent runtime errors
	3.	Perform the binary search:
	•	Use a WHILE loop to iteratively halve the search range
	•	Track the Low and High indices of the current search range
	•	Compute the Mid index and compare the target value with the array element at Mid
	•	Adjust the search range based on the comparison result
	4.	Handle search boundaries:
	•	Stop the search if the Low index exceeds the High index
	•	Output the index of the found value or -1 if the value is not present
	5.	Optimize for scan-cycle performance:
	•	Avoid unnecessary calculations and loops
	•	Minimize memory usage by using only the required variables
	6.	Add comments to explain the logic and control flow:
	•	Describe the binary search process
	•	Explain the role of each variable and the conditions for index updates
	•	Note any potential limitations or edge cases, such as handling large arrays or search failures

⸻

🟧 R (Result) – Expected Outcome

The function block will:
	•	Accept a target value and an enable flag
	•	Perform a binary search on a 100-element array
	•	Output the index of the found value or -1 if not found
	•	Be designed for scan

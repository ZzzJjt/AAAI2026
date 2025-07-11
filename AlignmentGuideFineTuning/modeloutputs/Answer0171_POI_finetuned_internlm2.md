### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 function block in Structured Text to compare two REAL values with configurable decimal precision, handling floating-point inaccuracies and input validation for reliable industrial automation logic.  

*(Key focus: Precision-based comparison, input safety, and PLC compatibility.)*

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
Create a reusable IEC 61131-3 function block in Structured Text to compare two REAL values with configurable decimal precision, handling floating-point inaccuracies and input validation for reliable industrial automation logic.  

*(Key focus: Precision-based comparison, input safety, and PLC compatibility.)*
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
	5.	Comment each section for clarity and maintainability. Ensure the function block is self-contained and can be reused in PLC code.

**C (Circumstances):**  
Develop a self-contained function block in IEC 61131-3 Structured Text to perform a binary search on a 100-element integer array. The function should efficiently locate a target value using binary search logic, include input validation (e.g., bounds check, sorted array assumption), handle search boundaries accurately to avoid indexing errors or infinite loops, and be modular and reusable in PLC programs where fast data lookup is essential.

**R (Rationale):**  
Binary search is a highly efficient algorithm for finding a target value in a sorted array. It halves the search space with each iteration, making it ideal for large datasets. In industrial control systems, fast data lookup is crucial for real-time processing and decision-making. Implementing a self-contained function block in IEC 61131-3 Structured Text ensures that the binary search logic is encapsulated, reusable, and easily integrated into PLC code. By including input validation and efficient handling of search boundaries, the function block can be used reliably in industrial automation applications.

**S (Solution):**  
Develop a self-contained function block in IEC 61131-3 Structured Text to perform a binary search on a 100-element integer array. The function should efficiently locate a target value using binary search logic, include input validation (e.g., bounds check, sorted array assumption), handle search boundaries accurately to avoid indexing errors or infinite loops, and be modular and reusable in PLC programs where fast data lookup is essential.

**A (Action):**  
Implement a binary search function block in IEC 61131-3 Structured Text with the following inputs and outputs:

Inputs:
	•	SearchArray (ARRAY[1..100] OF INT): The sorted array to search.
	•	TargetValue (INT): The value to find in the array.
	•	Enable (BOOL): A flag to start the search.

Outputs:
	•	Found (BOOL): Indicates whether the target value was found in the array.
	•	Index (INT): The index of the target value in the array (if found) or -1 (if not found).

Implement the binary search algorithm using a WHILE loop, ensuring that the search is performed efficiently and accurately. Include input validation to ensure that the array is sorted and the target value is within the array bounds. Document the function block with comments to explain

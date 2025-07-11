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
	5.	Comment each section for clarity and maintainability. Ensure efficient use of PLC memory and processing power.

⸻

Use this structured text function block in your PLC programs to perform fast, reliable, and efficient searches on integer arrays, improving response times and system performance in automation tasks.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Create a self-contained function block in IEC 61131-3 Structured Text to implement a binary search algorithm on a 100-integer array. Ensure the function block is modular, efficient, and includes input validation.

⸻

🟩 A (Action) – How to Do It

	•	Define the function block inputs:
	•	SearchArray : ARRAY[1..100] OF INT
	•	TargetValue : INT
	•	Enable : BOOL
	•	Define outputs:
	•	Found : BOOL
	•	Index : INT
	•	Implement the binary search algorithm using a WHILE loop:
	•	Assign Low := 1 and High := 100
	•	Perform the search while Low ≤ High
	•	Compute Mid := (Low + High) DIV 2
	•	Compare SearchArray[Mid] with TargetValue
	•	Adjust Low and High based on the comparison
	•	When the loop exits, check if the value was found
	•	Add input validation to ensure the array is sorted and within bounds
	•	Implement efficient handling of search boundaries to prevent infinite loops
	•	Include comments explaining the logic and steps

⸻

🟧 G (Goal) – What You’re Aiming For

	•	A self-contained function block that performs a binary search on a 100-integer array
	•	Includes input validation and efficient handling of search boundaries
	•	Works within the constraints of IEC 61131-3 Structured Text
	•	Is reusable and modular for use in PLC programs
	•	Improves search performance and system responsiveness in industrial automation

	•	Implement a self-contained function block in IEC 61131-3 Structured Text to perform a binary search on a 100-integer array, ensuring efficient and reliable search operations in PLC-based systems.

	•	Implement a self-contained function block in IEC 61131-3 Structured Text to perform a binary search on a 100-integer

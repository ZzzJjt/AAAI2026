### Intent:
**Intent Summary:**  
Create an IEC 61131-3 structured text function block to perform precise floating-point comparisons (REAL types) up to a user-defined decimal precision, including error handling and output flags for equality, greater-than, and less-than conditions.

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
Create an IEC 61131-3 structured text function block to perform precise floating-point comparisons (REAL types) up to a user-defined decimal precision, including error handling and output flags for equality, greater-than, and less-than conditions.
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
	5.	Comment each section for clarity and maintainability. Ensure the function block is self-contained and can be reused in other PLC programs.

**C (Circumstance):**  
Develop a self-contained function block in IEC 61131-3 Structured Text to perform a binary search on a 100-element integer array. The function should efficiently locate a target value using binary search logic, include input validation (e.g., bounds check, sorted array assumption), handle search boundaries accurately to avoid indexing errors or infinite loops, and be modular and reusable in PLC programs where fast data lookup is essential.

**R (Role):**  
Develop a self-contained function block in IEC 61131-3 Structured Text to perform a binary search on a 100-element integer array. The function should efficiently locate a target value using binary search logic, include input validation (e.g., bounds check, sorted array assumption), handle search boundaries accurately to avoid indexing errors or infinite loops, and be modular and reusable in PLC programs where fast data lookup is essential.

**A (Action):**  
Develop a self-contained function block in IEC 61131-3 Structured Text to perform a binary search on a 100-element integer array. The function should efficiently locate a target value using binary search logic, include input validation (e.g., bounds check, sorted array assumption), handle search boundaries accurately to avoid indexing errors or infinite loops, and be modular and reusable in PLC programs where fast data lookup is essential.

**P (Product):**  
Develop a self-contained function block in IEC 61131-3 Structured Text to perform a binary search on a 100-element integer array. The function should efficiently locate a target value using binary search logic, include input validation (e.g., bounds check, sorted array assumption), handle search boundaries accurately to avoid indexing errors or infinite loops, and be modular and reusable in PLC programs where fast data lookup is essential.

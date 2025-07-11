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
	5.	Comment each section for clarity and maintainability. Ensure the code is structured for easy integration into larger PLC programs.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In industrial automation, comparing two REAL values for equality or inequality is a common task. However, due to the nature of floating-point arithmetic, direct comparison can lead to unexpected results due to precision issues. This can cause logic errors in control systems, leading to safety hazards or production inefficiencies.

⸻

🟩 A (After) – The Desired Outcome

Create a self-contained function block in IEC 61131-3 Structured Text that compares two REAL values with configurable decimal precision. The function should:
	•	Allow the user to specify the number of decimal places for comparison
	•	Handle floating-point inaccuracies by rounding values to the specified precision
	•	Include input validation to ensure the values are REAL and the precision is a non-negative integer
	•	Provide outputs for comparison results (EQUAL, NOT_EQUAL, GREATER_THAN, LESS_THAN)
	•	Be reusable in PLC programs for precise control logic

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block interface with inputs for:
	•	Value1 : REAL
	•	Value2 : REAL
	•	DecimalPrecision : INT (non-negative)
	2.	Implement a rounding function to round both values to the specified decimal precision.
	3.	Compare the rounded values using standard comparison operators.
	4.	Include input validation to ensure the values are REAL and the precision is a non-negative integer.
	5.	Provide outputs for comparison results (EQUAL, NOT_EQUAL, GREATER_THAN, LESS_THAN).
	6.	Comment each section for clarity and maintainability. Ensure the code is structured for easy integration into larger PLC programs.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In industrial automation, it's crucial to handle input validation to prevent logic errors and ensure the safety and reliability of control systems. When comparing two REAL values, direct comparison can lead to unexpected results due to floating-point inaccuracies. This can cause logic errors in control systems, leading to safety hazards or production inefficiencies.

⸻

🟩 A (After) – The Desired Outcome

Create a self-contained function block in IEC 61131-3 Structured Text that compares two REAL values with configurable decimal precision. The function should:
	•	Allow the

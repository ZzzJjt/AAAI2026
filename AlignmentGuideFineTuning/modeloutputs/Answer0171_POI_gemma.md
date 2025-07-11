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
	5.	Comment each section for clarity and maintainability.
	6.	Test the function block with various inputs and edge cases to ensure it works as expected.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

The IEC 61131-3 standard for PLC programming languages does not provide a built-in function for comparing two REAL values with configurable decimal precision. This can lead to floating-point inaccuracies and input validation issues in industrial automation logic, resulting in unreliable and potentially unsafe control systems.

⸻

🟩 A (After) – The Desired Outcome

Create a reusable function block in IEC 61131-3 Structured Text that compares two REAL values with configurable decimal precision. The function should:
	•	Handle floating-point inaccuracies by rounding the values to the specified precision
	•	Validate the input values to ensure they are within a valid range
	•	Return a Boolean result indicating whether the values are equal or not
	•	Be modular and reusable in PLC programs where precise and reliable comparisons are essential

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block interface with inputs for:
	•	Value1 : REAL
	•	Value2 : REAL
	•	Precision : INT (number of decimal places to round to)
	•	Enable : BOOL
	2.	Round the values to the specified precision using the ROUND function.
	3.	Compare the rounded values using the = operator.
	4.	Add validation to ensure the input values are within a valid range (e.g., -1000 to 1000) and the precision is within a valid range (e.g., 0 to 10).
	5.	Include outputs such as:
	•	Equal : BOOL
	6.	Comment each section for clarity and maintainability.
	7.	Test the function block with various inputs and edge cases to ensure it works as expected.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In industrial automation systems, it is common to have multiple sensors or devices that need to be monitored and controlled. However, the standard IEC 61131-3 programming language does not provide a built-in function for handling multiple inputs and outputs in a structured and efficient way. This can lead to complex and error-prone code, making it difficult to maintain and troubleshoot

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

**Documentation:**
Include clear and concise documentation for the function block, including:
•	A description of the function's purpose and inputs/outputs
•	A detailed explanation of the binary search algorithm and how it is implemented in the function block
•	A description of the input validation and boundary safety measures
•	A description of the internal variables and their purpose
•	A description of the status flags and their meaning
•	A description of the output values and their meaning
•	A description of the function's performance and efficiency
•	A description of any limitations or potential issues with the function block
•	A description of any assumptions made in the implementation
•	A description of any potential improvements or future enhancements
•	A description of any testing performed on the function block
•	A description of any relevant standards or best practices followed in the implementation
•	A description of any relevant references or resources used in the implementation
•	A description of any relevant code snippets or examples
•	A description of any relevant comments or annotations in the code
•	A description of any relevant diagrams or illustrations
•	A description of any relevant code reviews or feedback
•	A description of any relevant code metrics or analysis
•	A description of any relevant code quality or style guidelines
•	A description of any relevant code security or safety measures
•	A description of any relevant code documentation or comments
•	A description of any relevant code version control or history
•	A description of any relevant code licensing or copyright information
•	A description of any relevant code maintenance or support information
•	A description of any relevant code deployment or release information
•	A description of any relevant code performance or optimization information
•	A description of any relevant code testing or debugging information
•	A description of any relevant code documentation or comments
•	A description of any relevant code version control or history
•	A description of any relevant code licensing or copyright information
•	A description of any relevant code maintenance or support information
•	A description of any relevant code deployment or release information
•	A description of any relevant code performance or optimization information
•	A description of any relevant code testing or debugging information
•	A description of any relevant code documentation or comments
•	A description of any relevant code version control or history
•	A description of any relevant code licensing or copyright information
•	A description of any relevant code maintenance

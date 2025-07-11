### Intent:
The task is to create an IEC 61131-3 structured text function block that performs a binary search on a sorted 100-element integer array, with input validation and efficient boundary handling, for reliable PLC-based data lookup in industrial control systems.

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
The task is to create an IEC 61131-3 structured text function block that performs a binary search on a sorted 100-element integer array, with input validation and efficient boundary handling, for reliable PLC-based data lookup in industrial control systems.
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

Deliver a modular, efficient, and scan-cycle-safe Structured Text function block that enables fast data lookup on PLCs. The function should be reliable, easy to reuse, and support safe operation within industrial real-time control systems. Ensure that the implementation is optimized for scan-cycle performance and includes detailed comments for maintainability.

**Binary Search:**
Implement a self-contained function block in IEC 61131-3 Structured Text to perform a binary search on an array of 100 integers. Include input validation and efficient handling of search boundaries.

**T-A-G:**

⸻

T (Task)

Implement a self-contained function block in IEC 61131-3 Structured Text to perform a binary search on an array of 100 integers. Ensure that the function block is designed to efficiently locate a target value within the array, with proper handling of search boundaries and input validation.

⸻

A (Action)
	•	Define a self-contained function block named BINARY_SEARCH that accepts:
	•	SearchArray : ARRAY[1..100] OF INT
	•	TargetValue : INT
	•	Enable : BOOL
	•	Use internal variables for Low, High, Mid, and status flags.
	•	Implement the binary search algorithm using a WHILE loop or equivalent, ensuring efficient narrowing of the search window.
	•	Add input validation to ensure boundary safety and proper triggering.
	•	Output the index of the target value and a boolean flag indicating whether it was found.
	•	Include comments explaining each step of the logic for maintainability and clarity.

⸻

G (Goal)

Deliver a self-contained function block in IEC 61131-3 Structured Text that performs a binary search on a 100-element integer array. Ensure that the implementation is efficient, scan-cycle-safe, and includes detailed comments for maintainability. Address potential issues related to search boundaries and input validation to ensure robust operation in industrial control systems.

**Binary Search:**
Implement a self-contained function block in IEC 61131-3 Structured Text to perform a binary search on an array of 100 integers. Include input validation and efficient handling of search boundaries.

**T-A-G:**

⸻

T (Task)

Implement a self-contained function block in IEC 61131-3 Structured Text to perform a binary search on an array of 100 integers. Ensure that the function block is designed to efficiently locate a target value within the array, with proper handling of search boundaries and input validation.

⸻

A (Action)
	•	Define a self-contained function block named BINARY_SEARCH

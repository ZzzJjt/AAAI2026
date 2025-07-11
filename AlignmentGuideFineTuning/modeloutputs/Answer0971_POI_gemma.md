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

Deliver a modular, efficient, and scan-cycle-safe Structured Text function block that enables fast data lookup on PLCs. The function should be reliable, easy to reuse, and support safe operation within industrial real-time control systems.

**Input Validation:**
Validate the input array to ensure it is sorted and contains no duplicate values. This will prevent the function from returning incorrect results or causing unexpected behavior.

**Efficient Boundary Handling:**
Handle the search boundaries efficiently to avoid unnecessary calculations and improve performance. This can be achieved by using the midpoint of the search window as the starting point for the search, and adjusting the boundaries as needed based on the result of the comparison.

**Reliable PLC-based Data Lookup:**
Ensure that the function is reliable and safe to use in a PLC-based control system. This can be achieved by using proper input validation, efficient boundary handling, and scan-cycle-safe programming techniques.

**Maintainability and Clarity:**
Include comments explaining each step of the logic for maintainability and clarity. This will make it easier for other developers to understand and modify the code in the future.

**Modular and Reusable:**
Make the function block self-contained and modular, so it can be easily reused in other projects. This will save time and effort in the long run.

**Scan-Cycle-Safe:**
Ensure that the function is scan-cycle-safe, so it can be used in real-time control systems without causing timing issues or other problems. This can be achieved by using proper programming techniques and avoiding unnecessary calculations.

**Efficient Performance:**
Optimize the function for efficient performance, so it can be used in real-time control systems without causing performance issues. This can be achieved by using efficient algorithms and avoiding unnecessary calculations.

**Robust and Reliable:**
Ensure that the function is robust and reliable, so it can be used in real-time control systems without causing unexpected behavior or errors. This can be achieved by using proper input validation, efficient boundary handling, and scan-cycle-safe programming techniques.

**Easy to Use:**
Make the function easy to use, so it can be easily integrated into other projects and used by other developers. This can be achieved by using clear and concise input and output parameters, and by providing clear documentation and examples.

**Safe and Secure:**
Ensure that the function is safe and secure, so it can be used in real-time control systems without causing security issues or other problems. This can be achieved by using proper programming techniques and avoiding unnecessary calculations.

**Scalable and Flexible:**
Make the function scalable and flexible, so it can be easily adapted to different project requirements and used in a variety of control systems. This can be achieved by using modular and

### Intent:
The task is to create a fixed traffic light control system in IEC 61131-3 Structured Text that implements a state machine with timed transitions, pedestrian crossing support, emergency vehicle priority, and safe light sequencing while adhering to PLC programming standards.

### Prompt:
**Programming Reference:**
Compile a comprehensive list of all valid keywords used in the IEC 61131-3 Structured Text programming language, ensuring that it covers both standard control flow structures and data types. Include examples of usage for key functions where applicable.

**B-A-B:**

🟥 Before – The Current Situation

You are working with IEC 61131-3 Structured Text, a standard language used in industrial automation for programmable logic controllers (PLCs). Developers often struggle to find a single, consolidated reference that lists all valid keywords, especially for control flow, data types, and functions, along with practical usage examples.

⸻

🟩 After – The Desired Outcome

You will have a comprehensive, well-organized programming reference that includes:
	•	All reserved keywords and standard identifiers in IEC 61131-3 Structured Text
	•	Control structures such as IF, CASE, FOR, WHILE, etc.
	•	Data types including BOOL, INT, REAL, ARRAY, STRUCT, and more
	•	Standard functions and function blocks, like TON, CTU, ABS, SQRT, with example usages
	•	Brief code snippets to demonstrate how the most important constructs are used in practice

⸻

🟦 Bridge – What You Need to Do

Compile and present a structured reference document that includes:
	1.	A keyword category breakdown:
	•	Control flow (IF, ELSIF, END_IF, CASE, FOR, REPEAT, etc.)
	•	Data types (BOOL, INT, REAL, TIME, STRING, etc.)
	•	Operators (AND, OR, MOD, NOT, etc.)
	•	System constants (TRUE, FALSE, MAX, MIN, etc.)
	2.	A section on standard functions and function blocks with:
	•	Brief descriptions
	•	IEC 61131-3-compliant usage examples
	•	Notes on any vendor-specific behavior, if applicable
	3.	A downloadable or easily searchable format, such as:
	•	A table or checklist format for fast lookup
	•	Highlighted example blocks like:

 VAR
  x: INT := 5;
  y: INT := 10;
  result: BOOL;
END_VAR

IF x < y THEN
  result := TRUE;
END_IF;

### Generated Code:
The task is to create a fixed traffic light control system in IEC 61131-3 Structured Text that implements a state machine with timed transitions, pedestrian crossing support, emergency vehicle priority, and safe light sequencing while adhering to PLC programming standards.
**Programming Reference:**
Compile a comprehensive list of all valid keywords used in the IEC 61131-3 Structured Text programming language, ensuring that it covers both standard control flow structures and data types. Include examples of usage for key functions where applicable.

**B-A-B:**

🟥 Before – The Current Situation

You are working with IEC 61131-3 Structured Text, a standard language used in industrial automation for programmable logic controllers (PLCs). Developers often struggle to find a single, consolidated reference that lists all valid keywords, especially for control flow, data types, and functions, along with practical usage examples.

⸻

🟩 After – The Desired Outcome

You will have a comprehensive, well-organized programming reference that includes:
	•	All reserved keywords and standard identifiers in IEC 61131-3 Structured Text
	•	Control structures such as IF, CASE, FOR, WHILE, etc.
	•	Data types including BOOL, INT, REAL, ARRAY, STRUCT, and more
	•	Standard functions and function blocks, like TON, CTU, ABS, SQRT, with example usages
	•	Brief code snippets to demonstrate how the most important constructs are used in practice

⸻

🟦 Bridge – What You Need to Do

Compile and present a structured reference document that includes:
	1.	A keyword category breakdown:
	•	Control flow (IF, ELSIF, END_IF, CASE, FOR, REPEAT, etc.)
	•	Data types (BOOL, INT, REAL, TIME, STRING, etc.)
	•	Operators (AND, OR, MOD, NOT, etc.)
	•	System constants (TRUE, FALSE, MAX, MIN, etc.)
	2.	A section on standard functions and function blocks with:
	•	Brief descriptions
	•	IEC 61131-3-compliant usage examples
	•	Notes on any vendor-specific behavior, if applicable
	3.	A downloadable or easily searchable format, such as:
	•	A table or checklist format for fast lookup
	•	Highlighted example blocks like:

 VAR
  x: INT := 5;
  y: INT := 10;
  result: BOOL;
END_VAR

IF x < y THEN
  result := TRUE;
END_IF;

	•	A PDF or HTML file with hyperlinks to relevant sections
	4.	A brief introduction to the language and its use in industrial automation
	5.	A list of references and resources for further study

⸻

**B-A-B:**

🟥 Before – The Current Situation

You are working on a project to create a fixed traffic light control system in IEC 61131-3 Structured Text. The system should implement a state machine with timed transitions, pedestrian crossing support, emergency vehicle priority, and safe light sequencing.

⸻

🟩 After – The Desired Outcome

You will have a working traffic light control system that meets the following requirements:
	•	A state machine with timed transitions, including:
	•	A state for each traffic light color (red, yellow, green)
	•	A state for the pedestrian crossing light
	•	A state for the emergency vehicle priority light
	•	A state for the safe light sequencing
	•	A state for the system to be in the "off" state
	•	Timed transitions between states, with a configurable time for each transition
	•	Pedestrian crossing support, including:
	•	A state for the pedestrian crossing light to be on
	•	A state for the pedestrian crossing light to be off
	•	A state for the pedestrian crossing light to be flashing
	•	A state for the pedestrian crossing light to be in the "off" state
	•	Emergency vehicle priority, including:
	•	A state for the emergency vehicle priority light to be on
	•	A state for the emergency vehicle priority light to be off
	•	A state for the emergency vehicle priority light to be in the "off" state
	•	Safe light sequencing, including:
	•	A state for the safe light sequencing to be on
	•	A state for the safe light sequencing to be off
	•	A state for the safe light sequencing to be in the "off" state
	•	A state for the system to be in the "off" state
	•	Adherence to PLC programming standards, including:
	•	Use of structured text programming language
	•	Adherence to IEC 61131-3 standards
	•	Adherence to industry best practices for PLC programming

⸻

🟦 Bridge – What You Need to Do

Create a fixed

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

⸻

🟦 Bonus – Additional Considerations

	1.	Include a section on common programming practices and style guidelines for IEC 61131-3 Structured Text, such as:
	•	Naming conventions for variables, functions, and programs
	•	Indentation and spacing guidelines
	•	Comments and documentation best practices
	•	Error handling and exception management
	2.	Provide a brief explanation of the state machine concept and its relevance to the traffic light control system, as well as examples of how it can be implemented in Structured Text.
	3.	Offer a sample Structured Text program for a basic traffic light control system, demonstrating the use of timed transitions, pedestrian crossing support, emergency vehicle priority, and safe light sequencing.
	4.	Include a section on common pitfalls and common mistakes when programming in IEC 61131-3 Structured Text, along with solutions or workarounds.
	5.	Provide a list of resources for further learning, such as books, online tutorials, and forums.

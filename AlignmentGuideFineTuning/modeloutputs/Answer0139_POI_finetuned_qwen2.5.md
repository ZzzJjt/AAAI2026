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
END_IF;	4.	Include a brief introduction explaining the importance of a structured reference for IEC 61131-3 programmers, emphasizing how it can improve code readability, maintainability, and collaboration across projects.

Compile a detailed IEC 61131-3 Structured Text reference for industrial automation, ensuring it covers all key aspects of the language and includes practical usage examples.

**B-A-B:**

🟥 Before – The Current Situation

You are working with IEC 61131-3 Structured Text, a widely used programming language in industrial automation. However, many developers lack a comprehensive reference that includes all valid keywords, data types, control structures, and standard functions. This can lead to inefficient programming, errors, and difficulties in maintaining or troubleshooting code.

⸻

🟩 After – The Desired Outcome

You will have a detailed IEC 61131-3 Structured Text reference that:
	•	Includes all reserved keywords and standard identifiers
	•	Organizes them into logical categories such as control flow, data types, and functions
	•	Provides usage examples for key functions and control structures
	•	Helps developers quickly find the information they need to write, understand, and maintain industrial automation programs
	•	Is structured for easy reference, with clear headings, examples, and explanations

⸻

🟦 Bridge – What You Need to Do

Compile a structured IEC 61131-3 reference that:
	1.	Organizes keywords and identifiers into logical categories:
	•	Control structures (IF, CASE, FOR, WHILE, etc.)
	•	Standard data types (BOOL, INT, REAL, TIME, STRING, etc.)
	•	Mathematical and logical operators
	•	Control functions (TON, CTU, ABS, SIN, etc.)
	•	Communication and network functions
	2.	Includes usage examples for key functions:
	•	Control flow: IF-THEN-ELSE, CASE statement, FOR loop
	•	Mathematical: ABS, SIN, COS, TAN, etc.
	•	Control: TON (on-delay timer), CTU (on-delay timer up), etc.
	•	Communication: Read/write to IO, Modbus, Profinet, etc.
	3.	Ensures that the reference is:
	•	Accurate and up-to-date with the IEC 61131-3 standard

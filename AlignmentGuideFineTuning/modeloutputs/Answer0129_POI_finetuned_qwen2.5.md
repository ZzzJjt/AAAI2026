### Intent:
**Intent Summary:**  
Create a comprehensive reference document listing all IEC 61131-3 Structured Text keywords, control structures, data types, and functions with usage examples for PLC programming.  

*(Focused on code generation: structured, searchable, and example-driven documentation.)*

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
**Intent Summary:**  
Create a comprehensive reference document listing all IEC 61131-3 Structured Text keywords, control structures, data types, and functions with usage examples for PLC programming.  

*(Focused on code generation: structured, searchable, and example-driven documentation.)*
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
END_IF;	4.	Include a detailed explanation of the limitations of the IEC 61131-3 Structured Text language, particularly in terms of unsupported features or limitations in certain PLC vendors.

	5.	Lastly, compile a list of references for further reading, including links to official standards, documentation, and relevant code examples.

⸻

Use this structured format to create a one-stop reference for IEC 61131-3 Structured Text, ensuring that it is both comprehensive and accessible for developers working with PLCs.

**B-A-B:**

Before – The Current Situation

Developers working with IEC 61131-3 Structured Text often face difficulties in locating a single, consolidated reference that lists all valid keywords, control structures, data types, and standard functions. This makes it challenging to find the correct usage of a keyword or function, especially when working with PLCs that may have vendor-specific limitations or extensions.

After – The Desired Outcome

Create a comprehensive IEC 61131-3 Structured Text reference document that includes:
	•	A detailed list of all reserved keywords and standard identifiers
	•	Control structures such as IF, CASE, FOR, WHILE, etc.
	•	All data types, including BOOL, INT, REAL, TIME, STRING, ARRAY, and STRUCT
	•	Standard functions and function blocks, such as TON, CTU, ABS, SQRT, with usage examples
	•	A structured format for easy lookup, such as a table or a categorized list
	•	Explanations of limitations and vendor-specific behavior, if applicable
	•	A list of references for further reading, including links to official standards, documentation, and code examples.

Bridge – What You Need to Do

	1.	Compile a detailed list of all reserved keywords and standard identifiers in IEC 61131-3 Structured Text, including:
	•	Control flow structures (IF, CASE, FOR, WHILE, etc.)
	•	Standard data types (BOOL, INT, REAL, TIME, STRING, ARRAY, STRUCT, etc.)
	•	Mathematical and logical operators (AND, OR, NOT, +, -, *, /, etc.)
	•	Control functions (TON, CTU, ABS, SQRT, etc.)
	•	Communication functions (such as Modbus, Profinet, etc.)
	•	Timer and counter functions
	•	IO and diagnostic

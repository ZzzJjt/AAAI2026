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
END_IF;

// OR

VAR
  x: INT := 5;
  y: INT := 10;
  result: BOOL;
END_VAR

IF x < y THEN
  result := TRUE;
ELSE
  result := FALSE;
END_IF;

// This is a valid IF statement

### IEC 61131-3 Structured Text Reference

#### Keywords

| Keyword | Description |
| --- | --- |
| AND | Logical AND operator |
| OR | Logical OR operator |
| NOT | Logical NOT operator |
| IF | Conditional control flow |
| ELSIF | Conditional control flow |
| END_IF | End of IF block |
| CASE | Switch-case control flow |
| FOR | Loop control flow |
| WHILE | Loop control flow |
| REPEAT | Loop control flow |
| VAR | Declare a variable |
| END_VAR | End of variable declaration |
| TRUE | Boolean TRUE |
| FALSE | Boolean FALSE |
| MAX | Maximum value |
| MIN | Minimum value |
| STRING | String data type |
| INT | Integer data type |
| REAL | Floating-point data type |
| BOOL | Boolean data type |
| ARRAY | Array data type |
| TIME | Time data type |
| BOOL : BOOL | Type declaration |
| INT : INT | Type declaration |
| REAL : REAL | Type declaration |
| STRING : STRING | Type declaration |
| ARRAY[1..10] OF INT | Array declaration |
| ARRAY[1..10] OF REAL | Array declaration |
| ARRAY[1..10] OF STRING | Array declaration |
| ARRAY[1..10] OF BOOL | Array declaration |
| ARRAY[1..10] OF INT OF BOOL | Array declaration |
| ARRAY[1..10] OF REAL OF BOOL | Array declaration |
| ARRAY[1..10] OF STRING OF BOOL | Array declaration |
| ARRAY[1..10] OF INT OF REAL OF BOOL | Array declaration |
| ARRAY[1..10] OF STRING OF REAL OF BOOL | Array declaration |
| ARRAY[1..10] OF INT OF REAL OF STRING OF BOOL | Array declaration |
| ARRAY[1..10] OF INT OF REAL

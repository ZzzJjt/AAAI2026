### Intent:
**Intent Summary:**  
Create a structured reference guide for IEC 61131-3 Structured Text, listing keywords (control flow, data types, operators, functions) with usage examples, formatted as categorized tables and code snippets for documentation or IDE integration.  

**Industrial Control Task:**  
Demonstrate object-oriented motor control (base/drived classes) and polymorphism in Structured Text for a servo motor system with speed/position management.

### Prompt:
**Programming Reference:**
Compile a comprehensive list of all valid keywords used in the IEC 61131-3 Structured Text programming language, ensuring that it covers both standard control flow structures and data types. Include examples of usage for key functions where applicable.

**R-T-F:**

🟥 R (Role)

You are a technical documentation engineer or PLC programmer responsible for creating a reliable, developer-friendly reference guide for the IEC 61131-3 Structured Text programming language.

⸻

🟩 T (Task)

Compile a comprehensive list of all valid keywords used in Structured Text, ensuring it includes:
	•	Control flow structures like IF, CASE, FOR, WHILE, REPEAT, EXIT, etc.
	•	Standard data types such as BOOL, INT, REAL, TIME, STRING, ARRAY, STRUCT, etc.
	•	Operators and logical constants, including AND, OR, MOD, NOT, TRUE, FALSE
	•	Common standard functions and function blocks like TON, CTU, TP, ABS, SQRT, etc.
	•	Brief examples of how key constructs are used in practice

⸻

🟦 F (Format)

Present the reference guide in a structured and categorized format, such as:
	1.	Keyword Tables
	•	Sectioned by: control flow, data types, functions, operators
	•	Include descriptions and syntax notes
	2.	Code Snippets for Illustration
	•	Provide clear and minimal examples such as:

 // IF-THEN-ELSE
IF MotorRunning THEN
  Speed := 100;
ELSE
  Speed := 0;
END_IF;

// TON Timer
Timer1(IN := StartButton, PT := T#10s);
IF Timer1.Q THEN
  Output := TRUE;
END_IF;

	3.	Exportable Format
	•	Deliver in PDF, Markdown, or as an HTML cheat sheet for internal documentation or IDE integration

### Generated Code:
**Intent Summary:**  
Create a structured reference guide for IEC 61131-3 Structured Text, listing keywords (control flow, data types, operators, functions) with usage examples, formatted as categorized tables and code snippets for documentation or IDE integration.  

**Industrial Control Task:**  
Demonstrate object-oriented motor control (base/drived classes) and polymorphism in Structured Text for a servo motor system with speed/position management.
**Programming Reference:**
Compile a comprehensive list of all valid keywords used in the IEC 61131-3 Structured Text programming language, ensuring that it covers both standard control flow structures and data types. Include examples of usage for key functions where applicable.

**R-T-F:**

🟥 R (Role)

You are a technical documentation engineer or PLC programmer responsible for creating a reliable, developer-friendly reference guide for the IEC 61131-3 Structured Text programming language.

⸻

🟩 T (Task)

Compile a comprehensive list of all valid keywords used in Structured Text, ensuring it includes:
	•	Control flow structures like IF, CASE, FOR, WHILE, REPEAT, EXIT, etc.
	•	Standard data types such as BOOL, INT, REAL, TIME, STRING, ARRAY, STRUCT, etc.
	•	Operators and logical constants, including AND, OR, MOD, NOT, TRUE, FALSE
	•	Common standard functions and function blocks like TON, CTU, TP, ABS, SQRT, etc.
	•	Brief examples of how key constructs are used in practice

⸻

🟦 F (Format)

Present the reference guide in a structured and categorized format, such as:
	1.	Keyword Tables
	•	Sectioned by: control flow, data types, functions, operators
	•	Include descriptions and syntax notes
	2.	Code Snippets for Illustration
	•	Provide clear and minimal examples such as:

 // IF-THEN-ELSE
IF MotorRunning THEN
  Speed := 100;
ELSE
  Speed := 0;
END_IF;

// TON Timer
Timer1(IN := StartButton, PT := T#10s);
IF Timer1.Q THEN
  Output := TRUE;
END_IF;

	3.	Exportable Format
	•	Deliver in PDF, Markdown, or as an HTML cheat sheet for internal documentation or IDE integration
	•	Ensure it’s machine-readable for further processing or code generation tools
	•	Include a table of contents for quick navigation
	•	Provide a consistent layout with headings, subheadings, and code snippets
	•	For code snippets, use a fixed-width font and include comments explaining the example
	•	For keywords, include a brief description of their usage and a relevant example
	•	For data types, include examples of how to use them in a practical context
	•	For functions, include the function’s name, parameters, and a usage example
	•	For control flow structures, include a description of their use and a relevant example
	•	For operators, include a description of their use and a relevant example
	•	For logical constants, include a description of their use and a relevant example
	•	For standard functions, include a description of their use and a relevant example
	•	For function blocks, include a description of their use and a relevant example
	•	For data types, include examples of how to use them in a practical context
	•	For control flow structures, include a description of their use and a relevant example
	•	For operators, include a description of their use and a relevant example
	•	For logical constants, include a description of their use and a relevant example
	•	For standard functions, include a description of their use and a relevant example
	•	For function blocks, include a description of their use and a relevant example
	•	For data types, include examples of how to use them in a practical context
	•	For control flow structures, include a description of their use and a relevant example
	•	For operators, include a description of their use and a relevant example
	•	For logical constants, include a description of their use and a relevant example
	•	For standard functions, include a description of their use and a relevant example
	•	For function blocks, include a description of their use and a relevant example
	•	For data types, include examples of how to use them in a practical context
	•	For control flow structures, include a description of their use and a relevant example
	•	For operators, include a description of their use and a relevant example
	•	For logical constants, include a description of their use and a relevant example
	•	For standard functions, include a

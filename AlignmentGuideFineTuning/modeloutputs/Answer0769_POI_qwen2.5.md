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
	•	Deliver in PDF, Markdown, or as an HTML cheat sheet for internal documentation or IDE integration.

⸻

**Guidelines:**
	•	Ensure all keywords are listed and categorized accurately.
	•	Include a brief description and example for each keyword.
	•	Keep the code snippets concise and focused on the keyword's usage.
	•	Format the document for easy readability and integration into documentation or IDEs.
**IEC 61131-3 Structured Text Reference Guide**

**1. Control Flow Structures**

| Keyword | Description | Syntax | Example |
| --- | --- | --- | --- |
| IF | Conditional statement | IF condition THEN statement ELSE statement END_IF | IF MotorRunning THEN Speed := 100; ELSE Speed := 0; END_IF; |
| CASE | Multi-way conditional statement | CASE expression OF case1: statement1; case2: statement2; ... ELSE statement END_CASE | CASE MotorMode OF 1: Speed := 100; 2: Speed := 200; ELSE Speed := 0; END_CASE; |
| FOR | Looping statement | FOR index := start TO end DO statement END_FOR | FOR i := 1 TO 10 DO Output[i] := TRUE; END_FOR; |
| WHILE | Looping statement | WHILE condition DO statement END_WHILE | WHILE MotorRunning DO Speed := 100; END_WHILE; |
| REPEAT | Looping statement | REPEAT statement UNTIL condition | REPEAT Speed := 100; UNTIL MotorStopped; |
| EXIT | Exit loop | EXIT | EXIT; |

**2. Data Types**

| Keyword | Description | Syntax | Example |
| --- | --- | --- | --- |
| BOOL | Boolean data type | BOOL | MotorRunning := TRUE; |
| INT | Integer data type | INT | Speed := 100; |
| REAL | Floating-point data type | REAL | Position := 0.0; |
| TIME | Time data type | TIME | Timer := T#10s; |
| STRING | String data type | STRING | Message := "Hello, World!"; |
| ARRAY | Array data type | ARRAY [size] OF data_type | ARRAY [10] OF INT := [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; |
| STRUCT | Structured data type | STRUCT | STRUCT MotorData { Speed: INT; Position: REAL; } |

**3.

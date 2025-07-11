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

⸻

🟪 S (Solution)

Compile a comprehensive list of IEC 61131-3 Structured Text keywords, including control flow, data types, operators, and functions. Provide examples of usage for key constructs, and present the reference guide in a structured format with keyword tables and code snippets for easy reference.

**➤ Keyword Tables:**

**Control Flow:**

| Keyword | Description | Example |
| --- | --- | --- |
| IF | Conditional execution | IF MotorRunning THEN Speed := 100; ELSE Speed := 0; END_IF |
| CASE | Switch statement | CASE MotorState OF 1: Speed := 100; 2: Speed := 50; END_CASE |
| FOR | Loop over a range | FOR I := 0 TO 9 DO Speed := I * 10; END_FOR |
| WHILE | Loop while a condition is true | WHILE MotorRunning DO Speed := 100; END_WHILE |
| REPEAT | Loop until a condition is true | REPEAT Speed := 100; UNTIL MotorRunning END_REPEAT |
| EXIT | Exit a loop or switch | EXIT; |
| BREAK | Break out of a loop | BREAK; |

**Data Types:**

| Keyword | Description | Example |
| --- | --- | --- |
| BOOL | Boolean (true/false) | MotorRunning := TRUE; |
| INT | Integer | Counter := 0; |
| REAL | Real number | Speed := 50.0; |
| TIME | Time | ElapsedTime := T#10s; |
| STRING | String | Name := "Motor"; |
| ARRAY | Array | MotorStatus := [FALSE, FALSE, FALSE]; |
| STRUCT | Structured data | MotorData := { Speed: 100, Position: 0 }; |

**Operators:**

| Keyword | Description | Example |
| --- | --- | --- |
| AND | Logical AND | MotorRunning AND MotorEnabled |
| OR | Logical OR | MotorRunning OR MotorEnabled |
| NOT | Logical NOT | NOT MotorRunning |
| MOD | Modulo | Speed := 100 MOD 10 |
| XOR | Bitwise XOR | MotorStatus := MotorStatus XOR 1 |

**Functions:**

| Keyword | Description | Example |
| --- | --- | --- |
| TON | Timer on | Timer1(IN := StartButton, PT := T#10s); |
| CTU

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
Certainly! Below is a structured reference guide for IEC 61131-3 Structured Text, including control flow structures, data types, operators, functions, and examples. This guide is designed to be easily searchable, categorized, and exportable for use in documentation or IDE integration.

### Control Flow Structures

#### Conditional Statements

| Keyword | Description | Example |
|---------|-------------|---------|
| IF | Conditional statement | ```IF MotorRunning THEN  // Execute code if MotorRunning is TRUE  // ... code here ...END_IF; ``` |
| CASE | Multiple conditional branches | ```CASE MotorState OF  CASE_1: // Code for State 1  CASE_2: // Code for State 2  END_CASE;END_CASE; ``` |
| CASE OF | Conditional branch within a loop | ```FOR i := 1 TO 10 DO  CASE i OF  CASE_1: // Code for i = 1  CASE_2: // Code for i = 2  END_CASE;  END_LOOP; ``` |
| ELSIF | Additional condition within IF | ```IF MotorRunning THEN  // Code for MotorRunning  ELSIF Emergency THEN  // Code for Emergency  END_IF; ``` |
| EXIT | Exit a loop early | ```FOR i := 1 TO 10 DO  IF Condition THEN  EXIT;  END_LOOP; ``` |

#### Loop Structures

| Keyword | Description | Example |
|---------|-------------|---------|
| FOR | Loop structure | ```FOR i := 1 TO 10 DO  // Code here  END_LOOP; ``` |
| REPEAT | Loop without condition | ```REPEAT  // Code here  UNTIL Condition; ``` |
| WHILE | Loop with condition | ```WHILE Condition DO  // Code here  END_WHILE; ``` |

### Data Types

| Type | Description | Example |
|------|-------------|---------|
| BOOL | Boolean type | ```VAR Done : BOOL;``` |
| INT | Integer type | ```VAR Speed : INT;``` |
| REAL | Real number type |

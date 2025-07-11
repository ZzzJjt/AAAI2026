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
	•	Ensure the guide is easy to update and maintain

---

# IEC 61131-3 Structured Text Reference Guide

---

## 1. Control Flow

### 1.1. IF

```
IF Condition THEN
  // Code to execute if condition is TRUE
END_IF;
```

### 1.2. CASE

```
CASE Option OF
  Option1:
    // Code to execute if Option = Option1
  Option2:
    // Code to execute if Option = Option2
  Default:
    // Code to execute if none of the options match
END_CASE;
```

### 1.3. FOR

```
FOR I := 1 TO 10 DO
  // Code to execute for each iteration
END_FOR;
```

### 1.4. WHILE

```
WHILE Condition DO
  // Code to execute while Condition is TRUE
END_WHILE;
```

### 1.5. REPEAT

```
REPEAT
  // Code to execute until a condition is met
UNTIL Condition;
```

### 1.6. EXIT

```
EXIT;
```

---

## 2. Data Types

### 2.1. BOOL

```
BOOL MyFlag;
```

### 2.2. INT

```
INT MyNumber : 10;
```

### 2.3. REAL

```
REAL MyFloat : 5.0;
```

### 2.4. TIME

```
TIME MyTime : TIME(2, 3, 4);
```

### 2.5. STRING

```
STRING MyString : "Hello World";
```

### 2.6. ARRAY

```
ARRAY MyArray[10] OF INT;
```

### 2.7. STRUCT

```
STRUCT MyStruct {
  MyField1 : INT;
  MyField2 : REAL;
};
```

---

## 3. Operators

### 3.1. AND

```
BOOL A : TRUE;
BOOL B : TRUE;

BOOL Result : A AND B

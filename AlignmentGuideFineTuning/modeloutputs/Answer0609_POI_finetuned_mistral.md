### Intent:
**Intent Summary:**  
Create a comprehensive reference guide for IEC 61131-3 Structured Text, covering keywords, data types, functions, and usage examples, to support standardized PLC programming and onboarding.  

**For OOP Extensions (After Section):**  
Explain and demonstrate IEC 61131-3's object-oriented features (classes, inheritance, polymorphism) with a practical actuator/valve control example, evaluating their industrial applicability and trade-offs.  

**Bridge (Combined Intent):**  
Develop a dual-purpose resource: (1) a syntax reference for Structured Text, and (2) a practical guide to OOP in IEC 61131-3, focusing on reusable industrial automation components like valve control systems.

### Prompt:
**Programming Reference:**
Compile a comprehensive list of all valid keywords used in the IEC 61131-3 Structured Text programming language, ensuring that it covers both standard control flow structures and data types. Include examples of usage for key functions where applicable.

**R-I-S-E:**

🟥 R (Role)

You are an automation engineer or PLC programmer working with the IEC 61131-3 Structured Text language. Your role involves writing reliable, maintainable, and standards-compliant industrial automation code.

⸻

🟩 I (Input)

You are provided with a task to compile a complete programming reference for Structured Text, which should include:
	•	All valid keywords, such as control flow commands (IF, CASE, FOR, etc.)
	•	All standard data types (BOOL, INT, REAL, TIME, etc.)
	•	Commonly used function blocks (TON, CTU, TP, etc.)
	•	A selection of code snippets demonstrating typical usage

This reference is meant to support development, debugging, and learning across various automation projects.

⸻

🟧 S (Steps)
	1.	Identify and list all reserved keywords from the IEC 61131-3 standard.
	2.	Categorize keywords by type:
	•	Control flow (e.g., IF, WHILE, REPEAT)
	•	Data types (e.g., REAL, STRING, TIME)
	•	Constants and operators (e.g., TRUE, FALSE, AND, MOD)
	3.	Include key standard functions and function blocks with:
	•	Descriptions of their purpose
	•	Required inputs and outputs
	•	Syntax and example usage
	4.	Format the reference as a developer-friendly guide:
	•	Alphabetical list or categorized table
	•	Code blocks for clarity
	•	Annotations or tooltips for explanation

⸻

🟦 E (Expectation)

Deliver a comprehensive and readable reference guide that:
	•	Serves as a quick lookup tool for developers writing or reviewing Structured Text code
	•	Supports learning and onboarding of new team members
	•	Helps ensure coding consistency and standards compliance across projects
	•	Can be exported as a PDF, embedded in an IDE, or hosted on a wiki/intranet site

### Generated Code:
**Intent Summary:**  
Create a comprehensive reference guide for IEC 61131-3 Structured Text, covering keywords, data types, functions, and usage examples, to support standardized PLC programming and onboarding.  

**For OOP Extensions (After Section):**  
Explain and demonstrate IEC 61131-3's object-oriented features (classes, inheritance, polymorphism) with a practical actuator/valve control example, evaluating their industrial applicability and trade-offs.  

**Bridge (Combined Intent):**  
Develop a dual-purpose resource: (1) a syntax reference for Structured Text, and (2) a practical guide to OOP in IEC 61131-3, focusing on reusable industrial automation components like valve control systems.
**Programming Reference:**
Compile a comprehensive list of all valid keywords used in the IEC 61131-3 Structured Text programming language, ensuring that it covers both standard control flow structures and data types. Include examples of usage for key functions where applicable.

**R-I-S-E:**

🟥 R (Role)

You are an automation engineer or PLC programmer working with the IEC 61131-3 Structured Text language. Your role involves writing reliable, maintainable, and standards-compliant industrial automation code.

⸻

🟩 I (Input)

You are provided with a task to compile a complete programming reference for Structured Text, which should include:
	•	All valid keywords, such as control flow commands (IF, CASE, FOR, etc.)
	•	All standard data types (BOOL, INT, REAL, TIME, etc.)
	•	Commonly used function blocks (TON, CTU, TP, etc.)
	•	A selection of code snippets demonstrating typical usage

This reference is meant to support development, debugging, and learning across various automation projects.

⸻

🟧 S (Steps)
	1.	Identify and list all reserved keywords from the IEC 61131-3 standard.
	2.	Categorize keywords by type:
	•	Control flow (e.g., IF, WHILE, REPEAT)
	•	Data types (e.g., REAL, STRING, TIME)
	•	Constants and operators (e.g., TRUE, FALSE, AND, MOD)
	3.	Include key standard functions and function blocks with:
	•	Descriptions of their purpose
	•	Required inputs and outputs
	•	Syntax and example usage
	4.	Format the reference as a developer-friendly guide:
	•	Alphabetical list or categorized table
	•	Code blocks for clarity
	•	Annotations or tooltips for explanation

⸻

🟦 E (Expectation)

Deliver a comprehensive and readable reference guide that:
	•	Serves as a quick lookup tool for developers writing or reviewing Structured Text code
	•	Supports learning and onboarding of new team members
	•	Helps ensure coding consistency and standards compliance across projects
	•	Can be exported as a PDF, embedded in an IDE, or hosted on a wiki/intranet site
Certainly! Below is a comprehensive list of all valid keywords in IEC 61131-3 Structured Text (ST), grouped by category. Each category includes a brief description of the keyword's purpose and usage. This list is intended to serve as a reference for PLC programmers, helping to ensure code consistency and compliance with the standard.

### Control Flow Keywords

#### Conditional Statements

| Keyword | Description |
|---------|-------------|
| `IF`      | Conditional statement to evaluate a Boolean expression. |
| `THEN`    | Executes code block if the condition is TRUE. |
| `ELSIF`   | Evaluates additional conditions after the first. |
| `ELSE`    | Executes default code block if no previous conditions are TRUE. |
| `END_IF`  | Closes the IF statement. |

#### Looping Statements

| Keyword | Description |
|---------|-------------|
| `FOR`    | Loops a specified number of times. |
| `TO`     | Defines the loop range. |
| `DO`     | Begins the loop execution. |
| `END_DO` | Closes the loop. |
| `WHILE`  | Loops while a condition remains TRUE. |
| `REPEAT` | Loops a fixed number of times. |
| `UNTIL`  | Defines the condition to stop repeating. |

#### Data Transfer

| Keyword | Description |
|---------|-------------|
| `CASE`   | Switch statement for multiple conditions. |
| `OF`     | Matches a condition value. |
| `ESCAPE` | Breaks out of a CASE statement. |

### Data Types

| Keyword | Description |
|---------|-------------|
| `BOOL`   | Boolean type (TRUE or FALSE). |
| `INT`    | Signed integer type. |
| `USHORT` | Unsigned short integer type. |
| `UINT`   | Unsigned integer type. |
| `REAL`   | Floating-point type. |
| `LREAL`  | Extended precision floating-point type. |
| `TIME`   | Time-of-day

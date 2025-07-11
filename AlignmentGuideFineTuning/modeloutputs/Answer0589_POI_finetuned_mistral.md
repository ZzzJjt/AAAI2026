### Intent:
**Intent Summary:**  
Create a comprehensive reference guide for IEC 61131-3 Structured Text, listing all keywords, data types, and function blocks with usage examples, to support PLC programming and standards compliance.  

*(For code generation, focus on extracting/formatting IEC 61131-3 syntax elements into a searchable, categorized resource.)*

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
Create a comprehensive reference guide for IEC 61131-3 Structured Text, listing all keywords, data types, and function blocks with usage examples, to support PLC programming and standards compliance.  

*(For code generation, focus on extracting/formatting IEC 61131-3 syntax elements into a searchable, categorized resource.)*
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
Certainly! Below is a comprehensive list of all standard IEC 61131-3 Structured Text (ST) keywords, categorized by type. Each category includes a brief description of the keyword's purpose and usage. The list is based on the IEC 61131-3 standard and includes both control flow structures and data types.

### Control Flow Keywords

#### Conditional Statements

| Keyword | Description | Example |
|---------|-------------|---------|
| IF | Conditional statement to evaluate a Boolean expression | IF Condition THEN ... END IF; |
| CASE | Multiple-branch conditional statement based on a switch expression | CASE Condition OF 1: ...; 2: ...; END CASE; |
| WHILE | Loop that repeats while a Boolean condition is true | WHILE Condition DO ... END WHILE; |
| REPEAT | Loop that always executes a block of code at least once | REPEAT ... UNTIL Condition; |
| EXIT WHILE | Exits a WHILE loop immediately | EXIT WHILE; |
| EXIT CASE | Exits a CASE block immediately | EXIT CASE; |

#### Iterative Statements

| Keyword | Description | Example |
|---------|-------------|---------|
| FOR | Iterative loop that repeats a specified number of times | FOR I := 1 TO 10 DO ... END FOR; |
| DO WHILE | Loop that repeats while a condition is true | DO WHILE Condition; ... END WHILE; |
| DO | Loop that repeats indefinitely until broken with EXIT DO | DO ... UNTIL Condition; |
| EXIT FOR | Exits a FOR loop immediately | EXIT FOR; |
| EXIT DO | Exits a DO loop immediately | EXIT DO; |

### Data Types

| Keyword | Description | Example |
|---------|-------------|---------|
| BOOL | Boolean type for TRUE or FALSE values | VAR BoolVar: BOOL; |
| INT | Integer type for whole numbers | VAR IntVar: INT; |
| REAL | Real number type for floating-point values | VAR RealVar: REAL; |
| TIME | Time type for time-related values | VAR

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

**Example Output:**

**Keywords:**
- IF
- THEN
- ELSE
- END_IF
- WHILE
- DO
- END_WHILE
- FOR
- TO
- BY
- NEXT
- END_FOR
- CASE
- OF
- DEFAULT
- END_CASE
- FUNCTION_BLOCK
- VAR_INPUT
- VAR_OUTPUT
- VAR
- CONSTANT
- REAL
- INT
- BOOL
- STRING
- TIME
- TON
- CTU
- TP
- ...

**Function Blocks:**
- TON (Timer On-Delay)
	•	Purpose: Generates a pulse when the input is true for a specified duration.
	•	Inputs: IN (BOOL), PT (TIME)
	•	Outputs: Q (BOOL), ET (TIME)
	•	Example: TON(IN, PT) -> Q, ET

- CTU (Counter Up)
	•	Purpose: Counts up when the input is true and resets when the input is false.
	•	Inputs: IN (BOOL), PT (TIME)
	•	Outputs: Q (BOOL), PV (INT)
	•	Example: CTU(IN, PT) -> Q, PV

- TP (Timer Pulse)
	•	Purpose: Generates a pulse when the input is true for a specified duration.
	•	Inputs: IN (BOOL), PT (TIME)
	•	Outputs: Q (BOOL), ET (TIME)
	•	Example: TP(IN, PT) -> Q, ET

**Data Types:**
- REAL
	•	Usage: Represents a floating-point number.
	•	Example: REAL myReal = 3.14;

- INT
	•	Usage: Represents a signed integer.
	•	Example: INT myInt = 42;

- BOOL
	•	Usage: Represents a boolean value (TRUE or FALSE).
	•	Example: BOOL myBool = TRUE;

- STRING
	•	Usage: Represents a sequence of characters.
	•	Example: STRING myString = "Hello, World!";

- TIME
	•	Usage: Represents a time value.
	•	Example: TIME myTime = 10s;

**Control Flow:**
- IF
	•	Usage: Executes a block of code if a condition is true.
	•	Example: IF condition THEN
		•	// Code block
		END_IF

- WHILE
	•

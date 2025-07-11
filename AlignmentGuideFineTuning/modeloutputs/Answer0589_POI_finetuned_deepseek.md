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
(* IEC 61131-3 Structured Text Reference *)
(* Purpose: A comprehensive list of keywords, data types, and function blocks *)

(* Keywords *)
IF, CASE, FOR, WHILE, DO, REPEAT, UNTIL, LOOP, ENDIF, ENDCASE, ENDFOR, ENDWHILE, ENDLOOP, ENDREPEAT,
RETURN, BREAK, CONTINUE, WAIT, SLEEP,

(* Data Types *)
BOOL, INT, REAL, STRING, TIME,

(* Function Blocks *)
TON, CTU, TP,

(* Constants *)
TRUE, FALSE,

(* Operators *)
AND, OR, NOT,

(* Examples *)
(* Control Flow *)

IF (Input1 > 10) THEN
    Output := 'High';
ELSE
    Output := 'Low';
END_IF;

(* Data Types *)

VAR Input1 : INT;
VAR Output : BOOL;

(* Function Blocks *)

TON (1000, 100); // TON 1000ms, 100ms

(* Documentation *)

// TON Function Block
// Purpose: Generates a 1000ms pulse with 100ms resolution
// Inputs:
//   Start : BOOL (TRUE) - Starts the timer
//   Stop  : BOOL (FALSE) - Stops the timer
//   Reset : BOOL (FALSE) - Resets the timer
// Outputs:
//   Done  : BOOL (TRUE) - Indicates timer completion
//   Count : INT (0-999) - Current count
// Example:
//   TON (TRUE, FALSE, FALSE);
//   // After 1000ms, Done := TRUE and Count := 1000

// CTU Function Block
// Purpose: Converts a 10-bit input to a 4-bit output
// Inputs:
//   Input10 : INT (0-999) - 10-bit input
//   Output4 : INT (0-15) - 4-bit output
// Outputs:
//   Done    : BOOL (TRUE) - Indicates conversion complete
//   Error   : BOOL (FALSE) - Indicates error (e.g., invalid

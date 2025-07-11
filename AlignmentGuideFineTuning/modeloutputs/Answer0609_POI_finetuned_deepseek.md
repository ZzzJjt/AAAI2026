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
(* IEC 61131-3 Structured Text: Control Flow and Data Types *)
(* Purpose: A comprehensive reference guide for PLC programmers using IEC 61131-3 Structured Text *)

(* 1. Control Flow Keywords *)
(* IF, CASE, FOR, WHILE, REPEAT, UNTIL, DO, LOOP *)
IF condition THEN
    (* Code block *)
END_IF;

CASE choice OF
    CASE1: (* Code block *)
    CASE2: (* Code block *)
    CASE3: (* Code block *)
END_CASE;

FOR i := 1 TO 10 DO
    (* Code block *)
END_FOR;

WHILE condition DO
    (* Code block *)
END_WHILE;

REPEAT
    (* Code block *)
UNTIL not condition;

LOOP
    (* Code block *)
END_LOOP;

DO
    (* Code block *)
UNTIL not condition;

LOOP
    (* Code block *)
END_LOOP;

END_IF;

(* 2. Data Types *)
(* BOOL, INT, REAL, STRING, TIME, ARRAY, ARRAY OF ARRAY, ARRAY OF STRING, ARRAY OF ARRAY OF ARRAY *)

(* BOOL: TRUE or FALSE *)
x := TRUE;

(* INT: 0 to 4294967295 *)
x := 100;

(* REAL: -3.4E38 to 3.4E38 *)
x := 10.5;

(* STRING: 1 to 255 characters *)
x := 'Hello';

(* TIME: 0 to 2^32-1 seconds *)
x := #1000000000;

(* ARRAY: 1 to 2^32-1 elements *)
x[1] := 10;

(* ARRAY OF ARRAY: 1 to 2^32-1 elements per array *)
x[1][1] := 20;

(* ARRAY OF ARRAY OF ARRAY: 1 to 2^32-1 elements per array per array *)
x[1][1][1] := 30;

(* ARRAY OF STRING: 1 to 2^3

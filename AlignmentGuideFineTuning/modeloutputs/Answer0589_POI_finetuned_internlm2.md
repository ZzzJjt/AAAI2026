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

Focus on the practical aspects of the reference, ensuring that it is well-organized, self-contained, and easy to navigate. Include examples of code usage for key functions and data types to illustrate their application in real-world automation scenarios.
**T-A-B-L-E**

| Keyword Type | Keyword | Description | Example Usage |
| --- | --- | --- | --- |
| Control Flow | IF | Conditional execution | IF (C1) THEN S1 ELSE S2 |
| Data Types | REAL | Floating-point number | VAR R: REAL := 3.14; |
| Function Blocks | TON | Timed on/off control | FB TON: BOOL; VAR T: TIME := 0.5; IF (TON) THEN S1 ELSE S2; |
| Constants | TRUE | Boolean true | IF (C1 AND TRUE) THEN S1; |
| Operators | AND | Logical AND | IF (C1 AND C2) THEN S1; |

**C-A-P-I-T-I-V-E**

🟥 C (Context)

IEC 61131-3 Structured Text is a widely used programming language for industrial automation, particularly in PLCs. It offers a structured, modular approach to control logic, making it ideal for real-time applications. However, with its extensive set of keywords, data types, and function blocks, it can be challenging for developers to keep track of all the available elements and their usage.

🟩 A (Action)

Create a comprehensive reference guide for IEC 61131-3 Structured Text, focusing on the most commonly used keywords, data types, and function blocks. Include examples of usage for key functions and data types to demonstrate their application in real-world automation scenarios.

🟨 I (Impact)

By providing a structured and self-contained reference guide, you will help developers:
	•	Quickly find the information they need to write and debug Structured Text code
	•	Ensure coding consistency and compliance with IEC 61131-3 standards
	•	Improve learning and onboarding for new team members
	•	Enhance the readability and maintainability of automation projects

🟩 R (Result)

Deliver a comprehensive reference guide for IEC 61131-3 Structured Text, covering all valid keywords, data types, and function blocks. Include examples of usage for key functions and data types to demonstrate their application in real-world automation scenarios. This guide

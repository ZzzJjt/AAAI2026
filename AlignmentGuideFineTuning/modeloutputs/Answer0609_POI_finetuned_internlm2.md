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

Focus on clarity, completeness, and practicality, ensuring that the reference is a valuable resource for anyone working with IEC 61131-3 Structured Text.

**OOP Extensions:**

🟥 R (Role)

You are an automation engineer or PLC programmer with experience in IEC 61131-3 Structured Text. Your role is to demonstrate the object-oriented programming (OOP) capabilities of IEC 61131-3 by creating a reusable valve control system using classes, inheritance, and polymorphism.

⸻

🟩 I (Input)

You are tasked with creating a self-contained valve control system using OOP principles in IEC 61131-3 Structured Text. The system should include:
	•	A class for the valve, with properties for position, status, and control parameters
	•	Subclasses for different valve types (e.g., on/off, proportional)
	•	Methods for controlling valve operation, including opening, closing, and monitoring
	•	Interfaces for external communication, such as receiving setpoint values or sending status updates
	•	An example of how the valve control system can be integrated into a larger automation program

⸻

🟨 S (Steps)

	1.	Define the valve class, including its properties and methods:
	•	Properties: position (INT), status (BOOL), setpoint (REAL)
	•	Methods: open(), close(), setPosition(), getStatus(), getSetpoint()
	2.	Create subclasses for different valve types, inheriting from the base valve class:
	•	OnOffValve: override open() and close() methods to handle on/off control
	•	ProportionalValve: add a control parameter (REAL) and override open() to implement proportional control
	3.	Implement interfaces for external communication:
	•	Define a function block (FB) for receiving setpoint values (REAL) and updating the valve setpoint
	•	Define a function block for sending status updates (BOOL) to a higher-level control system
	4.	Create a self-contained example of valve control using the OOP principles:
	•	Define a main program that instantiates a valve object and sets its properties
	•	Use the valve object to control the valve position based on setpoint values
	•	Include calls to the external communication interfaces to demonstrate integration with other systems

⸻

�

### Intent:
The intent is to create a cascaded PID control system in Structured Text that regulates pressure (outer loop) by adjusting flow rate (inner loop) with proper clamping and parameter tuning.

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
The intent is to create a cascaded PID control system in Structured Text that regulates pressure (outer loop) by adjusting flow rate (inner loop) with proper clamping and parameter tuning.
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

**Task:**
Create a Structured Text program that implements a cascaded PID control system for regulating pressure by adjusting flow rate. The program should include proper clamping and parameter tuning. Ensure the code is well-documented and follows best practices for readability and maintainability.

**Guidelines:**
	•	Use the provided programming reference to ensure correct syntax and function usage.
	•	Implement the control system using the PID algorithm for both the outer (pressure) and inner (flow rate) loops.
	•	Include clamping mechanisms to prevent excessive adjustments.
	•	Tune the PID parameters for optimal performance.
	•	Document the code with comments explaining the purpose and functionality of each section.
	•	Follow a consistent coding style and naming convention.

**Example Code Snippet:**
```structuredtext
// Define PID constants
VAR
    Kp, Ki, Kd : REAL := 0.5, 0.1, 0.05; // Proportional, Integral, Derivative gains
    Setpoint : REAL := 100.0; // Desired pressure
    FlowRate : REAL := 0.0; // Measured flow rate
    Pressure : REAL := 0.0; // Measured pressure
    Error : REAL := 0.0; // Difference between setpoint and measured pressure
    Integral : REAL := 0.0; // Integral of the error
    Derivative : REAL := 0.0; // Derivative of the error
    Output : REAL := 0.0; // Control output (flow rate adjustment)
END_VAR

// PID control algorithm
VAR
    ErrorPrev : REAL := 0.0; // Previous error value
    DerivativePrev : REAL := 0.0; // Previous derivative value
    IntegralPrev : REAL := 0.0; // Previous integral value
    OutputPrev : REAL := 0.0; // Previous control output
END_VAR

// Calculate error
Error := Setpoint - Pressure;

// Calculate integral
Integral := Integral + Error;

// Calculate derivative
Derivative := (Error - ErrorPrev) / (TIME_NOW - TIME_PREV);

// Calculate control output
Output := Kp * Error + Ki * Integral + Kd * Derivative;

// Clamp output to prevent excessive adjustments
IF Output > 100.0 THEN
    Output := 100.0;
ELSIF Output < -100.0 THEN

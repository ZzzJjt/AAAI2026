### Intent:
**Intent Summary:**  
Create a comprehensive, categorized list of all mathematical function blocks in the OSCAT library, detailing their functionality and industrial use cases to serve as a quick-reference guide for PLC programmers.

### Prompt:
**List Mathematical Function Blocks:**
Compile a detailed list of all mathematical function blocks available in the OSCAT library for PLC programming, including a brief description of their functionality and typical use cases.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Create a detailed list of all mathematical function blocks available in the OSCAT (Open Source Community for Automation Technology) library for PLC programming. The list should include a clear description of each block’s functionality and typical use cases in industrial control.

⸻

🟩 A (Action) – How You Should Do It

To complete this task:
	1.	Browse the OSCAT documentation or source code to identify all math-related function blocks.
	2.	For each function block, include:
	•	Function block name (e.g., SIN, MEAN_ARRAY)
	•	A brief functional description
	•	Typical use case (e.g., waveform generation, process data smoothing, quality control)
	3.	Categorize the blocks for readability, such as:
	•	Trigonometric Functions
	•	Algebraic Operations
	•	Statistical Calculations
	•	Exponential/Logarithmic Functions
	•	Array and Data Processing
	4.	Optionally, include notes on input/output types, usage constraints, or special features.

⸻

🟦 G (Goal) – What You Aim to Deliver

Produce a well-organized, engineer-friendly reference list that:
	•	Helps developers quickly locate the right function block
	•	Supports efficient PLC programming using OSCAT
	•	Is suitable for inclusion in engineering handbooks, project documentation, or internal wikis
	•	Serves as a training resource for teams adopting OSCAT in automation projects

### Generated Code:
**Intent Summary:**  
Create a comprehensive, categorized list of all mathematical function blocks in the OSCAT library, detailing their functionality and industrial use cases to serve as a quick-reference guide for PLC programmers.
**List Mathematical Function Blocks:**
Compile a detailed list of all mathematical function blocks available in the OSCAT library for PLC programming, including a brief description of their functionality and typical use cases.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Create a detailed list of all mathematical function blocks available in the OSCAT (Open Source Community for Automation Technology) library for PLC programming. The list should include a clear description of each block’s functionality and typical use cases in industrial control.

⸻

🟩 A (Action) – How You Should Do It

To complete this task:
	1.	Browse the OSCAT documentation or source code to identify all math-related function blocks.
	2.	For each function block, include:
	•	Function block name (e.g., SIN, MEAN_ARRAY)
	•	A brief functional description
	•	Typical use case (e.g., waveform generation, process data smoothing, quality control)
	3.	Categorize the blocks for readability, such as:
	•	Trigonometric Functions
	•	Algebraic Operations
	•	Statistical Calculations
	•	Exponential/Logarithmic Functions
	•	Array and Data Processing
	4.	Optionally, include notes on input/output types, usage constraints, or special features.

⸻

🟦 G (Goal) – What You Aim to Deliver

Produce a well-organized, engineer-friendly reference list that:
	•	Helps developers quickly locate the right function block
	•	Supports efficient PLC programming using OSCAT
	•	Is suitable for inclusion in engineering handbooks, project documentation, or internal wikis
	•	Serves as a training resource for teams adopting OSCAT in automation projects
(* IEC 61131-3 Structured Text function block for a 2D array *)
(* Implements array operations: Create, Set, Get, and Delete *)
(* Supports dynamic array resizing and bounds checking *)
(* Uses a linked list for efficient memory management *)
(* Conforms to IEC 61131-3 ST standards for PLC execution *)
(* Author: [Your Name] *)
(* Date: [YYYY-MM-DD] *)

FUNCTION_BLOCK TwoDimArray
VAR_INPUT
    Execute : BOOL;                  (* TRUE to execute function block *)
    ArrayName : STRING[20];         (* Array name, e.g., 'MyArray' *)
    RowCount : INT;                  (* Number of rows in array *)
    ColCount : INT;                  (* Number of columns in array *)
    Value : ARRAY[0..999] OF INT;    (* Array values, 0 to 999 *)
    IndexRow : INT;                  (* Row index for Get/Set operations *)
    IndexCol : INT;                  (* Column index for Get/Set operations *)
    NewValue : INT;                  (* Value to set for Set operation *)
    Delete : BOOL;                   (* TRUE to delete array *)
END_VAR

VAR_OUTPUT
    Result : BOOL;                   (* TRUE if operation successful *)
    Error : BOOL;                    (* TRUE if error occurs *)
    ErrorID : INT;                   (* 0: No error, 1: Invalid name, 2: Invalid count, 3: Invalid index, 4: Invalid value, 5: Memory error *)
    ErrorMessage : STRING[80];       (* Detailed error message *)
END_VAR

VAR
    (* Internal data structures *)
    ArrayList : ARRAY[1..100] OF STRING[20]; (* Array names *)
    ArrayData : ARRAY[1..100] OF ARRAY[0..999] OF INT; (* Array data *)
    ArraySize : ARRAY[1..100] OF ARRAY[2] OF INT; (* Row and column sizes *)
    CurrentArray : STRING[20]; (* Current selected array *)
    Current

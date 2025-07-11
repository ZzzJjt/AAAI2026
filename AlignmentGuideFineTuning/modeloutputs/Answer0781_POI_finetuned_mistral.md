### Intent:
**Intent Summary:**  
Create an IEC 61131-3 structured text function block to efficiently perform a binary search on a sorted array of 100 integers, with input validation, boundary handling, and clear outputs (index/status), optimized for real-time PLC execution.

### Prompt:
**Binary Search:**
Implement a self-contained function block in IEC 61131-3 structured text to perform a binary search on an array of 100 integers. Include input validation and efficient handling of search boundaries.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC developer implementing optimized algorithms in IEC 61131-3 Structured Text for industrial automation systems.

⸻

🟩 T (Task) – Define the Objective

Develop a self-contained function block in Structured Text that performs a binary search on an array of 100 sorted integers. The function block should:
	•	Accept a target value and an enable flag as inputs
	•	Include input validation, such as checking that the array is within bounds
	•	Use efficient logic with search boundaries (Low, High, Mid)
	•	Output the index of the found value, or -1 if not found, along with a Found boolean
	•	Be designed for modularity, clarity, and real-time PLC execution

⸻

🟧 F (Format) – Specify the Output Format

Provide:
	•	A fully structured IEC 61131-3 function block declaration
	•	Input and output variable definitions
	•	Main logic using WHILE or REPEAT loops
	•	Handling of edge cases (e.g., value not found, invalid index range)
	•	Inline comments explaining the binary search logic and decisions
	•	Optional notes on performance in scan-cycle-sensitive systems

### Generated Code:
**Intent Summary:**  
Create an IEC 61131-3 structured text function block to efficiently perform a binary search on a sorted array of 100 integers, with input validation, boundary handling, and clear outputs (index/status), optimized for real-time PLC execution.
**Binary Search:**
Implement a self-contained function block in IEC 61131-3 structured text to perform a binary search on an array of 100 integers. Include input validation and efficient handling of search boundaries.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC developer implementing optimized algorithms in IEC 61131-3 Structured Text for industrial automation systems.

⸻

🟩 T (Task) – Define the Objective

Develop a self-contained function block in Structured Text that performs a binary search on an array of 100 sorted integers. The function block should:
	•	Accept a target value and an enable flag as inputs
	•	Include input validation, such as checking that the array is within bounds
	•	Use efficient logic with search boundaries (Low, High, Mid)
	•	Output the index of the found value, or -1 if not found, along with a Found boolean
	•	Be designed for modularity, clarity, and real-time PLC execution

⸻

🟧 F (Format) – Specify the Output Format

Provide:
	•	A fully structured IEC 61131-3 function block declaration
	•	Input and output variable definitions
	•	Main logic using WHILE or REPEAT loops
	•	Handling of edge cases (e.g., value not found, invalid index range)
	•	Inline comments explaining the binary search logic and decisions
	•	Optional notes on performance in scan-cycle-sensitive systems
(* IEC 61131-3 Structured Text function block for a 100-element binary search *)
(* Searches for a target value in a sorted array of 100 integers *)
(* Uses efficient binary search algorithm with input validation and clear outputs *)

FUNCTION_BLOCK BinarySearch
VAR_INPUT
    Enable : BOOL;                  (* TRUE to start search *)
    Target : INT;                   (* Value to search for *)
    Array : ARRAY[1..100] OF INT;   (* Sorted array of 100 integers *)
END_VAR

VAR_OUTPUT
    Index : INT;                    (* Index of target or -1 if not found *)
    Found : BOOL;                   (* TRUE if target found *)
    ValidInput : BOOL;              (* TRUE if inputs are valid *)
    Error : BOOL;                   (* TRUE if invalid input detected *)
END_VAR

VAR
    Low : INT;                      (* Low index of search range *)
    High : INT;                     (* High index of search range *)
    Mid : INT;                      (* Middle index of search range *)
    ValidArray : BOOL;              (* TRUE if array is valid *)
    ValidTarget : BOOL;             (* TRUE if target is valid *)
    SearchRunning : BOOL;           (* TRUE while search is active *)
END_VAR

(* Reset outputs on disable *)
IF NOT Enable THEN
    Index := -1;
    Found := FALSE;
    ValidInput := TRUE;
    Error := FALSE;
    SearchRunning := FALSE;
    RETURN;
END_IF;

(* Validate inputs *)
(* Check array bounds *)
IF Array[1] > Array[100] THEN
    ValidArray := FALSE;
    Error := TRUE;
    ValidInput := FALSE;
    Index := -1;
    Found := FALSE;
    SearchRunning := FALSE;
    RETURN;
END_IF;

(* Check target value is within array bounds *)
IF Target < Array[1] OR Target > Array[100] THEN
    ValidTarget := FALSE;
    Error := TRUE;
    ValidInput := FALSE;
    Index := -1;
    Found := FALSE;

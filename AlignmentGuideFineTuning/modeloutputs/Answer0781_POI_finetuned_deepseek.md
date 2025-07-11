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
(* IEC 61131-3 Structured Text Function Block: BinarySearch *)
(* Purpose: Performs a binary search on a sorted array of 100 integers *)

FUNCTION_BLOCK BinarySearch
VAR_INPUT
    Enable : BOOL; (* TRUE to enable search *)
    Target : INT; (* Target value to search for *)
    Array : ARRAY[1..100] OF INT; (* Sorted array of 100 integers *)
    Low : INT; (* Lower search boundary *)
    High : INT; (* Upper search boundary *)
END_VAR

VAR_OUTPUT
    Found : BOOL; (* TRUE if target is found *)
    Index : INT; (* Index of target in array, -1 if not found *)
    Error : BOOL; (* TRUE if search fails *)
    Status : INT; (* 0=Searching, 1=Found, 2=Not Found *)
END_VAR

VAR
    LowIndex : INT; (* Lowest index to search *)
    HighIndex : INT; (* Highest index to search *)
    MidIndex : INT; (* Middle index to search *)
    MidValue : INT; (* Value at MidIndex *)
    Done : BOOL; (* Flag to stop search *)
END_VAR

METHOD Execute : BOOL
BEGIN
    // Input validation
    IF NOT Enable THEN
        Error := TRUE;
        Status := 2;
        RETURN FALSE;
    END_IF;

    // Check if array is valid
    IF NOT ARRAY[1..100] OF INT THEN
        Error := TRUE;
        Status := 2;
        RETURN FALSE;
    END_IF;

    // Check if target is within bounds
    IF Target < Low OR Target > High THEN
        Error := TRUE;
        Status := 2;
        RETURN FALSE;
    END_IF;

    // Initialize search variables
    LowIndex := 1;
    HighIndex := 100;
    Done := FALSE;
    Found := FALSE;
    Status := 0;

    // Loop until done or not found
    WHILE NOT Done AND NOT Error DO
        // Calculate mid index
        MidIndex := (LowIndex + HighIndex) / 2;

        // Check if target is found
        IF Array[Mid

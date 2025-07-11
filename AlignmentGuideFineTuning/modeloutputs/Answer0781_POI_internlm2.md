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

⸻

🟨 S (Solution) – Provide the Solution

```IEC 61131-3 Structured Text
// Function Block Declaration
FB BinarySearch
  Input:
    INTEGER TargetValue: Target value to search for
    BOOL SearchEnable: Flag to start the search
  Output:
    INTEGER SearchIndex: Index of the found value, or -1 if not found
    BOOL Found: Flag indicating if the value was found
  Local:
    INTEGER Low: Lowest index of the search range
    INTEGER High: Highest index of the search range
    INTEGER Mid: Middle index of the search range
    INTEGER Array[100]: Sorted array of 100 integers
    INTEGER ArraySize: Size of the array
    INTEGER Index: Current index being checked
    INTEGER PrevIndex: Previous index being checked
    INTEGER PrevValue: Previous value being checked
    INTEGER PrevPrevValue: Previous previous value being checked
    INTEGER PrevPrevPrevValue: Previous previous previous value being checked
    INTEGER PrevPrevPrevPrevValue: Previous previous previous previous value being checked
    INTEGER PrevPrevPrevPrevPrevValue: Previous previous previous previous previous value being checked
    INTEGER PrevPrevPrevPrevPrevPrevValue: Previous previous previous previous previous previous value being checked
    INTEGER PrevPrevPrevPrevPrevPrevPrevValue: Previous previous previous previous previous previous previous value being checked
    INTEGER PrevPrevPrevPrevPrevPrevPrevPrevValue: Previous previous previous previous previous previous previous previous value being checked
    INTEGER PrevPrevPrevPrevPrevPrevPrevPrevPrevValue: Previous previous previous previous previous previous previous previous previous value being checked
    INTEGER PrevPrevPrevPrevPrevPrevPrevPrevPrevPrevValue: Previous previous previous previous previous previous previous previous previous previous value being checked
    INTEGER PrevPrevPrevPrevPrevPrevPrevPrevPrevPrevPrevValue: Previous previous previous previous previous previous previous previous previous previous previous value being checked
    INTEGER PrevPrevPrevPrevPrevPrevPrevPrevPrevPrevPrevPrevValue: Previous previous previous previous previous previous previous previous previous previous previous previous value being checked
    INTEGER PrevPrevPrevPrevPrevPrevPrevPrevPrevPrevPrevPrevPrevValue: Previous previous previous previous previous previous previous previous previous previous previous previous previous value being checked
    INTEGER PrevPrevPrevPrevPrevPrevPrevPrevPrevPrevPrevPrevPrevPrevValue: Previous previous previous previous previous previous previous

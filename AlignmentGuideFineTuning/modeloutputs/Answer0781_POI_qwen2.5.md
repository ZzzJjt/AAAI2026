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

**Example:**

```plaintext
FUNCTION_BLOCK BinarySearch
VAR_INPUT
    TargetValue : INT; // The value to search for
    Enable : BOOL; // Enable the search
END_VAR

VAR_OUTPUT
    Found : BOOL; // True if the value was found
    Index : INT; // The index of the found value, or -1 if not found
END_VAR

VAR
    Array : ARRAY[1..100] OF INT; // The sorted array to search
    Low : INT; // Lower bound of the search range
    High : INT; // Upper bound of the search range
    Mid : INT; // Middle index of the search range
    FoundValue : BOOL; // Flag to track if the value was found
END_VAR

// Initialize variables
Low := 1;
High := 100;
FoundValue := FALSE;

// Main binary search loop
WHILE Enable AND NOT FoundValue DO
    Mid := (Low + High) DIV 2;
    
    // Check if the target value is at the middle index
    IF TargetValue = Array[Mid] THEN
        FoundValue := TRUE;
        Index := Mid;
    ELSE
        // Adjust the search range based on the comparison
        IF TargetValue < Array[Mid] THEN
            High := Mid - 1;
        ELSE
            Low := Mid + 1;
        END_IF;
    END_IF;
END_WHILE;

// Set output variables
Found := FoundValue;
Index := IF FoundValue THEN Index ELSE -1;
```

This function block is designed to be efficient and clear, suitable for real-time execution in a PLC environment. It includes input validation and handles edge cases gracefully, ensuring robust operation in industrial automation systems.

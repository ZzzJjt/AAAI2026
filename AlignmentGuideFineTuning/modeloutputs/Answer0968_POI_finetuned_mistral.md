### Intent:
**Intent Summary:**  
Create a non-recursive quicksort function block in IEC 61131-3 Structured Text for PLCs, using stack simulation for partitioning and scan-cycle-safe execution, enabling real-time sorting of integer arrays in industrial automation applications.  

*(Focus: PLC-compatible, iterative quicksort with stack management for deterministic performance in control systems.)*

### Prompt:
**Quicksort:**
Implement a self-contained function block in IEC 61131-3 structured text to perform the quicksort algorithm on an array of integers. Ensure efficient partitioning and recursion handling.

**T-A-G:**

🟥 T (Task)

Create a self-contained function block in IEC 61131-3 Structured Text to perform the quicksort algorithm on an array of integers in a PLC environment.

⸻

🟩 A (Action)
	•	Implement the quicksort logic using an iterative, non-recursive approach
	•	Simulate the recursive call stack with two internal arrays: LowStack and HighStack
	•	Manage subarray indices with a StackPointer
	•	Perform partitioning within each subarray using a scheme such as Lomuto or Hoare
	•	Sort the array in place, ensuring memory efficiency and scan-cycle compatibility
	•	Include execution control via inputs like Execute : BOOL and return sorting status with Done : BOOL
	•	Add clear inline comments and structure logic to allow partial execution across scan cycles, if needed

⸻

🟦 G (Goal)

Deliver a modular, PLC-compliant quicksort function block that avoids recursion, maintains performance, and can be safely used for real-time sorting tasks in automation systems. The implementation should be efficient, reusable, and easy to integrate into control applications that require sorted data (e.g., priority ranking, threshold alarms, sensor data processing).

### Generated Code:
**Intent Summary:**  
Create a non-recursive quicksort function block in IEC 61131-3 Structured Text for PLCs, using stack simulation for partitioning and scan-cycle-safe execution, enabling real-time sorting of integer arrays in industrial automation applications.  

*(Focus: PLC-compatible, iterative quicksort with stack management for deterministic performance in control systems.)*
**Quicksort:**
Implement a self-contained function block in IEC 61131-3 structured text to perform the quicksort algorithm on an array of integers. Ensure efficient partitioning and recursion handling.

**T-A-G:**

🟥 T (Task)

Create a self-contained function block in IEC 61131-3 Structured Text to perform the quicksort algorithm on an array of integers in a PLC environment.

⸻

🟩 A (Action)
	•	Implement the quicksort logic using an iterative, non-recursive approach
	•	Simulate the recursive call stack with two internal arrays: LowStack and HighStack
	•	Manage subarray indices with a StackPointer
	•	Perform partitioning within each subarray using a scheme such as Lomuto or Hoare
	•	Sort the array in place, ensuring memory efficiency and scan-cycle compatibility
	•	Include execution control via inputs like Execute : BOOL and return sorting status with Done : BOOL
	•	Add clear inline comments and structure logic to allow partial execution across scan cycles, if needed

⸻

🟦 G (Goal)

Deliver a modular, PLC-compliant quicksort function block that avoids recursion, maintains performance, and can be safely used for real-time sorting tasks in automation systems. The implementation should be efficient, reusable, and easy to integrate into control applications that require sorted data (e.g., priority ranking, threshold alarms, sensor data processing).
FUNCTION_BLOCK QuickSort
VAR_INPUT
    Execute : BOOL; // Trigger sorting on rising edge
    InputArray : ARRAY[1..100] OF INT; // Array to be sorted
END_VAR

VAR_OUTPUT
    SortedArray : ARRAY[1..100] OF INT; // Sorted output array
    Done : BOOL; // TRUE when sorting is complete
    Error : BOOL; // TRUE if an error occurs
END_VAR

VAR
    StackLow : ARRAY[1..50] OF INT; // Stack for low indices
    StackHigh : ARRAY[1..50] OF INT; // Stack for high indices
    StackPointer : INT := 0; // Pointer for stack management
    Temp : INT; // Temporary variable for swapping elements
    i, j : INT; // Loop variables
    PartitionIndex : INT; // Index returned by partitioning step
    Low, High : INT; // Subarray boundaries
    LowStack, HighStack : INT; // Current stack indices
    PartitionValue : INT; // Value used for partitioning
    iStack, jStack : INT; // Stack indices for partitioning
    PartitionFound : BOOL; // Flag to check if partitioning is complete
    iTemp, jTemp : INT; // Temporary variables for stack management
    iStackTop : INT; // Top of the stack
    iStackBottom : INT; // Bottom of the stack
    iStackSize : INT := 50; // Maximum stack size
    iStackUsed : INT := 0; // Current stack usage
    iStackIndex : INT; // Current stack index
    iStackValid : BOOL; // Validity check for stack indices
    iStackValidTemp : BOOL; // Temporary validity check
    iStackValidPrev : BOOL; // Previous validity check
    iStackValidNext : BOOL; // Next validity check
    iStackValidPrevNext : BOOL; // Previous and next validity checks
    iStackValidPrevNextPrev : BOOL; // Previous three validity checks
    iStackValidPrevNextNext : BOOL; // Previous two and next validity checks
    iStackValidPrevNextNextNext : BOOL; // Pre

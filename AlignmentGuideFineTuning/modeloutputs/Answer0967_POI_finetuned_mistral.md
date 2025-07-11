### Intent:
**Intent Summary:**  
Create a reusable Quicksort function block in IEC 61131-3 Structured Text to sort integer arrays iteratively (using stack-based bounds tracking) for PLC applications, with configurable execution control and completion signaling.  

*(Focus: Industrial sorting utility for PLCs, emphasizing iterative implementation, input/output handling, and deterministic execution.)*

### Prompt:
**PID Controller:**
Implement a self-contained function block in IEC 61131-3 structured text to create a PID controller. Include configurable parameters for proportional, integral, and derivative gains, with error handling and tuning capability.

**T-A-G:**

🟥 T (Task)

Implement a self-contained PID controller as a function block in IEC 61131-3 Structured Text for real-time control in PLC-based automation systems.

⸻

🟩 A (Action)
	•	Define the following inputs:
	•	Setpoint, ProcessVariable (for error calculation)
	•	Kp, Ki, Kd (gain tuning parameters)
	•	MinOutput, MaxOutput (output clamping)
	•	Enable, Reset (runtime control flags)
	•	Create the PID logic:
	•	Compute the control error: Error := Setpoint - ProcessVariable
	•	Accumulate the integral term using Ki and DeltaT, with anti-windup logic
	•	Calculate the derivative term from the rate of change of the process variable
	•	Compute the control output and apply output limits
	•	Reset internal states if Reset = TRUE
	•	Use internal memory to track previous values and ensure smooth scan-cycle execution
	•	Include comments for each computation block to improve readability and maintenance

⸻

🟦 G (Goal)

Deliver a robust, tunable, and reusable PID controller function block that performs well in real-time industrial control applications. The block should ensure safe, stable, and accurate output control with built-in safeguards like anti-windup and clamping, making it suitable for integration into any PLC-based closed-loop control system.

### Generated Code:
**Intent Summary:**  
Create a reusable Quicksort function block in IEC 61131-3 Structured Text to sort integer arrays iteratively (using stack-based bounds tracking) for PLC applications, with configurable execution control and completion signaling.  

*(Focus: Industrial sorting utility for PLCs, emphasizing iterative implementation, input/output handling, and deterministic execution.)*
**PID Controller:**
Implement a self-contained function block in IEC 61131-3 structured text to create a PID controller. Include configurable parameters for proportional, integral, and derivative gains, with error handling and tuning capability.

**T-A-G:**

🟥 T (Task)

Implement a self-contained PID controller as a function block in IEC 61131-3 Structured Text for real-time control in PLC-based automation systems.

⸻

🟩 A (Action)
	•	Define the following inputs:
	•	Setpoint, ProcessVariable (for error calculation)
	•	Kp, Ki, Kd (gain tuning parameters)
	•	MinOutput, MaxOutput (output clamping)
	•	Enable, Reset (runtime control flags)
	•	Create the PID logic:
	•	Compute the control error: Error := Setpoint - ProcessVariable
	•	Accumulate the integral term using Ki and DeltaT, with anti-windup logic
	•	Calculate the derivative term from the rate of change of the process variable
	•	Compute the control output and apply output limits
	•	Reset internal states if Reset = TRUE
	•	Use internal memory to track previous values and ensure smooth scan-cycle execution
	•	Include comments for each computation block to improve readability and maintenance

⸻

🟦 G (Goal)

Deliver a robust, tunable, and reusable PID controller function block that performs well in real-time industrial control applications. The block should ensure safe, stable, and accurate output control with built-in safeguards like anti-windup and clamping, making it suitable for integration into any PLC-based closed-loop control system.
FUNCTION_BLOCK QuicksortFB
VAR_INPUT
    InputArray : ARRAY[1..100] OF INT; // Input array to be sorted
    Execute : BOOL;                    // Trigger sorting on rising edge
    Reset : BOOL;                      // Reset internal state
END_VAR

VAR_OUTPUT
    SortedArray : ARRAY[1..100] OF INT; // Sorted array output
    Done : BOOL;                       // TRUE when sorting is complete
    Error : BOOL;                      // TRUE if error occurs
    ErrorCode : DWORD;                 // 0: No error, 1: Invalid input, 2: Stack overflow
END_VAR

VAR
    Stack : ARRAY[1..50] OF INT;        // Stack for storing indices
    Top : INT;                          // Top of the stack
    i, j, pivot, temp : INT;            // Temporary variables
    Low, High : INT;                    // Low and high indices for subarray
    PartitionIndex : INT;               // Index where pivot should be placed
    iStack, jStack : INT;               // Stack indices for i and j
    iStackTop : INT;                    // Top of i stack
    jStackTop : INT;                    // Top of j stack
    iStackBottom : INT;                 // Bottom of i stack
    jStackBottom : INT;                 // Bottom of j stack
    StackSize : INT;                    // Maximum stack size
    StackUsed : INT;                    // Current stack usage
    Partition : INT;                    // Partition index
    PartitionValue : INT;               // Value at partition index
    PartitionIndex : INT;               // Index where pivot should be placed
    iStackTemp : INT;                   // Temporary stack index
    jStackTemp : INT;                   // Temporary stack index
    iStackTemp2 : INT;                  // Temporary stack index
    jStackTemp2 : INT;                  // Temporary stack index
    iStackTemp3 : INT;                  // Temporary stack index
    jStackTemp3 : INT;                  // Temporary stack index
    iStackTemp4 : INT;                  // Temporary stack index

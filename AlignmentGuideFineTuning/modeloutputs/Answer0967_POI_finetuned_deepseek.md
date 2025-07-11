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
FUNCTION_BLOCK Quicksort
VAR_INPUT
    Execute : BOOL; // TRUE to start sorting
    Reset : BOOL; // TRUE to reset the sorting state
END_VAR

VAR_OUTPUT
    Done : BOOL; // TRUE when sorting is complete
    Error : BOOL; // TRUE if an error occurs
    ErrorCode : INT; // 0 = No error, 1 = Stack overflow, 2 = Invalid input
END_VAR

VAR
    Stack : ARRAY[1..100] OF INT; // Stack for recursion
    Top : INT; // Current top of the stack
    InputArray : ARRAY[1..100] OF INT; // Input array to sort
    Length : INT; // Length of the input array
    Temp : INT; // Temporary variable for swapping
    i, j : INT; // Loop counters
    StackIndex : INT; // Index for stack operations
END_VAR

// Initialize variables
Top := 0;
Length := 0;
Error := FALSE;
ErrorCode := 0;
Done := FALSE;

// Reset sorting state
IF Reset THEN
    Top := 0;
    Length := 0;
    Error := FALSE;
    ErrorCode := 0;
    Done := FALSE;
    RETURN;
END_IF;

// Execute sorting if Execute = TRUE
IF Execute THEN
    // Check input validity
    IF Length < 1 OR Length > 100 THEN
        Error := TRUE;
        ErrorCode := 1; // Stack overflow
        RETURN;
    END_IF;

    // Initialize stack and input array
    FOR i := 1 TO Length DO
        Stack[i] := i;
        InputArray[i] := i;
    END_FOR;

    // Sort the array using the quicksort algorithm
    FOR i := 1 TO Length DO
        j := i;
        WHILE j > 1 DO
            j := j - 1;
            IF Stack[j] > Stack[j + 1] THEN
                Temp := Stack[j];
                Stack[j] := Stack[j + 1];
                Stack[j + 1] := Temp;
            END_IF;
        END_WHILE;
    END_FOR;

    //

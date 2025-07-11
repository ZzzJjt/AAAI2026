### Intent:
**Intent Summary:**  
Create a self-contained, iterative Quicksort function block in IEC 61131-3 Structured Text for PLCs, using stack emulation to avoid recursion while sorting arrays in-place with configurable execution control and state tracking.  

*(Focus: Non-recursive, scan-cycle-safe sorting for industrial automation.)*

### Prompt:
**Timer:**
Implement a self-contained function block in IEC 61131-3 structured text to create a timer. Include configurable time duration, start/stop controls, and timeout handling.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

Timers are essential in industrial automation for sequencing operations, delays, and safety checks. However, relying on fixed or external timers can limit flexibility and reusability. A timer that lacks configurable duration, start/stop control, or timeout indication can lead to rigid control logic and poor maintainability in PLC systems.

⸻

🟩 A (After) – The Desired Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text that acts as a flexible timer. The function block should:
	•	Allow users to configure the time duration
	•	Support Start and Stop signals for runtime control
	•	Track elapsed time and indicate when the timer has timed out
	•	Provide output flags for Running, Done, and optionally RemainingTime

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block with inputs:
	•	Start : BOOL
	•	Stop : BOOL
	•	PresetTime : TIME
	2.	Use internal variables to:
	•	Store StartTime and ElapsedTime
	•	Reset when Stop = TRUE
	•	Accumulate time only when Start = TRUE and Stop = FALSE
	3.	Provide outputs:
	•	Running : BOOL – active while the timer is counting
	•	Done : BOOL – TRUE when elapsed time ≥ preset time
	•	RemainingTime : TIME – optional, shows remaining time until done
	4.	Ensure the timer is scan-cycle safe, reusable, and well-commented

### Generated Code:
**Intent Summary:**  
Create a self-contained, iterative Quicksort function block in IEC 61131-3 Structured Text for PLCs, using stack emulation to avoid recursion while sorting arrays in-place with configurable execution control and state tracking.  

*(Focus: Non-recursive, scan-cycle-safe sorting for industrial automation.)*
**Timer:**
Implement a self-contained function block in IEC 61131-3 structured text to create a timer. Include configurable time duration, start/stop controls, and timeout handling.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

Timers are essential in industrial automation for sequencing operations, delays, and safety checks. However, relying on fixed or external timers can limit flexibility and reusability. A timer that lacks configurable duration, start/stop control, or timeout indication can lead to rigid control logic and poor maintainability in PLC systems.

⸻

🟩 A (After) – The Desired Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text that acts as a flexible timer. The function block should:
	•	Allow users to configure the time duration
	•	Support Start and Stop signals for runtime control
	•	Track elapsed time and indicate when the timer has timed out
	•	Provide output flags for Running, Done, and optionally RemainingTime

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block with inputs:
	•	Start : BOOL
	•	Stop : BOOL
	•	PresetTime : TIME
	2.	Use internal variables to:
	•	Store StartTime and ElapsedTime
	•	Reset when Stop = TRUE
	•	Accumulate time only when Start = TRUE and Stop = FALSE
	3.	Provide outputs:
	•	Running : BOOL – active while the timer is counting
	•	Done : BOOL – TRUE when elapsed time ≥ preset time
	•	RemainingTime : TIME – optional, shows remaining time until done
	4.	Ensure the timer is scan-cycle safe, reusable, and well-commented for integration into control programs
(* IEC 61131-3 Structured Text: Quicksort Function Block *)
(* Purpose: Sorts an array in-place using non-recursive quicksort *)

FUNCTION_BLOCK QuicksortFB
VAR_INPUT
    Execute : BOOL;                  (* TRUE to execute sorting *)
    Array : ARRAY[1..100] OF INT;    (* Array to be sorted *)
    StartIndex : INT;                (* Index of first element to sort *)
    EndIndex : INT;                  (* Index of last element to sort *)
END_VAR

VAR_OUTPUT
    Sorted : BOOL;                   (* TRUE if sorting is complete *)
    Done : BOOL;                     (* TRUE when sorting is complete *)
    Error : BOOL;                    (* TRUE if error occurs *)
    ErrorID : DWORD;                 (* 0: No error, 1: Invalid input *)
    Message : STRING[80];            (* Error message *)
END_VAR

VAR
    Stack : ARRAY[1..10] OF INT;     (* Stack for recursion emulation *)
    Top : INT;                       (* Top of the stack *)
    PivotIndex : INT;                (* Index of pivot element *)
    Left : INT;                      (* Left index for partitioning *)
    Right : INT;                     (* Right index for partitioning *)
    i : INT;                         (* Loop variable *)
    Temp : INT;                      (* Temporary variable for swapping *)
    PartitionIndex : INT;            (* Index of partition element *)
    PartitionValue : INT;            (* Value of partition element *)
    Swap : BOOL;                     (* Flag to swap elements *)
    ValidInput : BOOL;               (* Flag for valid input *)
    iStack : ARRAY[1..10] OF INT;    (* Stack for stack emulation *)
    iTop : INT;                      (* Top of the stack for stack emulation *)
    iStack2 : ARRAY[1..10] OF INT;   (* Stack for stack emulation *)
    iTop2 : INT;                     (* Top of the stack for stack emulation *)
    iStack3 : ARRAY[1

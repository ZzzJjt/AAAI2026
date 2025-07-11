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
	4.	Ensure the timer is scan-cycle safe, reusable, and well-commented for clarity.
(* IEC 61131-3 Structured Text: Quicksort Function Block *)
(* Purpose: Implements a non-recursive, in-place quicksort algorithm *)

FUNCTION_BLOCK Quicksort
VAR_INPUT
    Execute : BOOL; (* TRUE to start sorting *)
    Array : ARRAY[1..100] OF INT; (* Input array to sort *)
END_VAR

VAR_OUTPUT
    Done : BOOL; (* TRUE when sorting is complete *)
    Error : BOOL; (* TRUE if an error occurs *)
    SortingProgress : REAL; (* Progress between 0.0 and 1.0 *)
    ArraySorted : ARRAY[1..100] OF INT; (* Sorted array *)
END_VAR

VAR
    i, j, pivot, temp : INT;
    stack : ARRAY[1..100] OF INT; (* Stack for partitioning *)
    stackTop : INT; (* Top of the stack *)
    stackSize : INT; (* Number of elements in the stack *)
    sorted : ARRAY[1..100] OF BOOL; (* Array to track sorted status *)
    sortedIndex : INT; (* Index of the last sorted element *)
    sortedCount : INT; (* Number of sorted elements *)
    sortedIndexMax : INT; (* Maximum index of the sorted array *)
    sortedCountMax : INT; (* Maximum number of sorted elements *)
    sortedIndexMin : INT; (* Minimum index of the sorted array *)
    sortedCountMin : INT; (* Minimum number of sorted elements *)
    sortedIndexMaxPrev : INT; (* Previous max index *)
    sortedCountMaxPrev : INT; (* Previous max count *)
    sortedIndexMinPrev : INT; (* Previous min index *)
    sortedCountMinPrev : INT; (* Previous min count *)
    sortedIndexMaxPrevPrev : INT; (* Previous previous max index *)
    sortedCountMaxPrevPrev : INT; (* Previous previous max count *)
    sortedIndexMinPrevPrev : INT; (* Previous previous min index *)
    sortedCountMinPrevPrev : INT; (* Previous previous min count *)
    sortedIndexMaxPrevPrevPrev : INT; (* Previous previous previous max index *)
    sortedCountMaxPrevPrevPrev : INT; (* Previous previous previous max count *)
    sortedIndexMinPrevPrevPrev : INT; (* Previous previous

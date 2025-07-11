### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block for an iterative heapsort algorithm that sorts integer arrays (1–100 elements) with configurable size, execution control, and error handling for industrial PLC applications.  

*(Focus: Configurable sorting, iterative design for PLCs, and safety/output flags.)*

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
Create a reusable IEC 61131-3 structured text function block for an iterative heapsort algorithm that sorts integer arrays (1–100 elements) with configurable size, execution control, and error handling for industrial PLC applications.  

*(Focus: Configurable sorting, iterative design for PLCs, and safety/output flags.)*
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
(* IEC 61131-3 Structured Text: Heapsort Function Block *)
(* Purpose: Sorts an array of integers using iterative heapsort algorithm *)

FUNCTION_BLOCK Heapsort
VAR_INPUT
    Execute : BOOL;                  (* TRUE to execute sorting *)
    InputArray : ARRAY[1..100] OF INT; (* Array to be sorted *)
    ArraySize : INT;                 (* Number of elements to sort, 1 to 100 *)
END_VAR

VAR_OUTPUT
    SortedArray : ARRAY[1..100] OF INT; (* Sorted array output *)
    Done : BOOL;                     (* TRUE when sorting is complete *)
    Error : BOOL;                    (* TRUE if invalid input *)
    ErrorID : DWORD;                 (* 0: No error, 1: Invalid size, 2: Invalid execute *)
END_VAR

VAR
    HeapSize : INT;                  (* Current heap size *)
    i, j, temp : INT;                (* Loop variables *)
    Parent, Child : INT;              (* Heap node indices *)
    MaxIndex : INT;                   (* Index of maximum element in subtree *)
    iMax : INT;                       (* Index of maximum element in heap *)
    Heapify : BOOL;                   (* TRUE to heapify subtree *)
    HeapifyRecursive : BOOL;         (* TRUE for recursive heapify *)
    HeapifyDone : BOOL;              (* TRUE when heapify is complete *)
    HeapifyError : BOOL;             (* TRUE if heapify fails *)
    HeapifyErrorID : DWORD;          (* 0: No error, 1: Invalid size, 2: Invalid execute *)
END_VAR

(* Reset outputs *)
Done := FALSE;
Error := FALSE;
ErrorID := 0;

(* Check inputs *)
IF NOT Execute THEN
    Done := FALSE;
    Error := FALSE;
    ErrorID := 0;
    RETURN;
END_IF;

IF ArraySize < 1 OR ArraySize > 100 THEN
    Done := FALSE;
    Error

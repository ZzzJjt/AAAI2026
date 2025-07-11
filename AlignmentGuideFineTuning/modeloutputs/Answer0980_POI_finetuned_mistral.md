### Intent:
The task is to implement a reusable timer function block in IEC 61131-3 Structured Text for PLC systems, featuring configurable timing, start/stop controls, and status outputs for automation sequencing and timeout handling.  

(Note: The provided code actually shows a heapsort implementation rather than a timer, but the intent summary is based on the original timer task description in the T-A-G section.)

### Prompt:
**Timer:**
Implement a self-contained function block in IEC 61131-3 structured text to create a timer. Include configurable time duration, start/stop controls, and timeout handling.


**T-A-G:**

🟥 T (Task)

Implement a self-contained timer function block in IEC 61131-3 Structured Text for use in PLC-based control systems.

⸻

🟩 A (Action)
	•	Define the timer with the following inputs:
	•	Start : BOOL — triggers the timer
	•	Stop : BOOL — resets or halts the timer
	•	PresetTime : TIME — sets the duration to time
	•	Create internal logic to:
	•	Detect the rising edge of the Start input
	•	Capture and update elapsed time using system clock functions
	•	Stop the timer if Stop = TRUE
	•	Provide outputs such as:
	•	Running : BOOL — indicates the timer is active
	•	Done : BOOL — becomes TRUE when the preset time is reached
	•	Optionally, RemainingTime : TIME — time left before timeout
	•	Ensure the function block is modular, edge-triggered, and safe for repeated use across scan cycles

⸻

🟦 G (Goal)

Deliver a flexible, reusable timer block that can be integrated into various automation routines for delay control, sequencing, or timeout handling. The timer should be easy to configure, scan-cycle safe, and support both momentary and continuous triggering logic.

### Generated Code:
The task is to implement a reusable timer function block in IEC 61131-3 Structured Text for PLC systems, featuring configurable timing, start/stop controls, and status outputs for automation sequencing and timeout handling.  

(Note: The provided code actually shows a heapsort implementation rather than a timer, but the intent summary is based on the original timer task description in the T-A-G section.)
**Timer:**
Implement a self-contained function block in IEC 61131-3 structured text to create a timer. Include configurable time duration, start/stop controls, and timeout handling.


**T-A-G:**

🟥 T (Task)

Implement a self-contained timer function block in IEC 61131-3 Structured Text for use in PLC-based control systems.

⸻

🟩 A (Action)
	•	Define the timer with the following inputs:
	•	Start : BOOL — triggers the timer
	•	Stop : BOOL — resets or halts the timer
	•	PresetTime : TIME — sets the duration to time
	•	Create internal logic to:
	•	Detect the rising edge of the Start input
	•	Capture and update elapsed time using system clock functions
	•	Stop the timer if Stop = TRUE
	•	Provide outputs such as:
	•	Running : BOOL — indicates the timer is active
	•	Done : BOOL — becomes TRUE when the preset time is reached
	•	Optionally, RemainingTime : TIME — time left before timeout
	•	Ensure the function block is modular, edge-triggered, and safe for repeated use across scan cycles

⸻

🟦 G (Goal)

Deliver a flexible, reusable timer block that can be integrated into various automation routines for delay control, sequencing, or timeout handling. The timer should be easy to configure, scan-cycle safe, and support both momentary and continuous triggering logic.
(* Heapsort Function Block Implementation in IEC 61131-3 Structured Text *)
(* Sorts an array of integers using the HeapSort algorithm *)
(* Designed for PLC-based control systems with scan-cycle safety *)

FUNCTION_BLOCK HeapSort
VAR_INPUT
    Execute : BOOL;                  (* TRUE to start sorting *)
    InputArray : ARRAY[1..100] OF INT; (* Array to be sorted *)
    ArraySize : INT;                 (* Number of elements to sort, 1 to 100 *)
END_VAR

VAR_OUTPUT
    SortedArray : ARRAY[1..100] OF INT; (* Sorted array output *)
    Done : BOOL;                     (* TRUE when sorting is complete *)
    Error : BOOL;                    (* TRUE if invalid input *)
END_VAR

VAR
    HeapSize : INT;                  (* Current heap size *)
    i, j, root, temp : INT;          (* Loop variables *)
    Heapify : BOOL;                  (* TRUE during heapify operation *)
    HeapTop : INT;                   (* Index of the top element in the heap *)
    HeapBottom : INT;                 (* Index of the bottom element in the heap *)
    ValidInput : BOOL;               (* Input validation flag *)
END_VAR

(* Initialize outputs *)
Done := FALSE;
Error := FALSE;

(* Input validation *)
IF Execute AND NOT ValidInput THEN
    (* Check for valid input *)
    ValidInput := (ArraySize >= 1) AND (ArraySize <= 100);
    Error := NOT ValidInput;
    Done := FALSE;
    RETURN;
END_IF;

(* Reset outputs when not executing *)
IF NOT Execute THEN
    Done := FALSE;
    FOR i := 1 TO 100 DO
        SortedArray[i] := InputArray[i];
    END_FOR;
    RETURN;
END_IF;

(* Initialize heap *)
HeapSize := ArraySize;
HeapTop := 1;
HeapBottom := HeapSize;

(* Main sorting loop *)
Heapify := TRUE;
WHILE

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
	4.	Ensure the timer is scan-cycle safe, reusable, and well-commented for clarity.
(* IEC 61131-3 Structured Text: Heapsort Function Block *)
(* Purpose: Implements an iterative heapsort algorithm for integer arrays *)

FUNCTION_BLOCK HeapSort
VAR_INPUT
    Execute : BOOL;                  (* TRUE to start sorting *)
    InputArray : ARRAY[1..100] OF INT; (* Input array to sort *)
END_VAR

VAR_OUTPUT
    Done : BOOL;                     (* TRUE when sorting is complete *)
    Error : BOOL;                    (* TRUE if an error occurs *)
    ErrorText : STRING[200];         (* Error message *)
    OutputArray : ARRAY[1..100] OF INT; (* Sorted array *)
    Running : BOOL;                  (* TRUE while sorting *)
    RemainingTime : TIME;            (* Optional: remaining time until Done *)
END_VAR

VAR
    i, j, temp, heapSize : INT;      (* Loop counters and heap size *)
    heap : ARRAY[1..100] OF INT;    (* Heap array *)
    heap_index : ARRAY[1..100] OF INT; (* Heap index array *)
    heap_ptr : ARRAY[1..100] OF INT; (* Heap pointer array *)
    heap_max_index : INT;           (* Max heap index *)
    heap_max_ptr : INT;             (* Max heap pointer *)
    heap_ptr_index : INT;           (* Heap pointer index *)
    heap_ptr_max_index : INT;       (* Max heap pointer index *)
    heap_ptr_max_index_prev : INT;  (* Previous max heap pointer index *)
    heap_ptr_index_prev : INT;      (* Previous heap pointer index *)
    heap_ptr_index_prev_prev : INT; (* Previous previous max heap pointer index *)
    heap_ptr_index_prev_prev_prev : INT; (* Previous previous previous max heap pointer index *)
    heap_ptr_index_prev_prev_prev_prev : INT; (* Previous previous previous previous max heap pointer index *)
    heap_ptr_index_prev_prev_prev_prev_prev : INT; (* Previous previous previous previous previous max heap pointer index *)
    heap_ptr_index_prev_prev_prev_prev_prev_prev

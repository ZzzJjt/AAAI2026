### Intent:
**Intent Summary:**  
Create a structured-text PLC function block for an industrial timer that handles edge-triggered start/stop, tracks elapsed/remaining time, and ensures robust timeout control with input validation and safety checks.  

*(Focus: Code generation for a reliable timer in automation systems, prioritizing edge detection, system-clock precision, and fail-safe logic.)*

### Prompt:
**P-ID Steam Water Cycle:**

Create a P&I diagram in textual notation for a steam water cycle in a power plant. Include equipment, instrumentation, piping, and control loops. Provide concrete tag names.


**T-A-G:**

🟥 T (Task)

Create a text-based Piping and Instrumentation Diagram (P&ID) for a steam-water cycle in a power plant.

⸻

🟩 A (Action)
	•	Represent all major equipment involved in the steam-water cycle, such as feedwater pumps, boiler, steam drum, condenser, etc.
	•	Include relevant instrumentation and control loops, such as flow transmitters (FT), level transmitters (LT), pressure transmitters (PT), controllers (FIC, LIC), and control valves (FCV, LCV).
	•	Use clear tag names (e.g., FT101, FCV102) based on industry standards.
	•	Show piping and flow direction using arrows (-->) and organize elements in process order.
	•	Format the diagram in clean plain-text notation, using indentation and alignment to convey process structure and control logic.

⸻

🟦 G (Goal)

Provide a structured, readable, and logic-complete textual P&ID that clearly documents the flow, control strategy, and tag references of a steam-water cycle, enabling use in early-stage engineering, PLC programming, or control narrative development when graphics are unavailable.

### Generated Code:
**Intent Summary:**  
Create a structured-text PLC function block for an industrial timer that handles edge-triggered start/stop, tracks elapsed/remaining time, and ensures robust timeout control with input validation and safety checks.  

*(Focus: Code generation for a reliable timer in automation systems, prioritizing edge detection, system-clock precision, and fail-safe logic.)*
**P-ID Steam Water Cycle:**

Create a P&I diagram in textual notation for a steam water cycle in a power plant. Include equipment, instrumentation, piping, and control loops. Provide concrete tag names.


**T-A-G:**

🟥 T (Task)

Create a text-based Piping and Instrumentation Diagram (P&ID) for a steam-water cycle in a power plant.

⸻

🟩 A (Action)
	•	Represent all major equipment involved in the steam-water cycle, such as feedwater pumps, boiler, steam drum, condenser, etc.
	•	Include relevant instrumentation and control loops, such as flow transmitters (FT), level transmitters (LT), pressure transmitters (PT), controllers (FIC, LIC), and control valves (FCV, LCV).
	•	Use clear tag names (e.g., FT101, FCV102) based on industry standards.
	•	Show piping and flow direction using arrows (-->) and organize elements in process order.
	•	Format the diagram in clean plain-text notation, using indentation and alignment to convey process structure and control logic.

⸻

🟦 G (Goal)

Provide a structured, readable, and logic-complete textual P&ID that clearly documents the flow, control strategy, and tag references of a steam-water cycle, enabling use in early-stage engineering, PLC programming, or control narrative development when graphics are unavailable.
(* IEC 61131-3 Structured Text Function Block for an Industrial Timer *)
(* Handles edge-triggered start/stop, tracks elapsed/remaining time, and includes input validation and safety checks *)

FUNCTION_BLOCK TimerFB
VAR_INPUT
    Start : BOOL;                  (* TRUE to start the timer *)
    Stop : BOOL;                   (* TRUE to stop the timer *)
    Reset : BOOL;                  (* TRUE to reset the timer *)
END_VAR

VAR_OUTPUT
    Elapsed : TIME;                (* Time elapsed since the last start *)
    Remaining : TIME;              (* Remaining time until the next stop *)
    Done : BOOL;                   (* TRUE when the timer is done *)
    Error : BOOL;                  (* TRUE if the timer is invalid *)
END_VAR

VAR
    StartTime : TIME;              (* Time when the timer was started *)
    StopTime : TIME;               (* Time when the timer was stopped *)
    ResetTime : TIME;              (* Time when the timer was reset *)
    ElapsedTime : TIME;            (* Time elapsed since the last start *)
    RemainingTime : TIME;          (* Remaining time until the next stop *)
    DoneFlag : BOOL;               (* Flag indicating that the timer is done *)
    ErrorFlag : BOOL;              (* Flag indicating that the timer is invalid *)
END_VAR

(* Initialize the timer when it is created *)
IF NOT DoneFlag THEN
    (* Reset the timer if it is reset *)
    IF Reset THEN
        StartTime := TIME(0, 0, 0);
        StopTime := TIME(0, 0, 0);
        ResetTime := TIME(0, 0, 0);
        ElapsedTime := TIME(0, 0, 0);
        RemainingTime := TIME(0, 0, 0);
        DoneFlag := FALSE;
        ErrorFlag := FALSE;
    ELSE
        (* Check if the timer is running *)
        IF Start THEN
            (* Calculate the elapsed time since the last start *)
            ElapsedTime := StopTime - StartTime;
            (* Calculate the remaining time until the next stop *)
            RemainingTime := StopTime - (StartTime + ElapsedTime);
            (* Check if the timer is done *)
            DoneFlag := TRUE;
            (*

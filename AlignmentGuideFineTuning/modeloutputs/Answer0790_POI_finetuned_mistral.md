### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 timer function block with configurable duration, start/stop controls, and real-time status outputs (running, done, remaining time) for industrial PLC applications.  

*(Focus: Modularity, scan-cycle efficiency, and precise timing logic.)*

### Prompt:
**Timer:**
Implement a self-contained function block in IEC 61131-3 structured text to create a timer. Include configurable time duration, start/stop controls, and timeout handling.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC programmer tasked with implementing a customizable timer function block using IEC 61131-3 Structured Text, suitable for precise and reusable industrial control logic.

⸻

🟩 T (Task) – Define the Objective

Develop a self-contained timer function block that includes:
	•	A configurable time duration input (PresetTime : TIME)
	•	Start and Stop Boolean inputs to control timing behavior
	•	Accurate elapsed time tracking
	•	Output flags to indicate timer status:
	•	Running : BOOL — timer is active
	•	Done : BOOL — timer has reached the preset time
	•	Optionally, RemainingTime : TIME

The timer must operate in a scan-cycle-compatible and modular way, with clean state handling and timeout logic.

⸻

🟧 F (Format) – Specify the Output Format

Provide a complete IEC 61131-3 Structured Text function block that includes:
	•	Inputs:
	•	Start : BOOL
	•	Stop : BOOL
	•	PresetTime : TIME
	•	Outputs:
	•	Running : BOOL
	•	Done : BOOL
	•	RemainingTime : TIME (optional)
	•	Internal Variables:
	•	StartTime : TIME
	•	ElapsedTime : TIME
	•	TriggerEdge : BOOL
	•	Logic Flow:
	•	Edge detection for Start
	•	Reset logic on Stop
	•	Time comparison to set Done and clear Running

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 timer function block with configurable duration, start/stop controls, and real-time status outputs (running, done, remaining time) for industrial PLC applications.  

*(Focus: Modularity, scan-cycle efficiency, and precise timing logic.)*
**Timer:**
Implement a self-contained function block in IEC 61131-3 structured text to create a timer. Include configurable time duration, start/stop controls, and timeout handling.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC programmer tasked with implementing a customizable timer function block using IEC 61131-3 Structured Text, suitable for precise and reusable industrial control logic.

⸻

🟩 T (Task) – Define the Objective

Develop a self-contained timer function block that includes:
	•	A configurable time duration input (PresetTime : TIME)
	•	Start and Stop Boolean inputs to control timing behavior
	•	Accurate elapsed time tracking
	•	Output flags to indicate timer status:
	•	Running : BOOL — timer is active
	•	Done : BOOL — timer has reached the preset time
	•	Optionally, RemainingTime : TIME

The timer must operate in a scan-cycle-compatible and modular way, with clean state handling and timeout logic.

⸻

🟧 F (Format) – Specify the Output Format

Provide a complete IEC 61131-3 Structured Text function block that includes:
	•	Inputs:
	•	Start : BOOL
	•	Stop : BOOL
	•	PresetTime : TIME
	•	Outputs:
	•	Running : BOOL
	•	Done : BOOL
	•	RemainingTime : TIME (optional)
	•	Internal Variables:
	•	StartTime : TIME
	•	ElapsedTime : TIME
	•	TriggerEdge : BOOL
	•	Logic Flow:
	•	Edge detection for Start
	•	Reset logic on Stop
	•	Time comparison to set Done and clear Running
	•	Calculate RemainingTime if Done is TRUE
	•	Commented code with explanation of each step
(* IEC 61131-3 Structured Text: Timer Function Block *)
(* Purpose: Provides a reusable timer with configurable duration, start/stop control, and status outputs *)

FUNCTION_BLOCK Timer
VAR_INPUT
    Start : BOOL;                  (* TRUE to start the timer *)
    Stop : BOOL;                   (* TRUE to stop the timer *)
    PresetTime : TIME;             (* Time duration to be timed, e.g., T#5s *)
END_VAR

VAR_OUTPUT
    Running : BOOL;                (* TRUE while the timer is active *)
    Done : BOOL;                   (* TRUE when the timer reaches PresetTime *)
    RemainingTime : TIME;          (* Remaining time until PresetTime *)
    Error : BOOL;                  (* TRUE if PresetTime is invalid *)
END_VAR

VAR
    StartTime : TIME;              (* Time when the timer starts *)
    ElapsedTime : TIME;            (* Time elapsed since the timer started *)
    TriggerEdge : BOOL;            (* Edge detection for Start *)
END_VAR

(* Initialize outputs *)
Running := FALSE;
Done := FALSE;
RemainingTime := T#0s;
Error := FALSE;

(* Main logic *)
IF NOT Stop THEN
    (* Edge detection for Start *)
    TriggerEdge := Start AND NOT TriggerEdge;

    (* Start the timer on rising edge of Start *)
    IF TriggerEdge THEN
        StartTime := TON;
        ElapsedTime := T#0s;
        Running := TRUE;
    END_IF;

    (* Stop the timer on rising edge of Stop *)
    IF Stop THEN
        Running := FALSE;
        Done := FALSE;
        ElapsedTime := T#0s;
    END_IF;

    (* Check if the timer has reached PresetTime *)
    IF Running AND ElapsedTime >= PresetTime THEN
        Done := TRUE;
        Running := FALSE;
    ELSE
        (* Update elapsed time *)
        ElapsedTime := TON - Start

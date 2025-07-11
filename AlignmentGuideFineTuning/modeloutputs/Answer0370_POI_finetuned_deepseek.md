### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text timer function block with configurable duration, start/stop controls, elapsed time tracking, and timeout flags for precise PLC automation tasks.

### Prompt:
**Timer:**
Implement a self-contained function block in IEC 61131-3 structured text to create a timer. Include configurable time duration, start/stop controls, and timeout handling.


**C-A-R-E:**

🟥 C (Context) – Background Situation

Timers are fundamental building blocks in PLC programming, used for delays, sequencing, and interlock conditions. However, many standard timers are rigid or lack modular control logic, making it difficult to customize behavior such as dynamically changing durations or adding start/stop logic. For reusable automation code, a flexible and configurable Structured Text timer block is preferred.

⸻

🟩 A (Action) – Task to Perform

Design a self-contained timer function block in IEC 61131-3 Structured Text that includes:
	•	Configurable time duration via PresetTime : TIME
	•	Start and Stop inputs to control execution dynamically
	•	Elapsed time tracking with a built-in timeout mechanism
	•	Internal logic to handle rising-edge detection and accurate scan-cycle timing
	•	Output flags including:
	•	Running : BOOL – TRUE when counting
	•	Done : BOOL – TRUE when the timer completes
	•	Optionally, RemainingTime : TIME

⸻

🟨 R (Result) – Expected Outcome

The outcome will be a modular, reusable timer block that:
	•	Integrates cleanly into any PLC program requiring timing functionality
	•	Enables dynamic control with start/stop inputs
	•	Offers scan-cycle accuracy and proper handling of timer overflow
	•	Can be used across a wide range of automation tasks (e.g., heating cycles, alarms, delays)

⸻

🟦 E (Example) – Concrete Illustration

Simplified logic:

IF Start AND NOT Stop THEN
    IF NOT Running THEN
        StartTime := TIME(); // Capture current time
        Running := TRUE;
    END_IF;

    ElapsedTime := TIME() - StartTime;

    IF ElapsedTime >= PresetTime THEN
        Done := TRUE;
        Running := FALSE;
    END_IF;
ELSIF Stop THEN
    Running := FALSE;
    Done := FALSE;
    ElapsedTime := T#0s;
END_IF;

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text timer function block with configurable duration, start/stop controls, elapsed time tracking, and timeout flags for precise PLC automation tasks.
**Timer:**
Implement a self-contained function block in IEC 61131-3 structured text to create a timer. Include configurable time duration, start/stop controls, and timeout handling.


**C-A-R-E:**

🟥 C (Context) – Background Situation

Timers are fundamental building blocks in PLC programming, used for delays, sequencing, and interlock conditions. However, many standard timers are rigid or lack modular control logic, making it difficult to customize behavior such as dynamically changing durations or adding start/stop logic. For reusable automation code, a flexible and configurable Structured Text timer block is preferred.

⸻

🟩 A (Action) – Task to Perform

Design a self-contained timer function block in IEC 61131-3 Structured Text that includes:
	•	Configurable time duration via PresetTime : TIME
	•	Start and Stop inputs to control execution dynamically
	•	Elapsed time tracking with a built-in timeout mechanism
	•	Internal logic to handle rising-edge detection and accurate scan-cycle timing
	•	Output flags including:
	•	Running : BOOL – TRUE when counting
	•	Done : BOOL – TRUE when the timer completes
	•	Optionally, RemainingTime : TIME

⸻

🟨 R (Result) – Expected Outcome

The outcome will be a modular, reusable timer block that:
	•	Integrates cleanly into any PLC program requiring timing functionality
	•	Enables dynamic control with start/stop inputs
	•	Offers scan-cycle accuracy and proper handling of timer overflow
	•	Can be used across a wide range of automation tasks (e.g., heating cycles, alarms, delays)

⸻

🟦 E (Example) – Concrete Illustration

Simplified logic:

IF Start AND NOT Stop THEN
    IF NOT Running THEN
        StartTime := TIME(); // Capture current time
        Running := TRUE;
    END_IF;

    ElapsedTime := TIME() - StartTime;

    IF ElapsedTime >= PresetTime THEN
        Done := TRUE;
        Running := FALSE;
    END_IF;
ELSIF Stop THEN
    Running := FALSE;
    Done := FALSE;
    ElapsedTime := T#0s;
END_IF;
FUNCTION_BLOCK TimerFB
VAR_INPUT
    Start : BOOL;
    Stop : BOOL;
    PresetTime : TIME; // Time in seconds
END_VAR

VAR_OUTPUT
    Running : BOOL;
    Done : BOOL;
    RemainingTime : TIME;
    Timeout : BOOL;
END_VAR

VAR
    StartTime : TIME;
    ElapsedTime : TIME;
    PrevTime : TIME;
    PrevStop : BOOL;
    PrevStart : BOOL;
    TimeoutFlag : BOOL;
END_VAR

METHOD Initialize : BOOL
VAR_INPUT
    PresetTime : TIME;
END_VAR

VAR_OUTPUT
    Done : BOOL;
    Timeout : BOOL;
END_VAR

IF NOT Done THEN
    StartTime := TIME();
    Running := TRUE;
    Done := FALSE;
    Timeout := FALSE;
END_IF;

METHOD Update : BOOL
VAR_INPUT
    Start : BOOL;
    Stop : BOOL;
END_VAR

VAR
    PrevStop : BOOL := Stop;
    PrevStart : BOOL := Start;
END_VAR

IF Start AND NOT Stop THEN
    IF NOT Running THEN
        StartTime := TIME();
        Running := TRUE;
    END_IF;

    ElapsedTime := TIME() - StartTime;

    IF ElapsedTime >= PresetTime THEN
        Done := TRUE;
        Running := FALSE;
        Timeout := TRUE;
    END_IF;
ELSIF Stop THEN
    Running := FALSE;
    Done := FALSE;
    ElapsedTime := T#0s;
    Timeout := FALSE;
    PrevStop := Stop;
    PrevStart := NOT Stop;
END_IF;

METHOD Reset : BOOL
VAR_INPUT
    PresetTime : TIME;
END_VAR

IF NOT Done THEN
    StartTime := TIME();
    Running := TRUE;
    Done := FALSE;
    Timeout := FALSE;
END_IF;

METHOD GetRemainingTime : TIME
VAR
    ElapsedTime : TIME;
END_VAR

IF NOT Done THEN
    ElapsedTime := TIME() - StartTime;
    IF ElapsedTime >= PresetTime THEN
        ElapsedTime := PresetTime - 1s;

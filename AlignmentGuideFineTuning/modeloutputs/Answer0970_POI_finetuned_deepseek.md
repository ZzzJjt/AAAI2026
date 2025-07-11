### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text timer function block with configurable duration, start/stop controls, and timeout outputs for PLC-based automation tasks.  

*(Focus: Modular timer logic for delays/sequencing, edge-triggered operation, and scan-cycle safety.)*

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
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text timer function block with configurable duration, start/stop controls, and timeout outputs for PLC-based automation tasks.  

*(Focus: Modular timer logic for delays/sequencing, edge-triggered operation, and scan-cycle safety.)*
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
FUNCTION_BLOCK Timer
VAR_INPUT
    Start : BOOL;
    Stop : BOOL;
    PresetTime : TIME;
END_VAR

VAR_OUTPUT
    Running : BOOL;
    Done : BOOL;
    RemainingTime : TIME;
END_VAR

VAR
    StartTime : TIME;
    ElapsedTime : TIME;
    TimerRunning : BOOL;
END_VAR

METHOD Initialize : VOID
BEGIN
    StartTime := NOW();
    ElapsedTime := TIME();
    TimerRunning := FALSE;
END_METHOD

METHOD Update : VOID
BEGIN
    IF Start THEN
        TimerRunning := TRUE;
    ELSIF Stop THEN
        TimerRunning := FALSE;
    END_IF;

    IF TimerRunning THEN
        ElapsedTime := NOW() - StartTime;
        IF ElapsedTime >= PresetTime THEN
            Done := TRUE;
            RemainingTime := TIME();
        END_IF;
    END_IF;
END_METHOD

METHOD Reset : VOID
BEGIN
    ElapsedTime := TIME();
    Done := FALSE;
    RemainingTime := TIME();
    TimerRunning := FALSE;
END_METHOD

METHOD GetRemainingTime : TIME
BEGIN
    IF TimerRunning AND Done THEN
        RemainingTime := PresetTime - ElapsedTime;
    ELSE
        RemainingTime := TIME();
    END_IF;
END_METHOD
END_FUNCTION_BLOCK

// Example usage:
// Start Timer
//   Start := TRUE;
//   PresetTime := PT(5.0); // 5 seconds
//   Done := FALSE;
//   RemainingTime := PT(0.0);
// End
// Stop Timer
//   Stop := TRUE;
//   Done := TRUE;
//   RemainingTime := PT(0.0);
// End
// Reset Timer
//   Reset;
// End
// Get Remaining Time
//   GetRemainingTime;
// End
// Configure for edge-triggered operation
//   Start := Rising_Edge(Start);
//   Stop := Rising_Edge(Stop);
//   Done := Rising_Edge(Done);
//   RemainingTime := Rising_Edge(RemainingTime);
// End
// Configure for scan-cycle

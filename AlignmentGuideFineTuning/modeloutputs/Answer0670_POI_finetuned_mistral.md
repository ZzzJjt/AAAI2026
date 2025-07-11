### Intent:
**Intent Summary:**  
Create a reusable, scan-cycle-safe timer function block in IEC 61131-3 Structured Text with configurable duration, start/stop controls, and real-time status outputs (running, done, remaining time) for precise industrial automation sequencing.  

*(Focus: Modular timer for PLCs, replacing standard TON/TP with tailored functionality.)*

### Prompt:
**Timer:**
Implement a self-contained function block in IEC 61131-3 structured text to create a timer. Include configurable time duration, start/stop controls, and timeout handling.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC developer creating a flexible and reusable timer function block in IEC 61131-3 Structured Text for use in industrial automation programs.

⸻

🟩 I (Input) – Information Provided

The timer must:
	•	Accept a configurable input PresetTime : TIME
	•	Be controlled with Start and Stop : BOOL inputs
	•	Track elapsed time internally
	•	Output status flags:
	•	Running : BOOL — timer is active
	•	Done : BOOL — timer reached its preset
	•	RemainingTime : TIME (optional)
	•	Be self-contained, scan-cycle safe, and suitable for ladder logic replacement

⸻

🟧 S (Steps) – Steps to Perform
	1.	Define the function block interface with inputs and outputs as described
	2.	Initialize and manage state:
	•	Detect rising edge of Start
	•	Store the system time as StartTime
	3.	While running:
	•	Continuously calculate ElapsedTime := CURRENT_TIME - StartTime
	•	Set Done := TRUE if ElapsedTime ≥ PresetTime
	•	Calculate RemainingTime := PresetTime - ElapsedTime
	4.	On Stop signal:
	•	Reset timer state and output flags
	5.	Use internal variables for state control and accurate tracking
	6.	Include comments to explain timing behavior and guard logic for reliability

⸻

🟦 E (Expectation) – Expected Outcome

You will deliver a robust, reusable timer function block suitable for precise delays and sequencing operations. It should:
	•	Work accurately across PLC scan cycles
	•	Allow runtime control via Start/Stop inputs
	•	Support easy integration with other logic structures
	•	Help replace standard timers (TON, TP, etc.) with more tailored functionality

### Generated Code:
**Intent Summary:**  
Create a reusable, scan-cycle-safe timer function block in IEC 61131-3 Structured Text with configurable duration, start/stop controls, and real-time status outputs (running, done, remaining time) for precise industrial automation sequencing.  

*(Focus: Modular timer for PLCs, replacing standard TON/TP with tailored functionality.)*
**Timer:**
Implement a self-contained function block in IEC 61131-3 structured text to create a timer. Include configurable time duration, start/stop controls, and timeout handling.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC developer creating a flexible and reusable timer function block in IEC 61131-3 Structured Text for use in industrial automation programs.

⸻

🟩 I (Input) – Information Provided

The timer must:
	•	Accept a configurable input PresetTime : TIME
	•	Be controlled with Start and Stop : BOOL inputs
	•	Track elapsed time internally
	•	Output status flags:
	•	Running : BOOL — timer is active
	•	Done : BOOL — timer reached its preset
	•	RemainingTime : TIME (optional)
	•	Be self-contained, scan-cycle safe, and suitable for ladder logic replacement

⸻

🟧 S (Steps) – Steps to Perform
	1.	Define the function block interface with inputs and outputs as described
	2.	Initialize and manage state:
	•	Detect rising edge of Start
	•	Store the system time as StartTime
	3.	While running:
	•	Continuously calculate ElapsedTime := CURRENT_TIME - StartTime
	•	Set Done := TRUE if ElapsedTime ≥ PresetTime
	•	Calculate RemainingTime := PresetTime - ElapsedTime
	4.	On Stop signal:
	•	Reset timer state and output flags
	5.	Use internal variables for state control and accurate tracking
	6.	Include comments to explain timing behavior and guard logic for reliability

⸻

🟦 E (Expectation) – Expected Outcome

You will deliver a robust, reusable timer function block suitable for precise delays and sequencing operations. It should:
	•	Work accurately across PLC scan cycles
	•	Allow runtime control via Start/Stop inputs
	•	Support easy integration with other logic structures
	•	Help replace standard timers (TON, TP, etc.) with more tailored functionality
FUNCTION_BLOCK FB_Timer
VAR_INPUT
    PresetTime : TIME; // Time duration to be timed
    Start : BOOL;      // Start the timer
    Stop : BOOL;       // Stop the timer
END_VAR

VAR_OUTPUT
    Running : BOOL;    // TRUE when the timer is actively counting
    Done : BOOL;       // TRUE when the timer has reached its preset time
    RemainingTime : TIME; // Remaining time until the preset is reached
END_VAR

VAR
    StartTime : TIME;   // Time when the timer started
    ElapsedTime : TIME; // Time elapsed since the timer started
    TimerActive : BOOL; // Internal flag to track if the timer is active
END_VAR

// Reset outputs when Stop is TRUE
IF Stop THEN
    Running := FALSE;
    Done := FALSE;
    RemainingTime := PresetTime;
    TimerActive := FALSE;
    StartTime := T#0s;
    RETURN;
END_IF;

// Initialize timer when Start is TRUE
IF Start AND NOT TimerActive THEN
    // Store the current time as StartTime
    StartTime := CURRENT_TIME;
    TimerActive := TRUE;
    Running := TRUE;
    RemainingTime := PresetTime;
END_IF;

// Check if the timer has reached its preset time
IF TimerActive AND ElapsedTime >= PresetTime THEN
    Done := TRUE;
    Running := FALSE;
    RemainingTime := T#0s;
END_IF;

// Calculate the elapsed time
IF TimerActive THEN
    ElapsedTime := CURRENT_TIME - StartTime;
END_IF;

// Reset the timer when Stop is TRUE
IF Stop THEN
    TimerActive := FALSE;
    Running := FALSE;
    RemainingTime := PresetTime;
END_IF;

// Return the remaining time
RemainingTime := PresetTime - ElapsedTime;
```

### Function Block Overview

This function block is designed to create a reusable timer that can be integrated into any IEC 61131-3 Structured Text program. It provides

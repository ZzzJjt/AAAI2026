### Intent:
The task is to create a reusable timer function block in IEC 61131-3 Structured Text with configurable duration, start/stop controls, and status outputs for precise industrial automation timing operations.

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
The task is to create a reusable timer function block in IEC 61131-3 Structured Text with configurable duration, start/stop controls, and status outputs for precise industrial automation timing operations.
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
    Running : BOOL;    // TRUE when the timer is active
    Done : BOOL;       // TRUE when the timer has reached its preset time
    RemainingTime : TIME; // Remaining time until the preset is reached
END_VAR

VAR
    StartTime : TIME;   // Time when the timer started
    ElapsedTime : TIME; // Time elapsed since the timer started
    PrevStart : BOOL;   // Previous state of the Start input
    PrevStop : BOOL;    // Previous state of the Stop input
END_VAR

// Reset outputs when Stop is TRUE
IF Stop THEN
    Running := FALSE;
    Done := FALSE;
    RemainingTime := PresetTime;
    StartTime := T#0s;
    PrevStart := FALSE;
    PrevStop := TRUE;
    RETURN;
END_IF;

// Check if the timer is currently running
Running := Start AND NOT Stop;

// Check if the timer has reached its preset time
IF Running AND NOT Done THEN
    // Store the current time as the start time if the timer is started
    IF Start AND NOT PrevStart THEN
        StartTime := CURRENT_TIME;
    END_IF;

    // Calculate the elapsed time
    ElapsedTime := CURRENT_TIME - StartTime;

    // Check if the elapsed time is greater than or equal to the preset time
    IF ElapsedTime >= PresetTime THEN
        Done := TRUE;
        RemainingTime := T#0s;
    ELSE
        RemainingTime := PresetTime - ElapsedTime;
    END_IF;
ELSE
    // Reset the timer when it reaches its preset time
    Running := FALSE;
    Done := TRUE;
    RemainingTime := T#0s;
END_IF;

// Store the current state of the Start and Stop inputs for the next cycle
PrevStart :=

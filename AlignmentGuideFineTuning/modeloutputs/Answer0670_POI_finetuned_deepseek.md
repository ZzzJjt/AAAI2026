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
    ElapsedTime : TIME;
END_VAR

VAR
    StartTime : TIME;
    ElapsedTime : TIME;
END_VAR

METHOD Execute : BOOL
BEGIN
    // Reset outputs
    Running := FALSE;
    Done := FALSE;
    RemainingTime := TIME(0);
    ElapsedTime := TIME(0);

    // Check if timer is running
    IF Start THEN
        // Store current time
        StartTime := CURRENT_TIME;
        Running := TRUE;
    END_IF;

    // Check if timer is stopped
    IF Stop THEN
        Running := FALSE;
        Done := TRUE;
    END_IF;

    // Calculate elapsed time
    IF Running THEN
        ElapsedTime := CURRENT_TIME - StartTime;
        IF ElapsedTime >= PresetTime THEN
            Done := TRUE;
        END_IF;

        // Calculate remaining time
        RemainingTime := PresetTime - ElapsedTime;
    END_IF;

    RETURN TRUE;
END_METHOD

METHOD Reset : BOOL
BEGIN
    // Reset outputs
    Running := FALSE;
    Done := FALSE;
    RemainingTime := TIME(0);
    ElapsedTime := TIME(0);

    RETURN TRUE;
END_METHOD
END_FUNCTION_BLOCK

// Example usage:
// StartTimer(TRUE, TRUE, TIME(5000)); // Start timer
// StopTimer(FALSE); // Stop timer
// IF TimerDone THEN
//     // Do something when timer is done
// END_IF;
// IF TimerRunning THEN
//     // Check if timer is running
// END_IF;
// IF TimerRemainingTime > 0 THEN
//     // Check if timer has remaining time
// END_IF;
// END_IF;
// END_IF;
// END_IF;
// END_IF;
// END_IF;
// END_IF;
// END_IF;
// END_IF;
// END_

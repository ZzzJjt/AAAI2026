### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text timer function block with configurable duration, start/stop controls, and status outputs (running/done/remaining time) for precise industrial automation sequencing.  

*(Focus: Replace standard PLC timers with a flexible, scan-cycle-safe solution.)*

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
Create a reusable IEC 61131-3 Structured Text timer function block with configurable duration, start/stop controls, and status outputs (running/done/remaining time) for precise industrial automation sequencing.  

*(Focus: Replace standard PLC timers with a flexible, scan-cycle-safe solution.)*
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
    Error : BOOL;
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
    Error := FALSE;

    // Check if timer is running
    IF Start THEN
        // Store current time
        StartTime := CURRENT_TIME;
        Running := TRUE;
    ELSIF Stop THEN
        // Stop timer and reset
        Running := FALSE;
        Done := TRUE;
    END_IF;

    // Check if timer is running
    IF Running THEN
        // Calculate elapsed time
        ElapsedTime := CURRENT_TIME - StartTime;

        // Check if timer has completed
        IF ElapsedTime >= PresetTime THEN
            Done := TRUE;
            RemainingTime := ElapsedTime - PresetTime;
        END_IF;
    END_IF;

    // Check for errors
    IF CURRENT_TIME < StartTime THEN
        Error := TRUE;
    END_IF;

    RETURN TRUE;
END_METHOD

METHOD Reset : BOOL
BEGIN
    // Reset timer
    StartTime := TIME(0);
    ElapsedTime := TIME(0);
    Done := FALSE;
    RemainingTime := TIME(0);
    Error := FALSE;
    Running := FALSE;
    RETURN TRUE;
END_METHOD
END_FUNCTION_BLOCK

// Example usage:
// PresetTime := TIME(1000); // 1 second
// Start Timer;
// IF Done THEN
//     // Timer has completed
// END_IF;
// Stop Timer;
// IF Error THEN
//     // Timer was not started
// END_IF;
// IF RemainingTime > 0 THEN
//     // Timer is still running
// END_IF;
// END_IF;
// END_IF;
// END_IF;
// END

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
FUNCTION_BLOCK Timer
VAR_INPUT
    PresetTime : TIME; // Input time in seconds
    Start : BOOL; // Start the timer
    Stop : BOOL; // Stop the timer
END_VAR

VAR_OUTPUT
    Running : BOOL; // Timer is running
    Done : BOOL; // Timer has completed
    RemainingTime : TIME; // Remaining time after timer completes
END_VAR

VAR
    StartTime : TIME; // Time when timer started
    ElapsedTime : TIME; // Time elapsed since timer started
    RemainingTime : TIME; // Remaining time after timer completes
END_VAR

METHOD Execute : BOOL
BEGIN
    // Reset outputs
    Running := FALSE;
    Done := FALSE;
    RemainingTime := TIME(0);

    // Check if timer is running
    IF Start THEN
        // Store current time
        StartTime := CURRENT_TIME;
        Running := TRUE;
    ELSIF Stop THEN
        // Stop the timer
        Running := FALSE;
    END_IF;

    // Check if timer has completed
    IF Running THEN
        // Calculate elapsed time
        ElapsedTime := CURRENT_TIME - StartTime;
        IF ElapsedTime >= PresetTime THEN
            // Timer has completed
            Done := TRUE;
            RemainingTime := CURRENT_TIME - StartTime - ElapsedTime;
        END_IF;
    END_IF;

    // Return TRUE if timer is running
    RETURN Running;
END_METHOD

METHOD Reset : BOOL
BEGIN
    // Reset outputs
    Running := FALSE;
    Done := FALSE;
    RemainingTime := TIME(0);

    // Reset timer state
    StartTime := TIME(0);
    ElapsedTime := TIME(0);
    RemainingTime := TIME(0);

    // Return TRUE if reset is successful
    RETURN TRUE;
END_METHOD
END_FUNCTION_BLOCK

// Example usage:
// PresetTime := TIME(5); // 5 seconds
// Start := TRUE;
// Done := Execute();
// IF Done THEN
//     // Timer has completed
// END_IF;
// Stop := FALSE;
// RemainingTime := Execute();
// IF RemainingTime > TIME(0) THEN
//

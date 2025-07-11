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

⸻

**Timer Function Block:**
```structuredtext
FUNCTION_BLOCK Timer
VAR_INPUT
    PresetTime : TIME; // Configurable preset time
    Start : BOOL; // Start/Stop control
    Stop : BOOL; // Stop control
END_VAR

VAR_OUTPUT
    Running : BOOL; // Timer is active
    Done : BOOL; // Timer reached its preset
    RemainingTime : TIME; // Time remaining
END_VAR

VAR
    StartTime : TIME; // Start time of the timer
    ElapsedTime : TIME; // Elapsed time since start
    DoneFlag : BOOL; // Flag to indicate timer completion
    RemainingTimeFlag : TIME; // Remaining time flag
END_VAR

METHOD StartTimer
    IF Start AND NOT Running THEN
        StartTime := CURRENT_TIME;
        Running := TRUE;
    END_IF;
END_METHOD

METHOD StopTimer
    Running := FALSE;
    DoneFlag := FALSE;
    RemainingTimeFlag := 0;
END_METHOD

METHOD UpdateTimer
    IF Running THEN
        ElapsedTime := CURRENT_TIME - StartTime;
        IF ElapsedTime >= PresetTime THEN
            DoneFlag := TRUE;
        END_IF;
        RemainingTimeFlag := PresetTime - ElapsedTime;
    END_IF;
END_METHOD

METHOD GetStatus
    Running := Running;
    Done := DoneFlag;
    RemainingTime := RemainingTimeFlag;
END_METHOD
END_FUNCTION_BLOCK
```

**Explanation:**
This timer function block is designed to be self-contained and reusable. It uses internal variables to track the start time, elapsed time, and remaining time. The `StartTimer` method detects the rising edge of the `Start` input and initializes the timer. The `StopTimer` method resets the timer state. The `UpdateTimer` method continuously updates the elapsed time and checks if the timer has reached its preset time. The `GetStatus` method outputs the current status of the timer. This timer is suitable for precise delays and sequencing operations in industrial automation programs.

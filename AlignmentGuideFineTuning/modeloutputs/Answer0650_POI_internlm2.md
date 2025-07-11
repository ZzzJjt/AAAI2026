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
	•	Be self-contained, meaning it doesn't rely on external variables or timers

---

**Solution:**

Here is a basic implementation of the timer function block in IEC 61131-3 Structured Text:

```struct
T_Timer : T_FuncBlock
  PRESETTIME : TIME := 0.0;  // Configurable preset time
  START : BOOL := FALSE;     // Start signal
  STOP : BOOL := FALSE;      // Stop signal
  RUNNING : BOOL := FALSE;   // Timer is active
  DONE : BOOL := FALSE;      // Timer reached its preset
  ELAPSED_TIME : TIME := 0.0; // Elapsed time
  REMAINING_TIME : TIME := 0.0; // Remaining time

  MAIN
    VAR_INPUT
      PresetTime : TIME;
      Start : BOOL;
      Stop : BOOL;
    END_VAR_INPUT

    VAR_OUTPUT
      Running : BOOL;
      Done : BOOL;
      RemainingTime : TIME;
    END_VAR_OUTPUT

    IF Start = TRUE AND NOT RUNNING THEN
      START := TRUE;
      ELAPSED_TIME := 0.0;
    END_IF

    IF NOT START THEN
      ELAPSED_TIME := 0.0;
    END_IF

    IF START AND NOT STOP THEN
      ELAPSED_TIME := ELAPSED_TIME + CURRENT_TIME - START_TIME;
      IF ELAPSED_TIME >= PresetTime THEN
        DONE := TRUE;
      END_IF
      REMAINING_TIME := PresetTime - ELAPSED_TIME;
    END_IF

    IF Stop = TRUE THEN
      START := FALSE;
      STOP := FALSE;
      RUNNING := FALSE;
      DONE := FALSE;
      ELAPSED_TIME := 0.0;
      REMAINING_TIME := 0.0;
    END_IF

    Running := START AND NOT STOP;
    Done := DONE;
    RemainingTime := REMAINING_TIME;
END_STRUCT
```

This function block accepts a configurable preset time, start and stop signals, and outputs the running status, done status, and remaining time. It initializes the timer when the start signal is received and stops when the stop signal is received. The elapsed time is continuously calculated and compared to the preset time to determine if the timer is done. The remaining time is calculated as the preset time minus the elapsed time. The timer is self-contained and suitable for ladder

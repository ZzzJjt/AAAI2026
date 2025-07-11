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
END_IF; To create a reusable IEC 61131-3 Structured Text timer function block with the specified features, follow these steps:

1. **Define Inputs and Outputs:**
   - PresetTime: TIME (Configurable duration)
   - Start: BOOL (Starts the timer)
   - Stop: BOOL (Stops the timer)
   - Running: BOOL (Indicates if the timer is running)
   - Done: BOOL (Indicates if the timer has completed)
   - RemainingTime: TIME (Optional, shows the remaining time)

2. **Initialize Variables:**
   - StartTime: TIME (Captures the start time)
   - ElapsedTime: TIME (Tracks the elapsed time)

3. **Implement Logic:**
   - Check for start condition and initialize timer if necessary.
   - Calculate elapsed time.
   - Check if the timer has completed.
   - Handle stop condition.

Here's the structured text code for the timer function block:

```structuredtext
FUNCTION_BLOCK Timer
VAR_INPUT
    PresetTime : TIME; // Configurable duration
    Start : BOOL; // Start the timer
    Stop : BOOL; // Stop the timer
END_VAR

VAR_OUTPUT
    Running : BOOL; // Timer is running
    Done : BOOL; // Timer has completed
    RemainingTime : TIME; // Remaining time (optional)
END_VAR

VAR
    StartTime : TIME; // Start time
    ElapsedTime : TIME; // Elapsed time
END_VAR

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

RemainingTime := PresetTime - ElapsedTime; // Optional: Calculate remaining time
```

### Explanation:
- **Inputs:**
  - `PresetTime`: Configurable duration for the timer.
  - `Start`: Boolean input to start the timer.
  - `Stop`: Boolean input to stop the timer.

- **Outputs:**
  - `Running`: Boolean output indicating if the timer is running.
  - `Done`: Boolean output indicating if the timer has completed.
  - `RemainingTime`: Optional output showing the

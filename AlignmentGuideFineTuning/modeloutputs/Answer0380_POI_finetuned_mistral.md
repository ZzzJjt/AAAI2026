### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block for a configurable timer with start/stop controls, elapsed/remaining time tracking, and timeout handling for industrial automation applications.

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
Create a reusable IEC 61131-3 Structured Text function block for a configurable timer with start/stop controls, elapsed/remaining time tracking, and timeout handling for industrial automation applications.
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
FUNCTION_BLOCK FB_DigitalCounter
VAR_INPUT
    Enable : BOOL; // Enable counter operation
    CountUp : BOOL; // Direction of counting: TRUE = Up, FALSE = Down
    StepSize : INT; // Step size for counting
    Reset : BOOL; // Reset the counter to initial value
    InitialValue : INT; // Initial value of the counter
END_VAR

VAR_OUTPUT
    CurrentValue : INT; // Current value of the counter
    AtLimit : BOOL; // Flag indicating if the counter has reached its limit
    Error : BOOL; // Flag indicating an error condition
    ErrorID : DWORD; // Error code
END_VAR

VAR
    PrevEnable : BOOL; // Previous value of Enable for edge detection
    LimitReached : BOOL; // Flag indicating if the counter has reached its limit
    TempValue : INT; // Temporary variable for counting
END_VAR

// Reset variables on reset input
IF Reset THEN
    CurrentValue := InitialValue;
    LimitReached := FALSE;
    Error := FALSE;
    ErrorID := 0;
    PrevEnable := FALSE;
    RETURN;
END_IF;

// Edge detection for Enable input
IF Enable AND NOT PrevEnable THEN
    // Initialize temporary variable with initial value
    TempValue := CurrentValue;
END_IF;

PrevEnable := Enable;

// Check if Enable is FALSE to disable the counter
IF NOT Enable THEN
    // Disable the counter and reset temporary variable
    TempValue := CurrentValue;
    LimitReached := FALSE;
    Error := FALSE;
    ErrorID := 0;
    RETURN;
END_IF;

// Check if StepSize is valid
IF StepSize < 1 OR StepSize > 32767 THEN
    Error := TRUE;
    ErrorID := 16#80010001; // Invalid StepSize
    CurrentValue := TempValue;
    LimitReached := FALSE;
    RETURN;
END_IF;

// Check if CountUp is TRUE or FALSE
IF CountUp THEN
    // Count up
    IF CurrentValue + StepSize <= 32767 THEN

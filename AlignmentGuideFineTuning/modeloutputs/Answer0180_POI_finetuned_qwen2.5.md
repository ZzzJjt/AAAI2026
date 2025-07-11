### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block for an iterative heapsort algorithm that sorts integer arrays (1–100 elements) with configurable size, execution control, and error handling for industrial PLC applications.  

*(Focus: Configurable sorting, iterative design for PLCs, and safety/output flags.)*

### Prompt:
**Timer:**
Implement a self-contained function block in IEC 61131-3 structured text to create a timer. Include configurable time duration, start/stop controls, and timeout handling.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

Timers are essential in industrial automation for sequencing operations, delays, and safety checks. However, relying on fixed or external timers can limit flexibility and reusability. A timer that lacks configurable duration, start/stop control, or timeout indication can lead to rigid control logic and poor maintainability in PLC systems.

⸻

🟩 A (After) – The Desired Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text that acts as a flexible timer. The function block should:
	•	Allow users to configure the time duration
	•	Support Start and Stop signals for runtime control
	•	Track elapsed time and indicate when the timer has timed out
	•	Provide output flags for Running, Done, and optionally RemainingTime

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block with inputs:
	•	Start : BOOL
	•	Stop : BOOL
	•	PresetTime : TIME
	2.	Use internal variables to:
	•	Store StartTime and ElapsedTime
	•	Reset when Stop = TRUE
	•	Accumulate time only when Start = TRUE and Stop = FALSE
	3.	Provide outputs:
	•	Running : BOOL – active while the timer is counting
	•	Done : BOOL – TRUE when elapsed time ≥ preset time
	•	RemainingTime : TIME – optional, shows remaining time until done
	4.	Ensure the timer is scan-cycle safe, reusable, and well-commented

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block for an iterative heapsort algorithm that sorts integer arrays (1–100 elements) with configurable size, execution control, and error handling for industrial PLC applications.  

*(Focus: Configurable sorting, iterative design for PLCs, and safety/output flags.)*
**Timer:**
Implement a self-contained function block in IEC 61131-3 structured text to create a timer. Include configurable time duration, start/stop controls, and timeout handling.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

Timers are essential in industrial automation for sequencing operations, delays, and safety checks. However, relying on fixed or external timers can limit flexibility and reusability. A timer that lacks configurable duration, start/stop control, or timeout indication can lead to rigid control logic and poor maintainability in PLC systems.

⸻

🟩 A (After) – The Desired Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text that acts as a flexible timer. The function block should:
	•	Allow users to configure the time duration
	•	Support Start and Stop signals for runtime control
	•	Track elapsed time and indicate when the timer has timed out
	•	Provide output flags for Running, Done, and optionally RemainingTime

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block with inputs:
	•	Start : BOOL
	•	Stop : BOOL
	•	PresetTime : TIME
	2.	Use internal variables to:
	•	Store StartTime and ElapsedTime
	•	Reset when Stop = TRUE
	•	Accumulate time only when Start = TRUE and Stop = FALSE
	3.	Provide outputs:
	•	Running : BOOL – active while the timer is counting
	•	Done : BOOL – TRUE when elapsed time ≥ preset time
	•	RemainingTime : TIME – optional, shows remaining time until done
	4.	Ensure the timer is scan-cycle safe, reusable, and well-commented for clarity.

⸻

**C-A-R-E:**

🟥 C (Context) – Background Situation

In industrial automation, precise timing is critical for process control, safety interlocks, and sequencing. However, many standard timer implementations lack the flexibility needed for dynamic control logic, especially in environments where scan-cycle duration or timer precision is not constant.

⸻

🟩 A (Action) – Task to Perform

Develop a self-contained function block in IEC 61131-3 Structured Text that:
	•	Accepts configurable time duration and control signals
	•	Accurately tracks elapsed time
	•	Notifies when the timer has reached its preset value
	•	Includes outputs for timer status and remaining time (optional)

⸻

🟧 R (Result) – Expected Outcome

The result should be a flexible, scan-cycle-safe timer function block that:
	•	Works reliably in scan-cycle environments
	•	Is reusable across different automation tasks
	•	Helps improve control logic flexibility and maintainability
	•	Includes detailed comments for clarity and documentation

⸻

🟩 E (Example) – Pictorial or Textual Representation

	•	Inputs:
	•	Start : BOOL — activates the timer
	•	Stop : BOOL — resets the timer
	•	PresetTime : TIME — sets the duration of the timer
	•	Outputs:
	•	Running : BOOL — timer is currently counting
	•	Done : BOOL — timer has reached its preset time
	•	RemainingTime : TIME — time remaining until the timer is done (optional)
	•	Internal:
	•	StartTime : TIME — when the timer was started
	•	ElapsedTime : TIME — time elapsed since the timer was started
	•	TimerRunning : BOOL — tracks whether the timer is currently running
	•	TimerDone : BOOL — timer has reached its preset time
	•	TimerReset : BOOL — timer has been reset
	•	TimerControl : BOOL — controls the timer’s start/stop logic
	•	TimerAccumulate : TIME — calculates elapsed time
	•	TimerDecrement : TIME — calculates remaining time
	•	TimerDoneSignal : BOOL — triggers when the timer is done
	•	TimerRunningSignal : BOOL — triggers when the timer is running
	•	TimerResetSignal : BOOL — triggers when the timer is reset
	•	TimerControlSignal

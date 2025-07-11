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

**C:**

🟥 C (Context) – The Situation

In industrial automation, timing is critical for controlling processes and coordinating operations. A timer function block that can be easily configured and reused across different applications would improve flexibility and reduce code duplication. However, many existing timer implementations lack the configurability and control needed for industrial use.

⸻

🟩 C (Constraints) – Assumptions, Limitations, and Other Factors

•	Implement the timer as a self-contained function block in IEC 61131-3 Structured Text.
•	Ensure the timer can be configured with a preset time duration.
•	Include start and stop controls to enable runtime flexibility.
•	Provide output flags for running status, completion, and optional remaining time.
•	Ensure the timer is safe for use in industrial PLC applications, with proper handling of edge cases and timing accuracy.

**R:**

🟥 R (Role) – The Role

You are an automation engineer responsible for developing reusable function blocks in IEC 61131-3 Structured Text for industrial control systems. Your role is to create a timer function block that is self-contained, configurable, and safe for use in PLC applications.

**A:**

🟩 A (Action) – The Task

Create a self-contained function block in IEC 61131-3 Structured Text to implement a timer with configurable time duration, start/stop controls, and output flags for running status, completion, and optional remaining time. Ensure the timer is safe for use in industrial PLC applications, with proper handling of edge cases and timing accuracy.

**I:**

🟥 I (Input) – The Input

•	Start (BOOL): Start the timer
•	Stop (BOOL): Stop the timer
•	PresetTime (TIME): Time duration to be set for the timer

**C:**

🟩 C (Context) – The Situation

Implement a timer function block in IEC 61131-3 Structured Text that can be used in industrial control systems. The timer should be self-contained, configurable, and safe for use in PLC applications. The timer should have start and stop controls, and output flags for running status, completion, and optional remaining time. Ensure proper handling of edge cases and timing accuracy.

**O:**

🟩 O (

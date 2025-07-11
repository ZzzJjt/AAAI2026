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
	4.	Ensure the timer is scan-cycle safe, reusable, and well-commented for easy maintenance

**Example Usage:**

```ST
VAR_INPUT
  Start : BOOL;
  Stop : BOOL;
  PresetTime : TIME := 5s;
END_VAR

VAR
  StartTime : TIME;
  ElapsedTime : TIME;
  Running : BOOL;
  Done : BOOL;
  RemainingTime : TIME;
END_VAR

IF Start THEN
  StartTime := TIME();
  Running := TRUE;
ELSE
  Running := FALSE;
END_IF

IF Stop THEN
  Running := FALSE;
  ElapsedTime := 0s;
ELSE
  IF Running THEN
    ElapsedTime := TIME() - StartTime;
  END_IF;
END_IF

IF ElapsedTime >= PresetTime THEN
  Done := TRUE;
ELSE
  Done := FALSE;
END_IF

IF Done THEN
  RemainingTime := 0s;
ELSE
  RemainingTime := PresetTime - ElapsedTime;
END_IF
```

**Additional Considerations:**

- The function block should be designed to be easily integrated into existing PLC code, minimizing the need for additional wiring and reducing the risk of errors.
- The function block should be thoroughly documented, including comments explaining the purpose, inputs, outputs, and behavior of the timer.
- The function block should be tested in a variety of scenarios, including different time durations, start/stop sequences, and edge cases, to ensure its reliability and robustness.
- The function block should be designed with safety in mind, including appropriate error handling and fail-safe mechanisms to prevent unexpected behavior or system failures.
- The function block should be designed to be easily configurable, allowing users to adjust the time duration, start/stop controls, and output flags as needed for their specific application.
- The function block should be designed to be easily reusable, allowing users to incorporate it into multiple PLC programs without the need for significant modification or duplication of code.
- The function block should be designed to be easily maintainable, including clear and consistent naming conventions, well-organized code structure, and appropriate use of comments and documentation.
- The function block should be designed to be easily scalable, allowing users to easily modify or extend its functionality as needed for their specific application.
- The function block should be designed to be easily debuggable, including appropriate use of breakpoints, logging, and other debugging tools to help users quickly identify and resolve issues.
- The function block should be designed to be easily extensible, allowing users to easily add new features or

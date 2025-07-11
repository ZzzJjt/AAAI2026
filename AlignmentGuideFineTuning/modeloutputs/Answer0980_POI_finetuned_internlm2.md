### Intent:
The task is to implement a reusable timer function block in IEC 61131-3 Structured Text for PLC systems, featuring configurable timing, start/stop controls, and status outputs for automation sequencing and timeout handling.  

(Note: The provided code actually shows a heapsort implementation rather than a timer, but the intent summary is based on the original timer task description in the T-A-G section.)

### Prompt:
**Timer:**
Implement a self-contained function block in IEC 61131-3 structured text to create a timer. Include configurable time duration, start/stop controls, and timeout handling.


**T-A-G:**

🟥 T (Task)

Implement a self-contained timer function block in IEC 61131-3 Structured Text for use in PLC-based control systems.

⸻

🟩 A (Action)
	•	Define the timer with the following inputs:
	•	Start : BOOL — triggers the timer
	•	Stop : BOOL — resets or halts the timer
	•	PresetTime : TIME — sets the duration to time
	•	Create internal logic to:
	•	Detect the rising edge of the Start input
	•	Capture and update elapsed time using system clock functions
	•	Stop the timer if Stop = TRUE
	•	Provide outputs such as:
	•	Running : BOOL — indicates the timer is active
	•	Done : BOOL — becomes TRUE when the preset time is reached
	•	Optionally, RemainingTime : TIME — time left before timeout
	•	Ensure the function block is modular, edge-triggered, and safe for repeated use across scan cycles

⸻

🟦 G (Goal)

Deliver a flexible, reusable timer block that can be integrated into various automation routines for delay control, sequencing, or timeout handling. The timer should be easy to configure, scan-cycle safe, and support both momentary and continuous triggering logic.

### Generated Code:
The task is to implement a reusable timer function block in IEC 61131-3 Structured Text for PLC systems, featuring configurable timing, start/stop controls, and status outputs for automation sequencing and timeout handling.  

(Note: The provided code actually shows a heapsort implementation rather than a timer, but the intent summary is based on the original timer task description in the T-A-G section.)
**Timer:**
Implement a self-contained function block in IEC 61131-3 structured text to create a timer. Include configurable time duration, start/stop controls, and timeout handling.


**T-A-G:**

🟥 T (Task)

Implement a self-contained timer function block in IEC 61131-3 Structured Text for use in PLC-based control systems.

⸻

🟩 A (Action)
	•	Define the timer with the following inputs:
	•	Start : BOOL — triggers the timer
	•	Stop : BOOL — resets or halts the timer
	•	PresetTime : TIME — sets the duration to time
	•	Create internal logic to:
	•	Detect the rising edge of the Start input
	•	Capture and update elapsed time using system clock functions
	•	Stop the timer if Stop = TRUE
	•	Provide outputs such as:
	•	Running : BOOL — indicates the timer is active
	•	Done : BOOL — becomes TRUE when the preset time is reached
	•	Optionally, RemainingTime : TIME — time left before timeout
	•	Ensure the function block is modular, edge-triggered, and safe for repeated use across scan cycles

⸻

🟦 G (Goal)

Deliver a flexible, reusable timer block that can be integrated into various automation routines for delay control, sequencing, or timeout handling. The timer should be easy to configure, scan-cycle safe, and support both momentary and continuous triggering logic. The timer should also provide clear status outputs to indicate its state and remaining time, if applicable.

**C-A-R-E:**

🟥 C (Context)

In industrial control systems, timing is a fundamental aspect of automation. Timers are often used to control sequences, monitor intervals, or enforce safety timeouts. However, implementing a timer in IEC 61131-3 Structured Text can be challenging due to the lack of built-in timer functions. This requires developers to create their own timer logic, which can be error-prone and difficult to maintain.

🟩 A (Action)

To address this challenge, you will implement a self-contained timer function block in IEC 61131-3 Structured Text. The timer should accept inputs for start/stop control and preset time, and provide outputs for running status, timeout indication, and remaining time (if applicable). The timer logic should be modular, edge-triggered, and safe for use in PLC-based control systems.

⸻

🟦 G (Goal)

The goal is to create a reusable timer function block that can be easily integrated into various automation routines. The timer should be configurable, with clear inputs and outputs, and should handle timing logic in a safe and modular manner. This will improve the reliability and maintainability of control systems by providing a standardized way to manage timing requirements.

**S-T-E-P-S:**

🟥 S (Situation)

In industrial control systems, timing is a critical aspect of automation. However, implementing a timer in IEC 61131-3 Structured Text can be challenging due to the lack of built-in timer functions. This requires developers to create their own timer logic, which can be error-prone and difficult to maintain.

🟩 T (Task)

Create a self-contained timer function block in IEC 61131-3 Structured Text that can be easily integrated into various automation routines. The timer should accept inputs for start/stop control and preset time, and provide outputs for running status, timeout indication, and remaining time (if applicable). The timer logic should be modular, edge-triggered, and safe for use in PLC-based control systems.

⸻

🟦 A (Action)

Implement a timer function block in IEC 61131-3 Structured Text that accepts inputs for start/stop control and preset time. The timer should provide outputs for running status, timeout indication, and remaining time (if applicable). Ensure the

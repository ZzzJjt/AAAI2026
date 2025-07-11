### Intent:
**Intent Summary:**  
Create a structured-text PLC function block for an industrial timer that handles edge-triggered start/stop, tracks elapsed/remaining time, and ensures robust timeout control with input validation and safety checks.  

*(Focus: Code generation for a reliable timer in automation systems, prioritizing edge detection, system-clock precision, and fail-safe logic.)*

### Prompt:
**P-ID Steam Water Cycle:**

Create a P&I diagram in textual notation for a steam water cycle in a power plant. Include equipment, instrumentation, piping, and control loops. Provide concrete tag names.


**T-A-G:**

🟥 T (Task)

Create a text-based Piping and Instrumentation Diagram (P&ID) for a steam-water cycle in a power plant.

⸻

🟩 A (Action)
	•	Represent all major equipment involved in the steam-water cycle, such as feedwater pumps, boiler, steam drum, condenser, etc.
	•	Include relevant instrumentation and control loops, such as flow transmitters (FT), level transmitters (LT), pressure transmitters (PT), controllers (FIC, LIC), and control valves (FCV, LCV).
	•	Use clear tag names (e.g., FT101, FCV102) based on industry standards.
	•	Show piping and flow direction using arrows (-->) and organize elements in process order.
	•	Format the diagram in clean plain-text notation, using indentation and alignment to convey process structure and control logic.

⸻

🟦 G (Goal)

Provide a structured, readable, and logic-complete textual P&ID that clearly documents the flow, control strategy, and tag references of a steam-water cycle, enabling use in early-stage engineering, PLC programming, or control narrative development when graphics are unavailable.

### Generated Code:
**Intent Summary:**  
Create a structured-text PLC function block for an industrial timer that handles edge-triggered start/stop, tracks elapsed/remaining time, and ensures robust timeout control with input validation and safety checks.  

*(Focus: Code generation for a reliable timer in automation systems, prioritizing edge detection, system-clock precision, and fail-safe logic.)*
**P-ID Steam Water Cycle:**

Create a P&I diagram in textual notation for a steam water cycle in a power plant. Include equipment, instrumentation, piping, and control loops. Provide concrete tag names.


**T-A-G:**

🟥 T (Task)

Create a text-based Piping and Instrumentation Diagram (P&ID) for a steam-water cycle in a power plant.

⸻

🟩 A (Action)
	•	Represent all major equipment involved in the steam-water cycle, such as feedwater pumps, boiler, steam drum, condenser, etc.
	•	Include relevant instrumentation and control loops, such as flow transmitters (FT), level transmitters (LT), pressure transmitters (PT), controllers (FIC, LIC), and control valves (FCV, LCV).
	•	Use clear tag names (e.g., FT101, FCV102) based on industry standards.
	•	Show piping and flow direction using arrows (-->) and organize elements in process order.
	•	Format the diagram in clean plain-text notation, using indentation and alignment to convey process structure and control logic.

⸻

🟦 G (Goal)

Provide a structured, readable, and logic-complete textual P&ID that clearly documents the flow, control strategy, and tag references of a steam-water cycle, enabling use in early-stage engineering, PLC programming, or control narrative development when graphics are unavailable.
### Function Block Diagram

Create a function block diagram (FBD) in textual notation for an edge-triggered timer that includes a timer function block, input/output elements, and control logic. Include detailed descriptions of the timer's operation, including edge detection, elapsed time calculation, and reset behavior.

### Description

This function block implements an edge-triggered timer that is designed to respond only when it detects a rising edge on its input signal. It tracks the elapsed time since the last rising edge and provides outputs for both the current time and a boolean flag indicating whether a rising edge has been detected. The function block is suitable for use in industrial automation applications where precise timing and event detection are required.

### Function Block Interface

#### Inputs

* `Enable` : `BOOL` – Enables the timer.
* `Reset` : `BOOL` – Resets the timer.
* `Start` : `BOOL` – Triggers the timer on a rising edge.
* `Clock` : `BOOL` – Represents the rising edge input signal.

#### Outputs

* `ElapsedTime` : `REAL` – The elapsed time in seconds since the last rising edge.
* `RisingEdgeDetected` : `BOOL` – Indicates whether a rising edge has been detected.
* `TimerActive` : `BOOL` – Indicates whether the timer is currently active.

### Control Logic

The function block operates as follows:

1. When `Enable` is `TRUE`, the timer becomes active.
2. When `Reset` is `TRUE`, the timer is reset to zero.
3. When `Start` is `TRUE` and `Clock` is `TRUE` (rising edge), the timer starts.
4. The timer continues to run until the next rising edge is detected or `Enable` is `FALSE`.
5. At each sampling interval, the timer calculates the elapsed time since the last rising edge and updates `ElapsedTime`.
6. `RisingEdgeDetected` is set to `TRUE` when a rising edge is detected.
7. `TimerActive` is set to `TRUE` when the timer is active.

### Textual FBD Representation

#### Function Block

```
EdgeTriggeredTimer
|
|-- Enable

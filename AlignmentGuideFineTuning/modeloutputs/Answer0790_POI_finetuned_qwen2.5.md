### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 timer function block with configurable duration, start/stop controls, and real-time status outputs (running, done, remaining time) for industrial PLC applications.  

*(Focus: Modularity, scan-cycle efficiency, and precise timing logic.)*

### Prompt:
**Timer:**
Implement a self-contained function block in IEC 61131-3 structured text to create a timer. Include configurable time duration, start/stop controls, and timeout handling.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC programmer tasked with implementing a customizable timer function block using IEC 61131-3 Structured Text, suitable for precise and reusable industrial control logic.

⸻

🟩 T (Task) – Define the Objective

Develop a self-contained timer function block that includes:
	•	A configurable time duration input (PresetTime : TIME)
	•	Start and Stop Boolean inputs to control timing behavior
	•	Accurate elapsed time tracking
	•	Output flags to indicate timer status:
	•	Running : BOOL — timer is active
	•	Done : BOOL — timer has reached the preset time
	•	Optionally, RemainingTime : TIME

The timer must operate in a scan-cycle-compatible and modular way, with clean state handling and timeout logic.

⸻

🟧 F (Format) – Specify the Output Format

Provide a complete IEC 61131-3 Structured Text function block that includes:
	•	Inputs:
	•	Start : BOOL
	•	Stop : BOOL
	•	PresetTime : TIME
	•	Outputs:
	•	Running : BOOL
	•	Done : BOOL
	•	RemainingTime : TIME (optional)
	•	Internal Variables:
	•	StartTime : TIME
	•	ElapsedTime : TIME
	•	TriggerEdge : BOOL
	•	Logic Flow:
	•	Edge detection for Start
	•	Reset logic on Stop
	•	Time comparison to set Done and clear Running

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 timer function block with configurable duration, start/stop controls, and real-time status outputs (running, done, remaining time) for industrial PLC applications.  

*(Focus: Modularity, scan-cycle efficiency, and precise timing logic.)*
**Timer:**
Implement a self-contained function block in IEC 61131-3 structured text to create a timer. Include configurable time duration, start/stop controls, and timeout handling.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC programmer tasked with implementing a customizable timer function block using IEC 61131-3 Structured Text, suitable for precise and reusable industrial control logic.

⸻

🟩 T (Task) – Define the Objective

Develop a self-contained timer function block that includes:
	•	A configurable time duration input (PresetTime : TIME)
	•	Start and Stop Boolean inputs to control timing behavior
	•	Accurate elapsed time tracking
	•	Output flags to indicate timer status:
	•	Running : BOOL — timer is active
	•	Done : BOOL — timer has reached the preset time
	•	Optionally, RemainingTime : TIME

The timer must operate in a scan-cycle-compatible and modular way, with clean state handling and timeout logic.

⸻

🟧 F (Format) – Specify the Output Format

Provide a complete IEC 61131-3 Structured Text function block that includes:
	•	Inputs:
	•	Start : BOOL
	•	Stop : BOOL
	•	PresetTime : TIME
	•	Outputs:
	•	Running : BOOL
	•	Done : BOOL
	•	RemainingTime : TIME (optional)
	•	Internal Variables:
	•	StartTime : TIME
	•	ElapsedTime : TIME
	•	TriggerEdge : BOOL
	•	Logic Flow:
	•	Edge detection for Start
	•	Reset logic on Stop
	•	Time comparison to set Done and clear Running
	•	Accurate elapsed time tracking
	•	RemainingTime calculation (optional)
	•	Scan-cycle-safe execution
	•	Include comments explaining the logic and usage

Ensure the function block is modular, scan-cycle efficient, and includes detailed comments for clarity and maintainability.

⸻

Use this R-T-F format to guide the implementation of a self-contained IEC 61131-3 Structured Text function block for a configurable timer, with inputs for start/stop control, a preset time duration, and outputs to indicate the timer’s status. Include logic for elapsed time tracking, timeout handling, and scan-cycle compatibility.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC programmer tasked with implementing a self-contained function block in IEC 61131-3 Structured Text to create a timer. Your function block should be modular, scan-cycle efficient, and suitable for use in industrial control systems.

⸻

🟩 T (Task) – Define the Objective

Develop a self-contained function block that:
	•	Accepts a configurable time duration as input
	•	Includes start and stop controls
	•	Accurately tracks elapsed time
	•	Outputs flags to indicate whether the timer is running, done, or has reached its preset time
	•	Handles scan-cycle compatibility and edge detection for start and stop inputs
	•	Includes detailed comments explaining the logic and usage

Ensure that the function block is designed for use in scan-cycle-sensitive environments, with efficient execution and clear status outputs.

⸻

🟧 F (Format) – Specify the Output Format

Provide a complete IEC 61131-3 Structured Text function block that:
	•	Includes inputs:
	•	PresetTime : TIME — the time duration for the timer
	•	Start : BOOL — triggers the timer to start
	•	Stop : BOOL — triggers the timer to stop
	•	Outputs:
	•	Running : BOOL — the timer is currently running
	•	Done : BOOL — the timer has reached its preset time
	•	RemainingTime : TIME — the time remaining until the timer is done (optional)
	•	Internal variables:
	•	StartTime : TIME — the start time of the timer
	•	ElapsedTime : TIME — the elapsed time since the timer started
	•	Include logic for:
	•	Starting the timer on rising edge

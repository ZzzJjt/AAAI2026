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
	•	ElapsedTime calculation
	•	RemainingTime calculation (optional)

⸻

🟦 E (Examples) – Provide Examples

Example 1:
```
FUNCTION Timer : BOOL
VAR_INPUT
	Start : BOOL;
	Stop : BOOL;
	PresetTime : TIME;
VAR_OUTPUT
	Running : BOOL;
	Done : BOOL;
	RemainingTime : TIME;
VAR
	StartTime : TIME;
	ElapsedTime : TIME;
	TriggerEdge : BOOL;
END_VAR

IF Start THEN
	TriggerEdge := NOT TriggerEdge;
	IF NOT TriggerEdge THEN
		StartTime := T#NOW;
	END_IF
END_IF

IF NOT Stop THEN
	IF TriggerEdge THEN
		ElapsedTime := T#NOW - StartTime;
		IF ElapsedTime >= PresetTime THEN
			Running := FALSE;
			Done := TRUE;
			RemainingTime := 0;
		ELSE
			Running := TRUE;
			Done := FALSE;
			RemainingTime := PresetTime - ElapsedTime;
		END_IF
	END_IF
END_FUNCTION
```

Example 2:
```
FUNCTION Timer : BOOL
VAR_INPUT
	Start : BOOL;
	Stop : BOOL;
	PresetTime : TIME;
VAR_OUTPUT
	Running : BOOL;
	Done : BOOL;
END_VAR
VAR
	StartTime : TIME;
	ElapsedTime : TIME;
	TriggerEdge : BOOL;
END_VAR

IF Start THEN
	TriggerEdge := NOT TriggerEdge;
	IF NOT TriggerEdge THEN
		StartTime := T#NOW;
	END_IF
END_IF

IF NOT Stop THEN
	IF TriggerEdge THEN
		ElapsedTime := T#NOW - StartTime;
		IF ElapsedTime >= PresetTime THEN
			Running := FALSE;
			Done := TRUE;
		ELSE

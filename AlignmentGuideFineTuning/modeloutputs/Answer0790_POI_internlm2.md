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
	•	RemainingTime calculation (optional)

⸻

🟨 S (Solution) – Provide a Solution

```IEC
FUNCTION_BLOCK Timer : BOOL
VAR_INPUT
  Start : BOOL;
  Stop : BOOL;
  PresetTime : TIME;
END_VAR
VAR
  StartTime : TIME;
  ElapsedTime : TIME;
  TriggerEdge : BOOL;
  Running : BOOL;
  Done : BOOL;
  RemainingTime : TIME;
END_VAR
BEGIN
  IF Start AND NOT TriggerEdge THEN
    TriggerEdge := TRUE;
    StartTime := TIME_PRESENT;
  END_IF;
  
  IF Stop THEN
    TriggerEdge := FALSE;
    Running := FALSE;
    Done := FALSE;
    ElapsedTime := TIME_ZERO;
  END_IF;
  
  IF TriggerEdge THEN
    IF NOT Running THEN
      Running := TRUE;
      ElapsedTime := TIME_ZERO;
    END_IF;
    
    IF ElapsedTime >= PresetTime THEN
      Running := FALSE;
      Done := TRUE;
      ElapsedTime := TIME_ZERO;
    ELSE
      ElapsedTime := TIME_DIFF( TIME_PRESENT, StartTime );
    END_IF;
  END_IF;
  
  IF Done THEN
    Running := FALSE;
    RemainingTime := TIME_ZERO;
  ELSE
    RemainingTime := PresetTime - ElapsedTime;
  END_IF;
END_FUNCTION
```

⸻

🟩 T (Test) – Verify the Solution

Test the function block with various scenarios, including:
	•	Starting and stopping the timer
	•	Setting different preset times
	•	Checking the status flags and remaining time

⸻

🟩 E (Evaluation) – Assess the Solution

Evaluate the function block based on the following criteria:
	•	Modularity: The function block should be self-contained and easy to reuse in different projects.
	•	Scan-cycle efficiency: The function block should operate in a way that minimizes scan-cycle time and maximizes performance.
	•	Precise timing logic: The function block should accurately track elapsed time and handle edge cases such as simultaneous start and stop events.

⸻

🟩 A (Application) – Apply the Solution

Integrate the timer function block into an industrial PLC application, using it to control various processes and systems based on precise timing requirements.

⸻

🟩 R (Review) –

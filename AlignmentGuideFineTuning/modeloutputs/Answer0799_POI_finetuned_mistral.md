### Intent:
The task is to create a structured NORSOK-compliant System Control Diagram (SCD) in textual notation for an LNG vaporizer system, detailing piping flows, instrumentation tags, control loops, and safety interlocks with standardized formatting.  

**Intent Summary:**  
*Generate a text-based SCD for LNG vaporization with tagged instrumentation, control loops, and interlocks in NORSOK format.*

### Prompt:
**SCD LNG Vaporizer:**

Create a NORSOK system control diagram (SCD) in textual notation for a LNG Vaporizer System. Include instrumentation, control loops, and interlocks. Provide concrete tag numbers and piping.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a process control engineer responsible for documenting a NORSOK-compliant System Control Diagram (SCD) for an LNG vaporizer system using structured textual notation.

⸻

🟩 T (Task) – Define the Objective

Create a text-based SCD for the LNG vaporizer that includes:
	•	The full piping and process flow from LNG inlet to gas outlet
	•	All relevant instrumentation with standard tag numbers (e.g., FT201, TT101, FIC202, FCV203)
	•	Key control loops for temperature, flow, and pressure regulation
	•	Associated interlocks for safety shutdowns (e.g., high-pressure trips, ESD logic)
	•	Clearly structured layout using directional arrows (-->) and indentation for clarity

⸻

🟧 F (Format) – Specify the Output Format

Present the output in plain-text format, organized as follows:
	•	One line per major flow segment (e.g., LNG Inlet --> FT201 --> FIC201 --> FCV201 --> Vaporizer)
	•	Grouped sections for each control loop (e.g., [Temperature Control Loop])
	•	Each control loop should show the measurement device, controller, and final control element
	•	Clearly label interlocks under a [Safety Interlocks] section with signal conditions and shutdown targets
	•	Use consistent tag naming and logical flow formatting throughout

### Generated Code:
The task is to create a structured NORSOK-compliant System Control Diagram (SCD) in textual notation for an LNG vaporizer system, detailing piping flows, instrumentation tags, control loops, and safety interlocks with standardized formatting.  

**Intent Summary:**  
*Generate a text-based SCD for LNG vaporization with tagged instrumentation, control loops, and interlocks in NORSOK format.*
**SCD LNG Vaporizer:**

Create a NORSOK system control diagram (SCD) in textual notation for a LNG Vaporizer System. Include instrumentation, control loops, and interlocks. Provide concrete tag numbers and piping.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a process control engineer responsible for documenting a NORSOK-compliant System Control Diagram (SCD) for an LNG vaporizer system using structured textual notation.

⸻

🟩 T (Task) – Define the Objective

Create a text-based SCD for the LNG vaporizer that includes:
	•	The full piping and process flow from LNG inlet to gas outlet
	•	All relevant instrumentation with standard tag numbers (e.g., FT201, TT101, FIC202, FCV203)
	•	Key control loops for temperature, flow, and pressure regulation
	•	Associated interlocks for safety shutdowns (e.g., high-pressure trips, ESD logic)
	•	Clearly structured layout using directional arrows (-->) and indentation for clarity

⸻

🟧 F (Format) – Specify the Output Format

Present the output in plain-text format, organized as follows:
	•	One line per major flow segment (e.g., LNG Inlet --> FT201 --> FIC201 --> FCV201 --> Vaporizer)
	•	Grouped sections for each control loop (e.g., [Temperature Control Loop])
	•	Each control loop should show the measurement device, controller, and final control element
	•	Clearly label interlocks under a [Safety Interlocks] section with signal conditions and shutdown targets
	•	Use consistent tag naming and logical flow formatting throughout
(* IEC 61131-3 Structured Text Program for PLC Control of a Conveyor System *)
(* Implements start/stop logic, speed control, and safety interlocks *)

PROGRAM ConveyorControl
VAR
    (* Inputs *)
    StartButton : BOOL;                 (* TRUE when Start button is pressed *)
    StopButton : BOOL;                  (* TRUE when Stop button is pressed *)
    EmergencyStop : BOOL;               (* TRUE when Emergency Stop is activated *)
    
    (* Outputs *)
    ConveyorRunning : BOOL;             (* TRUE when conveyor is running *)
    ConveyorSpeed : REAL;               (* Conveyor speed in m/s *)
    ConveyorStopped : BOOL;             (* TRUE when conveyor is stopped *)
    AlarmActive : BOOL;                 (* TRUE when an alarm is active *)
    
    (* Internal Variables *)
    ConveyorState : INT := 0;           (* 0=Stopped, 1=Starting, 2=Running *)
    SpeedRamp : REAL := 0.0;            (* Current speed ramp value *)
    RampTime : TIME := T#10s;           (* Ramp time for speed change *)
    RampStartTime : TIME;               (* Time when ramp started *)
    RampComplete : BOOL;                (* TRUE when ramp is complete *)
    EmergencyStopped : BOOL;            (* TRUE when conveyor is forced to stop *)
END_VAR

(* Main Control Logic *)
IF StartButton AND NOT StopButton AND NOT EmergencyStop THEN
    (* Start conveyor *)
    ConveyorState := 1;
    ConveyorRunning := FALSE;
    ConveyorStopped := FALSE;
    SpeedRamp := 0.0;
    RampComplete := FALSE;
    RampStartTime := T#NOW;
END_IF

IF StopButton OR EmergencyStop THEN
    (* Stop conveyor *)
    ConveyorState := 0;
    ConveyorRunning := FALSE;
    ConveyorStopped := TRUE;
    SpeedRamp := 0.0;
    RampComplete := FALSE;
    RampStartTime :=

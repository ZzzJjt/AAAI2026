### Intent:
**Intent Summary:**  
Develop a pressure relief interlock program for a chemical reactor that monitors sensor inputs (pressure, validity, valve status) and triggers safety actions (opening relief valves, alarms, shutdowns) to prevent overpressure hazards while allowing manual resets under safe conditions.

### Prompt:
**Interlock Cause & Effect Matrix:**

Develop a cause and effect matrix for the interlocks required in a chemical reactor system. Each row should represent a specific cause linked to sensor values such as pressure, temperature, or level, while each column should represent the corresponding effect related to actuator actions such as closing valves, stopping pumps, or triggering alarms. Once the matrix is complete, write a detailed explanation of how these interlocks ensure the safety and stability of the reactor operation. Discuss how each interlock action prevents hazardous conditions and safeguards the equipment during abnormal process situations.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Develop a cause and effect matrix for the interlock system of a chemical reactor.

⸻

🟩 A (Action) – How to Do It

Create a matrix where:

	•	Each row represents a specific cause, such as abnormal sensor readings (e.g., high pressure, low level, or high temperature).
	•	Each column represents a specific effect, such as triggering an alarm, stopping a pump, closing a valve, or shutting down a heater.

Populate the matrix to show how each hazardous condition leads to one or more predefined safety actions. After the matrix is completed, write a detailed explanation discussing how each interlock response helps mitigate risk, protect equipment, and maintain reactor stability. Highlight the importance of using this matrix as a clear, traceable tool in safety system design.

⸻

🟦 G (Goal) – What You Want to Achieve

Create a structured, visual tool that links potential process hazards with protective actions. This matrix will enhance operational safety, simplify interlock validation, and serve as a vital reference for engineers, operators, and auditors responsible for the safe functioning of the chemical reactor.

### Generated Code:
**Intent Summary:**  
Develop a pressure relief interlock program for a chemical reactor that monitors sensor inputs (pressure, validity, valve status) and triggers safety actions (opening relief valves, alarms, shutdowns) to prevent overpressure hazards while allowing manual resets under safe conditions.
**Interlock Cause & Effect Matrix:**

Develop a cause and effect matrix for the interlocks required in a chemical reactor system. Each row should represent a specific cause linked to sensor values such as pressure, temperature, or level, while each column should represent the corresponding effect related to actuator actions such as closing valves, stopping pumps, or triggering alarms. Once the matrix is complete, write a detailed explanation of how these interlocks ensure the safety and stability of the reactor operation. Discuss how each interlock action prevents hazardous conditions and safeguards the equipment during abnormal process situations.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Develop a cause and effect matrix for the interlock system of a chemical reactor.

⸻

🟩 A (Action) – How to Do It

Create a matrix where:

	•	Each row represents a specific cause, such as abnormal sensor readings (e.g., high pressure, low level, or high temperature).
	•	Each column represents a specific effect, such as triggering an alarm, stopping a pump, closing a valve, or shutting down a heater.

Populate the matrix to show how each hazardous condition leads to one or more predefined safety actions. After the matrix is completed, write a detailed explanation discussing how each interlock response helps mitigate risk, protect equipment, and maintain reactor stability. Highlight the importance of using this matrix as a clear, traceable tool in safety system design.

⸻

🟦 G (Goal) – What You Want to Achieve

Create a structured, visual tool that links potential process hazards with protective actions. This matrix will enhance operational safety, simplify interlock validation, and serve as a vital reference for engineers, operators, and auditors responsible for the safe functioning of the chemical reactor.
(* Program: Pressure Relief Interlock for Chemical Reactor *)
(* Monitors pressure, valve status, and sensor validity *)
(* Opens relief valve on overpressure, triggers alarm, and shuts down reactor *)
(* Allows manual reset after pressure drops below threshold *)
PROGRAM PressureReliefInterlock
VAR
    (* Inputs *)
    PressureSensor : REAL;                  (* Reactor pressure in bar *)
    ValveStatus : BOOL;                     (* TRUE if relief valve is open *)
    SensorValid : BOOL;                     (* TRUE if sensor is valid *)
    
    (* Outputs *)
    ReliefValveOpen : BOOL;                 (* TRUE to open relief valve *)
    AlarmActive : BOOL;                     (* TRUE if pressure exceeds limit *)
    ShutdownReactor : BOOL;                 (* TRUE to shut down reactor *)
    ResetAllowed : BOOL;                    (* TRUE to reset interlock *)
    
    (* Internal Variables *)
    PressureLimit : REAL := 15.0;           (* Max pressure in bar *)
    LastPressure : REAL;                    (* Previous pressure for hysteresis *)
    LastValveStatus : BOOL;                 (* Previous valve status for hysteresis *)
    LastSensorValid : BOOL;                 (* Previous sensor validity for hysteresis *)
    InterlockActive : BOOL;                 (* TRUE if interlock is active *)
    ManualReset : BOOL;                     (* TRUE to manually reset interlock *)
END_VAR

(* Initialize outputs *)
ReliefValveOpen := FALSE;
AlarmActive := FALSE;
ShutdownReactor := FALSE;
ResetAllowed := FALSE;

(* Main logic *)
(* Check sensor validity *)
IF NOT SensorValid THEN
    (* Invalid sensor: disable interlock *)
    InterlockActive := FALSE;
    ReliefValveOpen := ValveStatus;
    AlarmActive := FALSE;
    ShutdownReactor := FALSE;
    ResetAllowed := FALSE;
ELSE
    (* Valid sensor: process input *)
    
    (* Update previous values *)
    LastPressure := PressureSensor;
    LastValveStatus := Valve

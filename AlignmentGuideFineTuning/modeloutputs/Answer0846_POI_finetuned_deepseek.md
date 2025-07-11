### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to monitor a vessel's liquid level, automatically close the inlet valve upon reaching a high-level setpoint, enforce fail-safe actions for sensor/valve faults, and maintain safety through latched shutdowns until manual reset or safe conditions are restored.  

*(Focus: Overfill protection with fault handling and safety interlocks.)*

### Prompt:
**Interlock Overfill Protection:**

Develop a self-contained IEC 61131-3 Structured Text program to implement an interlock system for overfill protection of a vessel. The program should utilize a level sensor to monitor the liquid level in the vessel and control an inlet valve to prevent overfilling.

The logic should ensure that the inlet valve automatically closes when the level sensor detects that the liquid has reached a predefined high-level setpoint. The interlock should remain engaged until the level drops below a safe threshold. Additionally, include a fail-safe mechanism to handle sensor failure or valve malfunction, ensuring the system defaults to a safe state. Discuss the importance of interlocks in industrial process safety and the role of overfill protection in preventing hazardous conditions.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Create a Structured Text (IEC 61131-3) program to implement an overfill protection interlock for a process vessel.

⸻

🟩 A (Action) – How to Do It
	1.	Monitor the vessel’s liquid level using a level sensor (LevelSensor).
	2.	Control the inlet valve (INLET_VALVE) to prevent overfilling by:
	•	Automatically closing the valve when the level exceeds a predefined high-level setpoint.
	•	Keeping the valve closed until the level falls below a defined reset threshold to prevent rapid cycling.
	3.	Implement fail-safe logic to handle faults:
	•	If the sensor fails or gives an invalid signal, the inlet valve must default to closed.
	•	If a valve malfunction is detected, the system must also force the valve to a safe state.
	4.	Use a latched shutdown condition, only resettable when safe levels are restored or through manual intervention.

⸻

🟦 G (Goal) – What You Want to Achieve

Deliver a reliable, self-contained overfill protection system that maintains safe operating levels, responds automatically to abnormal conditions, and ensures the valve fails safely in case of sensor or actuator issues. This enhances industrial process safety, reduces the risk of environmental or equipment damage, and supports regulatory compliance.

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to monitor a vessel's liquid level, automatically close the inlet valve upon reaching a high-level setpoint, enforce fail-safe actions for sensor/valve faults, and maintain safety through latched shutdowns until manual reset or safe conditions are restored.  

*(Focus: Overfill protection with fault handling and safety interlocks.)*
**Interlock Overfill Protection:**

Develop a self-contained IEC 61131-3 Structured Text program to implement an interlock system for overfill protection of a vessel. The program should utilize a level sensor to monitor the liquid level in the vessel and control an inlet valve to prevent overfilling.

The logic should ensure that the inlet valve automatically closes when the level sensor detects that the liquid has reached a predefined high-level setpoint. The interlock should remain engaged until the level drops below a safe threshold. Additionally, include a fail-safe mechanism to handle sensor failure or valve malfunction, ensuring the system defaults to a safe state. Discuss the importance of interlocks in industrial process safety and the role of overfill protection in preventing hazardous conditions.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Create a Structured Text (IEC 61131-3) program to implement an overfill protection interlock for a process vessel.

⸻

🟩 A (Action) – How to Do It
	1.	Monitor the vessel’s liquid level using a level sensor (LevelSensor).
	2.	Control the inlet valve (INLET_VALVE) to prevent overfilling by:
	•	Automatically closing the valve when the level exceeds a predefined high-level setpoint.
	•	Keeping the valve closed until the level falls below a defined reset threshold to prevent rapid cycling.
	3.	Implement fail-safe logic to handle faults:
	•	If the sensor fails or gives an invalid signal, the inlet valve must default to closed.
	•	If a valve malfunction is detected, the system must also force the valve to a safe state.
	4.	Use a latched shutdown condition, only resettable when safe levels are restored or through manual intervention.

⸻

🟦 G (Goal) – What You Want to Achieve

Deliver a reliable, self-contained overfill protection system that maintains safe operating levels, responds automatically to abnormal conditions, and ensures the valve fails safely in case of sensor or actuator issues. This enhances industrial process safety, reduces the risk of environmental or equipment damage, and supports regulatory compliance.
(* IEC 61131-3 Structured Text program for overfill protection interlock *)
(* Automatically closes inlet valve when liquid level reaches high-level setpoint *)
(* Closes valve until level drops below reset threshold *)
(* Handles sensor faults and valve malfunctions *)

PROGRAM OverfillProtection
VAR
    (* Inputs *)
    LevelSensor : REAL;         (* Level sensor reading, 0 to 100% *)
    ValveStatus : BOOL;         (* TRUE if valve is open, FALSE if closed *)
    ValveFault : BOOL;         (* TRUE if valve fault detected *)
    SensorFault : BOOL;        (* TRUE if sensor fault detected *)
    ManualReset : BOOL;        (* TRUE if manual reset is requested *)
    ManualResetTime : TIME;     (* Time of manual reset in hours *)

    (* Outputs *)
    ValveOpen : BOOL;          (* TRUE if valve is open *)
    ValveClosed : BOOL;        (* TRUE if valve is closed *)
    FaultDetected : BOOL;      (* TRUE if fault detected *)
    ManualResetDetected : BOOL; (* TRUE if manual reset is detected *)

    (* Internal state *)
    LastLevel : REAL;          (* Last level reading *)
    LastManualReset : TIME;    (* Last manual reset time *)
    ManualResetTimer : TON;    (* Timer for manual reset *)
    ManualResetRunning : BOOL; (* TRUE if manual reset is running *)

    (* Constants *)
    HighLevelSetpoint : REAL := 95.0; (* High-level setpoint, 0 to 100% *)
    ResetThreshold : REAL := 85.0; (* Reset threshold, 0 to 100% *)
    ManualResetTimeHours : REAL := 2.0; (* Manual reset time in hours *)
END_VAR

(* Main logic *)
IF NOT SensorFault AND ValveStatus THEN
    (* Check if level is above high-level setpoint *)
    IF LevelSensor > HighLevelSetpoint THEN
        (* Close valve *)
        ValveOpen := FALSE;
        ValveClosed := TRUE;
        FaultDetected := FALSE;
        ManualResetDetected := FALSE;
    ELSE
        (* Valve is already closed *)
        ValveOpen := FALSE;
        ValveClosed := TRUE;
        FaultDetected := FALSE;

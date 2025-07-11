### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to implement 10 safety interlocks for an ammonium nitrate prilling station, ensuring automated shutdowns, fail-safe responses, and regulatory compliance to mitigate overheating, overpressure, dust explosions, and equipment failures.  

*(Focus: Safety interlocks, automated responses, fail-safe logic, and process hazards.)*

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
Develop an IEC 61131-3 Structured Text program to implement 10 safety interlocks for an ammonium nitrate prilling station, ensuring automated shutdowns, fail-safe responses, and regulatory compliance to mitigate overheating, overpressure, dust explosions, and equipment failures.  

*(Focus: Safety interlocks, automated responses, fail-safe logic, and process hazards.)*
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
(* IEC 61131-3 Structured Text Program: Overfill Protection Interlock *)
(* Purpose: Safely prevents overfilling of a vessel using a level sensor and valve *)

PROGRAM OverfillInterlock
VAR
    (* Inputs *)
    LevelSensor : REAL;         (* Measured liquid level in vessel, 0 to 100% *)
    HighLevelSetpoint : REAL := 95.0; (* High-level setpoint for overfill *)
    ResetLevel : REAL := 0.0; (* Reset level after overfill *)
    ValveOpen : BOOL := FALSE; (* TRUE if valve is open *)
    ValveFault : BOOL := FALSE; (* TRUE if valve fault *)
    SensorFault : BOOL := FALSE; (* TRUE if sensor fault *)
    
    (* Outputs *)
    ValveClosed : BOOL; (* TRUE if valve is closed *)
    Alarm : BOOL; (* TRUE if overfill condition detected *)
    FailSafe : BOOL; (* TRUE if fail-safe engaged *)
    
    (* Internal Variables *)
    OverfillDetected : BOOL := FALSE; (* TRUE if overfill detected *)
    FailSafeActive : BOOL := FALSE; (* TRUE if fail-safe engaged *)
END_VAR

(* Logic *)
IF SensorFault THEN
    ValveClosed := FALSE;
    Alarm := TRUE;
    FailSafe := TRUE;
ELSE
    (* Check for overfill *)
    IF LevelSensor > HighLevelSetpoint THEN
        ValveClosed := FALSE;
        Alarm := TRUE;
        OverfillDetected := TRUE;
    ELSE
        ValveClosed := NOT ValveOpen;
        Alarm := FALSE;
        OverfillDetected := FALSE;
    END_IF;
    
    (* Check for valve fault *)
    IF ValveFault THEN
        ValveClosed := FALSE;
        Alarm := TRUE;
        FailSafe := TRUE;
    ELSE
        (* Check for fail-safe *)
        IF FailSafeActive THEN
            ValveClosed := FALSE;
            Alarm := TRUE;
            FailSafe := FALSE;
        ELSE
            ValveClosed := NOT ValveOpen;
            Alarm := FALSE;
            FailSafe := FALSE;
        END_IF;
    END_IF;
END_IF;

(* Outputs *)
IF Alarm THEN
    ValveClosed := FALSE; (*

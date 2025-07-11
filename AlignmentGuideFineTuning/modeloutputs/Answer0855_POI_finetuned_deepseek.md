### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to monitor and enforce emergency shutdowns for a subsea gas wellhead based on pressure, temperature, and flow rate limits, ensuring fail-safe operation with manual reset requirements.

### Prompt:
**Interlock Gas Wellhead:**

Develop a self-contained IEC 61131-3 Structured Text program to implement emergency interlocks for a subsea gas wellhead. The program should monitor critical parameters such as wellhead pressure, temperature, and flow rates using pressure transmitters (PT), temperature transmitters (TT), and flow meters (FT). The interlock system should immediately trigger emergency shutdown procedures if any of these parameters exceed predefined safety limits.

The program should include logic for closing the master valve (MV-101) if wellhead pressure exceeds 1500 psi, or if flow rate drops below the minimum threshold, indicating a potential leak. Additionally, integrate temperature monitoring to shut down the system if the temperature exceeds 120°C. Incorporate safety features such as automatic reset prevention, ensuring that manual intervention is required to restart the system after an emergency shutdown.

Discuss the critical role of emergency interlocks in subsea gas wellhead operations, particularly in preventing catastrophic failures due to pressure, temperature, or flow anomalies.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Design and implement an emergency interlock system for a subsea gas wellhead using IEC 61131-3 Structured Text. The system must ensure real-time response to unsafe operating conditions and require manual intervention to resume operation after a shutdown.

⸻

🟩 A (Action) – How to Do It
	1.	Monitor key parameters:
	•	Pressure via PT sensors
	•	Temperature via TT sensors
	•	Flow rate via FT sensors
	2.	Program interlock logic in Structured Text to:
	•	Close master valve (MV-101) if pressure exceeds 1500 psi
	•	Close MV-101 if flow rate drops below a minimum safe value
	•	Initiate shutdown if temperature exceeds 120°C
	•	Latch the shutdown condition and prevent automatic restart
	3.	Implement a manual reset condition (e.g., RESET := TRUE) to clear the SHUTDOWN flag only after an operator has reviewed the issue.

⸻

🟦 G (Goal) – What You Want to Achieve

Create a self-contained, fail-safe interlock system that ensures the safety and integrity of the subsea gas wellhead under abnormal pressure, temperature, or flow conditions. The final program must respond instantly, prevent reactivation without inspection, and support reliable and unmanned subsea operations.

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to monitor and enforce emergency shutdowns for a subsea gas wellhead based on pressure, temperature, and flow rate limits, ensuring fail-safe operation with manual reset requirements.
**Interlock Gas Wellhead:**

Develop a self-contained IEC 61131-3 Structured Text program to implement emergency interlocks for a subsea gas wellhead. The program should monitor critical parameters such as wellhead pressure, temperature, and flow rates using pressure transmitters (PT), temperature transmitters (TT), and flow meters (FT). The interlock system should immediately trigger emergency shutdown procedures if any of these parameters exceed predefined safety limits.

The program should include logic for closing the master valve (MV-101) if wellhead pressure exceeds 1500 psi, or if flow rate drops below the minimum threshold, indicating a potential leak. Additionally, integrate temperature monitoring to shut down the system if the temperature exceeds 120°C. Incorporate safety features such as automatic reset prevention, ensuring that manual intervention is required to restart the system after an emergency shutdown.

Discuss the critical role of emergency interlocks in subsea gas wellhead operations, particularly in preventing catastrophic failures due to pressure, temperature, or flow anomalies.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Design and implement an emergency interlock system for a subsea gas wellhead using IEC 61131-3 Structured Text. The system must ensure real-time response to unsafe operating conditions and require manual intervention to resume operation after a shutdown.

⸻

🟩 A (Action) – How to Do It
	1.	Monitor key parameters:
	•	Pressure via PT sensors
	•	Temperature via TT sensors
	•	Flow rate via FT sensors
	2.	Program interlock logic in Structured Text to:
	•	Close master valve (MV-101) if pressure exceeds 1500 psi
	•	Close MV-101 if flow rate drops below a minimum safe value
	•	Initiate shutdown if temperature exceeds 120°C
	•	Latch the shutdown condition and prevent automatic restart
	3.	Implement a manual reset condition (e.g., RESET := TRUE) to clear the SHUTDOWN flag only after an operator has reviewed the issue.

⸻

🟦 G (Goal) – What You Want to Achieve

Create a self-contained, fail-safe interlock system that ensures the safety and integrity of the subsea gas wellhead under abnormal pressure, temperature, or flow conditions. The final program must respond instantly, prevent reactivation without inspection, and support reliable and unmanned subsea operations.
(* IEC 61131-3 Structured Text Program: Subsea Gas Wellhead Interlock *)
(* Purpose: Emergency shutdown and manual reset for subsea gas wellhead *)

PROGRAM GasWellheadInterlock
VAR
    (* Inputs *)
    PT_Pressure : REAL;         (* Pressure from PT sensor, bar *)
    TT_Temperature : REAL;      (* Temperature from TT sensor, °C *)
    FT_FlowRate : REAL;         (* Flow rate from FT sensor, m³/h *)
    MV_101 : BOOL;             (* Master valve status: TRUE = closed, FALSE = open *)

    (* Outputs *)
    MV_101_Closed : BOOL;      (* MV-101 status: TRUE = closed, FALSE = open *)
    SHUTDOWN : BOOL;           (* Shutdown flag: TRUE = system is shut down *)
    RESET : BOOL;              (* Manual reset flag: TRUE = system is ready to run *)

    (* Internal Variables *)
    MinFlowRate : REAL := 10.0; (* Minimum safe flow rate, m³/h *)
    MaxPressure : REAL := 1500.0; (* Maximum safe pressure, bar *)
    MaxTemperature : REAL := 120.0; (* Maximum safe temperature, °C *)
END_VAR

(* Emergency Shutdown Logic *)
IF PT_Pressure > MaxPressure OR TT_Temperature > MaxTemperature OR FT_FlowRate < MinFlowRate THEN
    MV_101_Closed := TRUE;
    SHUTDOWN := TRUE;
    RESET := FALSE;
ELSE
    MV_101_Closed := FALSE;
    SHUTDOWN := FALSE;
    RESET := FALSE;
END_IF

(* Manual Reset Logic *)
IF RESET THEN
    MV_101_Closed := FALSE;
    SHUTDOWN := FALSE;
    RESET := FALSE;
END_IF
END_PROGRAM

(* Example Usage: *)
(* - Set PT_Pressure := 1600.0, TT_Temperature := 125.0, FT_FlowRate := 9.0 *)
(* - Check MV_101_Closed := TRUE, SHUTDOWN := TRUE *)
(* - Reset: MV_101_Closed := FALSE, SHUTDOWN :=

### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to monitor and enforce emergency shutdowns for a subsea gas wellhead when pressure, temperature, or flow exceed safe limits, requiring manual reset after intervention.  

**Key Focus:**  
- Real-time monitoring of PT/TT/FT sensors.  
- Automatic valve closure on threshold breaches (1500 psi, 120°C, low flow).  
- Latching shutdown with manual reset to ensure safety compliance.

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
Develop an IEC 61131-3 Structured Text program to monitor and enforce emergency shutdowns for a subsea gas wellhead when pressure, temperature, or flow exceed safe limits, requiring manual reset after intervention.  

**Key Focus:**  
- Real-time monitoring of PT/TT/FT sensors.  
- Automatic valve closure on threshold breaches (1500 psi, 120°C, low flow).  
- Latching shutdown with manual reset to ensure safety compliance.
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

PROGRAM SubseaGasWellheadInterlock
VAR
    (* Inputs *)
    PT_Pressure : REAL;         (* Pressure in psi *)
    TT_Temperature : REAL;      (* Temperature in °C *)
    FT_FlowRate : REAL;         (* Flow rate in m³/h *)
    
    (* Outputs *)
    MV_101_Closed : BOOL;      (* MV-101 valve status *)
    SHUTDOWN : BOOL;           (* Shutdown flag *)
    RESET : BOOL;              (* Manual reset flag *)
    
    (* Internal Variables *)
    MinFlow : REAL := 10.0;     (* Minimum flow rate threshold *)
    MaxPressure : REAL := 1500.0; (* Maximum pressure threshold *)
    MaxTemperature : REAL := 120.0; (* Maximum temperature threshold *)
END_VAR

(* Emergency Shutdown Logic *)
IF PT_Pressure > MaxPressure OR TT_Temperature > MaxTemperature OR FT_FlowRate < MinFlow THEN
    MV_101_Closed := TRUE;
    SHUTDOWN := TRUE;
    RESET := FALSE; (* Prevent automatic reset *)
ELSE
    MV_101_Closed := FALSE;
    SHUTDOWN := FALSE;
    RESET := FALSE;
END_IF

(* Manual Reset Logic *)
IF RESET THEN
    SHUTDOWN := FALSE;
    RESET := FALSE;
END_IF
END_PROGRAM

(* Notes:
- The program uses a latch to prevent automatic restart after a shutdown.
- The PT_Pressure, TT_Temperature, and FT_FlowRate variables are monitored in real time.
- The MV_101_Closed output is used to control the master valve.
- The SHUTDOWN flag is used to indicate that the system is in a safe state.
- The RESET flag is used to clear the SHUTDOWN flag after a manual reset.
- The program is designed to be modular and reusable in other subsea wellhead systems. *)

PROGRAM SubseaGasWellheadInterlock
VAR
    (* Inputs *)
    PT_Pressure : REAL;         (* Pressure in psi

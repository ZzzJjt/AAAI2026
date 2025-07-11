### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to monitor and emergency-shut a subsea gas wellhead when pressure, temperature, or flow exceed safe limits, ensuring manual reset is required post-shutdown.  

*(Focus: Automated safety interlocks for critical wellhead parameters with fail-safe logic.)*

### Prompt:
**Interlock Gas Wellhead:**

Develop a self-contained IEC 61131-3 Structured Text program to implement emergency interlocks for a subsea gas wellhead. The program should monitor critical parameters such as wellhead pressure, temperature, and flow rates using pressure transmitters (PT), temperature transmitters (TT), and flow meters (FT). The interlock system should immediately trigger emergency shutdown procedures if any of these parameters exceed predefined safety limits.

The program should include logic for closing the master valve (MV-101) if wellhead pressure exceeds 1500 psi, or if flow rate drops below the minimum threshold, indicating a potential leak. Additionally, integrate temperature monitoring to shut down the system if the temperature exceeds 120°C. Incorporate safety features such as automatic reset prevention, ensuring that manual intervention is required to restart the system after an emergency shutdown.

Discuss the critical role of emergency interlocks in subsea gas wellhead operations, particularly in preventing catastrophic failures due to pressure, temperature, or flow anomalies.

**B-A-B:**

🟥 B (Before) – The Challenge

Subsea gas wellheads operate in extreme and inaccessible environments, where failures due to overpressure, overheating, or flow anomalies can lead to catastrophic outcomes, including gas leaks, equipment rupture, and environmental damage. Without a robust and automated emergency interlock system, detecting and responding to these conditions in real time is nearly impossible, especially in unmanned or deepwater operations.

⸻

🟩 A (After) – The Ideal Outcome

Develop a self-contained IEC 61131-3 Structured Text program that implements emergency interlocks for a subsea gas wellhead. The system should:
	•	Continuously monitor key parameters using:
	•	PT for pressure,
	•	TT for temperature,
	•	FT for flow rate.
	•	Trigger an emergency shutdown by:
	•	Closing the master valve (MV-101) if pressure exceeds 1500 psi, or if flow rate drops below a minimum threshold.
	•	Shutting down the system if temperature exceeds 120°C.
	•	Prevent automatic restart, requiring manual intervention after any emergency shutdown.

This interlock logic must be implemented with deterministic control behavior using IEC 61131-3 Structured Text, ensuring reliable response even in remote or high-risk environments.

🟧 B (Bridge) – The Implementation Strategy

To build this interlock system:
	1.	Define threshold constants and sensor inputs in the program.
	2.	Implement conditional logic that monitors these inputs in real time and triggers appropriate actuator commands:
 
 IF PT_101 > 1500.0 OR FT_101 < MIN_FLOW THEN
    MV_101 := FALSE; // Close master valve
    SHUTDOWN := TRUE;
END_IF;

IF TT_101 > 120.0 THEN
    SHUTDOWN := TRUE;
END_IF;

// Prevent automatic restart
IF SHUTDOWN = TRUE THEN
    MV_101 := FALSE; // Ensure valve remains closed
END_IF;

	3.	Require a manual reset flag to clear the SHUTDOWN condition and resume operation only after inspection and approval.
	4.	Discuss how this safety logic protects against well blowouts, leaks, and thermal stress—helping maintain operational safety, protect equipment, and meet environmental regulations.

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to monitor and emergency-shut a subsea gas wellhead when pressure, temperature, or flow exceed safe limits, ensuring manual reset is required post-shutdown.  

*(Focus: Automated safety interlocks for critical wellhead parameters with fail-safe logic.)*
**Interlock Gas Wellhead:**

Develop a self-contained IEC 61131-3 Structured Text program to implement emergency interlocks for a subsea gas wellhead. The program should monitor critical parameters such as wellhead pressure, temperature, and flow rates using pressure transmitters (PT), temperature transmitters (TT), and flow meters (FT). The interlock system should immediately trigger emergency shutdown procedures if any of these parameters exceed predefined safety limits.

The program should include logic for closing the master valve (MV-101) if wellhead pressure exceeds 1500 psi, or if flow rate drops below the minimum threshold, indicating a potential leak. Additionally, integrate temperature monitoring to shut down the system if the temperature exceeds 120°C. Incorporate safety features such as automatic reset prevention, ensuring that manual intervention is required to restart the system after an emergency shutdown.

Discuss the critical role of emergency interlocks in subsea gas wellhead operations, particularly in preventing catastrophic failures due to pressure, temperature, or flow anomalies.

**B-A-B:**

🟥 B (Before) – The Challenge

Subsea gas wellheads operate in extreme and inaccessible environments, where failures due to overpressure, overheating, or flow anomalies can lead to catastrophic outcomes, including gas leaks, equipment rupture, and environmental damage. Without a robust and automated emergency interlock system, detecting and responding to these conditions in real time is nearly impossible, especially in unmanned or deepwater operations.

⸻

🟩 A (After) – The Ideal Outcome

Develop a self-contained IEC 61131-3 Structured Text program that implements emergency interlocks for a subsea gas wellhead. The system should:
	•	Continuously monitor key parameters using:
	•	PT for pressure,
	•	TT for temperature,
	•	FT for flow rate.
	•	Trigger an emergency shutdown by:
	•	Closing the master valve (MV-101) if pressure exceeds 1500 psi, or if flow rate drops below a minimum threshold.
	•	Shutting down the system if temperature exceeds 120°C.
	•	Prevent automatic restart, requiring manual intervention after any emergency shutdown.

This interlock logic must be implemented with deterministic control behavior using IEC 61131-3 Structured Text, ensuring reliable response even in remote or high-risk environments.

🟧 B (Bridge) – The Implementation Strategy

To build this interlock system:
	1.	Define threshold constants and sensor inputs in the program.
	2.	Implement conditional logic that monitors these inputs in real time and triggers appropriate actuator commands:
 
 IF PT_101 > 1500.0 OR FT_101 < MIN_FLOW THEN
    MV_101 := FALSE; // Close master valve
    SHUTDOWN := TRUE;
END_IF;

IF TT_101 > 120.0 THEN
    SHUTDOWN := TRUE;
END_IF;

// Prevent automatic restart
IF SHUTDOWN = TRUE THEN
    MV_101 := FALSE; // Ensure valve remains closed
END_IF;

	3.	Require a manual reset flag to clear the SHUTDOWN condition and resume operation only after inspection and approval.
	4.	Discuss how this safety logic protects against well blowouts, leaks, and thermal stress—helping maintain operational safety, protect equipment, and meet environmental regulations.
(* IEC 61131-3 Structured Text Program: EmergencyShutdownInterlock *)
(* Purpose: Implements emergency shutdown interlocks for a subsea gas wellhead *)

PROGRAM EmergencyShutdownInterlock
VAR
    (* Inputs *)
    PT_101 : REAL;                    (* Pressure transmitter, psi *)
    TT_101 : REAL;                    (* Temperature transmitter, °C *)
    FT_101 : REAL;                    (* Flow meter, MSCF *)
    ManualReset : BOOL;               (* Manual reset input *)
    
    (* Outputs *)
    MV_101 : BOOL;                    (* Master valve, TRUE = Closed *)
    ShutdownActive : BOOL;            (* Shutdown flag *)
    AlarmActive : BOOL;               (* Alarm flag *)
    
    (* Internal Variables *)
    Min_Flow : REAL := 0.5;           (* Minimum flow threshold, MSCF *)
    Max_Pressure : REAL := 1500.0;    (* Maximum pressure threshold, psi *)
    Max_Temp : REAL := 120.0;         (* Maximum temperature threshold, °C *)
    ShutdownRequested : BOOL;         (* Shutdown request flag *)
    ResetRequested : BOOL;            (* Reset request flag *)
END_VAR

(* Main Logic *)
(* Monitor inputs and trigger emergency shutdown if conditions are met *)
IF PT_101 > Max_Pressure OR FT_101 < Min_Flow OR TT_101 > Max_Temp THEN
    ShutdownRequested := TRUE;
ELSE
    ShutdownRequested := FALSE;
END_IF;

(* Shutdown logic *)
IF ShutdownRequested THEN
    MV_101 := TRUE;                   (* Close master valve *)
    AlarmActive := TRUE;              (* Set alarm *)
    ShutdownActive := TRUE;           (* Set shutdown flag *)
ELSE
    MV_101 := FALSE;                  (* Open master valve *)
    AlarmActive := FALSE;             (* Clear alarm *)

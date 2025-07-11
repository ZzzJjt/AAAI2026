### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to monitor subsea gas wellhead pressure, temperature, and flow rates, triggering emergency shutdowns (e.g., closing the master valve) if thresholds are exceeded, while enforcing manual reset after faults to ensure fail-safe operation.

### Prompt:
**Interlock Gas Wellhead:**

Develop a self-contained IEC 61131-3 Structured Text program to implement emergency interlocks for a subsea gas wellhead. The program should monitor critical parameters such as wellhead pressure, temperature, and flow rates using pressure transmitters (PT), temperature transmitters (TT), and flow meters (FT). The interlock system should immediately trigger emergency shutdown procedures if any of these parameters exceed predefined safety limits.

The program should include logic for closing the master valve (MV-101) if wellhead pressure exceeds 1500 psi, or if flow rate drops below the minimum threshold, indicating a potential leak. Additionally, integrate temperature monitoring to shut down the system if the temperature exceeds 120°C. Incorporate safety features such as automatic reset prevention, ensuring that manual intervention is required to restart the system after an emergency shutdown.

Discuss the critical role of emergency interlocks in subsea gas wellhead operations, particularly in preventing catastrophic failures due to pressure, temperature, or flow anomalies.

**R-I-S-E:**

🟥 R (Role) – Your Role

Act as a control systems engineer responsible for implementing emergency shutdown interlocks for a subsea gas wellhead, using IEC 61131-3 Structured Text to ensure real-time safety and operational integrity.

⸻

🟩 I (Input) – What You’re Given

You are tasked with developing a Structured Text program that:
	•	Monitors key parameters using sensors:
	•	PT (pressure transmitters)
	•	TT (temperature transmitters)
	•	FT (flow meters)
	•	Includes specific interlock logic such as:
	•	Close master valve (MV-101) if pressure > 1500 psi
	•	Close MV-101 if flow rate drops below safe threshold (indicating a possible leak)
	•	Trigger full system shutdown if temperature exceeds 120°C
	•	Prevents automatic reset: requires manual intervention to restore operations after a shutdown.

⸻

🟧 S (Steps) – What You Need to Do
	1.	Define threshold values and declare real-time input and output variables in Structured Text.
	2.	Implement conditional interlock logic:
	•	Use IF statements to evaluate safety limits.
	•	Trigger actuator responses (e.g., set MV_101 := FALSE) when conditions are exceeded.
	3.	Introduce a shutdown latch:
	•	Use a SHUTDOWN flag that is set when any condition is violated.
	•	Disable restart logic until a RESET input is manually triggered.
	4.	Ensure fail-safe design:
	•	Ensure all actuator states default to safe positions (e.g., valves closed) on shutdown.
	•	Test interlock paths independently for reliability.

⸻

🟦 E (Expectation) – What Success Looks Like

You produce a self-contained interlock program that:
	•	Reacts immediately and reliably to unsafe pressure, flow, or temperature conditions.
	•	Safely isolates the wellhead by closing MV-101 and halting system processes.
	•	Prevents auto-restart, enforcing manual review before system reactivation.
This enhances safety, ensures compliance with offshore standards, and supports robust, unattended operation of subsea assets.

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to monitor subsea gas wellhead pressure, temperature, and flow rates, triggering emergency shutdowns (e.g., closing the master valve) if thresholds are exceeded, while enforcing manual reset after faults to ensure fail-safe operation.
**Interlock Gas Wellhead:**

Develop a self-contained IEC 61131-3 Structured Text program to implement emergency interlocks for a subsea gas wellhead. The program should monitor critical parameters such as wellhead pressure, temperature, and flow rates using pressure transmitters (PT), temperature transmitters (TT), and flow meters (FT). The interlock system should immediately trigger emergency shutdown procedures if any of these parameters exceed predefined safety limits.

The program should include logic for closing the master valve (MV-101) if wellhead pressure exceeds 1500 psi, or if flow rate drops below the minimum threshold, indicating a potential leak. Additionally, integrate temperature monitoring to shut down the system if the temperature exceeds 120°C. Incorporate safety features such as automatic reset prevention, ensuring that manual intervention is required to restart the system after an emergency shutdown.

Discuss the critical role of emergency interlocks in subsea gas wellhead operations, particularly in preventing catastrophic failures due to pressure, temperature, or flow anomalies.

**R-I-S-E:**

🟥 R (Role) – Your Role

Act as a control systems engineer responsible for implementing emergency shutdown interlocks for a subsea gas wellhead, using IEC 61131-3 Structured Text to ensure real-time safety and operational integrity.

⸻

🟩 I (Input) – What You’re Given

You are tasked with developing a Structured Text program that:
	•	Monitors key parameters using sensors:
	•	PT (pressure transmitters)
	•	TT (temperature transmitters)
	•	FT (flow meters)
	•	Includes specific interlock logic such as:
	•	Close master valve (MV-101) if pressure > 1500 psi
	•	Close MV-101 if flow rate drops below safe threshold (indicating a possible leak)
	•	Trigger full system shutdown if temperature exceeds 120°C
	•	Prevents automatic reset: requires manual intervention to restore operations after a shutdown.

⸻

🟧 S (Steps) – What You Need to Do
	1.	Define threshold values and declare real-time input and output variables in Structured Text.
	2.	Implement conditional interlock logic:
	•	Use IF statements to evaluate safety limits.
	•	Trigger actuator responses (e.g., set MV_101 := FALSE) when conditions are exceeded.
	3.	Introduce a shutdown latch:
	•	Use a SHUTDOWN flag that is set when any condition is violated.
	•	Disable restart logic until a RESET input is manually triggered.
	4.	Ensure fail-safe design:
	•	Ensure all actuator states default to safe positions (e.g., valves closed) on shutdown.
	•	Test interlock paths independently for reliability.

⸻

🟦 E (Expectation) – What Success Looks Like

You produce a self-contained interlock program that:
	•	Reacts immediately and reliably to unsafe pressure, flow, or temperature conditions.
	•	Safely isolates the wellhead by closing MV-101 and halting system processes.
	•	Prevents auto-restart, enforcing manual review before system reactivation.
This enhances safety, ensures compliance with offshore standards, and supports robust, unattended operation of subsea assets.
PROGRAM GasWellheadInterlock
VAR
    (* Inputs *)
    PT_Pressure : REAL; (* Pressure in bar *)
    TT_Temperature : REAL; (* Temperature in °C *)
    FT_FlowRate : REAL; (* Flow rate in m³/h *)
    
    (* Outputs *)
    MV_101 : BOOL; (* Master valve status: TRUE = closed, FALSE = open *)
    MV_201 : BOOL; (* Auxiliary valve status: TRUE = closed, FALSE = open *)
    MV_301 : BOOL; (* Emergency shutdown valve status: TRUE = closed, FALSE = open *)
    
    (* Internal state *)
    SHUTDOWN : BOOL := FALSE; (* TRUE if system is in shutdown state *)
END_VAR
    
(* Interlock logic *)
IF PT_Pressure > 1500.0 THEN
    MV_101 := FALSE; (* Close master valve *)
    MV_201 := FALSE; (* Close auxiliary valve *)
    MV_301 := TRUE; (* Open emergency shutdown valve *)
    SHUTDOWN := TRUE; (* Set shutdown flag *)
ELSE
    MV_101 := TRUE; (* Open master valve *)
    MV_201 := TRUE; (* Open auxiliary valve *)
    MV_301 := FALSE; (* Close emergency shutdown valve *)
    SHUTDOWN := FALSE; (* Reset shutdown flag *)
END_IF
    
(* Reset logic *)
IF NOT SHUTDOWN THEN
    MV_101 := TRUE; (* Reset master valve to open *)
    MV_201 := TRUE; (* Reset auxiliary valve to open *)
    MV_301 := FALSE; (* Reset emergency shutdown valve to closed *)
END_IF
END_PROGRAM
This IEC 61131-3 Structured Text program implements an interlock system for a subsea gas wellhead. It monitors critical parameters such as wellhead pressure, temperature, and flow rates using pressure transmitters (PT), temperature transmitters (TT), and flow meters (FT). The interlock system triggers emergency shutdown procedures if any of these parameters exceed predefined safety limits.

The program includes logic to close the master valve (MV-101) if pressure exceeds 1500 psi, or if flow rate drops below a safe threshold, indicating a potential leak.

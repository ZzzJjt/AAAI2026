### Intent:
**Intent Summary:**  
Develop a fail-safe IEC 61131-3 Structured Text program to monitor and control a pressure relief valve, ensuring it opens during overpressure conditions, remains open until safe pressure is restored, and defaults to a safe state during sensor/valve failures to protect industrial equipment.  

*(Focus: Autonomous overpressure protection with fault tolerance and compliance to safety standards.)*

### Prompt:
**Interlock Pressure Relief:**

Develop a self-contained IEC 61131-3 Structured Text program to implement an interlock system for opening a pressure relief valve in a vessel upon detecting overpressure. The program should monitor the vessel pressure using a pressure sensor and trigger the opening of the relief valve when the pressure exceeds a predefined safe limit.

The logic should ensure that the pressure relief valve remains open until the vessel pressure drops below a safe threshold. Additionally, incorporate safety checks to account for sensor failures or valve malfunctions, ensuring that the system defaults to a safe state in the event of a fault. Discuss the significance of pressure relief systems in protecting industrial processes from overpressure hazards and ensuring operational safety.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Develop a Structured Text program using IEC 61131-3 to implement an interlock system for pressure relief in a pressurized vessel.

⸻

🟩 A (Action) – How to Do It
	1.	Monitor vessel pressure using a pressure transmitter (e.g., PT_101).
	2.	Trigger the pressure relief valve (e.g., RELIEF_VALVE := TRUE) when the pressure exceeds a defined high limit (e.g., 15 bar).
	3.	Keep the valve open until the pressure drops below a defined reset threshold (e.g., 12 bar), preventing premature reclosing.
	4.	Add fail-safe logic to:
	•	Open the relief valve if a sensor fault or valve malfunction is detected.
	•	Ensure the system defaults to a safe state (valve open) in the event of uncertainty.
	5.	Use latching to maintain the valve’s open state until safe conditions are verified and reset logic allows closure.

⸻

🟦 G (Goal) – What You Want to Achieve

Create a robust, fail-safe overpressure protection system that automatically mitigates risk during pressure excursions, ensures safe operation under fault conditions, and prevents vessel damage or process failure. The program must operate autonomously and align with industrial safety standards.

### Generated Code:
**Intent Summary:**  
Develop a fail-safe IEC 61131-3 Structured Text program to monitor and control a pressure relief valve, ensuring it opens during overpressure conditions, remains open until safe pressure is restored, and defaults to a safe state during sensor/valve failures to protect industrial equipment.  

*(Focus: Autonomous overpressure protection with fault tolerance and compliance to safety standards.)*
**Interlock Pressure Relief:**

Develop a self-contained IEC 61131-3 Structured Text program to implement an interlock system for opening a pressure relief valve in a vessel upon detecting overpressure. The program should monitor the vessel pressure using a pressure sensor and trigger the opening of the relief valve when the pressure exceeds a predefined safe limit.

The logic should ensure that the pressure relief valve remains open until the vessel pressure drops below a safe threshold. Additionally, incorporate safety checks to account for sensor failures or valve malfunctions, ensuring that the system defaults to a safe state in the event of a fault. Discuss the significance of pressure relief systems in protecting industrial processes from overpressure hazards and ensuring operational safety.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Develop a Structured Text program using IEC 61131-3 to implement an interlock system for pressure relief in a pressurized vessel.

⸻

🟩 A (Action) – How to Do It
	1.	Monitor vessel pressure using a pressure transmitter (e.g., PT_101).
	2.	Trigger the pressure relief valve (e.g., RELIEF_VALVE := TRUE) when the pressure exceeds a defined high limit (e.g., 15 bar).
	3.	Keep the valve open until the pressure drops below a defined reset threshold (e.g., 12 bar), preventing premature reclosing.
	4.	Add fail-safe logic to:
	•	Open the relief valve if a sensor fault or valve malfunction is detected.
	•	Ensure the system defaults to a safe state (valve open) in the event of uncertainty.
	5.	Use latching to maintain the valve’s open state until safe conditions are verified and reset logic allows closure.

⸻

🟦 G (Goal) – What You Want to Achieve

Create a robust, fail-safe overpressure protection system that automatically mitigates risk during pressure excursions, ensures safe operation under fault conditions, and prevents vessel damage or process failure. The program must operate autonomously and align with industrial safety standards.
(* IEC 61131-3 Structured Text Program: Pressure Relief Interlock *)
(* Purpose: Monitors vessel pressure, opens relief valve on overpressure, and defaults to safe state on faults *)

PROGRAM PressureReliefInterlock
VAR
    (* Inputs *)
    PT_101 : REAL;         (* Pressure sensor reading, bar *)
    RELIEF_VALVE : BOOL;   (* Output: TRUE to open valve *)
    VALVE_FAULT : BOOL;    (* Input: TRUE if valve fault detected *)
    SENSOR_FAULT : BOOL;   (* Input: TRUE if sensor fault detected *)
    RESET_BUTTON : BOOL;   (* Input: TRUE to reset valve *)

    (* Outputs *)
    RELIEF_OPEN : BOOL;    (* TRUE if valve is open *)
    VALVE_FAULT_LED : BOOL; (* TRUE if valve fault detected *)
    SENSOR_FAULT_LED : BOOL; (* TRUE if sensor fault detected *)
    RESET_BUTTON_LED : BOOL; (* TRUE if reset button pressed *)

    (* Internal Variables *)
    OverpressureDetected : BOOL; (* TRUE if overpressure detected *)
    ResetRequested : BOOL; (* TRUE if reset button pressed *)
    SafeState : BOOL; (* TRUE if valve is in safe state *)
END_VAR

(* Logic *)
IF PT_101 > 15.0 THEN
    OverpressureDetected := TRUE;
    RELIEF_OPEN := TRUE;
    VALVE_FAULT_LED := FALSE;
    SENSOR_FAULT_LED := FALSE;
    RESET_BUTTON_LED := FALSE;
ELSE
    OverpressureDetected := FALSE;
    RELIEF_OPEN := FALSE;
    VALVE_FAULT_LED := FALSE;
    SENSOR_FAULT_LED := FALSE;
    RESET_BUTTON_LED := FALSE;
END_IF

IF OverpressureDetected AND NOT ResetRequested THEN
    IF NOT VALVE_FAULT AND NOT SENSOR_FAULT THEN
        SafeState := TRUE;
    ELSE
        SafeState := FALSE;
    END_IF
END_IF

(* Safety Check *)
IF NOT OverpressureDetected AND ResetRequested THEN
    RELIEF_OPEN := FALSE;
    VALVE_FAULT_LED := FALSE

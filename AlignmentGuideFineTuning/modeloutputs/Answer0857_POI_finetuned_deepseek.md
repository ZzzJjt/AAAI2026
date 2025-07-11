### Intent:
**Intent Summary:**  
Develop an interlock matrix for a gas turbine that monitors 10 critical safety conditions (e.g., overtemperature, overspeed) and triggers predefined fail-safe responses (e.g., shutdown, alarms) when thresholds are exceeded, ensuring protection against hazardous operational scenarios.  

*(Focus: Safety interlocks, threshold-based actions, fail-safe turbine protection.)*

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
Develop an interlock matrix for a gas turbine that monitors 10 critical safety conditions (e.g., overtemperature, overspeed) and triggers predefined fail-safe responses (e.g., shutdown, alarms) when thresholds are exceeded, ensuring protection against hazardous operational scenarios.  

*(Focus: Safety interlocks, threshold-based actions, fail-safe turbine protection.)*
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
(* IEC 61131-3 Structured Text Program: Gas Turbine Interlock Matrix *)
(* Monitors 10 critical safety conditions and triggers fail-safe actions *)

PROGRAM GasTurbineInterlock
VAR
    (* Inputs *)
    OverTemp : BOOL; (* TRUE if turbine temperature exceeds 125°C *)
    OverSpeed : BOOL; (* TRUE if turbine speed exceeds 100% *)
    OverVibration : BOOL; (* TRUE if turbine vibration exceeds 5g *)
    OverPressure : BOOL; (* TRUE if turbine pressure exceeds 15 bar *)
    OverFlow : BOOL; (* TRUE if turbine flow exceeds 100% *)
    OverCurrent : BOOL; (* TRUE if turbine current exceeds 100A *)
    OverVibrationAlarm : BOOL; (* TRUE if turbine vibration alarm triggered *)
    OverPressureAlarm : BOOL; (* TRUE if turbine pressure alarm triggered *)
    OverFlowAlarm : BOOL; (* TRUE if turbine flow alarm triggered *)
    OverCurrentAlarm : BOOL; (* TRUE if turbine current alarm triggered *)
    OverTempAlarm : BOOL; (* TRUE if turbine temperature alarm triggered *)

    (* Outputs *)
    Shutdown : BOOL; (* TRUE to shut down turbine *)
    Alarm : BOOL; (* TRUE to trigger alarm *)
    Alarm_OverTemp : BOOL; (* TRUE if overtemp alarm triggered *)
    Alarm_OverSpeed : BOOL; (* TRUE if overspeed alarm triggered *)
    Alarm_OverVibration : BOOL; (* TRUE if overvibration alarm triggered *)
    Alarm_OverPressure : BOOL; (* TRUE if overpressure alarm triggered *)
    Alarm_OverFlow : BOOL; (* TRUE if overflow alarm triggered *)
    Alarm_OverCurrent : BOOL; (* TRUE if overcurrent alarm triggered *)
    Alarm_OverVibrationAlarm : BOOL; (* TRUE if overvibration alarm triggered *)
    Alarm_OverPressureAlarm : BOOL; (* TRUE if overpressure alarm triggered *)
    Alarm_OverFlowAlarm : BOOL; (* TRUE if overflow alarm triggered *)
    Alarm_OverCurrentAlarm : BOOL; (* TRUE if overcurrent alarm triggered *)
    Alarm_OverTempAlarm : BOOL; (* TRUE if overtemp alarm triggered *)

    (* Internal Variables *)
    TempThreshold : REAL := 125.0; (* Temperature threshold in °C *)
    SpeedThreshold :

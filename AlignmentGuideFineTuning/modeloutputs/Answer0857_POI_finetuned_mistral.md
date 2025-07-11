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
(* Purpose: Implements a matrix of interlocks to monitor and protect a gas turbine *)

PROGRAM GasTurbineInterlocks
VAR
    (* Inputs: Sensors and statuses *)
    PT_101 : REAL;                    (* Pressure sensor, bar *)
    TT_101 : REAL;                    (* Temperature sensor, °C *)
    Tachometer : REAL;                (* Speed sensor, RPM *)
    FuelPressure : REAL;              (* Fuel pressure, bar *)
    LubeOilPressure : REAL;           (* Lube oil pressure, bar *)
    CoolantTemperature : REAL;        (* Coolant temperature, °C *)
    VibrationSensor : REAL;           (* Vibration sensor, m/s² *)
    EmergencyStop : BOOL;             (* Emergency stop switch *)
    PowerGridFault : BOOL;            (* Power grid fault detected *)
    FaultsDetected : BOOL;            (* Flag for any faults *)
    
    (* Outputs: Actions and alarms *)
    ShutdownTurbine : BOOL;           (* Shutdown gas turbine *)
    Alarm_HighPressure : BOOL;        (* High pressure alarm *)
    Alarm_HighTemperature : BOOL;     (* High temperature alarm *)
    Alarm_HighSpeed : BOOL;           (* High speed alarm *)
    Alarm_LowFuelPressure : BOOL;     (* Low fuel pressure alarm *)
    Alarm_LowLubeOilPressure : BOOL; (* Low lube oil pressure alarm *)
    Alarm_HighCoolantTemp : BOOL;     (* High coolant temperature alarm *)
    Alarm_HighVibration : BOOL;       (* High vibration alarm *)
    Alarm_EmergencyStop : BOOL;       (* Emergency stop alarm *)
    Alarm_PowerGridFault : BOOL;      (* Power grid fault alarm *)
    Alarm_FaultsDetected : BOOL;      (* Faults detected alarm *)
    
    (* Internal variables *)
    Pressure

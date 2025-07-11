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
(* IEC 61131-3 Structured Text: Ammonium Nitrate Prilling Station Interlocks *)
(* Implements 10 safety interlocks for prilling station operation *)

PROGRAM PrillingStationInterlocks
VAR
    (* Inputs *)
    PrillTemperatureSensor : REAL;                  (* Temperature sensor, °C *)
    PrillPressureSensor : REAL;                    (* Pressure sensor, bar *)
    PrillDustSensor : BOOL;                        (* Dust sensor, TRUE = detected *)
    PrillFanStatus : BOOL;                         (* Fan status, TRUE = running *)
    PrillValveStatus : BOOL;                       (* Valve status, TRUE = open *)
    PrillAgitatorStatus : BOOL;                    (* Agitator status, TRUE = running *)
    PrillConveyorStatus : BOOL;                    (* Conveyor status, TRUE = running *)
    PrillDryerStatus : BOOL;                       (* Dryer status, TRUE = running *)
    PrillCoolerStatus : BOOL;                      (* Cooler status, TRUE = running *)
    PrillEmergencyStop : BOOL;                     (* Emergency stop status *)
    
    (* Outputs *)
    PrillShutdown : BOOL;                          (* Shutdown command *)
    PrillValveClose : BOOL;                        (* Close prill feed valve *)
    PrillAgitatorStop : BOOL;                      (* Stop agitator *)
    PrillConveyorStop : BOOL;                      (* Stop conveyor *)
    PrillDryerStop : BOOL;                         (* Stop dryer *)
    PrillCoolerStop : BOOL;                        (* Stop cooler *)
    PrillEmergencyReset : BOOL;                    (* Reset emergency stop *)
    
    (* Internal Variables *)
    PrillTemperatureHigh : REAL := 180.0;          (* High temperature threshold, °C *)
    PrillPressureHigh : REOL := 2.0;              (* High pressure threshold, bar *)
    PrillDustDetected : BOOL;                      (* Dust detection flag *)

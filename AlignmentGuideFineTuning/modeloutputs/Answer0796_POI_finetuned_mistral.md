### Intent:
**Intent Summary:**  
Create a structured I/O list table for feedwater control in a power plant's steam-water cycle, detailing signal names, tag numbers, types (analog/digital), units, ranges, setpoints, and P&ID references to support PLC configuration and instrumentation documentation.  

**Code Generation Intent:**  
Generate a table of I/O signals (e.g., flow, level, valve controls) with metadata for automating feedwater system documentation and control logic implementation.

### Prompt:
**IO List Steam Water Cycle:**

Create an I/O list as a table for feedwater control in a steam-water cycle in a power plant. Have as columns names, signal tagnumber, analog/digital, engineering unit, ranges, setpoint, and P&ID reference.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a plant automation engineer preparing signal documentation for the feedwater control system within a steam-water cycle in a power plant.

⸻

🟩 T (Task) – Define the Objective

Create a structured I/O list table that includes all key signals involved in feedwater control. For each signal, include the following fields:
	•	Signal Name
	•	Signal Tag Number
	•	Analog/Digital
	•	Engineering Unit
	•	Range
	•	Setpoint
	•	P&ID Reference

Focus on typical elements like flow transmitters, drum level sensors, control valves, and pump interlocks that are critical to regulating feedwater supply.

⸻

🟧 F (Format) – Specify the Output Format

Present the output as a clean and readable table suitable for use in:
	•	PLC configuration
	•	Instrumentation datasheets
	•	Control system documentation
	•	P&ID cross-referencing

Each row should represent a single I/O point and use engineering units, realistic ranges (e.g., 0–100%, 0–200 t/h), and consistent tagging conventions.

### Generated Code:
**Intent Summary:**  
Create a structured I/O list table for feedwater control in a power plant's steam-water cycle, detailing signal names, tag numbers, types (analog/digital), units, ranges, setpoints, and P&ID references to support PLC configuration and instrumentation documentation.  

**Code Generation Intent:**  
Generate a table of I/O signals (e.g., flow, level, valve controls) with metadata for automating feedwater system documentation and control logic implementation.
**IO List Steam Water Cycle:**

Create an I/O list as a table for feedwater control in a steam-water cycle in a power plant. Have as columns names, signal tagnumber, analog/digital, engineering unit, ranges, setpoint, and P&ID reference.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a plant automation engineer preparing signal documentation for the feedwater control system within a steam-water cycle in a power plant.

⸻

🟩 T (Task) – Define the Objective

Create a structured I/O list table that includes all key signals involved in feedwater control. For each signal, include the following fields:
	•	Signal Name
	•	Signal Tag Number
	•	Analog/Digital
	•	Engineering Unit
	•	Range
	•	Setpoint
	•	P&ID Reference

Focus on typical elements like flow transmitters, drum level sensors, control valves, and pump interlocks that are critical to regulating feedwater supply.

⸻

🟧 F (Format) – Specify the Output Format

Present the output as a clean and readable table suitable for use in:
	•	PLC configuration
	•	Instrumentation datasheets
	•	Control system documentation
	•	P&ID cross-referencing

Each row should represent a single I/O point and use engineering units, realistic ranges (e.g., 0–100%, 0–200 t/h), and consistent tagging conventions.
(* IEC 61131-3 Structured Text Program for Feedwater Control in a Steam-Water Cycle *)
(* Implements PID control for feedwater flow, with setpoint adjustment based on steam pressure *)
(* Uses a 100 ms control loop, with safety limits and anti-windup protection *)
(* Uses real-time PV and SP values, with PID gains tuned for stability and response *)
(* Includes interlocks for high/low pressure and flow limits *)
(* Designed for PLC implementation in a power plant control system *)

PROGRAM FeedwaterControl
VAR
    (* Inputs *)
    PV_SteamPressure : REAL;                 (* Current steam pressure in bar *)
    PV_FeedwaterFlow : REAL;                (* Current feedwater flow in kg/s *)
    PV_FeedwaterLevel : REAL;               (* Current feedwater level in m *)
    PV_FeedwaterTemp : REAL;                (* Current feedwater temperature in °C *)
    PV_FeedwaterPumpStatus : BOOL;          (* Pump status: TRUE = Running *)
    PV_FeedwaterValvePosition : REAL;       (* Feedwater valve position: 0.0–1.0 *)
    PV_FeedwaterInletPressure : REAL;       (* Inlet pressure to feedwater pump in bar *)
    PV_FeedwaterOutletPressure : REAL;      (* Outlet pressure from feedwater pump in bar *)
    PV_FeedwaterPumpSpeed : REAL;           (* Pump speed in RPM *)
    PV_FeedwaterPumpTorque : REAL;          (* Pump torque in Nm *)
    PV_FeedwaterPumpCurrent : REAL;         (* Pump current in A *)
    PV_FeedwaterPumpTemperature : REAL;     (* Pump temperature in °C *)
    PV_FeedwaterPumpVibration : REAL;       (* Pump vibration in mm/s *)
    PV_FeedwaterPumpStatusFault : BOOL;     (* Pump fault status: TRUE = Fault *)
    PV_FeedwaterPumpMaintenance : BOOL;     (* Maintenance

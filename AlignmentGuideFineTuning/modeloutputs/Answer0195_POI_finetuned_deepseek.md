### Intent:
**Intent Summary:**  
Generate a structured I/O list table with 30 entries for a steel rolling mill, including signal names, I/O types, tagnumbers, analog/digital classification, engineering units, ranges, setpoints, and P&ID references to standardize control system documentation and ensure integration accuracy.

### Prompt:
**IO List Rolling Mill:**

Create an I/O list as a table with 30 lines for a rolling mill in a steel production plant. Have as columns signal name, input/output, signal tagnumber, analog/digital, engineering unit, ranges, setpoint, and P&ID reference.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

Designing and integrating control systems for a rolling mill in a steel production plant requires a detailed and standardized I/O list. Without a well-organized table capturing key signal characteristics, such as I/O type, ranges, and engineering units, engineers risk miswiring, mismatches in PLC logic, and inconsistent documentation across instrumentation, control panels, and HMI systems.

⸻

🟩 A (After) – The Desired Outcome

Create a structured I/O list table with 30 entries specific to a rolling mill system. The table should include the following columns for each signal:
	•	Signal Name
	•	Input/Output
	•	Signal Tagnumber
	•	Analog/Digital
	•	Engineering Unit
	•	Range
	•	Setpoint
	•	P&ID Reference

This list should serve as a foundation for instrumentation wiring, PLC configuration, and control narrative alignment, ensuring that all process signals are properly identified and described.

⸻

🟧 B (Bridge) – How to Get There
	1.	Identify typical signals in a rolling mill (e.g., entry tension, roll force, speed feedback, motor current, cooling valve command).
	2.	For each of the 30 entries, define:
	•	Whether the signal is an input (sensor) or output (actuator)
	•	Its analog/digital type
	•	Units such as bar, °C, m/min, kN
	•	Expected range and setpoint values
	•	Reference back to a P&ID drawing for traceability
	3.	Present the data in a clean, consistent tabular format, suitable for use in Excel, a PDF datasheet, or PLC documentation.

### Generated Code:
**Intent Summary:**  
Generate a structured I/O list table with 30 entries for a steel rolling mill, including signal names, I/O types, tagnumbers, analog/digital classification, engineering units, ranges, setpoints, and P&ID references to standardize control system documentation and ensure integration accuracy.
**IO List Rolling Mill:**

Create an I/O list as a table with 30 lines for a rolling mill in a steel production plant. Have as columns signal name, input/output, signal tagnumber, analog/digital, engineering unit, ranges, setpoint, and P&ID reference.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

Designing and integrating control systems for a rolling mill in a steel production plant requires a detailed and standardized I/O list. Without a well-organized table capturing key signal characteristics, such as I/O type, ranges, and engineering units, engineers risk miswiring, mismatches in PLC logic, and inconsistent documentation across instrumentation, control panels, and HMI systems.

⸻

🟩 A (After) – The Desired Outcome

Create a structured I/O list table with 30 entries specific to a rolling mill system. The table should include the following columns for each signal:
	•	Signal Name
	•	Input/Output
	•	Signal Tagnumber
	•	Analog/Digital
	•	Engineering Unit
	•	Range
	•	Setpoint
	•	P&ID Reference

This list should serve as a foundation for instrumentation wiring, PLC configuration, and control narrative alignment, ensuring that all process signals are properly identified and described.

⸻

🟧 B (Bridge) – How to Get There
	1.	Identify typical signals in a rolling mill (e.g., entry tension, roll force, speed feedback, motor current, cooling valve command).
	2.	For each of the 30 entries, define:
	•	Whether the signal is an input (sensor) or output (actuator)
	•	Its analog/digital type
	•	Units such as bar, °C, m/min, kN
	•	Expected range and setpoint values
	•	Reference back to a P&ID drawing for traceability
	3.	Present the data in a clean, consistent tabular format, suitable for use in Excel, a PDF datasheet, or PLC documentation.
	4.	Use this table as a reference during system design, commissioning, and maintenance.
(* IEC 61131-3 Structured Text: PID Control for Steel Rolling Mill *)
(* Purpose: Adjusts rolling mill process parameters to maintain optimal rolling *)
(* conditions, with adjustable setpoints for temperature, pressure, and *)
(* speed control. Includes alarm conditions for over/under-temperature, *)
(* over/under-pressure, and over/under-speed. *)

(* 1. Inputs *)
(*   - TempSetpoint: Target temperature in °C *)
(*   - PressureSetpoint: Target pressure in bar *)
(*   - SpeedSetpoint: Target rolling speed in m/min *)
(*   - TempSensor: Measured temperature in °C *)
(*   - PressureSensor: Measured pressure in bar *)
(*   - SpeedSensor: Measured rolling speed in m/min *)
(*   - TempAlarm: Over-temperature alarm flag *)
(*   - PressureAlarm: Over-pressure alarm flag *)
(*   - SpeedAlarm: Over-speed alarm flag *)
(*   - TempLimit: Minimum temperature limit in °C *)
(*   - PressureLimit: Minimum pressure limit in bar *)
(*   - SpeedLimit: Minimum rolling speed in m/min *)
(*   - TempLimitAlarm: Over-temperature limit alarm flag *)
(*   - PressureLimitAlarm: Over-pressure limit alarm flag *)
(*   - SpeedLimitAlarm: Over-speed limit alarm flag *)
(*   - TempAlarmActive: Over-temperature alarm active flag *)
(*   - PressureAlarmActive: Over-pressure alarm active flag *)
(*   - SpeedAlarmActive: Over-speed alarm active flag *)
(*   - TempLimitAlarmActive: Over-temperature limit alarm active flag *)
(*   - TempAlarmReset: Over-temperature alarm reset flag *)
(*   - PressureAlarmReset: Over-pressure alarm reset flag *)
(*   - SpeedAlarmReset: Over-speed alarm reset flag *)
(*   - TempLimitAlarmReset: Over-temperature limit alarm reset flag *)
(*   - ControlMode: Control mode (0=Manual, 1=Auto) *)
(*   - ManualOverride: Manual override flag *)
(*   - ManualOverrideActive: Manual override active flag *)
(*   - ManualOverrideReset: Manual override reset flag *)
(*   - ManualOverride

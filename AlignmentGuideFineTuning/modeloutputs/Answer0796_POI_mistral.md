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

⸻

**IO List Steam Water Cycle:**

| Signal Name | Tag Number | Analog/Digital | Engineering Unit | Range | Setpoint | P&ID Reference |
|-------------|-----------|---------------|------------------|-------|----------|----------------|
| Feedwater Flow | FW_FLOW_01 | Analog | m³/h | 0–100 | 80 | PID_001-001 |
| Feedwater Pressure | FW_PRESS_01 | Analog | bar | 0–100 | 40 | PID_001-002 |
| Feedwater Level | FW_LEVEL_01 | Analog | m | 0–10 | 5 | PID_001-003 |
| Feedwater Temperature | FW_TEMP_01 | Analog | °C | 0–100 | 50 | PID_001-004 |
| Feedwater Inlet Valve | FW_INLET_VALVE | Digital | % | 0–100 | 50 | PID_001-005 |
| Feedwater Outlet Valve | FW_OUTLET_VALVE | Digital | % | 0–100 | 50 | PID_001-006 |
| Feedwater Pump Status | FW_PUMP_STATUS | Digital | On/Off | - | - | PID_001-007 |
| Feedwater Pump Speed | FW_PUMP_SPEED | Analog | rpm | 0–1000 | 600 | PID_001-008 |
| Feedwater Pump Motor Current | FW_PUMP_MOTOR_CURRENT | Analog | A | 0–20 | 10 | PID_001-009 |
| Feedwater Pump Overpressure Protection | FW_OVERPRESSURE_PROT | Digital | On/Off | - | - | PID_001-010 |
| Feedwater Pump Und

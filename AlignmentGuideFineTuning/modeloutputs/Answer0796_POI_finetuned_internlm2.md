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

Each row should represent a single I/O point and use engineering units, realistic ranges (e.g., 0–100%, 0–200 t/h), and consistent tagging conventions. Include a brief description of the signal's function in the feedwater control system.

⸻

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

Each row should represent a single I/O point and use engineering units, realistic ranges (e.g., 0–100%, 0–200 t/h), and consistent tagging conventions. Include a brief description of the signal's function in the feedwater control system.

**I/O List for Feedwater Control in a Steam-Water Cycle:**

| Signal Name | Signal Tag Number | Analog/Digital | Engineering Unit | Range | Setpoint | P&ID Reference |
| --- | --- | --- | --- | --- | --- | --- |
| Feedwater Flow | FLOW_FW | Analog | m³/h | 0–200 | 100 | 1-1 |
| Feedwater Level | LEVEL_FW | Analog | m | 0–10 | 5 | 1-2 |
| Feedwater Pressure | PRESS_FW | Analog | bar | 0–5 | 2.5 | 1-3 |
| Feedwater Temperature | TEMP_FW | Analog | °C | 0–100 | 80 | 1-4 |
| Feedwater Valve Position | VALVE_FW | Digital | % | 0–100 | 50 | 1-5 |
| Feedwater Pump Status | PUMP_FW | Digital

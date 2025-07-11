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

Each row should represent a single I/O point and use engineering units, realistic ranges (e.g., 0–100%, 0–200 t/h), and consistent tagging conventions. Include a brief description of the signal's purpose and its role in the feedwater control loop.

⸻

**Example Table:**

| Signal Name | Signal Tag Number | Analog/Digital | Engineering Unit | Range | Setpoint | P&ID Reference |
|-------------|-------------------|----------------|------------------|-------|----------|----------------|
| Feedwater Flow | FLOW_FEEDWATER | Analog | t/h | 0–200 | 150 | P&ID-01 |
| Drum Level | LEVEL_DRUM | Analog | % | 0–100 | 50 | P&ID-02 |
| Feedwater Pump 1 Control | VALVE_FEEDWATER_PUMP_1 | Digital | % | 0–100 | 80 | P&ID-03 |
| Feedwater Pump 2 Control | VALVE_FEEDWATER_PUMP_2 | Digital | % | 0–100 | 70 | P&ID-04 |
| Feedwater Pump 3 Control | VALVE_FEEDWATER_PUMP_3 | Digital | % | 0–100 | 60 | P&ID-05 |
| Feedwater Pump 4 Control | VALVE_FEEDWATER_PUMP_4 | Digital | % | 0–100 | 50 | P&ID-06 |
| Feedwater Pump 5 Control | VALVE_FEEDWATER_PUMP_5 | Digital | % | 0–100 | 40 | P&ID-07 |
| Feedwater Pump 6 Control | VALVE_FEEDWATER_PUMP_6 | Digital | % | 0–100 | 30 | P&ID-08 |
| Feedwater Pump 7 Control | VALVE_FEEDWATER_PUMP_7 | Digital | % | 0–100 | 20 | P&ID-09 |
| Feedwater Pump 8 Control | VALVE_FEEDWATER_PUMP_8 | Digital | % | 0–100 | 10 | P&ID-10 |
| Feedwater Pump 9 Control | VALVE_FEEDWATER_PUMP_9 | Digital | % | 0–100 | 0 | P&ID-11 |
| Feedwater Pump 10 Control | VALVE_FEEDWATER_PUMP_10

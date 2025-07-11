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

🟨 A (Algorithm) – Describe the Process

1. 	Start with a blank table.
2. 	Identify all relevant signals in the feedwater control system.
3. 	For each signal, fill in the following fields:
	•	Signal Name
	•	Signal Tag Number
	•	Analog/Digital
	•	Engineering Unit
	•	Range
	•	Setpoint
	•	P&ID Reference
4. 	Ensure consistency in tagging conventions and engineering units.
5. 	Cross-reference the table with the P&ID to ensure accurate representation of the control system.
6. 	Review the table for accuracy and completeness.
7. 	Export the table as a suitable format (e.g., CSV, Excel, PDF) for use in PLC configuration, instrumentation datasheets, control system documentation, and P&ID cross-referencing.

⸻

🟩 O (Output) – Describe the Output

Output:

| Signal Name | Signal Tag Number | Analog/Digital | Engineering Unit | Range | Setpoint | P&ID Reference |
| --- | --- | --- | --- | --- | --- | --- |
| Flow Transmitter 1 | 101 | Analog | % | 0–100% | 50% | P&ID-1001 |
| Drum Level Sensor 1 | 102 | Analog | m | 0–200 m | 100 m | P&ID-1002 |
| Control Valve 1 | 103 | Analog | % | 0–100% | 50% | P&ID-1003 |
| Pump Interlock 1 | 104 | Digital |  |  |  | P&ID-1004 |
| ... | ... | ... | ... | ... | ... | ... |

⸻

🟨 E (Example) – Provide an Example

Example Output:

| Signal Name | Signal Tag Number | Analog/Digital | Engineering Unit | Range | Setpoint | P&ID Reference |
| --- | --- | --- | --- | --- | --- | --- |
| Flow Transmitter 1 | 101 | Analog |

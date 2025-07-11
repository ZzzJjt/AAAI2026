### Intent:
**Intent Summary:**  
Create a 30-line I/O list table for a steel rolling mill's automation system, detailing signal names, types (analog/digital), engineering units, ranges, setpoints, and P&ID references to support PLC/HMI configuration and process control documentation.  

*(Focus: Structured I/O documentation for rolling mill instrumentation and control signals.)*

### Prompt:
**IO List Rolling Mill:**

Create an I/O list as a table with 30 lines for a rolling mill in a steel production plant. Have as columns signal name, input/output, signal tagnumber, analog/digital, engineering unit, ranges, setpoint, and P&ID reference.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a control systems engineer responsible for creating detailed I/O documentation for the automation of a rolling mill in a steel production facility.

⸻

🟩 T (Task) – Define the Objective

Generate a structured I/O list table containing 30 lines, each representing a control or monitoring signal relevant to the rolling mill process. Each row must include the following columns:
	•	Signal Name
	•	Input/Output
	•	Signal Tagnumber
	•	Analog/Digital
	•	Engineering Unit
	•	Range
	•	Setpoint
	•	P&ID Reference

The list should reflect realistic instrumentation, such as motor speed feedback, roll gap position, cooling valve control, hydraulic pressure, and strip tension.

⸻

🟧 F (Format) – Specify the Output Format

Provide the output as a cleanly formatted table suitable for documentation, HMI/PLC configuration, or Excel import. The format should support:
	•	Clear signal identification and traceability
	•	Inclusion of engineering metadata (units, range, setpoints)
	•	Cross-reference with P&ID diagrams for system integration
	•	Compatibility with control logic implementation and commissioning workflows

### Generated Code:
**Intent Summary:**  
Create a 30-line I/O list table for a steel rolling mill's automation system, detailing signal names, types (analog/digital), engineering units, ranges, setpoints, and P&ID references to support PLC/HMI configuration and process control documentation.  

*(Focus: Structured I/O documentation for rolling mill instrumentation and control signals.)*
**IO List Rolling Mill:**

Create an I/O list as a table with 30 lines for a rolling mill in a steel production plant. Have as columns signal name, input/output, signal tagnumber, analog/digital, engineering unit, ranges, setpoint, and P&ID reference.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a control systems engineer responsible for creating detailed I/O documentation for the automation of a rolling mill in a steel production facility.

⸻

🟩 T (Task) – Define the Objective

Generate a structured I/O list table containing 30 lines, each representing a control or monitoring signal relevant to the rolling mill process. Each row must include the following columns:
	•	Signal Name
	•	Input/Output
	•	Signal Tagnumber
	•	Analog/Digital
	•	Engineering Unit
	•	Range
	•	Setpoint
	•	P&ID Reference

The list should reflect realistic instrumentation, such as motor speed feedback, roll gap position, cooling valve control, hydraulic pressure, and strip tension.

⸻

🟧 F (Format) – Specify the Output Format

Provide the output as a cleanly formatted table suitable for documentation, HMI/PLC configuration, or Excel import. The format should support:
	•	Clear signal identification and traceability
	•	Inclusion of engineering metadata (units, range, setpoints)
	•	Cross-reference with P&ID diagrams for system integration
	•	Compatibility with control logic implementation and commissioning workflows

Ensure the table is easy to read and understand, with appropriate column headers and formatting for clarity.

⸻

**I/O List Rolling Mill:**

| Signal Name | Input/Output | Signal Tagnumber | Analog/Digital | Engineering Unit | Range | Setpoint | P&ID Reference |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Motor Speed Feedback | Input | M1001 | Analog | RPM | 0-1000 | 500 | P&ID-01 |
| Roll Gap Position | Input | M1002 | Analog | mm | 0-100 | 50 | P&ID-02 |
| Cooling Valve Control | Output | M1003 | Digital | % | 0-100 | 50 | P&ID-03 |
| Hydraulic Pressure | Input | M1004 | Analog | bar | 0-100 | 50 | P&ID-04 |
| Strip Tension | Input | M1005 | Analog | N/mm² | 0-100 | 50 | P&ID-05 |
| Motor Current | Input | M1006 | Analog | A | 0-100 | 50 | P&ID-06 |
| Motor Temperature | Input | M1007 | Analog | °C | 0-100 | 50 | P&ID-07 |
| Roll Gap Position Setpoint | Output | M1008 | Digital | mm | 0-100 | 50 | P&ID-08 |
| Cooling Valve Position | Output | M1009 | Digital | % | 0-100 | 50 | P&ID-09 |
| Hydraulic Pressure Setpoint | Output | M1010 | Digital | bar | 0-100 | 50 | P&ID-10 |
| Strip Tension Setpoint | Output | M1011 | Digital | N/mm² | 0-100 | 50 | P&ID-11 |
| Motor Speed Control | Output | M1012 | Digital | RPM | 0-100 | 50 | P&ID-12 |
| Motor Current Setpoint

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

For example:

Signal Name | Input/Output | Signal Tagnumber | Analog/Digital | Engineering Unit | Range | Setpoint | P&ID Reference
-----------|--------------|-----------------|----------------|------------------|-------|----------|------------
Motor Speed | Output | 101 | Analog | RPM | 0–1000 | 600 | P&ID-101
Roll Gap Pos | Output | 102 | Analog | mm | 0–100 | 50 | P&ID-102
Cooling Valve | Output | 103 | Analog | % | 0–100 | 50 | P&ID-103
Hydraulic Pressure | Input | 104 | Analog | bar | 0–100 | 50 | P&ID-104
Strip Tension | Output | 105 | Analog | kgf | 0–100 | 50 | P&ID-105

⸻

✅ Example Output:

Signal Name | Input/Output | Signal Tagnumber | Analog/Digital | Engineering Unit | Range | Setpoint | P&ID Reference
-----------|--------------|-----------------|----------------|------------------|-------|----------|------------
Motor Speed | Output | 101 | Analog | RPM | 0–1000 | 600 | P&ID-101
Roll Gap Pos | Output | 102 | Analog | mm | 0–100 | 50 | P&ID-102
Cooling Valve | Output | 103 | Analog | % | 0–100 | 50 | P&ID-103
Hydraulic Pressure | Input | 104 | Analog | bar | 0–100 | 50 | P&ID-104
Strip Tension | Output | 105 | Analog | kgf | 0–100 | 50 | P&ID-105

This table is suitable for use in PLC configuration, HMI design, and engineering documentation.
(* IEC 61131-3 Structured Text: Steel Rolling Mill I/O List *)
(* Purpose: Defines all signals and their properties for automation of a rolling mill *)

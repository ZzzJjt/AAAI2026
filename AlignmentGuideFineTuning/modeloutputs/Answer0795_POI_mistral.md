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

⸻

**I/O List Rolling Mill:**

| Signal Name | Input/Output | Signal Tagnumber | Analog/Digital | Engineering Unit | Range | Setpoint | P&ID Reference |
|-------------|-------------|-----------------|---------------|-----------------|-------|---------|--------------|
| Motor Speed 1 | Output | M001 | Analog | RPM | 0-1000 | 500 | PID-001-001 |
| Motor Speed 2 | Output | M002 | Analog | RPM | 0-1000 | 550 | PID-001-002 |
| Roll Gap 1 | Input | I001 | Analog | mm | 0-100 | 50 | PID-002-001 |
| Roll Gap 2 | Input | I002 | Analog | mm | 0-100 | 55 | PID-002-002 |
| Cooling Valve 1 | Output | O001 | Digital | - | Open/Closed | - | PID-003-001 |
| Cooling Valve 2 | Output | O002 | Digital | - | Open/Closed | - | PID-003-002 |
| Hydraulic Pressure | Input | I003 | Analog | bar | 0-200 | 150 | PID-004-001 |
| Strip Tension | Input | I004 | Analog | N | 0-10000 | 5000 | PID-005-001 |
| Temperature Sensor 1 | Input | I005 | Analog | °C | -40-120 | 80 | PID-006-001 |
| Temperature Sensor 2 | Input | I006 | Analog | °C | -40-120 | 85 | PID-006-002 |
| Level Sensor 1 | Input

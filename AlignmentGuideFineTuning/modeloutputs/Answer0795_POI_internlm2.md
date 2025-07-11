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

🟨 I (Instructions) – Provide Detailed Instructions

1.	Signal Name: Use a descriptive name that clearly identifies the signal's purpose in the process. For example, "Roll Gap Position" or "Strip Tension."
2.	Input/Output: Indicate whether the signal is an input (I) or output (O) in the system. Inputs are typically sensors or feedback devices, while outputs are actuators or control devices.
3.	Signal Tagnumber: Provide a unique identifier for the signal, typically a numeric value assigned by the control system. This number is used to reference the signal in the PLC/HMI configuration.
4.	Analog/Digital: Specify if the signal is analog (A) or digital (D). Analog signals represent continuous values, while digital signals represent discrete states.
5.	Engineering Unit: List the unit of measurement for the signal, such as "meters" for position or "kPa" for pressure.
6.	Range: Provide the valid range of the signal, including the minimum and maximum values. This information is crucial for proper configuration and control logic.
7.	Setpoint: If applicable, include the setpoint value for the signal. Setpoints are often used for control loops or to define desired operating conditions.
8.	P&ID Reference: Cross-reference the signal with its corresponding P&ID diagram element. P&ID diagrams are used to visually represent the process and instrumentation, and this reference helps ensure accurate system integration.

⸻

🟩 S (Solution) – Provide a Sample Output

| Signal Name | Input/Output | Signal Tagnumber | Analog/Digital | Engineering Unit | Range | Setpoint | P&ID Reference |
|-------------|--------------|-----------------|----------------|------------------|-------|----------|----------------|
| Roll Gap Position | Input | 1001 | Analog | Meters | 0.0 - 1.0 | 0.5 | P1-001   |
| Strip Tension | Input | 1002 | Analog | N/m | 0.0 - 100.0 | 50.0 | P2-002   |
| Motor Speed | Input | 1003 | Analog | RPM | 0.0 - 3000.0 | 1500.0 | P3-003   |
| Cooling Valve Control | Output | 2001

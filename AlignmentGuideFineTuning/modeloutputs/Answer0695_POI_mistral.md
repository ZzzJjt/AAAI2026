### Intent:
**Intent Summary:**  
Generate a 30-line I/O list table for a steel rolling mill, specifying signal names, types (analog/digital), engineering units, ranges, setpoints, and P&ID references for PLC and instrumentation integration.

### Prompt:
**IO List Rolling Mill:**

Create an I/O list as a table with 30 lines for a rolling mill in a steel production plant. Have as columns signal name, input/output, signal tagnumber, analog/digital, engineering unit, ranges, setpoint, and P&ID reference.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as an industrial control engineer preparing the I/O specification for a rolling mill system in a steel production plant, ensuring clarity for instrumentation, automation, and electrical integration teams.

⸻

🟩 I (Input) – Information Provided

You are to create a detailed I/O list for the rolling mill that includes 30 signal entries. Each entry should include the following columns:
	•	Signal Name
	•	Input/Output
	•	Signal Tagnumber
	•	Analog/Digital
	•	Engineering Unit
	•	Range
	•	Setpoint
	•	P&ID Reference

The list should reflect real-world rolling mill variables such as roll speed, motor torque, cooling system actuation, gap feedback, and tension control.

⸻

🟧 S (Steps) – Implementation Steps
	1.	Identify 30 key control and monitoring signals commonly used in rolling mills.
	2.	For each signal, define:
	•	Whether it is an input (sensor) or output (actuator)
	•	Its analog/digital type
	•	Engineering units (e.g., mm, °C, bar, m/min)
	•	Typical range and control setpoint
	•	A unique tag number (e.g., RM1001)
	•	P&ID reference for traceability
	3.	Format the list as a structured table suitable for use in Excel, documentation, or PLC tag import.
	4.	Ensure consistency, clarity, and relevance to real plant instrumentation.

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a professional, standardized I/O list that:
	•	Covers 30 essential signals used in rolling mill operations
	•	Provides all necessary metadata for PLC configuration, field wiring, and HMI integration
	•	Aligns with best practices for project documentation, P&ID traceability, and commissioning support

### Generated Code:
**Intent Summary:**  
Generate a 30-line I/O list table for a steel rolling mill, specifying signal names, types (analog/digital), engineering units, ranges, setpoints, and P&ID references for PLC and instrumentation integration.
**IO List Rolling Mill:**

Create an I/O list as a table with 30 lines for a rolling mill in a steel production plant. Have as columns signal name, input/output, signal tagnumber, analog/digital, engineering unit, ranges, setpoint, and P&ID reference.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as an industrial control engineer preparing the I/O specification for a rolling mill system in a steel production plant, ensuring clarity for instrumentation, automation, and electrical integration teams.

⸻

🟩 I (Input) – Information Provided

You are to create a detailed I/O list for the rolling mill that includes 30 signal entries. Each entry should include the following columns:
	•	Signal Name
	•	Input/Output
	•	Signal Tagnumber
	•	Analog/Digital
	•	Engineering Unit
	•	Range
	•	Setpoint
	•	P&ID Reference

The list should reflect real-world rolling mill variables such as roll speed, motor torque, cooling system actuation, gap feedback, and tension control.

⸻

🟧 S (Steps) – Implementation Steps
	1.	Identify 30 key control and monitoring signals commonly used in rolling mills.
	2.	For each signal, define:
	•	Whether it is an input (sensor) or output (actuator)
	•	Its analog/digital type
	•	Engineering units (e.g., mm, °C, bar, m/min)
	•	Typical range and control setpoint
	•	A unique tag number (e.g., RM1001)
	•	P&ID reference for traceability
	3.	Format the list as a structured table suitable for use in Excel, documentation, or PLC tag import.
	4.	Ensure consistency, clarity, and relevance to real plant instrumentation.

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a professional, standardized I/O list that:
	•	Covers 30 essential signals used in rolling mill operations
	•	Provides all necessary metadata for PLC configuration, field wiring, and HMI integration
	•	Aligns with best practices for project documentation, P&ID traceability, and commissioning support

**IO List Rolling Mill:**

| Signal Name | Input/Output | Signal Tagnumber | Analog/Digital | Engineering Unit | Range | Setpoint | P&ID Reference |
|-------------|-------------|-----------------|---------------|-----------------|-------|----------|--------------|
| Roll Speed  | Input       | RM1001          | Analog        | m/min           | 0-100  | 50       | PID-001-001   |
| Motor Torque| Input       | RM1002          | Analog        | Nm              | 0-1000 | 500      | PID-001-002   |
| Coolant Temp| Input       | RM1003          | Analog        | °C              | 10-80  | 50       | PID-002-001   |
| Coolant Flow| Input       | RM1004          | Analog        | L/min           | 0-100  | 50       | PID-002-002   |
| Gap Feedback| Input       | RM1005          | Analog        | mm              | 0-10   | 2        | PID-003-001   |
| Tension Control| Output      | RM1006          | Digital        | N               | -100-100 | 0        | PID-004-001   |
| Roll Force   | Input       | RM1007          | Analog        | kN              | 0-1000 | 500      | PID-005-001   |
| Oil Pressure | Input       | RM1008          | Analog        | bar             | 0-100  | 50       | PID-006-001   |
| Oil Temperature| Input       | RM1009          | Analog        | °C              | 10-80  | 50       | PID-006-

### Intent:
**Intent Summary:**  
Generate a 30-entry I/O list table for a steel rolling mill, specifying signal names, types (input/output, analog/digital), engineering units, ranges, setpoints, and P&ID references for PLC/HMI integration.  

*(Context: Industrial control system documentation for instrumentation and automation teams.)*

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
Generate a 30-entry I/O list table for a steel rolling mill, specifying signal names, types (input/output, analog/digital), engineering units, ranges, setpoints, and P&ID references for PLC/HMI integration.  

*(Context: Industrial control system documentation for instrumentation and automation teams.)*
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

This list will serve as a critical reference for the instrumentation, automation, and electrical teams, facilitating seamless integration and efficient operation of the rolling mill system.

**I/O List Rolling Mill:**

| Signal Name | Input/Output | Signal Tagnumber | Analog/Digital | Engineering Unit | Range | Setpoint | P&ID Reference |
|-------------|--------------|------------------|----------------|------------------|-------|----------|----------------|
| Roll Speed  | Input        | RM1001           | Analog         | mm/min           | 0-1000 | 500      | P&ID-01        |
| Motor Torque| Output       | RM1002           | Analog         | Nm               | 0-1000 | 500      | P&ID-02        |
| Cooling Act | Output       | RM1003           | Digital        | %                | 0-100  | 50       | P&ID-03        |
| Gap Feedback| Input        | RM1004           | Analog         | mm               | 0-100  | 50       | P&ID-04        |
| Tension     | Input        | RM1005           | Analog         | N                | 0-1000 | 500      | P&ID-05        |
| Speed Control| Output      | RM1006           | Analog         | mm/min           | 0-1000 | 500      | P&ID-06        |
| Temperature | Input        | RM1007           | Analog         | °C               | 0-100  | 50       | P&ID-07        |
| Pressure    | Input        | RM1008           | Analog         | bar              | 0-100  | 50       | P&ID-08        |
| Flow Rate   | Input        | RM1009           | Analog         | m³/h             | 0-1000 | 500      | P&ID-09        |
| Power       | Input        | RM1010           | Analog         | kW               | 0-1000 | 500      | P&ID-10

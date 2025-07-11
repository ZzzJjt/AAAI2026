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
	•	Can be easily shared with cross-functional teams and used as a reference during system implementation
Certainly! Below is a detailed I/E list for the steam generator of a nuclear power plant, including 30 entries with signal names, input/output status, signal tags, analog/digital type, engineering units, ranges, setpoints, and P&ID references.

### Steam Generator I/E List

| Signal Name                  | I/O Status | Signal Tag | Analog/Digital | Engineering Unit | Range                 | Setpoint | P&ID Reference |
|------------------------------|------------|------------|-----------------|-------------------|-----------------------|-----------|----------------|
| Steam Generator Level        | Input      | SG01L      | Analog          | %                 | 0–100%                | 50%       | P&ID-SG-01      |
| Steam Generator Pressure     | Input      | SG01P      | Analog          | bar               | 0–180 bar             | 150 bar   | P&ID-SG-01      |
| Steam Generator Temperature  | Input      | SG01T      | Analog          | °C                | 500–600°C             | 550°C     | P&ID-SG-01      |
| Feedwater Flow Rate          | Input      | FW01F      | Analog          | kg/s              | 0–1000 kg/s          | 500 kg/s  | P&ID-FW-01      |
| Feedwater Temperature       | Input      | FW01T      | Analog          | °C                | 280–320°C             | 295°C     | P&ID-FW-01      |
| Feedwater Level              | Input      | FW01L      | Analog          | %                 | 0–100%                | 50%       | P&ID-FW-01      |
| Feedwater Pump Speed         | Input      | FW01SP     | Analog          | rpm               |

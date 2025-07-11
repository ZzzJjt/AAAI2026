### Intent:
**Intent Summary:**  
Create an IEC 61131-3 Sequential Function Chart (SFC) to control a single intersection traffic light system with timed states (Green: 5s, Yellow: 2s, Red: 5s) using mutually exclusive outputs and cyclic operation.  

*(Focus: PLC logic for timed traffic light sequencing with looped states.)*

### Prompt:
**IO List Steam Water Cycle:**

Create an I/O list as a table for feedwater control in a steam-water cycle in a power plant. Have as columns names, signal tagnumber, analog/digital, engineering unit, ranges, setpoint, and P&ID reference.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a control systems engineer responsible for defining instrumentation and signal documentation for the feedwater control system in a steam-water cycle of a power plant.

⸻

🟩 I (Input) – Information Provided

You are to create an I/O list in table format that includes the following columns for each signal:
	•	Signal Name
	•	Signal Tag Number
	•	Analog/Digital
	•	Engineering Unit
	•	Range
	•	Setpoint
	•	P&ID Reference

This list will cover essential elements of the feedwater control loop, such as flow transmitters, drum level indicators, control valves, and pump statuses.

⸻

🟧 S (Steps) – Steps to Perform
	1.	Identify common I/O signals associated with feedwater control, including:
	•	Drum Level Transmitters
	•	Feedwater Flow Transmitters
	•	Control Valve Positions
	•	Pump Start/Stop Signals
	2.	Assign each signal a unique tagnumber and specify whether it is analog or digital.
	3.	Add appropriate engineering units (e.g., %, t/h, bar), define realistic ranges (e.g., 0–100%), and enter typical setpoints.
	4.	Ensure each entry is linked to a P&ID reference for traceability and cross-discipline alignment.
	5.	Format the data into a clean, consistent table that can be imported into design tools, PLC/HMI projects, or engineering reports.

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a complete and professionally structured I/O list for the feedwater control section of the steam-water cycle. This list will support:
	•	PLC configuration
	•	Instrumentation specification
	•	HMI integration
	•	Commissioning and validation aligned with P&ID documentation

### Generated Code:
**Intent Summary:**  
Create an IEC 61131-3 Sequential Function Chart (SFC) to control a single intersection traffic light system with timed states (Green: 5s, Yellow: 2s, Red: 5s) using mutually exclusive outputs and cyclic operation.  

*(Focus: PLC logic for timed traffic light sequencing with looped states.)*
**IO List Steam Water Cycle:**

Create an I/O list as a table for feedwater control in a steam-water cycle in a power plant. Have as columns names, signal tagnumber, analog/digital, engineering unit, ranges, setpoint, and P&ID reference.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a control systems engineer responsible for defining instrumentation and signal documentation for the feedwater control system in a steam-water cycle of a power plant.

⸻

🟩 I (Input) – Information Provided

You are to create an I/O list in table format that includes the following columns for each signal:
	•	Signal Name
	•	Signal Tag Number
	•	Analog/Digital
	•	Engineering Unit
	•	Range
	•	Setpoint
	•	P&ID Reference

This list will cover essential elements of the feedwater control loop, such as flow transmitters, drum level indicators, control valves, and pump statuses.

⸻

🟧 S (Steps) – Steps to Perform
	1.	Identify common I/O signals associated with feedwater control, including:
	•	Drum Level Transmitters
	•	Feedwater Flow Transmitters
	•	Control Valve Positions
	•	Pump Start/Stop Signals
	2.	Assign each signal a unique tagnumber and specify whether it is analog or digital.
	3.	Add appropriate engineering units (e.g., %, t/h, bar), define realistic ranges (e.g., 0–100%), and enter typical setpoints.
	4.	Ensure each entry is linked to a P&ID reference for traceability and cross-discipline alignment.
	5.	Format the data into a clean, consistent table that can be imported into design tools, PLC/HMI projects, or engineering reports.

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a complete and professionally structured I/O list for the feedwater control section of the steam-water cycle. This list will support:
	•	PLC configuration
	•	Instrumentation specification
	•	HMI integration
	•	Commissioning and validation aligned with P&ID documentation

**I/O List for Feedwater Control in a Steam-Water Cycle:**

| Signal Name | Signal Tag Number | Analog/Digital | Engineering Unit | Range | Setpoint | P&ID Reference |
|-------------|------------------|---------------|------------------|-------|----------|----------------|
| Drum Level 1 | PW_DrumLevel1 | Analog | % | 0–100 | 70 | PID-001-001 |
| Drum Level 2 | PW_DrumLevel2 | Analog | % | 0–100 | 75 | PID-001-002 |
| Feedwater Flow | PW_Flow | Analog | t/h | 0–1000 | 800 | PID-001-003 |
| Control Valve 1 Position | PW_Valve1Pos | Digital | % | 0–100 | 50 | PID-001-004 |
| Control Valve 2 Position | PW_Valve2Pos | Digital | % | 0–100 | 50 | PID-001-005 |
| Pump 1 Status | PW_Pump1Status | Digital | On/Off | - | - | PID-001-006 |
| Pump 2 Status | PW_Pump2Status | Digital | On/Off | - | - | PID-001-007 |

**Traffic Light SFC:**

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a control systems engineer responsible for designing a Sequential Function Chart (SFC) for a single intersection traffic light system.

⸻

🟩 I (Input) – Information Provided

You are to create an SFC that controls a traffic light system with timed states (Green: 5s, Yellow: 2s, Red: 5s) using mutually exclusive outputs and cyclic operation.

⸻

🟧 S (Steps) – Steps to Perform

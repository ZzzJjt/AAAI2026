### Intent:
**Intent Summary:**  
Develop a PLC-based control narrative for ethanol fermentation, specifying setpoints (e.g., 32–35°C, pH 4.5–5.0), instrumentation (temperature/pH sensors, dosing pumps), and interlocks (temperature/pH deviations, failed inoculation) to automate batch fermentation with safety and quality compliance.  

*(Focus: Code generation for fermentation control logic, alarms, and interlocks in ethanol production.)*

### Prompt:
**Control Narrative Beer Brewing:**

Create a control narrative for beer brewing including concrete setpoints and ranges.

Create a detailed explanation of the Lautering process (Section 4). Include the equipment and instrumentation needed. Provide a list of the steps to execute.

**R-T-F:**

🟥 R (Role) – Define Your Role

You are a process automation engineer tasked with writing a structured control narrative for a beer brewing system, with emphasis on process instrumentation and control logic.

⸻

🟩 T (Task) – Define the Objective

Develop a detailed control narrative for the beer brewing process, including:
	•	Concrete setpoints and control ranges for each brewing stage
	•	A comprehensive Section 4 – Lautering, which must include:
	•	Description of required equipment and instrumentation
	•	A step-by-step procedure for lautering
	•	Embedded control logic and interlocks, such as turbidity thresholds and flow control

⸻

🟧 F (Format) – Specify the Output Format

Deliver the control narrative in a structured format consisting of:
	1.	Process Overview
	•	Define key stages: mashing, lautering, boiling, fermentation, etc.
	•	Include numeric control parameters (e.g., mash temperature: 66 °C ± 1 °C, sparge water temp: 76 °C)
	2.	Section 4 – Lautering
	•	Equipment: Lauter tun, rake motor, flow meters, level sensors, turbidity probe
	•	Instrumentation:
	•	LT-401: Lauter tun level transmitter
	•	FT-402: Wort outlet flow transmitter
	•	TT-403: Sparge water temperature sensor
	•	TU-404: Turbidity meter at wort outlet
	•	Control Sequence:
	1.	Initiate recirculation
	2.	Monitor turbidity until it falls below 200 NTU
	3.	Begin wort transfer to kettle while initiating sparge water at 76 °C
	4.	Maintain level in lauter tun (60–80%)
	5.	Stop lautering when flow < 0.5 L/min or target volume reached
	3.	Outputs:
	•	Control flags (LauterStart, LauterStop, DivertCloudyWort)
	•	Comments and logic interlocks

### Generated Code:
**Intent Summary:**  
Develop a PLC-based control narrative for ethanol fermentation, specifying setpoints (e.g., 32–35°C, pH 4.5–5.0), instrumentation (temperature/pH sensors, dosing pumps), and interlocks (temperature/pH deviations, failed inoculation) to automate batch fermentation with safety and quality compliance.  

*(Focus: Code generation for fermentation control logic, alarms, and interlocks in ethanol production.)*
**Control Narrative Beer Brewing:**

Create a control narrative for beer brewing including concrete setpoints and ranges.

Create a detailed explanation of the Lautering process (Section 4). Include the equipment and instrumentation needed. Provide a list of the steps to execute.

**R-T-F:**

🟥 R (Role) – Define Your Role

You are a process automation engineer tasked with writing a structured control narrative for a beer brewing system, with emphasis on process instrumentation and control logic.

⸻

🟩 T (Task) – Define the Objective

Develop a detailed control narrative for the beer brewing process, including:
	•	Concrete setpoints and control ranges for each brewing stage
	•	A comprehensive Section 4 – Lautering, which must include:
	•	Description of required equipment and instrumentation
	•	A step-by-step procedure for lautering
	•	Embedded control logic and interlocks, such as turbidity thresholds and flow control

⸻

🟧 F (Format) – Specify the Output Format

Deliver the control narrative in a structured format consisting of:
	1.	Process Overview
	•	Define key stages: mashing, lautering, boiling, fermentation, etc.
	•	Include numeric control parameters (e.g., mash temperature: 66 °C ± 1 °C, sparge water temp: 76 °C)
	2.	Section 4 – Lautering
	•	Equipment: Lauter tun, rake motor, flow meters, level sensors, turbidity probe
	•	Instrumentation:
	•	LT-401: Lauter tun level transmitter
	•	FT-402: Wort outlet flow transmitter
	•	TT-403: Sparge water temperature sensor
	•	TU-404: Turbidity meter at wort outlet
	•	Control Sequence:
	1.	Initiate recirculation
	2.	Monitor turbidity until it falls below 200 NTU
	3.	Begin wort transfer to kettle while initiating sparge water at 76 °C
	4.	Maintain level in lauter tun (60–80%)
	5.	Stop lautering when flow < 0.5 L/min or target volume reached
	3.	Outputs:
	•	Control flags (LauterStart, LauterStop, DivertCloudyWort)
	•	Comments and logic interlocks (e.g., TurbidityAlarm, FlowAlarm)

⸻

✅ Example Output:

Control Narrative for Beer Brewing

Process Overview

Key Stages:

•	Mashing: 66 °C ± 1 °C
•	Lautering:
•	Equipment:
•	Lauter tun
•	Rake motor
•	Flow meters
•	Level transmitters
•	Turbidity probe
•	Wort outlet flow transmitter
•	Sparge water temperature sensor
•	Turbidity meter at wort outlet
•	Control Sequence:
•	Initiate recirculation
•	Monitor turbidity until it falls below 200 NTU
•	Begin wort transfer to kettle while initiating sparge water at 76 °C
•	Maintain level in lauter tun (60–80%)
•	Stop lautering when flow < 0.5 L/min or target volume reached

Section 4 – Lautering

•	Equipment:
•	Lauter tun
•	Rake motor
•	Flow meters
•	Level transmitters
•	Turbidity probe
•	Wort outlet flow transmitter
•	Sparge water temperature sensor
•	Turbidity meter at wort outlet

•	Instrumentation:
•	LT-401: Lauter tun level transmitter
•	FT-402: Wort outlet flow transmitter
•	TT-403: Sparge water temperature sensor
•	TU-404: Turbidity meter at wort outlet

•	Control Sequence:
•	Initiate recirculation
•	Monitor turbidity until it falls below 200 NTU
•	Begin wort transfer to kettle while initiating sparge water at 76 °C
•	Maintain level in lauter tun (60–80%)
•	Stop lautering when flow < 0.5 L/min or target volume reached

Outputs:

•	Control flags:
•	LauterStart
•	LauterStop
•	DivertCloudyWort
•	Interlocks:
•	TurbidityAlarm
•	FlowAlarm

### Beer Brewing Control Narrative

#### 1. Process Overview

Key Stages:

•	Mashing:

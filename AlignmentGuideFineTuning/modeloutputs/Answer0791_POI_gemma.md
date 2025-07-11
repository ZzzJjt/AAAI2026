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
	•	Comments and logic interlocks (e.g., turbidity threshold, flow control)
	4.	References:
	•	Beer Brewing Process Overview
	•	Lautering Process
	•	Lautering Control Sequence
	•	Lautering Control Logic

**Control Narrative Ethanol Fermentation:**

Create a control narrative for ethanol fermentation including concrete setpoints and ranges.

Create a detailed explanation of the fermentation process (Section 4). Include the equipment and instrumentation needed. Provide a list of the steps to execute.

**R-T-F:**

🟥 R (Role) – Define Your Role

You are a process automation engineer tasked with writing a structured control narrative for an ethanol fermentation system, with emphasis on process instrumentation and control logic.

⸻

🟩 T (Task) – Define the Objective

Develop a detailed control narrative for the ethanol fermentation process, including:
	•	Concrete setpoints and control ranges for each fermentation stage
	•	A comprehensive Section 4 – Fermentation, which must include:
	•	Description of required equipment and instrumentation
	•	A step-by-step procedure for fermentation
	•	Embedded control logic and interlocks, such as temperature and pH thresholds

⸻

🟧 F (Format) – Specify the Output Format

Deliver the control narrative in a structured format consisting of:
	1.	Process Overview
	•	Define key stages: inoculation, fermentation, distillation, etc.
	•	Include numeric control parameters (e.g., fermentation temperature: 32–35 °C, pH: 4.5–5.0)
	2.	Section 4 – Fermentation
	•	Equipment: Fermentation tank, temperature/pH sensors, dosing pumps
	•	Instrumentation:
	•	TT-401: Fermentation tank temperature sensor
	•	PH-402: Fermentation tank pH sensor
	•	Control Sequence:
	1.	Initiate inoculation
	2.	Monitor temperature and pH
	3.	Adjust temperature and pH as needed
	4.	Distill when pH < 4.0
	3.	Outputs:
	•	Control flags (FermentStart, FermentStop, Distill)
	•	Comments and logic interlocks (e.g., temperature and pH thresholds)
	4.	References:
	•	Ethanol Fermentation Process Overview
	•	Fermentation Process
	•	Fermentation Control Sequence

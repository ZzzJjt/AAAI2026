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
	•	Comments and logic interlocks

⸻

🟥 A (Action) – Execute the Task

Write a detailed control narrative for the beer brewing process, including concrete setpoints and control ranges for each brewing stage. Focus on Section 4 – Lautering, providing a description of the required equipment and instrumentation, as well as a step-by-step procedure for lautering. Include embedded control logic and interlocks, such as turbidity thresholds and flow control.

**C-A-R-E:**

🟥 C (Context) – Set the Stage

Beer brewing is a complex process that requires precise control of temperature, flow, and turbidity to ensure consistent quality. The lautering stage is critical for separating the liquid wort from the solid grains, and it must be executed with care to avoid cloudy wort or over-extraction of flavor compounds.

⸻

🟩 A (Action) – Peform the Task

Write a detailed control narrative for the beer brewing process, focusing on Section 4 – Lautering. Include the following information:

•	Equipment and instrumentation required for lautering
•	A step-by-step procedure for lautering, including control logic and interlocks
•	Concrete setpoints and control ranges for lautering

⸻

🟨 R (Result) – Show the Result

Provide a detailed control narrative for the beer brewing process, with a focus on Section 4 – Lautering. Include a description of the required equipment and instrumentation, as well as a step-by-step procedure for lautering. Ensure that the control logic and interlocks are clearly defined, and that the setpoints and control ranges are concrete and specific.

**Ethanol Fermentation:**

Create a control narrative for the fermentation process in an ethanol production facility. Include concrete setpoints and ranges for temperature, pH, and dissolved oxygen. Discuss the instrumentation required for monitoring and control, and describe the interlocks and safety measures in place to ensure process integrity.

**R-T-F:**

🟥 R (Role) – Define Your Role

You are a process automation engineer responsible for developing a control narrative for the fermentation process in an ethanol production facility. Your task is to provide a detailed description of the process, including setpoints, instrumentation, and interlocks, to ensure safe and efficient operation.

⸻

🟩 T (Task) – Define the

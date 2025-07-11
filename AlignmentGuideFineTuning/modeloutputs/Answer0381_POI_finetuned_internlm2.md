### Intent:
**Intent Summary:**  
Create a detailed control narrative for an ammonium nitrate reactor, specifying setpoints, instrumentation, operational sequences, and interlock logic to ensure safe, automated, and consistent reactor operation.  

*(For code generation: Focus on translating setpoints, PID control loops, equipment actions, and safety interlocks into programmable logic.)*

### Prompt:
**Control Narrative Beer Brewing:**

Create a control narrative for beer brewing including concrete setpoints and ranges.

Create a detailed explanation of the Lautering process (Section 4). Include the equipment and instrumentation needed. Provide a list of the steps to execute.

**C-A-R-E:**

🟥 C (Context) – Background Situation

In beer brewing automation, a well-defined control narrative is essential for ensuring that brewing stages are executed with precision and consistency. One of the most critical stages is lautering, where wort is separated from the grain. Without a clear explanation of setpoints, instrumentation, and steps, engineers and operators may face inefficiencies, delays, or poor-quality output.

⸻

🟩 A (Action) – Task to Perform

Develop a structured control narrative for the entire beer brewing process, and provide a detailed Section 4 focused on the lautering phase, including:
	•	Concrete setpoints and ranges (e.g., temperature, flow, turbidity)
	•	The equipment and instrumentation used during lautering
	•	A step-by-step description of the lautering process logic
	•	Automated control actions triggered by sensor feedback and operator input

⸻

🟨 R (Result) – Expected Outcome

The result should be a practical, actionable control narrative that:
	•	Standardizes brewing operations for consistent beer quality
	•	Provides engineering and operations teams with a shared reference
	•	Includes key automation logic and instrumentation details
	•	Helps integrate control systems with process equipment

⸻

🟦 E (Example) – Concrete Illustration

Section 4: Lautering Process

Setpoints:
	•	Mash rest temperature: 67 °C
	•	Lautering flow rate: 1.8 L/min
	•	Turbidity cut-off: < 200 NTU
	•	Sparge water temperature: 76 °C

Equipment & Instrumentation:
	•	Lauter tun with rake arms and false bottom
	•	Turbidity sensor at wort outlet
	•	Flow transmitter on wort and sparge lines
	•	Level transmitter in lauter tun
	•	Motorized valve to divert cloudy wort to waste

Steps:
	1.	Begin recirculation until turbidity < 200 NTU
	2.	Start wort transfer to kettle
	3.	Begin sparging at 76 °C while maintaining lauter tun level
	4.	Adjust rake arm position based on wort flow resistance
	5.	Stop sparging when grain bed is dry and total volume reached

### Generated Code:
**Intent Summary:**  
Create a detailed control narrative for an ammonium nitrate reactor, specifying setpoints, instrumentation, operational sequences, and interlock logic to ensure safe, automated, and consistent reactor operation.  

*(For code generation: Focus on translating setpoints, PID control loops, equipment actions, and safety interlocks into programmable logic.)*
**Control Narrative Beer Brewing:**

Create a control narrative for beer brewing including concrete setpoints and ranges.

Create a detailed explanation of the Lautering process (Section 4). Include the equipment and instrumentation needed. Provide a list of the steps to execute.

**C-A-R-E:**

🟥 C (Context) – Background Situation

In beer brewing automation, a well-defined control narrative is essential for ensuring that brewing stages are executed with precision and consistency. One of the most critical stages is lautering, where wort is separated from the grain. Without a clear explanation of setpoints, instrumentation, and steps, engineers and operators may face inefficiencies, delays, or poor-quality output.

⸻

🟩 A (Action) – Task to Perform

Develop a structured control narrative for the entire beer brewing process, and provide a detailed Section 4 focused on the lautering phase, including:
	•	Concrete setpoints and ranges (e.g., temperature, flow, turbidity)
	•	The equipment and instrumentation used during lautering
	•	A step-by-step description of the lautering process logic
	•	Automated control actions triggered by sensor feedback and operator input

⸻

🟨 R (Result) – Expected Outcome

The result should be a practical, actionable control narrative that:
	•	Standardizes brewing operations for consistent beer quality
	•	Provides engineering and operations teams with a shared reference
	•	Includes key automation logic and instrumentation details
	•	Helps integrate control systems with process equipment

⸻

🟦 E (Example) – Concrete Illustration

Section 4: Lautering Process

Setpoints:
	•	Mash rest temperature: 67 °C
	•	Lautering flow rate: 1.8 L/min
	•	Turbidity cut-off: < 200 NTU
	•	Sparge water temperature: 76 °C

Equipment & Instrumentation:
	•	Lauter tun with rake arms and false bottom
	•	Turbidity sensor at wort outlet
	•	Flow transmitter on wort and sparge lines
	•	Level transmitter in lauter tun
	•	Motorized valve to divert cloudy wort to waste

Steps:
	1.	Begin recirculation until turbidity < 200 NTU
	2.	Start wort transfer to kettle
	3.	Begin sparging at 76 °C while maintaining lauter tun level
	4.	Adjust rake arm position based on wort flow resistance
	5.	Stop sparging when grain bed is dry and total volume reached
	6.	Flush lauter tun with hot water to clean and prepare for next batch

⸻

🟩 I (Impact) – Benefits and Risks

Benefits:
	•	Improved consistency in lautering process
	•	Reduced risk of stuck sparging or incomplete lautering
	•	Enhanced efficiency in wort transfer and sparging

Risks:
	•	Improperly calibrated instrumentation may lead to incorrect setpoint control
	•	Inadequate rake arm positioning could result in uneven wort flow
	•	Over- or under-sparging may impact beer quality and yield

⸻

🟩 A (Action) – Task to Perform

Develop a detailed control narrative for the entire beer brewing process, including concrete setpoints and ranges, and provide a step-by-step description of the lautering process, including equipment and instrumentation used. Ensure that the narrative is actionable and provides clear guidance for engineering and operations teams.
**C-A-R-E:**

🟥 C (Context) – Background Situation

In the beer brewing process, lautering is a critical stage where wort is separated from the grain. Proper control of temperature, flow, and turbidity is essential to ensure efficient separation and consistent beer quality. However, without a clear control narrative, operators may struggle to maintain precise setpoints and execute the lautering process effectively.

⸻

🟩 A (Action) – Task to Perform

Develop a detailed control narrative for the lautering process, including concrete setpoints and ranges for temperature, flow, and turbidity. Describe the equipment and instrumentation used during lautering, and provide a step-by-step description of the process logic, including automated control actions triggered by sensor feedback and operator input.

⸻

🟨 R (Result) – Expected Outcome

The result should be a comprehensive control narrative that:
	•	Defines setpoints and ranges for lautering, including temperature, flow, and turbidity
	•	Describes the equipment and instrumentation used during lautering, such as the lauter tun, rake arms, and turbidity sensor
	•	Outlines the step-by-step process logic for lautering, including recirculation, wort transfer, sparging, and cleaning
	•	Explains how automated

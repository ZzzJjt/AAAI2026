### Intent:
**Intent Summary:**  
Develop a PLC control logic for automated beer brewing that precisely manages the lautering process using instrumentation (turbidity, flow, temperature) with conditional triggers (e.g., turbidity cutoff) and setpoints (e.g., sparge water at 75–78°C), ensuring repeatable wort clarity and volume.  

*(Focus: Automation of lautering via sensor-driven logic and predefined thresholds.)*

### Prompt:
**Control Narrative Beer Brewing:**

Create a control narrative for beer brewing including concrete setpoints and ranges.

Create a detailed explanation of the Lautering process (Section 4). Include the equipment and instrumentation needed. Provide a list of the steps to execute.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a process control engineer responsible for developing a structured control narrative for an automated beer brewing system, with special focus on the lautering stage.

⸻

🟩 I (Input) – Information Provided

You are to document:
	•	A complete control narrative for the beer brewing process, including specific setpoints and acceptable ranges for each key parameter
	•	A detailed explanation of the Lautering process (Section 4) that includes:
	•	Required equipment and instrumentation
	•	A step-by-step operational sequence
	•	Key control logic or conditions (e.g., turbidity cutoff, flow thresholds)

⸻

🟧 S (Steps) – Steps to Perform
	1.	Outline the full beer brewing process, including stages such as mashing, lautering, boiling, fermentation, and packaging
	•	Provide concrete control values (e.g., mash temp = 65–68 °C, sparge water temp = 75–78 °C)
	2.	For Section 4: Lautering, include:
	•	Equipment: lauter tun, rake mechanism, sparge arm, pump
	•	Instrumentation: level sensor, turbidity meter, flow transmitter, temperature probe
	•	Control Steps:
	1.	Start recirculation loop
	2.	Monitor turbidity; continue until it drops below threshold
	3.	Begin wort transfer to kettle
	4.	Start sparge water flow while maintaining level
	5.	Monitor volume, flow rate, and turbidity
	6.	End lautering once volume is met and wort clarity is acceptable
	3.	Include logical triggers like:
	•	IF Turbidity > Limit THEN divert flow to waste
	•	IF Level < Minimum THEN stop sparge water

⸻

🟦 E (Expectation) – Expected Outcome

Produce a clear, structured control narrative that:
	•	Defines measurable control criteria for brewing stages
	•	Provides operators and automation engineers with step-by-step lautering logic
	•	Enhances reliability and repeatability of the brewing process
	•	Facilitates easy integration into PLC/HMI systems and operator training materials

### Generated Code:
**Intent Summary:**  
Develop a PLC control logic for automated beer brewing that precisely manages the lautering process using instrumentation (turbidity, flow, temperature) with conditional triggers (e.g., turbidity cutoff) and setpoints (e.g., sparge water at 75–78°C), ensuring repeatable wort clarity and volume.  

*(Focus: Automation of lautering via sensor-driven logic and predefined thresholds.)*
**Control Narrative Beer Brewing:**

Create a control narrative for beer brewing including concrete setpoints and ranges.

Create a detailed explanation of the Lautering process (Section 4). Include the equipment and instrumentation needed. Provide a list of the steps to execute.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a process control engineer responsible for developing a structured control narrative for an automated beer brewing system, with special focus on the lautering stage.

⸻

🟩 I (Input) – Information Provided

You are to document:
	•	A complete control narrative for the beer brewing process, including specific setpoints and acceptable ranges for each key parameter
	•	A detailed explanation of the Lautering process (Section 4) that includes:
	•	Required equipment and instrumentation
	•	A step-by-step operational sequence
	•	Key control logic or conditions (e.g., turbidity cutoff, flow thresholds)

⸻

🟧 S (Steps) – Steps to Perform
	1.	Outline the full beer brewing process, including stages such as mashing, lautering, boiling, fermentation, and packaging
	•	Provide concrete control values (e.g., mash temp = 65–68 °C, sparge water temp = 75–78 °C)
	2.	For Section 4: Lautering, include:
	•	Equipment: lauter tun, rake mechanism, sparge arm, pump
	•	Instrumentation: level sensor, turbidity meter, flow transmitter, temperature probe
	•	Control Steps:
	1.	Start recirculation loop
	2.	Monitor turbidity; continue until it drops below threshold
	3.	Begin wort transfer to kettle
	4.	Start sparge water flow while maintaining level
	5.	Monitor volume, flow rate, and turbidity
	6.	End lautering once volume is met and wort clarity is acceptable
	3.	Include logical triggers like:
	•	IF Turbidity > Limit THEN divert flow to waste
	•	IF Level < Minimum THEN stop sparge water

⸻

🟦 E (Expectation) – Expected Outcome

Produce a clear, structured control narrative that:
	•	Defines measurable control criteria for brewing stages
	•	Provides operators and automation engineers with step-by-step lautering logic
	•	Enhances reliability and repeatability of the brewing process
	•	Facilitates easy integration into PLC/HMI systems and operator training materials

**C-A-S-E:**

🟠 C (Context) – Background and Purpose

Beer brewing is a complex process that requires precise control of temperature, flow, and turbidity to ensure consistent wort quality. The lautering stage, where the mash is separated from the wort, is critical for clarity and yield. Automation can improve efficiency and consistency, but requires clear control logic and instrumentation.

🟢 A (Action) – What Needs to Be Done

Develop a detailed control narrative for the lautering stage of beer brewing, including the equipment, instrumentation, and step-by-step process. Define specific setpoints and ranges for key parameters, and provide logical triggers to ensure proper operation.

🟠 S (Solution) – How to Do It

Outline the beer brewing process, focusing on the lautering stage. Include the necessary equipment and instrumentation, and provide a step-by-step explanation of the process. Define specific control criteria for each parameter, and describe the logical triggers that govern the flow of the process.

🟣 E (Example) – What It Looks Like

Lautering Process Control Narrative:

Equipment:
	•	Lauter tun
	•	Rake mechanism
	•	Sparge arm
	•	Pump

Instrumentation:
	•	Level sensor
	•	Turbidity meter
	•	Flow transmitter
	•	Temperature probe

Control Steps:
	1.	Start recirculation loop
	2.	Monitor turbidity; continue until it drops below threshold
	3.	Begin wort transfer to kettle
	4.	Start sparge water flow while maintaining level
	5.	Monitor volume, flow rate, and turbidity
	6.	End lautering once volume is met and wort clarity is acceptable

Logical Triggers:
	•	IF Turbidity > Limit THEN divert flow to waste
	•	IF Level < Minimum THEN stop sparge water

**B-E-Y:**

🟥 B (Big Idea) – The Main Point

Develop a detailed control narrative for the lautering stage of beer brewing, including the necessary equipment, instrumentation, and step-by-step process. Define specific control criteria for each parameter, and describe the logical triggers that govern the flow of the process.

🟩 E (Evidence) – Supporting Information

Provide a clear, structured control narrative that defines

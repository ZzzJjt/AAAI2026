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

**Control Narrative Beer Brewing:**

**1. Mashing**

*Equipment:* Mash tun, malt mill, heat exchanger, pump

*Instrumentation:* pH probe, temperature probe, flow transmitter

*Control Steps:*

1.	Add malted grains to mash tun
2.	Add water to mash tun
3.	Start mash tun agitation
4.	Heat water to target mash temperature (65–68 °C)
5.	Monitor pH and temperature during mashing process
6.	Mash for specified time (60–90 minutes)
7.	Recirculate wort during mashing
8.	Drain wort from mash tun to lauter tun

**2. Lautering**

*Equipment:* Lauter tun, rake mechanism, sparge arm, pump

*Instrumentation:* level sensor, turbidity meter, flow transmitter, temperature probe

*Control Steps:*

1.	Start recirculation loop
2.	Monitor turbidity; continue until it drops below threshold (e.g., 20 NTU)
3.	Begin wort transfer to kettle
4.	Start sparge water flow while maintaining level
5.	Monitor volume, flow rate, and turbidity
6.	End lautering once volume is met and wort clarity is acceptable (e.g., turbidity < 5 NTU)
7.	IF Turbidity > Limit THEN divert flow to waste
8.	IF Level < Minimum THEN stop sparge water

**3. Boiling**

*Equipment:* Kettle, heat exchanger, whirlpool, pump

*Instrumentation:* temperature probe, flow transmitter

*Control Steps:*

1.	Transfer wort from lauter tun to kettle
2.	Heat wort to boiling point (100 °C)
3.	Add hops during boiling
4.	Maintain boil for specified time (60–90 minutes)
5.	Recirculate wort during boiling
6.	Whirlpool

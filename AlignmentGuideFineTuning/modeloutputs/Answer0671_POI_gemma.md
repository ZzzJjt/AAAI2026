### Intent:
"Generate a detailed I/O list for a feedwater control system in a power plant's steam-water cycle, including signal tags, types, units, ranges, setpoints, and P&ID references."

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
"Generate a detailed I/O list for a feedwater control system in a power plant's steam-water cycle, including signal tags, types, units, ranges, setpoints, and P&ID references."
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

**Control Narrative for Beer Brewing**

**1. Introduction**

This control narrative describes the process of brewing beer, with a focus on the lautering stage. The goal of this narrative is to provide a clear and structured set of control criteria for the brewing stages, as well as a detailed explanation of the lautering process. This will help to ensure the reliability and repeatability of the brewing process, and facilitate easy integration into PLC/HMI systems and operator training materials.

**2. Brewing Stages**

The brewing process can be divided into several stages, including mashing, lautering, boiling, fermentation, and packaging. Each stage has its own set of control criteria that must be met in order to produce a high-quality beer.

**2.1 Mashing**

Mashing is the process of converting the starches in the grain into fermentable sugars. The mashing stage typically takes place in a mash tun, and involves heating the grain and water mixture to a specific temperature range (e.g., 65–68 °C). The mashing stage is important for extracting the maximum amount of fermentable sugars from the grain, and for ensuring that the final beer has the desired flavor and body.

**2.2 Lautering**

Lautering is the process of separating the wort (the liquid containing the fermentable sugars) from the spent grain. The lautering stage typically takes place in a lauter tun, and involves using a rake mechanism to move the grain and wort through the tun. The wort is then transferred to a kettle for boiling, while the spent grain is removed.

**2.3 Boiling**

Boiling is the process of boiling the wort to sterilize it and to concentrate the sugars. The boiling stage typically takes place in a kettle, and involves heating the wort to a specific temperature range (e.g., 75–78 °C). The boiling stage is important for killing any bacteria or other contaminants that may be present in the wort, and for concentrating the sugars to produce a more flavorful beer.

**2.4 Fermentation**

Fermentation is the process of converting the fermentable sugars into alcohol and carbon dioxide. The fermentation stage typically takes place in a fermentation tank, and involves adding yeast to the wort and allowing it to ferment for a period of time (e.g., 7–10 days). The fermentation stage is important for producing the alcohol and carbon dioxide that give beer its characteristic flavor and carbonation.

**

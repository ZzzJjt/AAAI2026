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

⸻

🟩 S (Solution) – Your Work

1.	Control Narrative:

| Stage | Control Parameters | Setpoints | Range |
| --- | --- | --- | --- |
| Mashing | Mash temperature | 65–68 °C |  |
| Mashing | Sparge water temperature | 75–78 °C |  |
| Lautering | Lauter tun level |  |  |
| Lautering | Turbidity |  |  |
| Lautering | Wort flow rate |  |  |
| Lautering | Sparge water flow rate |  |  |

2.	Lautering Process (Section 4):

| Equipment | Description |
| --- | --- |
| Lauter tun | Receives mash and separates wort |
| Rake mechanism | Manually or automatically moves grain bed |
| Sparge arm | Directs sparge water into mash bed |
| Pump | Serves as wort and sparge water transfer mechanism |

| Instrumentation | Description |
| --- | --- |
| Level sensor | Monitors lauter tun level |
| Turbidity meter | Measures turbidity of wort |
| Flow transmitter | Monitors wort and sparge water flow rates |
| Temperature probe | Monitors mash and sparge water temperatures |

| Control Steps | Description |
| --- | --- |
| 1 | Start recirculation loop |
| 2 | Monitor turbidity; continue until it drops below threshold |
| 3 | Begin wort transfer to kettle |
| 4 | Start sparge water flow while maintaining level |
| 5 | Monitor volume, flow rate, and turbidity |
| 6 | End lautering once volume is met and wort clarity is acceptable |

3.	Logical Triggers:

•	IF Turbidity > Limit THEN divert flow to waste
•	IF Level < Minimum THEN stop sparge water

⸻

🟨 I (Implementation) – Your Next Steps

1.	Review the control narrative and lautering process for clarity and completeness.
2.	Ensure that the control parameters and steps are well-defined and easy to understand.
3.	Consider integrating the control narrative and la

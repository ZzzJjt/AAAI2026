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
	•	Includes concrete ranges and setpoints for critical parameters
	•	Ensures safe and efficient operation of the lautering process
	•	Is suitable for use in brewing control systems, including PID loops and alarm conditions
	•	Is compliant with brewing standards and best practices
	•	Includes a P&ID diagram for the Lautering process, detailing instrumentation and control loops
	•	Is written in a clear, structured format with headings and subheadings for easy navigation
	•	Includes a list of equipment and instrumentation needed for the Lautering process
	•	Outlines the operational sequence for lautering, including specific steps and control conditions
	•	Includes concrete setpoints and acceptable ranges for key parameters, such as turbidity, flow rates, and temperature
	•	Describes the role of instrumentation, including level sensors, turbidity meters, and flow transmitters
	•	Outlines the control logic for the Lautering process, including conditions for starting and stopping the process, as well as alarms and safety interlocks
	•	Includes a P&ID diagram for the Lautering process, detailing instrumentation and control loops
	•	Is suitable for use in brewing control systems, including PID loops and alarm conditions
	•	Is written in a clear, structured format with headings and subheadings for easy navigation
	•	Includes a list of equipment and instrumentation needed for the Lautering process
	•	Outlines the operational sequence for lautering, including specific steps and control conditions
	•	Includes concrete setpoints and acceptable ranges for key parameters, such as turbidity, flow rates, and temperature
	•	Describes the role of instrumentation, including level sensors, turbidity meters, and flow transmitters
	•	Outlines the control logic for the Lautering process, including conditions for starting and stopping the process, as well as alarms and safety interlocks
	•	Includes a P&ID diagram for the Lautering process, detailing instrumentation and control loops
	•	Is suitable for use in brewing control systems, including PID loops and alarm conditions
	•	Is written in a clear, structured format with headings and subheadings for easy navigation
	•	Includes a list of equipment and instrumentation needed for the Lautering process
	•	Outlines the operational sequence for lautering, including specific steps and control conditions
	•	Includes concrete setpoints and acceptable ranges for key

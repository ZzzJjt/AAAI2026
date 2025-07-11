### Intent:
**Intent Summary:**  
Develop a control narrative for automated beer brewing with specific setpoints, focusing on the lautering process (equipment, instrumentation, and step-by-step logic) to ensure repeatability and integration with PLC/HMI systems.  

**Code Generation Intent:**  
Create structured control logic for beer brewing automation, emphasizing lautering stage parameters (turbidity, flow, temperature) with conditional triggers for operational reliability.

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
Develop a control narrative for automated beer brewing with specific setpoints, focusing on the lautering process (equipment, instrumentation, and step-by-step logic) to ensure repeatability and integration with PLC/HMI systems.  

**Code Generation Intent:**  
Create structured control logic for beer brewing automation, emphasizing lautering stage parameters (turbidity, flow, temperature) with conditional triggers for operational reliability.
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

---

**Control Narrative Beer Brewing:**

**1. Beer Brewing Process**

The beer brewing process consists of several stages, each with its own set of control parameters. These stages include:

- **Mashing:** The process of converting starches in the grain into fermentable sugars. Control parameters include mash temperature, pH, and time.
- **Lautering:** The process of separating the liquid wort from the solid spent grain. Control parameters include lauter tun temperature, turbidity, and flow rate.
- **Boiling:** The process of sterilizing the wort and adding hops for bitterness and flavor. Control parameters include boiling time, temperature, and hop addition schedule.
- **Fermentation:** The process of converting sugars into alcohol and carbon dioxide. Control parameters include temperature, pH, and oxygen levels.
- **Packaging:** The process of filling and packaging the finished beer. Control parameters include fill volume, carbonation level, and temperature.

**2. Lautering Process**

The lautering process is a critical stage in the beer brewing process. It involves separating the liquid wort from the solid spent grain. The following equipment and instrumentation are required for this process:

- **Lauter Tun:** A large, insulated vessel used to hold the mash and lauter water.
- **Rake Mechanism:** A device used to stir the mash and ensure even distribution of water.
- **Sparge Arm:** A pipe used to introduce sparge water into the lauter tun.
- **Pump:** A device used to circulate the wort and sparge water.
- **Level Sensor:** A device used to measure the level of the wort in the lauter tun.
- **Turbidity Meter:** A device used to measure the clarity of the wort.
- **Flow Transmitter:** A device used to measure the flow rate of the wort and sparge water.
- **Temperature Probe:** A device used to measure the temperature of the wort and sparge water.

**3. Lautering Process Steps**

The following steps should be followed during the lautering process:

1. **Start Recirculation Loop:** Begin circulating the wort and sparge water through the lauter tun using the pump.
2. **Monitor Turbidity:** Continuously monitor the turbidity of the wort using the turbidity meter. Continue rec

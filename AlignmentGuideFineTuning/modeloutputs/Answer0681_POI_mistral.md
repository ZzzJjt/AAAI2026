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

**Code Generation:**

```
// Beer Brewing Control Logic

// Define key parameters and setpoints
const MASH_TEMP = 65.0 - 68.0;
const SPARGE_WATER_TEMP = 75.0 - 78.0;
const TURBIDITY_LIMIT = 10.0;
const MIN_LEVEL = 0.5;

// Lautering Control Logic
function lautering() {
  // Start recirculation loop
  startRecirculation();

  // Monitor turbidity
  let turbidity = getTurbidity();
  while (turbidity > TURBIDITY_LIMIT) {
    turbidity = getTurbidity();
  }

  // Begin wort transfer to kettle
  startWortTransfer();

  // Start sparge water flow
  startSparseWater();

  // Monitor volume, flow rate, and turbidity
  let volume = getVolume();
  let flowRate = getFlowRate();
  let currentTurbidity = getTurbidity();

  // End lautering once volume is met and wort clarity is acceptable
  while (volume < TARGET_VOLUME && currentTurbidity <= TURBIDITY_LIMIT) {
    volume = getVolume();
    flowRate = getFlowRate();
    currentTurbidity = getTurbidity();
  }

  // IF Turbidity > Limit THEN divert flow to waste
  if (currentTurbidity > TURBIDITY_LIMIT) {
    divertFlowToWaste();
  }

  // IF Level < Minimum THEN stop sparge water
  if (getLevel() < MIN_LEVEL) {
    stopSparseWater();
  }
}
```

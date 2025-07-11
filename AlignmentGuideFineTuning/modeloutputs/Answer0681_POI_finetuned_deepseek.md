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
FUNCTION_BLOCK FB_LauteringControl
VAR_INPUT
    Turbidity_Threshold : REAL; // Turbidity threshold (e.g., 100 NTU)
    Level_Min : REAL;          // Minimum lauter tun level (e.g., 100 mm)
    Flow_Max : REAL;           // Maximum lauter tun flow rate (e.g., 100 L/min)
    Temperature_Min : REAL;     // Minimum lauter tun temperature (e.g., 75 °C)
    Temperature_Max : REAL;     // Maximum lauter tun temperature (e.g., 80 °C)
END_VAR

VAR_OUTPUT
    Turbidity_Val : REAL;      // Current turbidity reading (e.g., 100 NTU)
    Level_Val : REAL;          // Current lauter tun level (e.g., 100 mm)
    Flow_Val : REAL;           // Current lauter tun flow rate (e.g., 100 L/min)
    Temperature_Val : REAL;    // Current lauter tun temperature (e.g., 75 °C)
    Trigger_Lautering : BOOL; // TRUE if lautering is active
    Trigger_Stop : BOOL;      // TRUE if lautering is complete
END_VAR

VAR
    Turbidity_Sensor : REAL;   // Turbidity sensor reading
    Level_Sensor : REAL;       // Level sensor reading
    Flow_Sensor : REAL;        // Flow sensor reading
    Temperature_Sensor : REAL; // Temperature sensor reading
END_VAR

// Initialize outputs
Turbidity_Val := 0.0;
Level_Val := 0.0;
Flow_Val := 0.0;
Temperature_Val := 0.0;
Trigger_Lautering := FALSE;
Trigger_Stop := FALSE;

// Step 1: Check Turbidity
IF Turbidity_Sensor > Turbidity_Threshold THEN
    Turbidity_Val := Turbidity_Sensor;
    Trigger_Lautering := TRUE;
END_IF;

// Step 2: Check Level
IF Level_Sensor < Level_Min THEN
    Level_Val := Level_Sensor;
    Trigger_Laut

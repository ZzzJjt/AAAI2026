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

---

**Control Narrative Beer Brewing:**

**1. Introduction**

The beer brewing process is a complex series of steps that transform raw materials into a finished product. This control narrative outlines the key stages of the brewing process, including the lautering stage, and provides specific setpoints and ranges for each stage. The lautering stage is critical for separating the liquid wort from the solid grains, and this narrative details the equipment, instrumentation, and control logic required to execute this process successfully.

**2. Mashing**

- **Setpoint:** Mash temperature = 65–68°C
- **Range:** Maintain temperature within ±1°C of setpoint
- **P&ID Reference:** [Mash Tank]

**3. Boiling**

- **Setpoint:** Boil time = 60 minutes
- **Range:** Maintain boil time within ±5 minutes of setpoint
- **P&ID Reference:** [Boiler]

**4. Lautering**

**4.1 Equipment and Instrumentation**

- **Lauter Tun:** Vessel for separating wort from spent grains
- **Rake Mechanism:** Stirring device to maintain grain bed stability
- **Sparge Arm:** Arm with perforated tube for sparging hot water
- **Pump:** For recirculation and wort transfer
- **Level Sensor:** Monitors lauter tun level
- **Turbidity Meter:** Measures wort clarity
- **Flow Transmitter:** Monitors sparge water flow rate
- **Temperature Probe:** Measures wort and sparge water temperature

**4.2 Control Steps**

1. **Start Recirculation Loop:**
   - Begin recirculation of wort through lauter tun to maintain grain bed stability
   - Setpoint: Flow rate = 10–15 L/min
   - Range: Maintain flow rate within ±5% of setpoint
   - P&ID Reference: [Recirculation Pump]

2. **Monitor Turbidity:**
   - Continuously monitor turbidity until it drops below a predetermined threshold
   - Setpoint: Turbidity = 5 NTU (Nephelometric Turbidity Units)
   - Range: Maintain turbidity within ±1 NTU of setpoint
   - P&ID Reference: [Turbidity

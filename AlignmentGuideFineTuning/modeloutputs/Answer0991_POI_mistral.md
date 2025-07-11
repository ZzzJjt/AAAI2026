### Intent:
**Intent Summary:**  
Create an automation-ready control narrative for an LNG vaporizer system (100,000 kg/h capacity) with detailed process flows, instrumentation tags (NORSOK I-005), PID control loops, and safety interlocks to ensure safe, efficient vaporization of LNG to natural gas at specified setpoints (e.g., 10°C outlet, 4.5 bar pressure).  

*(Focus: Code generation for industrial control logic, instrumentation mapping, and interlock implementation.)*

### Prompt:
**Control Narrative Beer Brewing:**

Create a control narrative for beer brewing including concrete setpoints and ranges.

Create a detailed explanation of the Lautering process (Section 4). Include the equipment and instrumentation needed. Provide a list of the steps to execute.

**T-A-G:**

🟥 T (Task)

Create a control narrative for an automated beer brewing process, with emphasis on specifying concrete setpoints and detailing the lautering phase (Section 4).

⸻

🟩 A (Action)
	•	Define the brewing process stages, including specific setpoints and control ranges for parameters like temperature, flow rate, and volume.
	•	In Section 4 – Lautering, include:
	•	A list of required equipment: lauter tun, rake motor, sparge system, wort pump
	•	A list of required instrumentation: turbidity meter, flow transmitter, level sensor, temperature probe
	•	A step-by-step procedure for the lautering process, such as:
	1.	Start recirculation of wort
	2.	Monitor turbidity; wait until it drops below 200 NTU
	3.	Begin transferring wort to the kettle
	4.	Add sparge water at 76 °C to maintain lauter tun level between 60–80%
	5.	Stop process based on turbidity or volume criteria
	•	Include interlock logic, such as:
	•	IF Turbidity > Limit THEN open waste valve
	•	IF Level < Minimum THEN stop sparging

⸻

🟦 G (Goal)

Deliver a clear, structured, and automation-ready control narrative that can be used by control engineers, brewers, and programmers to ensure consistency, quality, and operational reliability in the beer brewing process—especially during the critical lautering phase.

### Generated Code:
**Intent Summary:**  
Create an automation-ready control narrative for an LNG vaporizer system (100,000 kg/h capacity) with detailed process flows, instrumentation tags (NORSOK I-005), PID control loops, and safety interlocks to ensure safe, efficient vaporization of LNG to natural gas at specified setpoints (e.g., 10°C outlet, 4.5 bar pressure).  

*(Focus: Code generation for industrial control logic, instrumentation mapping, and interlock implementation.)*
**Control Narrative Beer Brewing:**

Create a control narrative for beer brewing including concrete setpoints and ranges.

Create a detailed explanation of the Lautering process (Section 4). Include the equipment and instrumentation needed. Provide a list of the steps to execute.

**T-A-G:**

🟥 T (Task)

Create a control narrative for an automated beer brewing process, with emphasis on specifying concrete setpoints and detailing the lautering phase (Section 4).

⸻

🟩 A (Action)
	•	Define the brewing process stages, including specific setpoints and control ranges for parameters like temperature, flow rate, and volume.
	•	In Section 4 – Lautering, include:
	•	A list of required equipment: lauter tun, rake motor, sparge system, wort pump
	•	A list of required instrumentation: turbidity meter, flow transmitter, level sensor, temperature probe
	•	A step-by-step procedure for the lautering process, such as:
	1.	Start recirculation of wort
	2.	Monitor turbidity; wait until it drops below 200 NTU
	3.	Begin transferring wort to the kettle
	4.	Add sparge water at 76 °C to maintain lauter tun level between 60–80%
	5.	Stop process based on turbidity or volume criteria
	•	Include interlock logic, such as:
	•	IF Turbidity > Limit THEN open waste valve
	•	IF Level < Minimum THEN stop sparging

⸻

🟦 G (Goal)

Deliver a clear, structured, and automation-ready control narrative that can be used by control engineers, brewers, and programmers to ensure consistency, quality, and operational reliability in the beer brewing process—especially during the critical lautering phase.

---

**Control Narrative for Beer Brewing:**

**1. Mashing**

*Equipment:* Mash tun, malt mill, pump, temperature probe, flow meter

*Setpoints:*
	•	Mash temperature: 65°C
	•	Mash time: 60 minutes
	•	Mash thickness: 1.5 kg/L

*Procedure:*
	1.	Add malt to the mash tun
	2.	Add water to achieve the desired mash thickness
	3.	Start the malt mill
	4.	Heat the mash tun to the target temperature
	5.	Maintain the temperature for the specified time
	6.	Drain the mash tun into the lauter tun

**2. Sparge**

*Equipment:* Lauter tun, rake motor, sparge system, wort pump, temperature probe, flow transmitter, level sensor

*Setpoints:*
	•	Lauter tun temperature: 76°C
	•	Lauter tun level: 60–80%

*Procedure:*
	1.	Start recirculation of wort
	2.	Monitor turbidity; wait until it drops below 200 NTU
	3.	Begin transferring wort to the kettle
	4.	Add sparge water at 76°C to maintain lauter tun level between 60–80%
	5.	Stop process based on turbidity or volume criteria

*Interlocks:*
	•	IF Turbidity > Limit THEN open waste valve
	•	IF Level < Minimum THEN stop sparging

**3. Boiling**

*Equipment:* Kettle, heat exchanger, temperature probe, flow meter

*Setpoints:*
	•	Kettle temperature: 100°C
	•	Boil time: 90 minutes

*Procedure:*
	1.	Transfer wort from the lauter tun to the kettle
	2.	Heat the wort to the target temperature
	3.	Maintain the temperature for the specified time

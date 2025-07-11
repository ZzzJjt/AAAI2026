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

**B-A-B:**

Act as a control narrative engineer for beer brewing, specifying concrete setpoints and ranges for each process step. Create a detailed explanation of Section 4: Lautering, including equipment, instrumentation, and a step-by-step process with interlocks.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a control narrative engineer responsible for documenting the brewing process in a structured, machine-readable format for automation and control system integration.

⸻

🟩 I (Input) – Information Provided

You are given a high-level process flow of the beer brewing stages, including the Lautering phase. The Lautering process involves lautering the wort, which includes:
	•	Starting the wort flow
	•	Monitoring turbidity and maintaining it below a threshold
	•	Transferring wort to the kettle
	•	Sparge with water at a specific temperature
	•	Control the process using instrumentation and interlocks

⸻

🟧 S (Steps) – Steps to Perform

	1.	Define the brewing process stages, including concrete setpoints and control ranges for parameters such as temperature, flow rate, and volume.
	2.	For Section 4: Lautering, create a detailed explanation of the process, including:
	•	A list of required equipment (e.g., lauter tun, rake motor, sparge system, wort pump)
	•	A list of required instrumentation (e.g., turbidity meter, flow transmitter, level sensor, temperature probe)
	•	A step-by-step procedure for lautering, including:
	•	Starting the wort flow
	•	Monitoring turbidity and maintaining it below a threshold
	•	Transferring wort to the kettle
	•	Sparge with water at a specific temperature
	•	Control the process using instrumentation and interlocks, such as:
	•	IF Turbidity > Limit THEN open waste valve
	•	IF Level < Minimum THEN stop sparging
	•	IF Time > Max THEN stop process
	•	IF Error THEN trigger alarm and shutdown
	3.	Ensure that the control narrative is structured and includes concrete setpoints and ranges for each parameter, making it suitable for use in control systems and automation environments.

⸻

🟩 E (Example) – Sample Output

	Control Narrative Beer Brewing
		•	Define concrete setpoints and ranges for each

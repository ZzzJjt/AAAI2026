### Intent:
**Intent Summary:**  
Create a text-based P&ID (Piping & Instrumentation Diagram) for a power plant's steam-water cycle, detailing equipment, instrumentation, control loops, and process flows to guide automation (e.g., PLC/HMI configuration) with clear setpoints, alarms, and signal logic.  

*(Focus: Structured documentation for control system implementation.)*

### Prompt:
**Control Narrative Beer Brewing:**

Create a control narrative for beer brewing including concrete setpoints and ranges.

Create a detailed explanation of the Lautering process (Section 4). Include the equipment and instrumentation needed. Provide a list of the steps to execute.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In brewery automation projects, engineers often lack standardized documentation for complex processes like beer brewing. Without a well-structured control narrative, it’s difficult to define setpoints, control logic, and instrumentation for each phase—especially for stages like lautering, which involve precise timing, flow control, and mechanical coordination. Inconsistent or vague narratives can lead to inefficiencies or errors during automation design or commissioning.

⸻

🟩 A (After) – The Desired Outcome

Develop a comprehensive control narrative for the beer brewing process, including:
	•	Clear setpoints and acceptable operating ranges for key parameters (e.g., temperature, flow, timing)
	•	A focused explanation of the lautering process (Section 4), covering:
	•	Required equipment and instrumentation (e.g., lauter tun, rake system, flow transmitters)
	•	Step-by-step procedure for lautering
	•	Relevant automation logic or decision conditions

⸻

🟧 B (Bridge) – How to Get There
	1.	Begin by outlining the overall brewing process with specific control points, such as:
	•	Mash temperature: 65–68 °C
	•	Sparge water temperature: 75–78 °C
	•	Lautering flow rate: 1.5–2.0 L/min
	•	Holding tank level: 50–80%
	2.	In Section 4 (Lautering):
	•	Describe the physical components: lauter tun, rake motor, underlet system, flowmeters
	•	List instrumentation: temperature sensors, turbidity sensors, level transmitters
	•	Step-by-step control logic, including:
	•	Rake arm position control
	•	Flow ramp-up sequence
	•	Turbidity-based decision to stop lautering
	3.	Include control logic like:
	•	IF turbidity > threshold THEN divert flow to waste
	•	IF level < min THEN stop sparge water
	4.	Use structured formatting and bullet points or numbered steps for clarity

### Generated Code:
**Intent Summary:**  
Create a text-based P&ID (Piping & Instrumentation Diagram) for a power plant's steam-water cycle, detailing equipment, instrumentation, control loops, and process flows to guide automation (e.g., PLC/HMI configuration) with clear setpoints, alarms, and signal logic.  

*(Focus: Structured documentation for control system implementation.)*
**Control Narrative Beer Brewing:**

Create a control narrative for beer brewing including concrete setpoints and ranges.

Create a detailed explanation of the Lautering process (Section 4). Include the equipment and instrumentation needed. Provide a list of the steps to execute.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In brewery automation projects, engineers often lack standardized documentation for complex processes like beer brewing. Without a well-structured control narrative, it’s difficult to define setpoints, control logic, and instrumentation for each phase—especially for stages like lautering, which involve precise timing, flow control, and mechanical coordination. Inconsistent or vague narratives can lead to inefficiencies or errors during automation design or commissioning.

⸻

🟩 A (After) – The Desired Outcome

Develop a comprehensive control narrative for the beer brewing process, including:
	•	Clear setpoints and acceptable operating ranges for key parameters (e.g., temperature, flow, timing)
	•	A focused explanation of the lautering process (Section 4), covering:
	•	Required equipment and instrumentation (e.g., lauter tun, rake system, flow transmitters)
	•	Step-by-step procedure for lautering
	•	Relevant automation logic or decision conditions

⸻

🟧 B (Bridge) – How to Get There
	1.	Begin by outlining the overall brewing process with specific control points, such as:
	•	Mash temperature: 65–68 °C
	•	Sparge water temperature: 75–78 °C
	•	Lautering flow rate: 1.5–2.0 L/min
	•	Holding tank level: 50–80%
	2.	In Section 4 (Lautering):
	•	Describe the physical components: lauter tun, rake motor, underlet system, flowmeters
	•	List instrumentation: temperature sensors, turbidity sensors, level transmitters
	•	Step-by-step control logic, including:
	•	Rake arm position control
	•	Flow ramp-up sequence
	•	Turbidity-based decision to stop lautering
	3.	Include control logic like:
	•	IF turbidity > threshold THEN divert flow to waste
	•	IF level < min THEN stop sparge water
	4.	Use structured formatting and bullet points or numbered steps for clarity.

**Control Narrative: Beer Brewing**

**1. Mashing**

*Equipment:* Mash tun, heating system, temperature sensor

*Setpoints:*
	- Mash temperature: 65–68 °C

*Procedure:*
	1. Add malted grains to the mash tun.
	2. Add hot water to the mash tun to achieve the desired temperature.
	3. Monitor and maintain the mash temperature using the heating system.

**2. Mash Rest**

*Equipment:* Mash tun, temperature sensor

*Setpoints:*
	- Mash temperature: 65–68 °C

*Procedure:*
	1. Allow the mash to rest for a specified period (e.g., 60 minutes).
	2. Monitor and maintain the mash temperature.

**3. Mash Out**

*Equipment:* Mash tun, heating system, temperature sensor

*Setpoints:*
	- Mash temperature: 76–78 °C

*Procedure:*
	1. Increase the temperature of the mash to the mash-out temperature.
	2. Hold the mash-out temperature for a specified period (e.g., 15 minutes).
	3. Monitor and maintain the mash-out temperature.

**4. Lautering**

*Equipment:* Lauter tun, rake system, underlet system, flowmeters, temperature sensors, turbidity sensors, level transmitters

*Setpoints:*
	- Lautering flow rate: 1.5–2.0 L/min
	- Lautering temperature: 76–78 °C
	- Lautering turbidity: 100–200 NTU
	- Holding tank level: 50–80%

*Procedure:*
	1. Transfer the mash to the lauter tun.
	2. Start the rake system to agitate the mash.
	3. Begin sparging with hot water (75–78 °C) to rinse the grains.
	4

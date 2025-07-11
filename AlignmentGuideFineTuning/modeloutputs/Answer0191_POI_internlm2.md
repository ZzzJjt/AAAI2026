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
	4.	Use structured formatting and bullet points or numbered steps for clarity and ease of understanding.

**Control Narrative Beer Brewing:**

**Brewing Process Control Narrative**

**1.** **Mashing**
	•	Target temperature: 65–68 °C
	•	Acceptable range: 63–70 °C
	•	Control logic: Monitor mash temperature and adjust heating/cooling as needed.

**2.** **Sparge**
	•	Target temperature: 75–78 °C
	•	Acceptable range: 72–80 °C
	•	Control logic: Monitor sparge water temperature and adjust heating/cooling as needed.

**3.** **Lautering**
	•	Target flow rate: 1.5–2.0 L/min
	•	Acceptable range: 1.2–2.5 L/min
	•	Control logic: Monitor flow rate and adjust rake arm position to maintain target rate.

**4.** **Lautering Process**
	•	Required equipment:
		- Lauter tun
		- Rake system (rake arm, motor)
		- Underlet system (flowmeters, valves)
	•	Instrumentation:
		- Temperature sensors (mash, wort)
		- Turbidity sensors (wort)
		- Level transmitters (holding tank)
	•	Step-by-step procedure:
		1.	Start rake arm at bottom of lauter tun
		2.	Increase rake arm speed to ramp up flow
		3.	Monitor turbidity sensors
		4.	When turbidity reaches threshold, stop rake arm
		5.	Check level transmitters
		6.	When level reaches minimum, stop sparge water
		7.	Check flow rate
		8.	When flow rate is within acceptable range, stop rake arm
		9.	Check temperature sensors
		10.	When temperature is within acceptable range, complete lautering process

**5.** **Control Logic**
	•	IF turbidity > threshold THEN divert flow to waste
	•	IF level < min THEN stop sparge water
	•	IF flow rate < min THEN adjust rake arm position
	•	IF flow rate > max THEN adjust rake arm position
	•	IF temperature < min THEN heat sparge water
	•	IF temperature

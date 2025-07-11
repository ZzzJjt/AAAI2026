### Intent:
**Intent Summary:**  
Create a standardized control narrative for beer brewing automation, specifying setpoints, instrumentation, and step-by-step lautering logic (including equipment, sensors, and conditional actions like turbidity-based flow diversion).  

*(Focus: Documentation for PLC/DCS implementation with precise parameters and procedural clarity.)*

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
Create a standardized control narrative for beer brewing automation, specifying setpoints, instrumentation, and step-by-step lautering logic (including equipment, sensors, and conditional actions like turbidity-based flow diversion).  

*(Focus: Documentation for PLC/DCS implementation with precise parameters and procedural clarity.)*
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

**1.** **Mash Phase**

**Setpoints:**
- Mash temperature: 65–68 °C
- Mash pH: 5.2–5.4
- Mash time: 60–90 minutes

**Instrumentation:**
- Temperature sensor
- pH sensor
- Flowmeter

**Procedure:**
1. Heat mash water to desired temperature.
2. Add crushed grains to the mash tun.
3. Mix the mash and monitor temperature and pH.
4. Maintain the mash temperature and pH within the specified range.
5. Drain the mash and transfer it to the lauter tun.

**2.** **Sparge Phase**

**Setpoints:**
- Sparge water temperature: 75–78 °C
- Sparge flow rate: 1.5–2.0 L/min
- Holding tank level: 50–80%

**Instrumentation:**
- Temperature sensor
- Flowmeter
- Level transmitter

**Procedure:**
1. Heat sparge water to the desired temperature.
2. Start the sparge pump and control the flow rate.
3. Monitor the holding tank level and adjust the sparge flow rate as needed.
4. Maintain the sparge water temperature within the specified range.

**3.** **Lautering Phase**

**Equipment:**
- Lauter tun
- Rake system
- Underlet system
- Flowmeters

**Instrumentation:**
- Temperature sensors
- Turbidity sensors
- Level transmitters

**Procedure:**
1. Start the rake motor and position the rake arm at the bottom of the lauter tun.
2. Open the underlet valve and start the lautering process.
3. Monitor the flow rate and turbidity of the wort.
4. When the turbidity reaches a certain threshold, stop the rake motor and close the underlet valve.
5. Divert the wort to the holding tank if the level is below the minimum threshold.
6. Repeat the process until the lauter tun is empty.

**4.** **Lautering Process**

**Setpoints:**
- Lautering flow rate: 1.5–2.0 L/min
- Holding tank level: 50–80%

**Procedure:**
1. Start the rake motor and position the r

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
	4.	Use structured formatting and bullet points or numbered steps for clarity.

⸻

Use this control narrative as a reference for designing and documenting the automation system for beer brewing, ensuring that all stages are clearly defined and that engineers have a complete understanding of the brewing process and its control requirements.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a control systems engineer or automation process designer responsible for documenting the brewing process, including the Lautering phase, for a brewery automation system. Your goal is to create a control narrative that clearly outlines setpoints, instrumentation, and process logic for each phase of beer brewing.

⸻

🟩 I (Input) – What You’re Given

You are provided with:
	•	A basic understanding of the beer brewing process
	•	Concrete setpoints and acceptable ranges for key brewing parameters
	•	An empty control narrative structure to fill in
	•	A focus on Section 4: Lautering, which includes:
	•	Required equipment and instrumentation
	•	A detailed explanation of the lautering process
	•	Control logic for managing the lautering phase

⸻

🟧 S (Steps) – How to Proceed

	1.	Define the brewing process stages and control parameters:
	•	Mash, lautering, boiling, fermentation, conditioning
	•	Include typical setpoints for temperature, flow, and timing
	2.	For Section 4: Lautering:
	•	Describe the equipment: lauter tun, rake system, underlet, flow transmitters
	•	Explain the instrumentation: temperature, turbidity, level sensors
	•	Outline the steps of the lautering process:
	•	Transfer wort to lauter tun
	•	Apply sparge water at optimal temperature
	•	Use a rake to stir and clarify wort
	•	Control flow rate and timing
	•	Stop lautering based on turbidity or volume
	3.	Develop control logic for Section 4:
	•	IF turbidity > threshold THEN stop sparge
	•	IF flow rate < minimum THEN reduce rake speed
	•	IF level < minimum THEN stop sparge
	•	Include concrete setpoints and ranges for each control action
	4.	Organize the control narrative in a clear, structured format:
	•	Use headings and subheadings for each process stage
	•	Break down Section 4 into logical steps with control logic
	•	Provide a summary of the

### Intent:
**Intent Summary:**  
Generate a text-based Process Flow Diagram (PFD) for penicillin fermentation, detailing unit operations, material flows, instrumentation (e.g., TT101, pH201), and control strategies (e.g., PID loops, safety interlocks) to support process design and automation.  

*(Focus: Structured documentation for engineering/control teams, emphasizing tags, flow arrows (-->), and control logic.)*

### Prompt:
**PFD Penicillin Fermentation:**

Create a Process Flow Diagram (PFD) in textual notation for a fermentation process to produce penicillin. Include instrumentation and control philosophy.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a bioprocess engineer responsible for documenting the penicillin fermentation process using a structured, text-based Process Flow Diagram (PFD) format suitable for engineering design, control system integration, or early-stage collaboration.

⸻

🟩 I (Input) – Information Provided

You need to create a textual PFD that outlines the core process units, instrumentation, and control strategy for a penicillin fermentation process. The PFD should:
	•	Describe major unit operations (e.g., water tank, nutrient mixer, sterilizer, fermenter, separator, product tank)
	•	Use arrows (-->) to show the flow of materials
	•	Include instrument tags (e.g., TT101, pH201, FCV301) for measurement and control
	•	Describe how parameters like temperature, pH, and agitation are managed through control loops or manual control

⸻

🟧 S (Steps) – Steps to Perform
	1.	List the main process equipment in the order of operation.
	2.	Connect units using arrows to indicate material flow.
	3.	For each unit, specify key instrumentation, such as:
	•	Temperature transmitters and controllers (TT → TIC → Valve)
	•	pH probes and dosing pumps
	•	Level and flow indicators
	4.	Include a brief description of the control strategy per unit (e.g., PID control loop, manual override, or safety interlocks).
	5.	Format the information clearly using consistent indentation and tagging.

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a readable, text-based PFD that accurately reflects the process sequence, instrumentation, and control philosophy for penicillin production. This document will support:
	•	Process design and review
	•	PLC/DCS configuration
	•	Control narrative development
	•	Communication across engineering and automation teams

### Generated Code:
**Intent Summary:**  
Generate a text-based Process Flow Diagram (PFD) for penicillin fermentation, detailing unit operations, material flows, instrumentation (e.g., TT101, pH201), and control strategies (e.g., PID loops, safety interlocks) to support process design and automation.  

*(Focus: Structured documentation for engineering/control teams, emphasizing tags, flow arrows (-->), and control logic.)*
**PFD Penicillin Fermentation:**

Create a Process Flow Diagram (PFD) in textual notation for a fermentation process to produce penicillin. Include instrumentation and control philosophy.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a bioprocess engineer responsible for documenting the penicillin fermentation process using a structured, text-based Process Flow Diagram (PFD) format suitable for engineering design, control system integration, or early-stage collaboration.

⸻

🟩 I (Input) – Information Provided

You need to create a textual PFD that outlines the core process units, instrumentation, and control strategy for a penicillin fermentation process. The PFD should:
	•	Describe major unit operations (e.g., water tank, nutrient mixer, sterilizer, fermenter, separator, product tank)
	•	Use arrows (-->) to show the flow of materials
	•	Include instrument tags (e.g., TT101, pH201, FCV301) for measurement and control
	•	Describe how parameters like temperature, pH, and agitation are managed through control loops or manual control

⸻

🟧 S (Steps) – Steps to Perform
	1.	List the main process equipment in the order of operation.
	2.	Connect units using arrows to indicate material flow.
	3.	For each unit, specify key instrumentation, such as:
	•	Temperature transmitters and controllers (TT → TIC → Valve)
	•	pH probes and dosing pumps
	•	Level and flow indicators
	4.	Include a brief description of the control strategy per unit (e.g., PID control loop, manual override, or safety interlocks).
	5.	Format the information clearly using consistent indentation and tagging.

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a readable, text-based PFD that accurately reflects the process sequence, instrumentation, and control philosophy for penicillin production. This document will support:
	•	Process design and review
	•	PLC/DCS configuration
	•	Control narrative development
	•	Communication across engineering and automation teams

**Penicillin Fermentation PFD:**

**Fermentation Process:**

Fermentation is a process used to produce penicillin, an antibiotic used to treat bacterial infections. The process involves growing the fungus Penicillium chrysogenum in a controlled environment to produce the desired antibiotic.

**Process Flow Diagram:**

The following is a text-based Process Flow Diagram (PFD) for a penicillin fermentation process:

**Water Tank:**

1.	Water Tank (WT101)
	•	Temperature Transmitter (TT101)
	•	Temperature Controller (TIC101)
	•	Temperature Control Valve (FCV101)
	•	Water is heated to 30°C and pumped to the Nutrient Mixer.

**Nutrient Mixer:**

2.	Nutrient Mixer (NM101)
	•	pH Probe (pH201)
	•	pH Dosing Pump (DP201)
	•	Nutrient is mixed with water and adjusted to pH 7.0.

**Sterilizer:**

3.	Sterilizer (ST101)
	•	Temperature Transmitter (TT301)
	•	Temperature Controller (TIC301)
	•	Temperature Control Valve (FCV301)
	•	Sterilizer is heated to 121°C and sterilized for 15 minutes.

**Fermenter:**

4.	Fermenter (F101)
	•	Agitation Motor (AM101)
	•	Agitation Speed Controller (SC101)
	•	Agitation Speed Control Valve (FCV102)
	•	Agitation is set to 100 rpm.
	•	Temperature Transmitter (TT401)
	•	Temperature Controller (TIC401)
	•	Temperature Control Valve (FCV401)
	•	Temperature is maintained at 30°C.
	•	pH Probe (pH301)
	•	pH Dosing Pump (DP301)
	•	pH is adjusted to 7.0.
	•	Fermenter is inoculated with Penicillium chrysogenum.

**Separator:**

5.	Separator (SP101)
	•	Level Transmitter (LT101)
	•

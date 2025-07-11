### Intent:
**Intent Summary:**  
Create a structured, text-based Process Flow Diagram (PFD) for penicillin fermentation, detailing unit operations, material flows, instrumentation (e.g., TT101, pH201), and control strategies (PID loops, safety interlocks) to support process design, automation, and cross-team collaboration.  

**Code Generation Intent:**  
Generate a textual PFD with tagged instrumentation and control logic for penicillin fermentation, formatted for engineering use.

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
Create a structured, text-based Process Flow Diagram (PFD) for penicillin fermentation, detailing unit operations, material flows, instrumentation (e.g., TT101, pH201), and control strategies (PID loops, safety interlocks) to support process design, automation, and cross-team collaboration.  

**Code Generation Intent:**  
Generate a textual PFD with tagged instrumentation and control logic for penicillin fermentation, formatted for engineering use.
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

⸻

**T-A-G:**

⸻

Create a text-based Process Flow Diagram (PFD) for a penicillin fermentation process, detailing instrumentation and control philosophy for engineering design, automation, and collaboration.

⸻

**T-A-G:**

⸻

Create a text-based Process Flow Diagram (PFD) for a penicillin fermentation process, detailing instrumentation and control philosophy for engineering design, automation, and collaboration.

⸻
**PFD Penicillin Fermentation:**

Create a Process Flow Diagram (PFD) in textual notation for a fermentation process to produce penicillin. Include instrumentation and control philosophy.

	•	Include major unit operations such as water tank, nutrient mixer, sterilizer, fermenter, separator, and product tank
	•	Use arrows (-->) to show the flow of materials
	•	Include instrument tags (e.g., TT101, pH201, FCV301) for measurement and control
	•	Describe how parameters like temperature, pH, and agitation are managed through control loops or manual control
	•	For example:
	•		TT101 → TIC101 → FCV101 (Temperature control loop for heating)
	•		pH201 → PID201 → FCV202 (pH control loop with dosing)
	•		FCV301 → Separator (Flow control to the separator)
	•	Include a control narrative for each unit, specifying the control strategy (e.g., PID, manual, interlocks)
	•	For instance:
	•	"Control Narrative: The sterilizer is maintained at 121°C using a PID loop with an output to an inlet valve. The temperature setpoint is 121°C, and the control valve adjusts based on the temperature feedback."
	•	Format the PFD using consistent indentation and clear tag notation for each instrument and control loop
	•	For example:
	•		"Water Tank --> Nutrient Mixer --> Sterilizer --> Fermenter --> Separator --> Product Tank"
	•	•	Include a control narrative for each unit, specifying the control strategy (e.g., PID, manual, interlocks)
	•	•	For instance:
	•	•	"Control Narrative: The sterilizer is maintained at 121°C using a PID loop with an output to an inlet valve. The temperature setpoint

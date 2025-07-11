### Intent:
**Intent Summary:**  
Create a text-based Process Flow Diagram (PFD) for penicillin fermentation, detailing unit operations, instrumentation (e.g., sensors, valves), and control strategies (e.g., PID loops, dosing) to guide process design and automation.  

*(For code generation: Generate a structured textual PFD with tagged instruments, material flows, and control logic for penicillin production.)*

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
Create a text-based Process Flow Diagram (PFD) for penicillin fermentation, detailing unit operations, instrumentation (e.g., sensors, valves), and control strategies (e.g., PID loops, dosing) to guide process design and automation.  

*(For code generation: Generate a structured textual PFD with tagged instruments, material flows, and control logic for penicillin production.)*
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

🟪 A (Action) – What to Do

Create a text-based Process Flow Diagram (PFD) for penicillin fermentation, including the following elements:

	•	Unit operations (e.g., water tank, nutrient mixer, sterilizer, fermenter, separator, product tank)
	•	Instrumentation tags (e.g., TT101, pH201, FCV301)
	•	Control loops (e.g., PID for temperature, pH, and agitation)
	•	Flow arrows (-->) to show material movement

Focus on clarity and organization, ensuring that each unit operation is described with its associated instrumentation and control strategy. Use consistent indentation and tagging to make the PFD easy to read and understand.
**PFD Penicillin Fermentation:**

Penicillin Fermentation Process Flow Diagram

**Water Tank:**

	▸	Inlet: TT101 (Temperature Transmitter)
	▸	Outlet: FCV301 (Fermentation Control Valve)
	▸	Control: TIC (Temperature Indicator Controller)

**Nutrient Mixer:**

	▸	Inlet: TT102 (Temperature Transmitter), pH201 (pH Probe)
	▸	Outlet: FCV302 (Fermentation Control Valve)
	▸	Control: PID (Proportional-Integral-Derivative) for temperature and pH

**Sterilizer:**

	▸	Inlet: TT103 (Temperature Transmitter), pH202 (pH Probe)
	▸	Outlet: FCV303 (Fermentation Control Valve)
	▸	Control: PID for temperature and pH

**Fermenter:**

	▸	Inlet: TT104 (Temperature Transmitter), pH203 (pH Probe)
	▸	Outlet: FCV304 (Fermentation Control Valve)
	▸	Control: PID for temperature, pH, and agitation

**Separator:**

	▸	Inlet: TT105 (Temperature Transmitter), pH204 (pH Probe)
	▸	Outlet: FCV305 (Fermentation Control Valve)
	▸	Control: PID for temperature and pH

**Product Tank:**

	▸	Inlet: TT106 (Temperature Transmitter), pH205 (pH Probe

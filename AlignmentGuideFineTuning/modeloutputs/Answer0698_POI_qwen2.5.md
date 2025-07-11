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

**PFD Textual Representation:**

```plaintext
Penicillin Fermentation Process

1. Water Tank (WT)
   - Inlet: Water supply
   - Outlet: Water to Nutrient Mixer

2. Nutrient Mixer (NM)
   - Inlet: Water from WT
   - Inlet: Nutrient feed
   - Outlet: Nutrient solution to Sterilizer

3. Sterilizer (ST)
   - Inlet: Nutrient solution from NM
   - Outlet: Sterilized solution to Fermenter

4. Fermenter (F)
   - Inlet: Sterilized solution from ST
   - Inlet: Air supply
   - Outlet: Fermentation broth to Separator

5. Separator (S)
   - Inlet: Fermentation broth from F
   - Outlet: Penicillin-containing broth to Product Tank
   - Outlet: Solid waste to Waste Tank

6. Product Tank (PT)
   - Inlet: Penicillin-containing broth from S
   - Outlet: Penicillin product to Packaging

Instrumentation and Control:

- WT: TT101 (Temperature), FCV101 (Flow Control Valve)
- NM: TT201 (Temperature), FCV201 (Flow Control Valve), pH201 (pH Probe), FCV202 (pH Control Valve)
- ST: TT301 (Temperature), FCV301 (Flow Control Valve)
- F: TT401 (Temperature), TT402 (pH), FCV401 (Agitation Control Valve), FCV402 (Air Flow Control Valve)
- S: TT501 (Temperature), TT502 (pH), FCV501 (Flow Control Valve)
- PT: TT601 (Temperature), TT602 (pH), FCV601 (Flow Control Valve)

Control Strategy:
- All units use PID control loops for temperature and pH.
- Agitation and air flow are controlled manually.
- Safety interlocks are in place to prevent overpressure and overheating.

```

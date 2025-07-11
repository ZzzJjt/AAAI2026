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

⸻

**PFD Textual Representation:**

```plaintext
Penicillin Fermentation Process

1. Water Tank (WT)
   - Inlet: Raw Water (RW)
   - Outlet: Process Water (PW)

2. Nutrient Mixer (NM)
   - Inlet: Process Water (PW)
   - Inlet: Nutrient Solution (NS)
   - Outlet: Mixed Nutrient Solution (MNS)

3. Sterilizer (ST)
   - Inlet: Mixed Nutrient Solution (MNS)
   - Outlet: Sterilized Nutrient Solution (SNS)

4. Fermenter (F)
   - Inlet: Sterilized Nutrient Solution (SNS)
   - Inlet: Penicillin Spores (PS)
   - Outlet: Fermentation Broth (FB)

5. Agitator (AG)
   - Inlet: Fermentation Broth (FB)
   - Control: Agitation Speed (AS)

6. pH Control (pH)
   - Inlet: Fermentation Broth (FB)
   - Control: pH Adjustment (PA)

7. Temperature Control (T)
   - Inlet: Fermentation Broth (FB)
   - Control: Temperature Adjustment (TA)

8. Product Separator (PS)
   - Inlet: Fermentation Broth (FB)
   - Outlet: Penicillin Crystals (PC)
   - Outlet: Supernatant (SN)

9. Product Tank (PT)
   - Inlet: Penicillin Crystals (PC)
   - Inlet: Supernatant (SN)
   - Outlet: Penicillin Product (PP)

Instrumentation and Control:
- TT101: Temperature Transmitter for Fermenter (F)
- TIC101: Temperature Controller for Fermenter (F)
- FCV101: Flow Control Valve for Nutrient Mixer (NM)
- pH201: pH Probe for Fermenter (F)
- FCV201: Flow Control Valve for pH Adjustment (PA)
- FCV301: Flow Control Valve for Temperature Adjustment (TA)
- FCV401: Flow Control Valve for Product Separator (PS)
- FCV501: Flow Control Valve for Product Tank (PT)

Control Strategy:
- PID control loops for temperature (T) and pH (pH) in the fermenter (F)
- Manual control for agitation speed (AS) in the fermenter

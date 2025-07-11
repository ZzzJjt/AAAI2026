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

**PFD Textual Representation:**

```plaintext
Penicillin Fermentation Process Flow Diagram

1. Water Tank (WT)
   - Material: Water
   - Instrumentation: Level Transmitter (LT101)
   - Control: Manual Fill

2. Nutrient Mixer (NM)
   - Material: Water, Nutrients
   - Instrumentation: Level Transmitter (LT102), pH Probe (pH201)
   - Control: PID Control Loop (pH201 → pHIC → FCV301)

3. Sterilizer (ST)
   - Material: Nutrient Mixture
   - Instrumentation: Temperature Transmitter (TT103)
   - Control: PID Control Loop (TT103 → TIC → FCV302)

4. Fermenter (FE)
   - Material: Sterilized Nutrient Mixture
   - Instrumentation: Temperature Transmitter (TT104), pH Probe (pH202), Agitator (AG101)
   - Control: PID Control Loop (TT104 → TIC → FCV303), PID Control Loop (pH202 → pHIC → FCV304), Manual Agitation

5. Separator (SE)
   - Material: Fermentation Broth
   - Instrumentation: Level Transmitter (LT105), pH Probe (pH203)
   - Control: PID Control Loop (pH203 → pHIC → FCV305)

6. Product Tank (PT)
   - Material: Penicillin
   - Instrumentation: Level Transmitter (LT106)
   - Control: Manual Fill

7. Dosing System (DS)
   - Material: Penicillin
   - Instrumentation: Flow Controller (FCV306)
   - Control: PID Control Loop (FCV306 → FCIC → FCV307)

8. Quality Control (QC)
   - Material: Penicillin
   - Instrumentation: pH Probe (pH204), Temperature Transmitter (TT107)
   - Control: Manual Inspection

9. Discharge (DIS)
   - Material: Finished Product
   - Instrumentation: Level Transmitter (LT108)
   - Control: Manual Discharge

10. Safety Interlocks
    - Inter

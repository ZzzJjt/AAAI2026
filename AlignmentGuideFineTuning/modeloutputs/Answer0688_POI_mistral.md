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

**PFD Example:**

```
Penicillin Fermentation Process Flow Diagram

1. Water Tank (WT)
   - Instrumentation:
     - Level Indicator (LI101)
     - Temperature Transmitter (TT101)
     - Temperature Controller (TIC101)
     - Valve (V101)
   - Control Strategy:
     - Maintain water level using TIC101 and V101
     - Setpoint: 80% of tank capacity

2. Nutrient Mixing (NM)
   - Instrumentation:
     - pH Probe (PH201)
     - pH Controller (PHC201)
     - Dosing Pump (DP101)
     - Flow Indicator (FI101)
   - Control Strategy:
     - Maintain pH at 6.8 using PHC201 and DP101
     - Setpoint: 6.8

3. Sterilization (ST)
   - Instrumentation:
     - Temperature Transmitter (TT201)
     - Temperature Controller (TIC201)
     - Valve (V201)
   - Control Strategy:
     - Sterilize nutrient solution at 121°C for 15 minutes using TIC201 and V201

4. Fermenter (F)
   - Instrumentation:
     - Temperature Transmitter (TT301)
     - Temperature Controller (TIC301)
     - pH Probe (PH301)
     - pH Controller (PHC301)
     - Agitator (A)
     - Agitator Speed Controller (ASC)
     - Air Sparger (AS)
     - Air Flow Indicator (FI201)
   - Control Strategy:
     - Maintain temperature at 37°C using TIC301
     - Maintain pH at 6.8 using PHC301
     - Control agitator speed using ASC
     -

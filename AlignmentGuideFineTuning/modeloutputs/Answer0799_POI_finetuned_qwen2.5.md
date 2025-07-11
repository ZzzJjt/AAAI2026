### Intent:
The task is to create a structured NORSOK-compliant System Control Diagram (SCD) in textual notation for an LNG vaporizer system, detailing piping flows, instrumentation tags, control loops, and safety interlocks with standardized formatting.  

**Intent Summary:**  
*Generate a text-based SCD for LNG vaporization with tagged instrumentation, control loops, and interlocks in NORSOK format.*

### Prompt:
**SCD LNG Vaporizer:**

Create a NORSOK system control diagram (SCD) in textual notation for a LNG Vaporizer System. Include instrumentation, control loops, and interlocks. Provide concrete tag numbers and piping.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a process control engineer responsible for documenting a NORSOK-compliant System Control Diagram (SCD) for an LNG vaporizer system using structured textual notation.

⸻

🟩 T (Task) – Define the Objective

Create a text-based SCD for the LNG vaporizer that includes:
	•	The full piping and process flow from LNG inlet to gas outlet
	•	All relevant instrumentation with standard tag numbers (e.g., FT201, TT101, FIC202, FCV203)
	•	Key control loops for temperature, flow, and pressure regulation
	•	Associated interlocks for safety shutdowns (e.g., high-pressure trips, ESD logic)
	•	Clearly structured layout using directional arrows (-->) and indentation for clarity

⸻

🟧 F (Format) – Specify the Output Format

Present the output in plain-text format, organized as follows:
	•	One line per major flow segment (e.g., LNG Inlet --> FT201 --> FIC201 --> FCV201 --> Vaporizer)
	•	Grouped sections for each control loop (e.g., [Temperature Control Loop])
	•	Each control loop should show the measurement device, controller, and final control element
	•	Clearly label interlocks under a [Safety Interlocks] section with signal conditions and shutdown targets
	•	Use consistent tag naming and logical flow formatting throughout

### Generated Code:
The task is to create a structured NORSOK-compliant System Control Diagram (SCD) in textual notation for an LNG vaporizer system, detailing piping flows, instrumentation tags, control loops, and safety interlocks with standardized formatting.  

**Intent Summary:**  
*Generate a text-based SCD for LNG vaporization with tagged instrumentation, control loops, and interlocks in NORSOK format.*
**SCD LNG Vaporizer:**

Create a NORSOK system control diagram (SCD) in textual notation for a LNG Vaporizer System. Include instrumentation, control loops, and interlocks. Provide concrete tag numbers and piping.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a process control engineer responsible for documenting a NORSOK-compliant System Control Diagram (SCD) for an LNG vaporizer system using structured textual notation.

⸻

🟩 T (Task) – Define the Objective

Create a text-based SCD for the LNG vaporizer that includes:
	•	The full piping and process flow from LNG inlet to gas outlet
	•	All relevant instrumentation with standard tag numbers (e.g., FT201, TT101, FIC202, FCV203)
	•	Key control loops for temperature, flow, and pressure regulation
	•	Associated interlocks for safety shutdowns (e.g., high-pressure trips, ESD logic)
	•	Clearly structured layout using directional arrows (-->) and indentation for clarity

⸻

🟧 F (Format) – Specify the Output Format

Present the output in plain-text format, organized as follows:
	•	One line per major flow segment (e.g., LNG Inlet --> FT201 --> FIC201 --> FCV201 --> Vaporizer)
	•	Grouped sections for each control loop (e.g., [Temperature Control Loop])
	•	Each control loop should show the measurement device, controller, and final control element
	•	Clearly label interlocks under a [Safety Interlocks] section with signal conditions and shutdown targets
	•	Use consistent tag naming and logical flow formatting throughout the document

⸻

**SCD LNG Vaporizer:**

Create a NORSOK system control diagram (SCD) in textual notation for a LNG Vaporizer System. Include instrumentation, control loops, and interlocks. Provide concrete tag numbers and piping.

	•	Include concrete tag numbers and piping for LNG inlet, FT201 flow transmitters, TT101 temperature transmitters, FIC201 flow controllers, FCV201 control valves, and the vaporizer outlet.
	•	Describe the control loops for temperature regulation, flow control, and pressure monitoring, including concrete tag numbers for each control loop and the associated instrumentation.
	•	Include concrete tag numbers and piping for the interlocks, including high-pressure trip and emergency shutdown logic, and clearly define the conditions and actions for each interlock.

	•	Provide concrete tag numbers and piping for LNG inlet, FT201 flow transmitters, TT101 temperature transmitters, FIC201 flow controllers, FCV201 control valves, and the vaporizer outlet.

	•	Describe the control loops for temperature regulation, flow control, and pressure monitoring, including concrete tag numbers for each control loop and the associated instrumentation.

	•	Include concrete tag numbers and piping for the interlocks, including high-pressure trip and emergency shutdown logic, and clearly define the conditions and actions for each interlock.

	•	Use a consistent and structured format for the textual notation, with clear headings and logical flow to ensure readability and maintainability.

	•	Ensure that the notation follows NORSOK standards for clarity and compliance, with appropriate use of arrows, tags, and control logic.

	•	For example, the LNG inlet can be tagged as LNG-01, FT201 as FT-01, TT101 as TT-01, FIC201 as FIC-01, FCV201 as FCV-01, and the vaporizer outlet as LNG-02. Control loops and interlocks should be clearly identified with concrete tag numbers and conditions.

	•	For instance, a temperature control loop could be described as: TT-01 → FIC-01 → FCV-01 → Vaporizer, with concrete tag numbers and piping. Interlocks could include a high-pressure trip tagged as ESD-01, with concrete tag numbers and shutdown conditions.

	•	Ensure that the notation is detailed enough to convey the full system

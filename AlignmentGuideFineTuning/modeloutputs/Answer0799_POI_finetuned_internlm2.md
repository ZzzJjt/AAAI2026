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
	•	Use consistent tag naming and logical flow formatting throughout

⸻

🟥 T (Time) – Set the Deadline

Complete the SCD within 15 minutes.

⸻

🟩 S (Solution) – Deliver the Output

LNG Vaporizer System Control Diagram (SCD):

	[Instrumentation and Control Loops]

	FT201: LNG Inlet Temperature
	FT202: Vaporizer Outlet Temperature
	FT203: Vaporizer Pressure
	FT204: Vaporizer Flow

	[Control Loops]

	[Vaporizer Temperature Control Loop]
	FT201 --> FIC201 --> FCV201 --> FT202

	[Vaporizer Pressure Control Loop]
	FT203 --> FIC202 --> FCV202 --> FT204

	[Vaporizer Flow Control Loop]
	FT204 --> FIC203 --> FCV203 --> FT203

	[Safety Interlocks]

	[High Pressure Trip]
	FT203 > 15.0 --> ESD Logic --> Shutdown

	[Low Flow Trip]
	FT204 < 0.1 --> ESD Logic --> Shutdown

	[Vaporizer Overheating]
	FT202 > 100.0 --> ESD Logic --> Shutdown

	[Vaporizer Under-Pressurization]
	FT203 < 0.5 --> ESD Logic --> Shutdown

	[Vaporizer Flow Blockage]
	FT204 = 0 --> ESD Logic --> Shutdown

	[Vaporizer Over-Pressurization]
	FT203 > 20.0 --> ESD Logic --> Shutdown

	[Vaporizer Under-Heating]
	FT201 < −50.0 --> ESD Logic --> Shutdown

	[Vaporizer Over-Heating]
	FT202 > 200.0 --> ESD Logic --> Shutdown

	[Vaporizer Under-Pressurization]
	FT203 < 0.1 --> ESD Logic --> Shutdown

	[Vaporizer Flow Blockage]
	FT204 = 0 --> ESD Logic --> Shutdown

	[Vaporizer Over-Pressurization]
	FT203 > 25.0 --> ESD Logic --> Shutdown

	[Vaporizer Under-Heating]
	FT201 < −60.0 --> ESD Logic --> Shutdown

	[Vaporizer Over-Heating]
	FT202 > 250.

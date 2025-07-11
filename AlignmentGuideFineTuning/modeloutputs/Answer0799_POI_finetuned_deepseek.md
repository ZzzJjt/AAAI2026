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

Example:

LNG Vaporizer System SCD

LNG Inlet --> FT201 --> FIC201 --> FCV201 --> Vaporizer

[Temperature Control Loop]

FT201 --> TIC201 --> TIC202 --> TIC203 --> FCV201

[Flow Control Loop]

FT201 --> FIC201 --> FIC202 --> FIC203 --> FCV201

[Pressure Control Loop]

FT201 --> PIC201 --> PIC202 --> PIC203 --> FCV201

[Safety Interlocks]

FT201 --> FT202 --> FT203 --> FT204 --> FT205 --> FT206 --> FT207 --> FT208 --> FT209 --> FT210 --> FT211 --> FT212 --> FT213 --> FT214 --> FT215 --> FT216 --> FT217 --> FT218 --> FT219 --> FT220 --> FT221 --> FT222 --> FT223 --> FT224 --> FT225 --> FT226 --> FT227 --> FT228 --> FT229 --> FT230 --> FT231 --> FT232 --> FT233 --> FT234 --> FT235 --> FT236 --> FT237 --> FT238 --> FT239 --> FT240 --> FT241 --> FT242 --> FT243 --> FT244 --> FT245 --> FT246 --> FT247 --> FT248 --> FT249 --> FT250 --> FT251 --> FT252 --> FT253 --> FT254 --> FT255 --> FT256 --> FT257 --> FT258 --> FT259 --> FT260 --> FT261 --> FT262 --> FT263 --> FT264 --> FT265 --> FT266 --> FT267 --> FT268 --> FT269 --> FT270 --> FT271

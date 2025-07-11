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

**SCD Textual Notation:**

```plaintext
LNG Inlet --> FT201 --> FIC201 --> FCV201 --> Vaporizer --> Gas Outlet

[Temperature Control Loop]
TT101 --> PID101 --> FCV202

[Flow Control Loop]
FIC201 --> PID201 --> FCV201

[Pressure Control Loop]
PT101 --> PID301 --> FCV203

[Safety Interlocks]
High Pressure Trip (HH PT101) --> ESD101
ESD Logic --> ESD102
```

**Explanation:**

This textual SCD provides a clear and structured overview of the LNG vaporizer system, including all necessary instrumentation, control loops, and safety interlocks. The format is designed to be easily readable and maintainable, adhering to NORSOK standards.

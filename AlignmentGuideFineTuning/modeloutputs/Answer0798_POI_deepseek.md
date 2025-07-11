### Intent:
The task is to create a text-based Process Flow Diagram (PFD) for penicillin fermentation, detailing process units, instrumentation, flow directions, and control logic (e.g., PID loops) to support automation design and process control implementation.  

**Intent Summary:**  
*Generate a structured textual PFD for penicillin fermentation with units, instrumentation tags, flow paths, and control philosophy (e.g., temperature/pH regulation via PID loops).*

### Prompt:
**PFD Penicillin Fermentation:**

Create a Process Flow Diagram (PFD) in textual notation for a fermentation process to produce penicillin. Include instrumentation and control philosophy.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a process design engineer documenting the penicillin fermentation process using a text-based Process Flow Diagram (PFD) to support automation design and process control implementation.

⸻

🟩 T (Task) – Define the Objective

Create a PFD in textual notation that includes:
	•	The main process units (e.g., water tank, nutrient mixer, sterilizer, fermenter, separator, product tank)
	•	Flow direction between units using arrows (-->)
	•	Key instrumentation with specific tag names (e.g., TT101, pH201, LT301)
	•	A concise control philosophy, describing how critical parameters (temperature, pH, agitation) are monitored and controlled—such as using PID loops or manual setpoints

⸻

🟧 F (Format) – Specify the Output Format

Present the information in a structured plain-text format, including:
	•	A flow line for each process stage
	•	A block below each unit showing associated instruments and control loops
	•	Consistent use of indentation, tag naming, and directional symbols
	•	Example control loop logic such as:

 TT201 → TIC201 → Steam Control Valve (TCV201)

### Generated Code:
The task is to create a text-based Process Flow Diagram (PFD) for penicillin fermentation, detailing process units, instrumentation, flow directions, and control logic (e.g., PID loops) to support automation design and process control implementation.  

**Intent Summary:**  
*Generate a structured textual PFD for penicillin fermentation with units, instrumentation tags, flow paths, and control philosophy (e.g., temperature/pH regulation via PID loops).*
**PFD Penicillin Fermentation:**

Create a Process Flow Diagram (PFD) in textual notation for a fermentation process to produce penicillin. Include instrumentation and control philosophy.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a process design engineer documenting the penicillin fermentation process using a text-based Process Flow Diagram (PFD) to support automation design and process control implementation.

⸻

🟩 T (Task) – Define the Objective

Create a PFD in textual notation that includes:
	•	The main process units (e.g., water tank, nutrient mixer, sterilizer, fermenter, separator, product tank)
	•	Flow direction between units using arrows (-->)
	•	Key instrumentation with specific tag names (e.g., TT101, pH201, LT301)
	•	A concise control philosophy, describing how critical parameters (temperature, pH, agitation) are monitored and controlled—such as using PID loops or manual setpoints

⸻

🟧 F (Format) – Specify the Output Format

Present the information in a structured plain-text format, including:
	•	A flow line for each process stage
	•	A block below each unit showing associated instruments and control loops
	•	Consistent use of indentation, tag naming, and directional symbols
	•	Example control loop logic such as:

 TT201 → TIC201 → Steam Control Valve (TCV201) → Steam Supply

 pH201 → PID201 → Agitation Motor (AM201) → Fermenter

 LT301 → Temperature Control Valve (TCV301) → Fermenter

⸻

🟨 P (Procedure) – Describe the Procedure

1. Begin by listing the main process units, their associated instruments, and the flow direction between them.
2. Describe the control philosophy for each critical parameter, including the instrumentation used, the control loop logic, and the target setpoints.
3. Indent and format the information in a structured text format, ensuring clarity and readability.

⸻

🟩 T (Test) – Test the Output

Test the output by reviewing the PFD for clarity, completeness, and adherence to the specified format. Ensure that all process units, instrumentation, and control loops are accurately represented.

⸻

🟨 E (Example) – Provide an Example

```
R - Process Design Engineer
T - Create a PFD for Penicillin Fermentation
F - Plain Text Format
P - Follow the Procedure

Main Process Units:
1. Water Tank (WT101)
2. Nutrient Mixer (NM101)
3. Sterilizer (ST101)
4. Fermenter (FR101)
5. Separator (SP101)
6. Product Tank (PT101)

TT101 --> WT101
TT201 --> NM101
TT301 --> ST101
TT401 --> FR101
TT501 --> SP101
TT601 --> PT101

Instrumentation:
TT101 - Temperature
TT201 - pH
TT301 - Dissolved Oxygen
TT401 - Temperature
TT501 - Temperature
TT601 - Temperature

Control Philosophy:
1. Temperature:
TT101 → PID201 → FR101 (Setpoint: 30°C)
2. pH:
TT201 → PID201 → FR101 (Setpoint: 6.5)
3. Diss

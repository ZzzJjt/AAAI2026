### Intent:
The task involves creating a detailed control narrative for an ammonium nitrate reactor, specifying process parameters, instrumentation, control loops, operational sequences, and safety interlocks to ensure safe and efficient continuous operation.  

**Intent Summary:**  
*Generate a structured control system configuration for an ammonium nitrate reactor, including process logic, instrumentation tags, PID loops, sequenced operations (startup/steady-state/shutdown), and safety interlocks, formatted for automation system implementation.*

### Prompt:
**P-ID Steam Water Cycle:**

Create a P&I diagram in textual notation for a steam water cycle in a power plant. Include equipment, instrumentation, piping, and control loops. Provide concrete tag names.


**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a process engineer or control system designer responsible for creating a text-based Piping and Instrumentation Diagram (P&ID) for a steam-water cycle in a power plant.

⸻

🟩 T (Task) – Define the Objective

Develop a P&ID in textual notation that clearly describes the steam-water cycle, including:
	•	All major equipment (e.g., boiler, feedwater pump, steam drum, condenser)
	•	Instrumentation (e.g., transmitters, controllers, control valves)
	•	Piping and flow paths, shown using text arrows (-->)
	•	Complete control loops with realistic and consistent tag names (e.g., FT101, FCV102, LT103)

The diagram should reflect actual process logic and signal relationships, structured clearly in text format.

⸻

🟧 F (Format) – Specify the Output Format

Provide the output as a plain-text diagram, formatted for readability and easy integration into documentation or code repositories. Use a consistent layout to show:
	•	Equipment blocks connected by signal and flow arrows
	•	Control loops such as:

 P01 --> FT101 --> FIC101 --> FCV101 --> Boiler B01

 	•	Instrument tags in ISA style and logical grouping by process section (e.g., feedwater, boiler, condensate return)

### Generated Code:
The task involves creating a detailed control narrative for an ammonium nitrate reactor, specifying process parameters, instrumentation, control loops, operational sequences, and safety interlocks to ensure safe and efficient continuous operation.  

**Intent Summary:**  
*Generate a structured control system configuration for an ammonium nitrate reactor, including process logic, instrumentation tags, PID loops, sequenced operations (startup/steady-state/shutdown), and safety interlocks, formatted for automation system implementation.*
**P-ID Steam Water Cycle:**

Create a P&I diagram in textual notation for a steam water cycle in a power plant. Include equipment, instrumentation, piping, and control loops. Provide concrete tag names.


**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a process engineer or control system designer responsible for creating a text-based Piping and Instrumentation Diagram (P&ID) for a steam-water cycle in a power plant.

⸻

🟩 T (Task) – Define the Objective

Develop a P&ID in textual notation that clearly describes the steam-water cycle, including:
	•	All major equipment (e.g., boiler, feedwater pump, steam drum, condenser)
	•	Instrumentation (e.g., transmitters, controllers, control valves)
	•	Piping and flow paths, shown using text arrows (-->)
	•	Complete control loops with realistic and consistent tag names (e.g., FT101, FCV102, LT103)

The diagram should reflect actual process logic and signal relationships, structured clearly in text format.

⸻

🟧 F (Format) – Specify the Output Format

Provide the output as a plain-text diagram, formatted for readability and easy integration into documentation or code repositories. Use a consistent layout to show:
	•	Equipment blocks connected by signal and flow arrows
	•	Control loops such as:

 P01 --> FT101 --> FIC101 --> FCV101 --> Boiler B01

 	•	Instrument tags in ISA style and logical grouping by process section (e.g., feedwater, boiler, condensate return)
	•	Optional notes or comments for clarity

For example:

Feedwater Control Loop:

P01 --> FT101 --> FIC101 --> FCV101 --> Boiler B01

Feedwater Pressure Transmitter: PT101
Feedwater Flow Transmitter: PT102

Feedwater Control Valve: FCV101

Feedwater Flow Control Loop:

P02 --> PT102 --> FCV102 --> Feedwater Pump

Feedwater Pressure Control Loop:

P03 --> PT101 --> FCV103 --> Feedwater Pump

Feedwater Level Transmitter: PT104

Feedwater Level Control Valve: FCV104
Feedwater Level Control Loop:

P04 --> PT104 --> FCV104 --> Feedwater Level Control

Feedwater Level Flow Control Loop:

P05 --> PT105 --> FCV105 --> Feedwater Level Pump
Feedwater Level Pressure Control Loop:

P06 --> PT106 --> FCV106 --> Feedwater Level Pressure Control

Feedwater Level Flow Control Loop:

P07 --> PT107 --> FCV107 --> Feedwater Level Flow Control

Feedwater Level Level Control Loop:

P08 --> PT108 --> FCV108 --> Feedwater Level Level Control

Feedwater Level Level Flow Control Loop:

P09 --> PT109 --> FCV109 --> Feedwater Level Level Flow Control

Feedwater Level Level Pressure Control Loop:

P10 --> PT110 --> FCV110 --> Feedwater Level Level Pressure Control

Feedwater Level Level Flow Control Loop:

P11 --> PT111 --> FCV111 --> Feedwater Level Level Flow Control

Feedwater Level Level Pressure Control Loop:

P12 --> PT112 --> FCV112 --> Feedwater Level Level Pressure Control

Feedwater Level Level Flow Control Loop:

P13 --> PT113 --> FCV113 --> Feedwater Level Level Flow Control

Feedwater Level Level Pressure Control Loop:

P14 --> PT114 --> FCV114 --> Feedwater Level Level Pressure

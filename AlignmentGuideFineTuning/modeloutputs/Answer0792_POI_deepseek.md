### Intent:
**Intent Summary:**  
Create a structured control narrative for an ammonium nitrate reactor, specifying process parameters, instrumentation, operational sequences, and safety interlocks to ensure safe and efficient production.  

*(For code generation: Focus on translating the defined setpoints, control loops, and interlock logic into programmable automation code.)*

### Prompt:
**Control Narrative for Ammonium Nitrate Reactor**

Create a control narrative for a reactor producing ammonium nitrates including concrete setpoints and ranges.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a process control engineer developing a formal control narrative for a reactor producing ammonium nitrate, intended for automation system configuration, safety documentation, and operator reference.

⸻

🟩 T (Task) – Define the Objective

Draft a control narrative that:
	•	Describes the process purpose and operating principles of the ammonium nitrate reactor
	•	Specifies key process parameters with setpoints and acceptable ranges (e.g., temperature, pressure, pH, flow ratios)
	•	Details the required instrumentation and control equipment, including control loops (e.g., TIC, PIC, FIC), sensors, and valves
	•	Outlines the sequence of operation for startup, normal operation, and shutdown
	•	Includes interlock conditions and alarm logic to ensure safe and stable operation

⸻

🟧 F (Format) – Specify the Output Format

Structure the control narrative as follows:
	1.	Process Overview
	•	Purpose: Neutralize nitric acid with ammonia to produce ammonium nitrate
	•	Reactor Type: Continuous Stirred Tank Reactor (CSTR)
	•	Normal flow conditions and operational limits
	2.	Key Setpoints and Ranges
	•	Temperature (TIC-101): 175 °C ± 2 °C
	•	Pressure (PIC-102): 4.8 bar ± 0.2 bar
	•	Ammonia:Acid Ratio (FRC-103): 1.01:1
	•	pH Control (AIC-105): Target = 6.2, acceptable range = 5.8–6.5
	3.	Instrumentation and Equipment
	•	Flow transmitters (FIC-103, FIC-104), pH analyzer (AIC-105)
	•	Safety interlocks: high-pressure switch, high-temperature alarm, emergency shutoff valve (ESD-106)
	4.	Sequence of Operation
	•	Startup: Initialize controllers, ramp up feed flows, preheat reactor, activate ratio and pH control
	•	Steady-State: Maintain PID loops, monitor deviation alarms, and log key values
	•	Shutdown: Isolate feeds, depressurize, stop heating, drain reactor contents
	5.	Interlocks and Alarms
	•	Temperature > 185 °C → emergency shutdown
	•	Pressure > 5.2 bar → close feed valves
	•	pH < 5.5 → alarm + reduce ammonia flow

### Generated Code:
**Intent Summary:**  
Create a structured control narrative for an ammonium nitrate reactor, specifying process parameters, instrumentation, operational sequences, and safety interlocks to ensure safe and efficient production.  

*(For code generation: Focus on translating the defined setpoints, control loops, and interlock logic into programmable automation code.)*
**Control Narrative for Ammonium Nitrate Reactor**

Create a control narrative for a reactor producing ammonium nitrates including concrete setpoints and ranges.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a process control engineer developing a formal control narrative for a reactor producing ammonium nitrate, intended for automation system configuration, safety documentation, and operator reference.

⸻

🟩 T (Task) – Define the Objective

Draft a control narrative that:
	•	Describes the process purpose and operating principles of the ammonium nitrate reactor
	•	Specifies key process parameters with setpoints and acceptable ranges (e.g., temperature, pressure, pH, flow ratios)
	•	Details the required instrumentation and control equipment, including control loops (e.g., TIC, PIC, FIC), sensors, and valves
	•	Outlines the sequence of operation for startup, normal operation, and shutdown
	•	Includes interlock conditions and alarm logic to ensure safe and stable operation

⸻

🟧 F (Format) – Specify the Output Format

Structure the control narrative as follows:
	1.	Process Overview
	•	Purpose: Neutralize nitric acid with ammonia to produce ammonium nitrate
	•	Reactor Type: Continuous Stirred Tank Reactor (CSTR)
	•	Normal flow conditions and operational limits
	2.	Key Setpoints and Ranges
	•	Temperature (TIC-101): 175 °C ± 2 °C
	•	Pressure (PIC-102): 4.8 bar ± 0.2 bar
	•	Ammonia:Acid Ratio (FRC-103): 1.01:1
	•	pH Control (AIC-105): Target = 6.2, acceptable range = 5.8–6.5
	3.	Instrumentation and Equipment
	•	Flow transmitters (FIC-103, FIC-104), pH analyzer (AIC-105)
	•	Safety interlocks: high-pressure switch, high-temperature alarm, emergency shutoff valve (ESD-106)
	4.	Sequence of Operation
	•	Startup: Initialize controllers, ramp up feed flows, preheat reactor, activate ratio and pH control
	•	Steady-State: Maintain PID loops, monitor deviation alarms, and log key values
	•	Shutdown: Isolate feeds, depressurize, stop heating, drain reactor contents
	5.	Interlocks and Alarms
	•	Temperature > 185 °C → emergency shutdown
	•	Pressure > 5.2 bar → close feed valves
	•	pH < 5.5 → alarm + reduce ammonia flow
	•	High ammonia flow → alarm + reduce acid flow
	•	High acid flow → alarm + reduce ammonia flow

⸻

🟨 C (Code) – Translate the Narrative into Code

Translate the control narrative into programmable automation code, using a suitable programming language and platform (e.g., ladder logic for Allen-Bradley PLCs, Structured Text for Siemens S7-1200).

1.	Create a new ladder diagram in your preferred programming software.
2.	Add the following tags to the diagram:
	•	`TIC-101`
	•	`PIC-102`
	•	`FRC-103`
	•	`AIC-105`
	•	`ESD-106`
3.	Create a new function block for each interlock condition and alarm logic.
4.	Connect the function blocks to the appropriate tags in the ladder diagram.
5.	Write the code for each function block, using the defined setpoints, ranges, and alarm logic.
6.	Test the code for accuracy and functionality.

⸻

🟩 E (Evaluation) – Evaluate the Control Narrative

Evaluate the control narrative by:
	1.	Ensuring that all key process parameters and interlock conditions are included
	2.	Confirming that the control narrative is clear, concise, and easy to understand
	3.	Checking that the control narrative can be translated into a functional automation code
	4.	Ensuring that the control narrative is compliant with relevant safety regulations and industry standards

⸻

🟩 R (Result) – Report on the Results

Report on the results of the evaluation, including any necessary revisions or improvements to the control narrative.

⸻

🟩 T (Task) – Finalize the Control Narrative

Finalize the control narrative based on the evaluation results, ensuring that it is complete, accurate, and compliant with safety regulations and industry standards.

⸻

🟩 E (Execute) – Implement the Control Narrative

Implement the control narrative in the automation system, ensuring that all setpoints, interlock conditions, and alarm logic are correctly configured and functioning as intended.

⸻

🟩

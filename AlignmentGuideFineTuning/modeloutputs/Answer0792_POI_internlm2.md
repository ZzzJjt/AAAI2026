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
	•	pH > 6.8 → alarm + increase acid flow

⸻

🟨 C (Content) – Provide the Control Narrative

1.	Process Overview
	•	Purpose: The ammonium nitrate reactor is designed to neutralize nitric acid with ammonia, producing a stable and high-purity ammonium nitrate solution. The reactor employs a continuous stirred tank reactor (CSTR) design, which allows for efficient mixing and heat transfer.
	•	Normal flow conditions: The reactor operates at a constant flow rate of 100 m³/h, with a 1:1 ammonia:acid ratio. The temperature is maintained at 175 °C, and the pH is controlled within a range of 5.8–6.5.
	•	Operational limits: The reactor can withstand a maximum pressure of 5.2 bar and a minimum temperature of 160 °C. Any deviation from these setpoints may result in process instability or safety hazards.
2.	Key Setpoints and Ranges
	•	Temperature (TIC-101): The temperature setpoint is 175 °C, with an acceptable range of 173 °C to 177 °C. Any deviation from this range may indicate a process disturbance or equipment malfunction.
	•	Pressure (PIC-102): The pressure setpoint is 4.8 bar, with an acceptable range of 4.6 bar to 5.0 bar. Any deviation from this range may indicate a potential safety hazard or equipment failure.
	•	Ammonia:Acid Ratio (FRC-103): The desired ratio is 1.01:1, with a tolerance of ±0.05. Any significant deviation from this ratio may impact the product quality or process stability.
	•	pH Control (AIC-105): The target pH is 6.2, with an acceptable range of 5.8 to 6.5. Any deviation from this range may indicate a need for process adjustments or quality control measures.
3.	Instrumentation and Equipment
	•	Flow transmitters (FIC-103, FIC-104): These devices measure the flow rates of ammonia and nitric acid, providing feedback for the flow ratio control

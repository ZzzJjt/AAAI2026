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
	•	pH > 6.7 → alarm + increase ammonia flow

⸻

**Control Narrative for Ammonium Nitrate Reactor**

**1. Process Overview**

The ammonium nitrate reactor is designed to neutralize nitric acid with ammonia to produce ammonium nitrate. The reactor is a Continuous Stirred Tank Reactor (CSTR) with a normal flow rate of 1000 kg/h of nitric acid and 1010 kg/h of ammonia. The reactor operates at a temperature of 175 °C and a pressure of 4.8 bar. The ratio of ammonia to nitric acid is 1.01:1, and the pH of the reactor is maintained at 6.2.

**2. Key Setpoints and Ranges**

	•	Temperature (TIC-101): 175 °C ± 2 °C
	•	Pressure (PIC-102): 4.8 bar ± 0.2 bar
	•	Ammonia:Acid Ratio (FRC-103): 1.01:1
	•	pH Control (AIC-105): Target = 6.2, acceptable range = 5.8–6.5

**3. Instrumentation and Equipment**

	•	Flow transmitters (FIC-103, FIC-104), pH analyzer (AIC-105)
	•	Safety interlocks: high-pressure switch, high-temperature alarm, emergency shutoff valve (ESD-106)

**4. Sequence of Operation**

	•	Startup: Initialize controllers, ramp up feed flows, preheat reactor, activate ratio and pH control
	•	Steady-State: Maintain PID loops, monitor deviation alarms, and log key values
	•	Shutdown: Isolate feeds, depressurize, stop heating, drain reactor contents

**5. Interlocks and Alarms**

	•	Temperature > 185 °C → emergency shutdown
	•	Pressure > 5.2 bar → close feed valves
	•	pH < 5.5 → alarm + reduce ammonia flow
	•	pH > 6.7 → alarm + increase ammonia flow

**Code Generation:**

```python
# Define setpoints and ranges
TIC_1

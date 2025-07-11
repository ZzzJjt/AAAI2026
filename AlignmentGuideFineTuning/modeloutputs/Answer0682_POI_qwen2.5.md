### Intent:
**Intent Summary:**  
Create a control narrative for an ammonium nitrate reactor, specifying setpoints, instrumentation, procedures, and safety interlocks to automate and document safe, efficient reactor operation.  

*(Focused on reactor control parameters, automation readiness, and safety compliance.)*

### Prompt:
**Control Narrative for Ammonium Nitrate Reactor**

Create a control narrative for a reactor producing ammonium nitrates including concrete setpoints and ranges.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

You are a process control engineer responsible for developing a clear, automation-ready control narrative for an ammonium nitrate reactor used in industrial chemical production.

⸻

🟩 I (Input) – Information Provided

The reactor operates by reacting ammonia and nitric acid in a controlled environment. Your control narrative must include:
	•	Concrete setpoints and operational ranges for temperature, pressure, flow, and pH
	•	A list of critical instrumentation and equipment (e.g., TICs, PICs, flow controllers, analyzers)
	•	Normal startup, operation, and shutdown procedures
	•	Safety interlocks and alarm triggers for deviations from normal conditions

⸻

🟧 S (Steps) – Steps to Perform
	1.	Define the core control parameters:
	•	Temperature: 175 °C (range: 173–177 °C)
	•	Pressure: 4.8 bar (range: 4.6–5.0 bar)
	•	Flow ratio: Ammonia:Acid = 1.01:1
	•	pH: 6.2 (acceptable range: 5.8–6.5)
	2.	List required instrumentation:
	•	TIC-101 (reactor temperature controller)
	•	PIC-102 (reactor pressure controller)
	•	FIC-103/FIC-104 (ammonia/nitric acid flow controllers)
	•	AIC-105 (pH analyzer)
	•	LSH-106 (high-level switch for overfill protection)
	3.	Describe operating procedures:
	•	Startup: Valve checks, initialize jacket heating, ramp up flows
	•	Normal Operation: Maintain setpoints with PID loops; monitor pH and adjust feed as needed
	•	Shutdown: Stop feeds, vent pressure, cool reactor, close all valves
	4.	Define interlocks and alarms:
	•	ESD if Temp > 185 °C, Pressure > 5.2 bar, or pH < 5.5
	•	Trigger alarms and lockout if ammonia or acid feed deviates ±10% from target ratio

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a clear, structured, and technically sound control narrative that:
	•	Can be used by automation teams to configure DCS/PLC systems
	•	Supports safety, efficiency, and compliance in reactor operation
	•	Provides the basis for interlock diagrams, HMI logic, and alarm design
	•	Enhances operator understanding and engineering documentation

### Generated Code:
**Intent Summary:**  
Create a control narrative for an ammonium nitrate reactor, specifying setpoints, instrumentation, procedures, and safety interlocks to automate and document safe, efficient reactor operation.  

*(Focused on reactor control parameters, automation readiness, and safety compliance.)*
**Control Narrative for Ammonium Nitrate Reactor**

Create a control narrative for a reactor producing ammonium nitrates including concrete setpoints and ranges.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

You are a process control engineer responsible for developing a clear, automation-ready control narrative for an ammonium nitrate reactor used in industrial chemical production.

⸻

🟩 I (Input) – Information Provided

The reactor operates by reacting ammonia and nitric acid in a controlled environment. Your control narrative must include:
	•	Concrete setpoints and operational ranges for temperature, pressure, flow, and pH
	•	A list of critical instrumentation and equipment (e.g., TICs, PICs, flow controllers, analyzers)
	•	Normal startup, operation, and shutdown procedures
	•	Safety interlocks and alarm triggers for deviations from normal conditions

⸻

🟧 S (Steps) – Steps to Perform
	1.	Define the core control parameters:
	•	Temperature: 175 °C (range: 173–177 °C)
	•	Pressure: 4.8 bar (range: 4.6–5.0 bar)
	•	Flow ratio: Ammonia:Acid = 1.01:1
	•	pH: 6.2 (acceptable range: 5.8–6.5)
	2.	List required instrumentation:
	•	TIC-101 (reactor temperature controller)
	•	PIC-102 (reactor pressure controller)
	•	FIC-103/FIC-104 (ammonia/nitric acid flow controllers)
	•	AIC-105 (pH analyzer)
	•	LSH-106 (high-level switch for overfill protection)
	3.	Describe operating procedures:
	•	Startup: Valve checks, initialize jacket heating, ramp up flows
	•	Normal Operation: Maintain setpoints with PID loops; monitor pH and adjust feed as needed
	•	Shutdown: Stop feeds, vent pressure, cool reactor, close all valves
	4.	Define interlocks and alarms:
	•	ESD if Temp > 185 °C, Pressure > 5.2 bar, or pH < 5.5
	•	Trigger alarms and lockout if ammonia or acid feed deviates ±10% from target ratio

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a clear, structured, and technically sound control narrative that:
	•	Can be used by automation teams to configure DCS/PLC systems
	•	Supports safety, efficiency, and compliance in reactor operation
	•	Provides the basis for interlock diagrams, HMI logic, and alarm design
	•	Enhances operator understanding and engineering documentation

⸻

**Control Narrative for Ammonium Nitrate Reactor**

**1. Control Parameters:**
	- Temperature: 175 °C (173–177 °C)
	- Pressure: 4.8 bar (4.6–5.0 bar)
	- Flow ratio: Ammonia:Acid = 1.01:1
	- pH: 6.2 (5.8–6.5)

**2. Instrumentation:**
	- TIC-101: Reactor Temperature Controller
	- PIC-102: Reactor Pressure Controller
	- FIC-103/FIC-104: Ammonia/Nitric Acid Flow Controllers
	- AIC-105: pH Analyzer
	- LSH-106: High-Level Switch for Overfill Protection

**3. Operating Procedures:**
	- **Startup:**
		1. Perform valve checks.
		2. Initialize jacket heating.
		3. Ramp up ammonia and nitric acid flows.
	- **Normal Operation:**
		1. Maintain setpoints using PID loops.
		2. Monitor pH and adjust feed as needed.
	- **Shutdown:**
		1. Stop ammonia and nitric acid feeds.
		2. Vent pressure.
		3. Cool reactor.
		4. Close all valves.

**4. Interlocks and Alarms:**
	- **ESD (Emergency Shutdown):**
		1. If Temperature > 185 °C
		2. If Pressure > 5.2 bar
		3. If pH < 5.5
	- **Trigger Alarms and Lockout:**
		1. If ammonia or acid feed deviates ±10% from target ratio

**5. Safety Interlocks:**
	- **High-Level Switch (LSH-106):**
		1. Lockout if reactor level exceeds safe limit.

**6. Automation Readiness:**
	- Ensure all control parameters, instrumentation, and procedures are documented and ready for automation configuration.
	- Develop interlock diagrams, HMI logic, and alarm design based on this control narrative.
	- Enhance operator understanding and engineering documentation for safe and efficient reactor operation.

**7. Compliance:**
	- Ensure all control parameters, instrumentation,

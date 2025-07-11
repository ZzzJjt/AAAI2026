### Intent:
**Intent Summary:**  
Create an automation-ready control narrative for an ammonium nitrate reactor, specifying setpoints (temperature, pressure, flow, pH), instrumentation (TICs, PICs, analyzers), operating procedures (startup, normal, shutdown), and safety interlocks/alarms to ensure safe and efficient reactor operation.  

*(For code generation: Translate this narrative into DCS/PLC logic with PID loops, interlocks, and alarm thresholds.)*

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
Create an automation-ready control narrative for an ammonium nitrate reactor, specifying setpoints (temperature, pressure, flow, pH), instrumentation (TICs, PICs, analyzers), operating procedures (startup, normal, shutdown), and safety interlocks/alarms to ensure safe and efficient reactor operation.  

*(For code generation: Translate this narrative into DCS/PLC logic with PID loops, interlocks, and alarm thresholds.)*
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

🟨 S (Safety) – Safety Considerations

Ensure that the control narrative:
	•	Complies with local, national, and international safety standards
	•	Considers the potential hazards associated with ammonium nitrate production
	•	Includes safety interlocks and alarms to prevent accidents and minimize risks
	•	Is subject to a thorough safety review by a qualified engineer before implementation

⸻

🟩 C (Compliance) – Compliance Considerations

Ensure that the control narrative:
	•	Complies with relevant industry standards and regulations (e.g., OSHA, EPA)
	•	Considers the environmental impact of ammonium nitrate production
	•	Includes measures to minimize waste and emissions
	•	Is subject to a thorough compliance review by a qualified engineer before implementation

⸻

🟧 A (Assumptions) – Assumptions Made

The control narrative assumes:
	•	Availability of necessary resources (e.g., DCS/PLC systems, instrumentation, personnel)
	•	Competent and trained operators to implement and monitor the control system
	•	Effective maintenance and calibration procedures for the control system and instrumentation
	•	Properly designed and installed equipment to ensure safe and efficient operation

⸻

🟥 E (Ethics) – Ethical Considerations

The control narrative should:
	•	Ensure the safety and well-being of all personnel involved in reactor operation
	•	Minimize the environmental impact of ammonium nitrate production
	•	Comply with all applicable laws, regulations, and ethical standards
	•	Be subject to a thorough ethical review by a qualified engineer before implementation

⸻

🟧 R (Resources) – Resources Required

The control narrative requires:
	•	Process control engineering expertise
	•	Knowledge of DCS/PLC systems and programming
	•	Access to relevant industry standards and regulations
	•	Access to safety and compliance guidelines for ammonium nitrate production
	•	Access to relevant environmental regulations and guidelines

⸻

🟧 S (Skills) – Skills Required

The control narrative requires:
	•	Process control engineering skills
	•	Expertise in DCS/PLC systems and programming
	•	Knowledge of

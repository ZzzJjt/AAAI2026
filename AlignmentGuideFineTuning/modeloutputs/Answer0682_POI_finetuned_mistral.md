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
Certainly! Below is a detailed control narrative for the ammonium nitrate reactor, including setpoints, instrumentation, procedures, and interlocks.

### Control Narrative for Ammonium Nitrate Reactor

#### Overview
The ammonium nitrate reactor is a continuous-flow reactor that produces ammonium nitrate by reacting ammonia and nitric acid in a controlled environment. The reactor operates at a fixed temperature and pressure, with precise flow ratios of ammonia to nitric acid. The process is monitored using a suite of instrumentation, and safety interlocks are in place to prevent overpressure, overheating, and off-spec product.

#### Setpoints and Operational Ranges

| Parameter       | Setpoint                 | Operational Range                 |
|-----------------|--------------------------|-----------------------------------|
| Temperature     | 175°C                    | 173°C to 177°C                   |
| Pressure        | 4.8 bar                  | 4.6 bar to 5.0 bar                |
| Flow Ratio       | 1.01:1                   | 0.95:1 to 1.05:1                 |
| pH              | 6.2                       | 5.8 to 6.5                       |

#### Instrumentation and Equipment

| Instrument/Equipment | Role

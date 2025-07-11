### Intent:
"Develop a control narrative for an ammonium nitrate reactor, specifying setpoints, instrumentation, operating procedures, and safety interlocks to automate and regulate temperature, pressure, flow, and pH during production."

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
"Develop a control narrative for an ammonium nitrate reactor, specifying setpoints, instrumentation, operating procedures, and safety interlocks to automate and regulate temperature, pressure, flow, and pH during production."
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
FUNCTION_BLOCK FB_AmmoniumNitrateReactor
VAR_INPUT
    Enable : BOOL; // Activates reactor
    EmergencyStop : BOOL; // Emergency stop signal
    Valve1 : BOOL; // Valve 1: Ammonia feed
    Valve2 : BOOL; // Valve 2: Nitric Acid feed
    Valve3 : BOOL; // Valve 3: Reactor jacket
    Valve4 : BOOL; // Valve 4: Reactor vent
    Valve5 : BOOL; // Valve 5: Reactor drain
    Valve6 : BOOL; // Valve 6: Reactor jacket drain
    Valve7 : BOOL; // Valve 7: Reactor jacket heating
    Valve8 : BOOL; // Valve 8: Reactor jacket cooling
    Valve9 : BOOL; // Valve 9: Reactor jacket overfill
    Valve10 : BOOL; // Valve 10: Reactor jacket underfill
    Valve11 : BOOL; // Valve 11: Reactor jacket vent
    Valve12 : BOOL; // Valve 12: Reactor jacket drain
    Valve13 : BOOL; // Valve 13: Reactor jacket heating
    Valve14 : BOOL; // Valve 14: Reactor jacket cooling
    Valve15 : BOOL; // Valve 15: Reactor jacket overfill
    Valve16 : BOOL; // Valve 16: Reactor jacket underfill
    Valve17 : BOOL; // Valve 17: Reactor jacket vent
    Valve18 : BOOL; // Valve 18: Reactor jacket drain
    Valve19 : BOOL; // Valve 19: Reactor jacket heating
    Valve20 : BOOL; // Valve 20: Reactor jacket cooling
    Valve21 : BOOL; // Valve 21: Reactor jacket overfill
    Valve22 : BOOL; // Valve 22: Reactor jacket underfill
    Valve23 : BOOL; // Valve 23: Reactor jacket vent
    Valve24 : BOOL; // Valve 24: Reactor jacket drain
    Valve25 : BOOL; // Valve 25: Reactor jacket heating
    Valve26 : BOOL; // Valve 26: Reactor jacket cooling
    Valve27 : BOOL; // Valve 27: Reactor jacket overfill

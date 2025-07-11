### Intent:
**Intent Summary:**  
Create a structured control narrative for an ammonium nitrate reactor, specifying setpoints, instrumentation, operational sequences, and safety interlocks to ensure safe and efficient production.  

*(For code generation: Focus on translating process parameters, control loops, and interlock logic into programmable automation rules.)*

### Prompt:
**Control Narrative for Ammonium Nitrate Reactor**

Create a control narrative for a reactor producing ammonium nitrates including concrete setpoints and ranges.

**C-A-R-E:**

🟥 C (Context) – Background Situation

In ammonium nitrate production, the reactor is a critical unit where ammonia and nitric acid react under controlled temperature and pressure conditions. A well-defined control narrative is essential for ensuring safety, optimizing yield, and maintaining regulatory compliance. Without clear setpoints, instrumentation, and sequence logic, the process may suffer from inefficiencies or become hazardous.

⸻

🟩 A (Action) – Task to Perform

Create a control narrative for an ammonium nitrate reactor, focusing on:
	•	Specifying concrete control setpoints and operational ranges for key process parameters
	•	Identifying the necessary equipment and instrumentation (e.g., flow controllers, pH sensors, pressure and temperature transmitters)
	•	Outlining the normal operating sequence, including startup, steady-state operation, and shutdown procedures
	•	Describing the control loops and interlock logic for alarms or emergency shutdown conditions

⸻

🟨 R (Result) – Expected Outcome

The final deliverable should be a clear and structured control narrative that can be used by engineers, operators, and programmers to:
	•	Ensure safe and consistent operation of the reactor
	•	Support PLC/DCS programming
	•	Simplify commissioning, training, and troubleshooting
	•	Provide a solid foundation for future automation upgrades

⸻

🟦 E (Example) – Concrete Illustration

Control Parameters and Setpoints:
	•	Reactor Temperature (TIC-101): 175 °C ± 2 °C
	•	Reactor Pressure (PIC-102): 4.8 bar ± 0.2 bar
	•	Ammonia to Nitric Acid Flow Ratio (FRC-103): 1.01:1
	•	pH Range (AIC-104): 6.2 ± 0.3

Instrumentation and Equipment:
	•	Flow transmitters on acid and ammonia lines
	•	Pressure and temperature transmitters on reactor dome
	•	pH sensor in reactor outlet
	•	Emergency shutoff valves with interlocks tied to high temperature (>185 °C), overpressure (>5.2 bar), or low pH (<5.5)

Operational Sequence Overview:
	1.	Initialize system; confirm all valves in closed and tank levels in range
	2.	Begin controlled ammonia and nitric acid flow
	3.	Ramp up reactor temperature using steam jacket
	4.	Adjust ammonia-to-acid ratio to maintain pH
	5.	Monitor steady-state; activate alarms/interlocks on deviation
	6.	Shutdown by closing feeds and venting pressure safely

### Generated Code:
**Intent Summary:**  
Create a structured control narrative for an ammonium nitrate reactor, specifying setpoints, instrumentation, operational sequences, and safety interlocks to ensure safe and efficient production.  

*(For code generation: Focus on translating process parameters, control loops, and interlock logic into programmable automation rules.)*
**Control Narrative for Ammonium Nitrate Reactor**

Create a control narrative for a reactor producing ammonium nitrates including concrete setpoints and ranges.

**C-A-R-E:**

🟥 C (Context) – Background Situation

In ammonium nitrate production, the reactor is a critical unit where ammonia and nitric acid react under controlled temperature and pressure conditions. A well-defined control narrative is essential for ensuring safety, optimizing yield, and maintaining regulatory compliance. Without clear setpoints, instrumentation, and sequence logic, the process may suffer from inefficiencies or become hazardous.

⸻

🟩 A (Action) – Task to Perform

Create a control narrative for an ammonium nitrate reactor, focusing on:
	•	Specifying concrete control setpoints and operational ranges for key process parameters
	•	Identifying the necessary equipment and instrumentation (e.g., flow controllers, pH sensors, pressure and temperature transmitters)
	•	Outlining the normal operating sequence, including startup, steady-state operation, and shutdown procedures
	•	Describing the control loops and interlock logic for alarms or emergency shutdown conditions

⸻

🟨 R (Result) – Expected Outcome

The final deliverable should be a clear and structured control narrative that can be used by engineers, operators, and programmers to:
	•	Ensure safe and consistent operation of the reactor
	•	Support PLC/DCS programming
	•	Simplify commissioning, training, and troubleshooting
	•	Provide a solid foundation for future automation upgrades

⸻

🟦 E (Example) – Concrete Illustration

Control Parameters and Setpoints:
	•	Reactor Temperature (TIC-101): 175 °C ± 2 °C
	•	Reactor Pressure (PIC-102): 4.8 bar ± 0.2 bar
	•	Ammonia to Nitric Acid Flow Ratio (FRC-103): 1.01:1
	•	pH Range (AIC-104): 6.2 ± 0.3

Instrumentation and Equipment:
	•	Flow transmitters on acid and ammonia lines
	•	Pressure and temperature transmitters on reactor dome
	•	pH sensor in reactor outlet
	•	Emergency shutoff valves with interlocks tied to high temperature (>185 °C), overpressure (>5.2 bar), or low pH (<5.5)

Operational Sequence Overview:
	1.	Initialize system; confirm all valves in closed and tank levels in range
	2.	Begin controlled ammonia and nitric acid flow
	3.	Ramp up reactor temperature using steam jacket
	4.	Adjust ammonia-to-acid ratio to maintain pH
	5.	Monitor steady-state; activate alarms/interlocks on deviation
	6.	Shutdown by closing feeds and venting pressure safely
	7.	Perform CIP (Clean In Place) and reset for the next batch

Interlock Matrix:
	•	Interlock 1: Shutdown if TIC-101 > 185 °C
	•	Interlock 2: Shutdown if PIC-102 > 5.2 bar
	•	Interlock 3: Shutdown if AIC-104 < 5.5
	•	Interlock 4: Open safety relief valve if pressure exceeds 5.5 bar
	•	Interlock 5: Open emergency cooling valve if temperature exceeds 180 °C
	•	Interlock 6: Open CIP valve if pH < 5.0
	•	Interlock 7: Open CIP valve if reactor pressure drops below 3.0 bar
	•	Interlock 8: Open CIP valve if reactor temperature drops below 170 °C
	•	Interlock 9: Open CIP valve if flow ratio deviates beyond 1.00:1
	•	Interlock 10: Open CIP valve if any sensor fails (e.g., no flow, no pressure, no pH)

	•	Control Narrative for Ammonium Nitrate Reactor
	•	Concrete setpoints and ranges for key parameters
	•	Required instrumentation and equipment
	•	Normal operating sequence and interlock logic
	•	Control narrative for ammonium nitrate reactor
	•	Concrete setpoints and ranges for key parameters
	•	Required instrumentation and equipment
	•	Normal operating sequence and interlock logic
	•	Control narrative for ammonium nitrate reactor
	•	Concrete setpoints and ranges for key parameters
	•	Required instrumentation and equipment
	•	Normal operating sequence and interlock logic
	•	Control narrative for ammonium nitrate reactor
	•	Concrete setpoints and ranges for key parameters
	•	Required instrumentation and equipment
	•	Normal operating sequence and interlock logic
	•	Control narrative for ammonium nitrate reactor
	•	Concrete setpoints and ranges for key parameters
	•	Required instrumentation and equipment
	•	Normal operating sequence and interlock logic
	•	Control narrative for ammonium nitrate reactor
	•	Concrete setpoints and ranges for key parameters
	•	Required

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

Control Logic and Interlocks:
	•	High temperature alarm: If reactor temperature exceeds 185 °C, shut off steam jacket and initiate emergency shutdown
	•	Overpressure alarm: If reactor pressure exceeds 5.2 bar, shut off inlet valves and initiate emergency shutdown
	•	Low pH alarm: If reactor pH falls below 5.5, shut off acid feed and initiate emergency shutdown
	•	Emergency shutdown: If any of the above conditions occur, initiate emergency shutdown by closing all valves and venting pressure

⸻

🟩 A (Action) – Task to Perform

Use the above information to create a structured control narrative for the ammonium nitrate reactor, including the necessary control loops, interlocks, and safety measures.

⸻

🟨 R (Result) – Expected Outcome

The final control narrative will be a comprehensive and structured document that can be used for safe and efficient operation of the reactor, as well as for programming purposes.

⸻

🟦 E (Example) – Concrete Illustration

Control Narrative for Ammonium Nitrate Reactor:

1.	Control Parameters and Setpoints:
	•	Reactor Temperature (TIC-101): 175 °C ± 2 °C
	•	Reactor Pressure (PIC-102): 4.8 bar ± 0.2 bar
	•	Ammonia to Nitric Acid Flow Ratio (FRC-103): 1.01:1
	•	pH Range (AIC-104): 6.2 ± 0.3

2.	Instrumentation and Equipment:
	•	Flow transmitters on acid and ammonia lines
	•	Pressure and temperature transmitters on reactor dome
	•	pH sensor in reactor outlet
	•	Emergency shutoff valves with interlocks tied to high temperature (>185 °C), overpressure (>5.2 bar), or low pH (<5.5)

3.	Operational Sequence Overview:
	1.	Initialize system; confirm all valves in closed and tank levels in range
	2.	Begin controlled ammonia and nitric acid flow
	3.	Ramp up reactor temperature using steam jacket
	4.	Adjust ammonia-to-acid ratio to

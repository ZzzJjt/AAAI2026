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
	7.	Cool reactor to ambient temperature; drain and clean

Interlock Logic:
	•	High temperature interlock: If TIC-101 > 185 °C, shut down reactor and vent steam
	•	Overpressure interlock: If PIC-102 > 5.2 bar, shut down reactor and vent excess pressure
	•	Low pH interlock: If AIC-104 < 5.5, shut down reactor and add ammonia

⸻

🟧 E (Example) – Code Generation

Using the control narrative as a guide, generate the following automation rules in a PLC/DCS programming language:

1.	Control Loop for Reactor Temperature (TIC-101):
	•	Input: Temperature sensor (TIC-101)
	•	Output: Steam valve (SV-201)
	•	Control: Proportional-Integral (PI) controller with setpoint 175 °C
	•	Interlock: If TIC-101 > 185 °C, shut down reactor and vent steam

2.	Control Loop for Reactor Pressure (PIC-102):
	•	Input: Pressure sensor (PIC-102)
	•	Output: Pressure relief valve (PRV-202)
	•	Control: Proportional-Integral (PI) controller with setpoint 4.8 bar
	•	Interlock: If PIC-102 > 5.2 bar, shut down reactor and vent excess pressure

3.	Control Loop for Ammonia-to-Acid Flow Ratio (FRC-103):
	•	Input: Flow transmitters (FIC-101, FIC-102)
	•	Output: Ammonia and acid flow control valves (FCV-101, FCV-102)
	•	Control: Proportional-Integral (PI) controller with setpoint 1.01:1
	•	Interlock: If FRC-103 deviates from 1.01:1, adjust flow valves

4.	Interlock Logic for pH (AIC-104):
	•	Input: pH sensor (AIC-104)
	•	Output: Ammonia feed valve (AFV-103)
	•	Control: Proportional-Integral (PI) controller with set

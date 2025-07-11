### Intent:
**Intent Summary:**  
Create a detailed control narrative for an ammonium nitrate reactor, specifying setpoints, instrumentation, and control logic to ensure safe and efficient operation, including temperature, pressure, flow ratio, and pH regulation with interlocks for deviations.  

*(For code generation: Focus on translating defined setpoints, PID loops, and safety interlocks into programmable logic for reactor automation.)*

### Prompt:
**Control Narrative for Ammonium Nitrate Reactor**

Create a control narrative for a reactor producing ammonium nitrates including concrete setpoints and ranges.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In the production of ammonium nitrate, the reactor stage is critical for maintaining safety, product quality, and process efficiency. However, without a clearly defined control narrative—including setpoints, ranges, and instrumentation—operators and control systems risk process instability, inefficient reactions, or unsafe operating conditions. Generic documentation often lacks the precision needed for automation or regulatory compliance.

⸻

🟩 A (After) – The Desired Outcome

Develop a comprehensive control narrative for the ammonium nitrate reactor, including:
	•	Concrete setpoints and control ranges for key parameters such as:
	•	Reaction temperature (e.g., 170–180 °C)
	•	Reactor pressure (e.g., 4.5–5.0 bar)
	•	Ammonia-to-nitric acid ratio
	•	pH control
	•	Identification of critical instrumentation: temperature sensors, pressure transmitters, flow meters, pH analyzers
	•	Description of control logic and interlocks for normal operation and safety shutdowns

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the process overview:
	•	Neutralization of nitric acid with ammonia in a continuous stirred-tank reactor (CSTR)
	2.	List key control loops and their setpoints:
	•	Temperature control loop: TIC-101 setpoint = 175 °C ± 2 °C
	•	Pressure control loop: PIC-102 = 4.8 bar ± 0.2 bar
	•	Flow ratio control: Ammonia:Acid = 1.01:1
	•	pH control loop: target = 6.0–6.5
	3.	Add equipment and instrumentation references (e.g., FIC-103 for ammonia feed, LSH-104 for high-level interlock)
	4.	Detail startup and normal operation sequence, followed by shutdown logic triggered by deviations from pressure, temperature, or flow

### Generated Code:
**Intent Summary:**  
Create a detailed control narrative for an ammonium nitrate reactor, specifying setpoints, instrumentation, and control logic to ensure safe and efficient operation, including temperature, pressure, flow ratio, and pH regulation with interlocks for deviations.  

*(For code generation: Focus on translating defined setpoints, PID loops, and safety interlocks into programmable logic for reactor automation.)*
**Control Narrative for Ammonium Nitrate Reactor**

Create a control narrative for a reactor producing ammonium nitrates including concrete setpoints and ranges.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In the production of ammonium nitrate, the reactor stage is critical for maintaining safety, product quality, and process efficiency. However, without a clearly defined control narrative—including setpoints, ranges, and instrumentation—operators and control systems risk process instability, inefficient reactions, or unsafe operating conditions. Generic documentation often lacks the precision needed for automation or regulatory compliance.

⸻

🟩 A (After) – The Desired Outcome

Develop a comprehensive control narrative for the ammonium nitrate reactor, including:
	•	Concrete setpoints and control ranges for key parameters such as:
	•	Reaction temperature (e.g., 170–180 °C)
	•	Reactor pressure (e.g., 4.5–5.0 bar)
	•	Ammonia-to-nitric acid ratio
	•	pH control
	•	Identification of critical instrumentation: temperature sensors, pressure transmitters, flow meters, pH analyzers
	•	Description of control logic and interlocks for normal operation and safety shutdowns

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the process overview:
	•	Neutralization of nitric acid with ammonia in a continuous stirred-tank reactor (CSTR)
	2.	List key control loops and their setpoints:
	•	Temperature control loop: TIC-101 setpoint = 175 °C ± 2 °C
	•	Pressure control loop: PIC-102 = 4.8 bar ± 0.2 bar
	•	Flow ratio control: Ammonia:Acid = 1.01:1
	•	pH control loop: target = 6.0–6.5
	3.	Add equipment and instrumentation references (e.g., FIC-103 for ammonia feed, LSH-104 for high-level interlock)
	4.	Detail startup and normal operation sequence, followed by shutdown logic triggered by deviations from pressure, temperature, or flow limits
	5.	Include safety interlocks (e.g., for overpressure, high temperature, or low flow) and their actions (e.g., valve closures, alarms, or emergency stops)
	6.	For automation or documentation, create a structured text (ST) program or a control narrative table with concrete values and ranges.

⸻

Use this control narrative as a basis for generating code snippets in IEC 61131-3 Structured Text (ST) or Function Block Diagram (FBD) to implement the defined control logic in a PLC or distributed control system (DCS) environment. Ensure that the control narrative is detailed enough to guide both control system implementation and process documentation.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In the production of ammonium nitrates, maintaining optimal control of the reactor’s temperature, pressure, and chemical ratios is essential for both safety and product quality. Without a clearly defined control narrative—including concrete setpoints, ranges, and instrumentation—operators and control systems risk process instability, inefficient reactions, or unsafe operating conditions. Generic documentation often lacks the precision needed for automation or regulatory compliance.

⸻

🟩 A (After) – The Desired Outcome

Develop a comprehensive control narrative for the ammonium nitrate reactor, including:
	•	Concrete setpoints and control ranges for key parameters such as:
	•	Reaction temperature (e.g., 170–180 °C)
	•	Reactor pressure (e.g., 4.5–5.0 bar)
	•	Ammonia-to-nitric acid ratio
	•	pH control
	•	Identification of critical instrumentation: temperature sensors, pressure transmitters, flow meters, pH analyzers
	•	Description of control logic and interlocks for normal operation and safety shutdowns

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the process overview:
	•	Neutralization of nitric acid with ammonia in a continuous stirred-tank reactor (CSTR)
	2.	List key control loops and their setpoints:
	•	Temperature control loop: TIC-101 setpoint = 175 °C ± 2 °C
	•	Pressure control loop: PIC-102 = 4.8 bar ± 0.2 bar
	•	Flow ratio control: Ammonia

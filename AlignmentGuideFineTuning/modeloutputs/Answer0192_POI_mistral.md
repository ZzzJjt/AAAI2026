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
	4.	Detail startup and normal operation sequence, followed by shutdown logic triggered by deviations from pressure, temperature, or flow ratio setpoints
	5.	Include safety interlocks for high temperature, high pressure, low flow ratio, and low pH
	6.	Outline troubleshooting procedures for common issues
	7.	Document calibration and maintenance requirements for sensors and control valves
	8.	Include a section for operator training and competency assessment

**Control Narrative Outline**

1.	Process Overview
	1.1	Reactor Description
	1.2	Reaction Chemistry
	1.3	Reactor Configuration

2.	Control Loops and Setpoints
	2.1	Temperature Control Loop
	2.2	Pressure Control Loop
	2.3	Flow Ratio Control
	2.4	pH Control Loop

3.	Instrumentation
	3.1	Temperature Sensors
	3.2	Pressure Transmitters
	3.3	Flow Meters
	3.4	pH Analyzers

4.	Control Logic and Interlocks
	4.1	Startup Sequence
	4.2	Normal Operation
	4.3	Safety Shutdowns
	4.4	Troubleshooting Procedures

5.	Safety Interlocks
	5.1	High Temperature
	5.2	High Pressure
	5.3	Low Flow Ratio
	5.4	Low pH

6.	Calibration and Maintenance
	6.1	Sensor Calibration
	6.2	Control Valve Maintenance

7.	Operator Training and Competency Assessment

**Code Generation**

1.	Define the control loops and their setpoints in the PLC code:
	•	Temperature control loop:
		a.	Setpoint: TIC-101 = 175
		b.	Upper limit: TIC-101_UP = 177
		c.	Lower limit: TIC-101_DN = 173
	•	Pressure control loop:
		a.	Setpoint: PIC-102 = 4.8
		b.	Upper limit: PIC

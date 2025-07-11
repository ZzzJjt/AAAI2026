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
	5.	Include safety interlocks for high-level, low-level, and high-temperature conditions
	6.	Ensure that the control narrative is clear, concise, and easy to understand for operators and control system engineers

**Control Narrative for Ammonium Nitrate Reactor**

**Process Overview:**

The ammonium nitrate reactor is a continuous stirred-tank reactor (CSTR) that neutralizes nitric acid with ammonia to produce ammonium nitrate. The reactor is equipped with temperature, pressure, and flow control loops to maintain safe and efficient operation.

**Control Loops:**

1.	Temperature Control Loop (TIC-101):
	•	Setpoint: 175 °C ± 2 °C
	•	Control action: PID
	•	Instrumentation: temperature sensor (T-101)
	•	Interlocks: high-temperature shutdown (LSH-101)

2.	Pressure Control Loop (PIC-102):
	•	Setpoint: 4.8 bar ± 0.2 bar
	•	Control action: PID
	•	Instrumentation: pressure transmitter (P-102)
	•	Interlocks: high-pressure shutdown (LSH-102)

3.	Flow Ratio Control:
	•	Setpoint: Ammonia:Acid = 1.01:1
	•	Control action: PID
	•	Instrumentation: flow meters (F-103, F-104)
	•	Interlocks: low-flow shutdown (LSH-103, LSH-104)

4.	pH Control Loop (PIC-105):
	•	Setpoint: 6.0–6.5
	•	Control action: PID
	•	Instrumentation: pH analyzer (PH-105)
	•	Interlocks: low-pH shutdown (LSH-105)

**Startup and Normal Operation:**

To start the reactor, the following steps are performed:
	1.	Open the ammonia and nitric acid feed valves (V-103, V-104)
	2.	Start the reactor agitator (A-101)
	3.	Set the temperature setpoint to 175 °C
	4.	Set the pressure setpoint

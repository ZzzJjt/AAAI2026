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
	4.	Detail startup and normal operation sequence, followed by shutdown logic triggered by deviations from pressure, temperature, or flow ratios
	5.	Use structured tags (e.g., <PID>, <Interlock>, <Alarm>) to organize logic and instrumentation
(* Control Narrative for Ammonium Nitrate Reactor *)

(* 1. Process Overview *)

The ammonium nitrate reactor is a continuous stirred-tank reactor (CSTR) that neutralizes nitric acid with ammonia. The process is controlled using a PID loop for temperature, pressure, and flow ratio, and pH control is achieved through a separate loop. The reactor is equipped with instrumentation such as temperature sensors, pressure transmitters, flow meters, and pH analyzers.

(* 2. Key Control Loops *)

(* 2.1 Temperature Control Loop *)

* Setpoint: TIC-101 = 175 °C ± 2 °C
* PID loop with:
  - Kp = 1.5
  - Ki = 0.1
  - Kd = 0.05
  - Sampling time = 10 s
  - Output: TIC-101_PV

(* 2.2 Pressure Control Loop *)

* Setpoint: PIC-102 = 4.8 bar ± 0.2 bar
* PID loop with:
  - Kp = 1.2
  - Ki = 0.1
  - Kd = 0.05
  - Sampling time = 10 s
  - Output: PIC-102_PV

(* 2.3 Flow Ratio Control Loop *)

* Setpoint: Ammonia:Acid = 1.01:1
* PID loop with:
  - Kp = 0.5
  - Ki = 0.05
  - Kd = 0.01
  - Sampling time = 10 s
  - Output: FIC-103_PV

(* 2.4 pH Control Loop *)

* Setpoint: pH = 6.0–6.5
* PID loop with:
  - Kp = 0.2
  - Ki = 0.01
  - Kd = 0.001
  - Sampling time = 10 s
  - Output: pH_PV

(* 3.

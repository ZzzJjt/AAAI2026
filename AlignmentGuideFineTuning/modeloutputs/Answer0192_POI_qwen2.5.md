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
	5.	Include safety interlocks for:
	•	High pressure (e.g., 5.5 bar) to shut down the reactor
	•	High temperature (e.g., 185 °C) to initiate cooling and shutdown
	•	High flow ratio (e.g., 1.05:1) to prevent overfeeding
	•	Low flow ratio (e.g., 0.95:1) to prevent underfeeding
	•	Low pH (e.g., 5.5) to initiate pH adjustment
	•	High pH (e.g., 7.0) to initiate pH adjustment
	6.	Provide a summary of the control narrative, including a table of setpoints, ranges, and interlocks

**Control Narrative for Ammonium Nitrate Reactor**

**Process Overview:**
The ammonium nitrate reactor is a continuous stirred-tank reactor (CSTR) where nitric acid is neutralized with ammonia to produce ammonium nitrate. The reactor operates at a temperature of 170–180 °C and a pressure of 4.5–5.0 bar. The ammonia-to-nitric acid ratio is maintained at 1.01:1, and the pH is controlled between 6.0 and 6.5.

**Control Loops and Setpoints:**

| Control Loop | Setpoint | Range |
| --- | --- | --- |
| Temperature Control Loop | TIC-101 | 175 °C ± 2 °C |
| Pressure Control Loop | PIC-102 | 4.8 bar ± 0.2 bar |
| Flow Ratio Control | Ammonia:Acid | 1.01:1 |
| pH Control Loop | pH Analyzer | 6.0–6.5 |

**Equipment and Instrumentation:**

| Equipment/Instrumentation | Reference |
| --- | --- |
| Ammonia Feed Flow Control | FIC-103 |
| High-Level Interlock | LSH-104 |
| Temperature Sensors | T-101, T-102 |
| Pressure Transmitters | P-101, P-102 |
| Flow Meters | F-101, F-102 |
| pH Analyzer | pH-101 |

**Startup

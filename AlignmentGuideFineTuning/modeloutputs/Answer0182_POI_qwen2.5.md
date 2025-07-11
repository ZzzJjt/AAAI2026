### Intent:
**Intent Summary:**  
Create a detailed control narrative for an ammonium nitrate reactor, specifying setpoints, instrumentation, and control logic to ensure safe and efficient operation.  

*(For code generation: Focus on translating reactor parameters like temperature, pressure, flow ratios, and pH into programmable control loops with defined setpoints and interlocks.)*

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
Create a detailed control narrative for an ammonium nitrate reactor, specifying setpoints, instrumentation, and control logic to ensure safe and efficient operation.  

*(For code generation: Focus on translating reactor parameters like temperature, pressure, flow ratios, and pH into programmable control loops with defined setpoints and interlocks.)*
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
	4.	Detail startup and normal operation sequence, followed by shutdown logic triggered by deviations from pressure, temperature, or flow setpoints
	5.	Include safety interlocks for high/low pressure, high/low temperature, and high/low level
	6.	Provide a summary of the control narrative, including a list of all control loops, setpoints, and interlocks

⸻

**Control Narrative for Ammonium Nitrate Reactor**

**1. Process Overview:**
The ammonium nitrate reactor is a continuous stirred-tank reactor (CSTR) where nitric acid is neutralized with ammonia to produce ammonium nitrate. The reaction is exothermic, and the reactor is equipped with temperature and pressure control loops to maintain the reaction conditions.

**2. Key Control Loops and Setpoints:**

**Temperature Control Loop:**
- TIC-101: Setpoint = 175 °C ± 2 °C
- Instrumentation: Temperature sensor (TS-101) and temperature controller (TC-101)

**Pressure Control Loop:**
- PIC-102: Setpoint = 4.8 bar ± 0.2 bar
- Instrumentation: Pressure transmitter (PT-102) and pressure controller (PC-102)

**Flow Ratio Control:**
- Ammonia:Acid = 1.01:1
- Instrumentation: Flow meters (FM-101 for ammonia, FM-102 for nitric acid)

**pH Control Loop:**
- Target = 6.0–6.5
- Instrumentation: pH analyzer (PA-101) and pH controller (PC-101)

**3. Equipment and Instrumentation References:**
- FIC-103: Ammonia feed flow controller
- LSH-104: High-level interlock for the reactor

**4. Startup and Normal Operation Sequence:**
- Start the reactor by introducing ammonia and nitric acid into the reactor.
- Monitor the temperature and pressure, and adjust the flow rates of ammonia and nitric acid to maintain the setpoints.
- Monitor the pH and adjust the flow rates of ammonia and nitric acid to maintain the setpoint.

**5. Shutdown Logic:**
- If the temperature exceeds 180 °C or falls below 170 °C, the reactor will shut down.
- If the pressure exceeds 5.0 bar or falls below 4.5 bar

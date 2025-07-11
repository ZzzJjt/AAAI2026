### Intent:
**Intent Summary:**  
Develop an automated control narrative for beer brewing, specifying setpoints, instrumentation, procedural logic, and safety interlocks to ensure consistent quality and operational reliability across milling, mashing, lautering, boiling, fermentation, and conditioning phases.  

*(Focus: Automation-ready process control with precise parameters and fail-safes for PLC/DCS implementation.)*

### Prompt:
**Control Narrative for Ammonium Nitrate Reactor**

Create a control narrative for a reactor producing ammonium nitrates including concrete setpoints and ranges.

**T-A-G:**

🟥 T (Task)

Develop a control narrative for a reactor producing ammonium nitrate, focusing on automation-ready descriptions that include concrete process setpoints, equipment, and operating logic.

⸻

🟩 A (Action)
	•	Define the process context: continuous neutralization of nitric acid with ammonia in a stirred reactor
	•	Include concrete setpoints and ranges for critical parameters:
	•	Temperature: 175 °C ± 2 °C
	•	Pressure: 4.8 bar ± 0.2 bar
	•	Ammonia-to-acid molar ratio: 1.01:1
	•	pH range: 6.2 ± 0.3
	•	Specify the instrumentation and control elements:
	•	TIC-101 (reactor temperature controller), PIC-102 (pressure), FIC-103/104 (flow control), AIC-105 (pH)
	•	Outline the operating sequence:
	1.	Startup: Valve alignment, flow ramp-up, temperature control, pH stabilization
	2.	Normal operation: Maintain loop control with alarm monitoring
	3.	Shutdown: Stop feeds, isolate reactor, relieve pressure
	•	Define interlocks and alarm logic:
	•	Trip if pressure > 5.2 bar
	•	Emergency shutdown if temperature > 185 °C
	•	Reduce ammonia feed if pH < 5.5

⸻

🟦 G (Goal)

Produce a clear, structured, and automation-friendly control narrative that supports safe reactor operation, facilitates PLC/DCS implementation, and ensures consistent ammonium nitrate quality through well-defined control logic and interlocks.

### Generated Code:
**Intent Summary:**  
Develop an automated control narrative for beer brewing, specifying setpoints, instrumentation, procedural logic, and safety interlocks to ensure consistent quality and operational reliability across milling, mashing, lautering, boiling, fermentation, and conditioning phases.  

*(Focus: Automation-ready process control with precise parameters and fail-safes for PLC/DCS implementation.)*
**Control Narrative for Ammonium Nitrate Reactor**

Create a control narrative for a reactor producing ammonium nitrates including concrete setpoints and ranges.

**T-A-G:**

🟥 T (Task)

Develop a control narrative for a reactor producing ammonium nitrate, focusing on automation-ready descriptions that include concrete process setpoints, equipment, and operating logic.

⸻

🟩 A (Action)
	•	Define the process context: continuous neutralization of nitric acid with ammonia in a stirred reactor
	•	Include concrete setpoints and ranges for critical parameters:
	•	Temperature: 175 °C ± 2 °C
	•	Pressure: 4.8 bar ± 0.2 bar
	•	Ammonia-to-acid molar ratio: 1.01:1
	•	pH range: 6.2 ± 0.3
	•	Specify the instrumentation and control elements:
	•	TIC-101 (reactor temperature controller), PIC-102 (pressure), FIC-103/104 (flow control), AIC-105 (pH)
	•	Outline the operating sequence:
	1.	Startup: Valve alignment, flow ramp-up, temperature control, pH stabilization
	2.	Normal operation: Maintain loop control with alarm monitoring
	3.	Shutdown: Stop feeds, isolate reactor, relieve pressure
	•	Define interlocks and alarm logic:
	•	Trip if pressure > 5.2 bar
	•	Emergency shutdown if temperature > 185 °C
	•	Reduce ammonia feed if pH < 5.5

⸻

🟦 G (Goal)

Produce a clear, structured, and automation-friendly control narrative that supports safe reactor operation, facilitates PLC/DCS implementation, and ensures consistent ammonium nitrate quality through well-defined control logic and interlocks.
### Control Narrative for Beer Brewing Process

#### 1. Introduction
This control narrative describes the automation of the beer brewing process, which consists of six main stages: milling, mashing, lautering, boiling, fermentation, and conditioning. Each stage includes specific setpoints, instrumentation, and procedural logic to ensure consistent product quality and operational reliability. The narrative is designed to support PLC/DCS implementation and includes safety interlocks, alarm logic, and startup/shutdown procedures.

#### 2. Milling

##### 2.1 Setpoints and Instrumentation
- **Milling Duration**: 15 minutes
- **Milling Speed**: 100 RPM
- **Instrumentation**:
  - TIC-101: Temperature Controller (setpoint: 20°C)
  - PIC-102: Pressure Controller (setpoint: 0.5 bar)
  - FIC-103: Flow Controller (setpoint: 100 L/min)
  - AIC-104: Analog Input (grist temperature)
  - AIC-105: Analog Input (grist moisture)
  - EIC-106: Emergency Stop

##### 2.2 Procedural Logic
- **Startup**:
  1. Verify emergency stop is off (AIC-106 = 0).
  2. Set milling speed to 100 RPM.
  3. Start milling.
  4. Monitor temperature and moisture levels.
- **Normal Operation**:
  1. Maintain temperature at 20°C.
  2. Maintain moisture level below 10%.
  3. Monitor for abnormal conditions:
    - Temperature > 22°C: trigger alarm, reduce speed.
    - Moisture > 12%: trigger alarm, reduce speed.
    - Emergency stop activated: stop milling, set milling speed to 0.
- **Shutdown**:
  1. Stop milling.
  2. Set milling speed to 0.
  3. Disable flow and pressure control.

#### 3. Mashing

####

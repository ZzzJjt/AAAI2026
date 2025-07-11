### Intent:
**Intent Summary:**  
Develop a PLC-ready timer function block for industrial automation that implements edge-triggered timing with precise system-clock tracking, input validation, and safety checks to support reactor control sequencing or process timeouts.  

*(Focus: Code generation for a robust timer in process control systems, ensuring reliability and IEC 61131-3 compliance.)*

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
Develop a PLC-ready timer function block for industrial automation that implements edge-triggered timing with precise system-clock tracking, input validation, and safety checks to support reactor control sequencing or process timeouts.  

*(Focus: Code generation for a robust timer in process control systems, ensuring reliability and IEC 61131-3 compliance.)*
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
### Control Narrative for Ammonium Nitrate Reactor

#### 1. Process Overview
The ammonium nitrate reactor is a continuous process that neutralizes nitric acid with ammonia in a stirred reactor. The reaction produces ammonium nitrate, which is a white solid. The process operates under controlled conditions of temperature, pressure, and pH to ensure safe and efficient operation.

#### 2. Process Parameters and Setpoints

##### 2.1 Temperature
- **Setpoint**: 175°C ± 2°C
- **Measured Value**: TIC-101 (Temperature Controller)
- **Control Element**: TIC-101 (Temperature Controller)

##### 2.2 Pressure
- **Setpoint**: 4.8 bar ± 0.2 bar
- **Measured Value**: PIC-102 (Pressure Controller)
- **Control Element**: PIC-102 (Pressure Controller)

##### 2.3 Ammonia-to-Acid Molar Ratio
- **Setpoint**: 1.01:1
- **Measured Value**: Ratio Calculated from Flow Rates
- **Control Element**: FIC-103/104 (Flow Controllers)

##### 2.4 pH
- **Setpoint**: 6.2 ± 0.3
- **Measured Value**: AIC-105 (pH Controller)
- **Control Element**: AIC-105 (pH Controller)

#### 3. Instrumentation and Control Elements

##### 3.1 Temperature Control
- **TIC-101**: Temperature Controller
- **TIC-101 Input**: Reactor Outlet Temperature
- **TIC-101 Output**: Heating Medium Flow Adjustment

##### 3.2 Pressure Control
- **PIC-102**: Pressure Controller
- **PIC-102 Input**: Reactor Pressure
- **PIC-102 Output**: Pressure Relief Valve Adjustment

##### 3.3 Flow Control
- **FIC-1

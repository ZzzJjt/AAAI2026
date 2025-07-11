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

---

**Control Narrative for Ammonium Nitrate Reactor**

**Task (T):** Develop a control narrative for a continuous ammonium nitrate reactor, focusing on automation-ready descriptions that include concrete process setpoints, equipment, and operating logic.

**Action (A):**

1. **Process Context:** The reactor neutralizes nitric acid with ammonia in a stirred reactor.

2. **Setpoints and Ranges:**
   - Temperature: 175 °C ± 2 °C (TIC-101)
   - Pressure: 4.8 bar ± 0.2 bar (PIC-102)
   - Ammonia-to-acid molar ratio: 1.01:1 (FIC-103)
   - pH range: 6.2 ± 0.3 (AIC-105)

3. **Instrumentation and Control Elements:**
   - TIC-101 (Reactor Temperature Controller)
   - PIC-102 (Pressure Controller)
   - FIC-103/104 (Flow Controllers for Ammonia and Nitric Acid)
   - AIC-105 (pH Controller)

4. **Operating Sequence:**
   1. **Startup:**
      - Align valves
      - Ramp up flows
      - Initiate temperature control
      - Stabilize pH
   2. **Normal Operation:**
      - Maintain loop control
      - Monitor alarms
   3. **Shutdown:**
      - Stop feeds
      - Isolate reactor
      - Relieve pressure

5. **Interlocks and Alarm Logic:**
   - Trip if pressure > 5.2 bar
   - Emergency shutdown if temperature > 185 °C
   - Reduce ammonia feed if pH < 5.5

**Goal (G):** Produce a clear, structured, and automation-friendly control narrative that supports safe reactor operation, facilitates PLC/DCS implementation, and

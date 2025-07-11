### Intent:
**Intent Summary:**  
Create a textual P&ID representation of a power plant steam-water cycle, including tagged equipment, instrumentation, piping, and control loops, using standardized notation for clarity in documentation and control system development.  

*(Focus: Structured plain-text P&ID for process clarity, team alignment, and control logic reference.)*

### Prompt:
**P-ID Steam Water Cycle:**

Create a P&I diagram in textual notation for a steam water cycle in a power plant. Include equipment, instrumentation, piping, and control loops. Provide concrete tag names.


**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In a power plant’s steam-water cycle, effective communication between design, control, and operations teams depends on clear and consistent Piping and Instrumentation Diagrams (P&IDs). When graphical tools aren’t available or when quick documentation is needed, a text-based P&ID can help bridge understanding. However, without standardized textual notation, equipment relationships, signal flow, and control loops may be ambiguous or misinterpreted.

⸻

🟩 A (After) – The Desired Outcome

Create a text-based P&ID representation of the steam-water cycle in a power plant that clearly includes:
	•	Major equipment (e.g., boiler, drum, condenser, pumps)
	•	Instrumentation (e.g., level transmitters, flow meters, pressure sensors)
	•	Piping connections and flow direction
	•	Control loops with specific tag names for valves and transmitters (e.g., LT101, FCV201)

This P&ID should be readable in a plain-text format and structured in a way that conveys both process flow and instrumentation logic, enabling control system development and documentation review.

⸻

🟧 B (Bridge) – How to Get There
	1.	Identify and list core process equipment: e.g., Boiler (B01), Feedwater Pump (P01), Steam Drum (D01), Condenser (C01).
	2.	Assign tag names to instruments using common standards: LT (Level Transmitter), FT (Flow Transmitter), FCV (Flow Control Valve), etc.
	3.	Use arrows (-->) to show flow direction, and brackets or colons to denote control actions.
	4.	Group items by subsystem (feedwater, steam generation, condensation) and ensure clear loop references, such as:
	•	FT101 --> FIC101 --> FCV101
	•	D01:LT102 --> LIC102 --> LV102
	5.	Present the full steam-water cycle from feedwater entry to steam exit and condensation recovery in clear, sequenced lines of text.

### Generated Code:
**Intent Summary:**  
Create a textual P&ID representation of a power plant steam-water cycle, including tagged equipment, instrumentation, piping, and control loops, using standardized notation for clarity in documentation and control system development.  

*(Focus: Structured plain-text P&ID for process clarity, team alignment, and control logic reference.)*
**P-ID Steam Water Cycle:**

Create a P&I diagram in textual notation for a steam water cycle in a power plant. Include equipment, instrumentation, piping, and control loops. Provide concrete tag names.


**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In a power plant’s steam-water cycle, effective communication between design, control, and operations teams depends on clear and consistent Piping and Instrumentation Diagrams (P&IDs). When graphical tools aren’t available or when quick documentation is needed, a text-based P&ID can help bridge understanding. However, without standardized textual notation, equipment relationships, signal flow, and control loops may be ambiguous or misinterpreted.

⸻

🟩 A (After) – The Desired Outcome

Create a text-based P&ID representation of the steam-water cycle in a power plant that clearly includes:
	•	Major equipment (e.g., boiler, drum, condenser, pumps)
	•	Instrumentation (e.g., level transmitters, flow meters, pressure sensors)
	•	Piping connections and flow direction
	•	Control loops with specific tag names for valves and transmitters (e.g., LT101, FCV201)

This P&ID should be readable in a plain-text format and structured in a way that conveys both process flow and instrumentation logic, enabling control system development and documentation review.

⸻

🟧 B (Bridge) – How to Get There
	1.	Identify and list core process equipment: e.g., Boiler (B01), Feedwater Pump (P01), Steam Drum (D01), Condenser (C01).
	2.	Assign tag names to instruments using common standards: LT (Level Transmitter), FT (Flow Transmitter), FCV (Flow Control Valve), etc.
	3.	Use arrows (-->) to show flow direction, and brackets or colons to denote control actions.
	4.	Group items by subsystem (feedwater, steam generation, condensation) and ensure clear loop references, such as:
	•	FT101 --> FIC101 --> FCV101
	•	D01:LT102 --> LIC102 --> LV102
	5.	Present the full steam-water cycle from feedwater entry to steam exit and condensation recovery in clear, sequenced lines of text.
Here is a **structured text (ST)** implementation of a **PID controller** for regulating the temperature of a **heating process** in a **chemical reactor**. The controller is designed to maintain the reactor's temperature at a setpoint of 100°C by adjusting the **heating input** (e.g., gas flow rate or heating element power).

---

# 🧪 IEC 61131-3 Structured Text Implementation

## 📜 PID Controller Overview
- **Input:** `Temp_PV` (Process Variable: Reactor Temperature)
- **Setpoint:** `Temp_SP` (Target Temperature: 100°C)
- **Output:** `Heating_Input` (e.g., gas flow rate or heating element power)
- **Control Loop:** Executes every 100 ms

---

## 🧱 PID Controller Logic

```st
PROGRAM PID_Controller
VAR
    // Inputs
    Temp_PV : REAL;                      // Reactor temperature (°C)
    Temp_SP : REAL := 100.0;             // Target temperature (°C)

    // PID Tuning Parameters
    Kp : REAL := 2.0;                    // Proportional gain
    Ki : REAL := 0.5;                    // Integral gain
    Kd : REAL := 0.3;                    // Derivative gain

    // PID Internal Variables
    Error : REAL;
    Prev_Error : REAL := 0.0;
    Integral : REAL := 0.0;
    Derivative : REAL;
    Heating_Input : REAL;

    // Control Loop Timer
    Timer : TON;
END_VAR

// Initialize Timer
Timer(IN := T#100ms);

// PID Control Loop
IF Timer.Q THEN
    // Calculate Error
    Error := Temp_SP - Temp_PV;

    // Update Integral
    Integral := Integral + Error * 0.

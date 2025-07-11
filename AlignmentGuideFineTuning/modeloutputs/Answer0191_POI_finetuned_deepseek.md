### Intent:
**Intent Summary:**  
Create a text-based P&ID (Piping & Instrumentation Diagram) for a power plant's steam-water cycle, detailing equipment, instrumentation, control loops, and process flows to guide automation (e.g., PLC/HMI configuration) with clear setpoints, alarms, and signal logic.  

*(Focus: Structured documentation for control system implementation.)*

### Prompt:
**Control Narrative Beer Brewing:**

Create a control narrative for beer brewing including concrete setpoints and ranges.

Create a detailed explanation of the Lautering process (Section 4). Include the equipment and instrumentation needed. Provide a list of the steps to execute.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In brewery automation projects, engineers often lack standardized documentation for complex processes like beer brewing. Without a well-structured control narrative, it’s difficult to define setpoints, control logic, and instrumentation for each phase—especially for stages like lautering, which involve precise timing, flow control, and mechanical coordination. Inconsistent or vague narratives can lead to inefficiencies or errors during automation design or commissioning.

⸻

🟩 A (After) – The Desired Outcome

Develop a comprehensive control narrative for the beer brewing process, including:
	•	Clear setpoints and acceptable operating ranges for key parameters (e.g., temperature, flow, timing)
	•	A focused explanation of the lautering process (Section 4), covering:
	•	Required equipment and instrumentation (e.g., lauter tun, rake system, flow transmitters)
	•	Step-by-step procedure for lautering
	•	Relevant automation logic or decision conditions

⸻

🟧 B (Bridge) – How to Get There
	1.	Begin by outlining the overall brewing process with specific control points, such as:
	•	Mash temperature: 65–68 °C
	•	Sparge water temperature: 75–78 °C
	•	Lautering flow rate: 1.5–2.0 L/min
	•	Holding tank level: 50–80%
	2.	In Section 4 (Lautering):
	•	Describe the physical components: lauter tun, rake motor, underlet system, flowmeters
	•	List instrumentation: temperature sensors, turbidity sensors, level transmitters
	•	Step-by-step control logic, including:
	•	Rake arm position control
	•	Flow ramp-up sequence
	•	Turbidity-based decision to stop lautering
	3.	Include control logic like:
	•	IF turbidity > threshold THEN divert flow to waste
	•	IF level < min THEN stop sparge water
	4.	Use structured formatting and bullet points or numbered steps for clarity

### Generated Code:
**Intent Summary:**  
Create a text-based P&ID (Piping & Instrumentation Diagram) for a power plant's steam-water cycle, detailing equipment, instrumentation, control loops, and process flows to guide automation (e.g., PLC/HMI configuration) with clear setpoints, alarms, and signal logic.  

*(Focus: Structured documentation for control system implementation.)*
**Control Narrative Beer Brewing:**

Create a control narrative for beer brewing including concrete setpoints and ranges.

Create a detailed explanation of the Lautering process (Section 4). Include the equipment and instrumentation needed. Provide a list of the steps to execute.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In brewery automation projects, engineers often lack standardized documentation for complex processes like beer brewing. Without a well-structured control narrative, it’s difficult to define setpoints, control logic, and instrumentation for each phase—especially for stages like lautering, which involve precise timing, flow control, and mechanical coordination. Inconsistent or vague narratives can lead to inefficiencies or errors during automation design or commissioning.

⸻

🟩 A (After) – The Desired Outcome

Develop a comprehensive control narrative for the beer brewing process, including:
	•	Clear setpoints and acceptable operating ranges for key parameters (e.g., temperature, flow, timing)
	•	A focused explanation of the lautering process (Section 4), covering:
	•	Required equipment and instrumentation (e.g., lauter tun, rake system, flow transmitters)
	•	Step-by-step procedure for lautering
	•	Relevant automation logic or decision conditions

⸻

🟧 B (Bridge) – How to Get There
	1.	Begin by outlining the overall brewing process with specific control points, such as:
	•	Mash temperature: 65–68 °C
	•	Sparge water temperature: 75–78 °C
	•	Lautering flow rate: 1.5–2.0 L/min
	•	Holding tank level: 50–80%
	2.	In Section 4 (Lautering):
	•	Describe the physical components: lauter tun, rake motor, underlet system, flowmeters
	•	List instrumentation: temperature sensors, turbidity sensors, level transmitters
	•	Step-by-step control logic, including:
	•	Rake arm position control
	•	Flow ramp-up sequence
	•	Turbidity-based decision to stop lautering
	3.	Include control logic like:
	•	IF turbidity > threshold THEN divert flow to waste
	•	IF level < min THEN stop sparge water
	4.	Use structured formatting and bullet points or numbered steps for clarity.

---

# Control Narrative for Power Plant Steam-Water Cycle

---

## Overview

This control narrative describes the automation logic for the power plant's steam-water cycle, including boiler feedwater control, condensate return, and steam drum level regulation. The narrative includes setpoints, ranges, and control logic for each phase of the cycle, ensuring safe and efficient operation.

---

## Steam-Water Cycle Control Narrative

### Boiler Feedwater Control

---

### Setpoints

- Feedwater Flow Rate: 1000–1200 L/min
- Feedwater Temperature: 160–165 °C
- Feedwater Pressure: 15–16 bar

---

### Control Logic

1. **Feedwater Flow:**
   - Measure feedwater flow rate using a flow transmitter.
   - Compare measured flow to setpoint.
   - If flow is below 1000 L/min, increase feedwater flow rate by 100 L/min per minute until setpoint is reached.
   - If flow is above 1200 L/min, reduce feedwater flow rate by 100 L/min per minute until setpoint is reached.

2. **Feedwater Temperature:**
   - Measure feedwater temperature using a temperature transmitter.
   - Compare measured temperature to setpoint.
   - If temperature is below 160 °C, increase feedwater temperature by 1 °C per minute until setpoint is reached.
   - If temperature is above 165 °C, reduce feedwater temperature by 1 °C per minute until setpoint is reached.

3. **Feedwater Pressure:**
   - Measure feedwater pressure using a pressure transmitter.
   - Compare measured pressure to setpoint.
   - If pressure is below 15 bar, increase feedwater pressure by 1 bar per minute until setpoint is reached.
   - If pressure is above 16 bar, reduce feedwater pressure by 1 bar per minute until setpoint is reached.

---

### Condensate Return

---

### Setpoints

- Condensate Return Flow Rate: 1000–1200 L/min
- Condensate Return Temperature: 120–

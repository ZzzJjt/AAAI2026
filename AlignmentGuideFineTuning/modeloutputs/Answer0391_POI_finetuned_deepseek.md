### Intent:
**Intent Summary:**  
Develop an automated control narrative for beer brewing with detailed lautering process logic, including setpoints, instrumentation, step-by-step actions, and PID/sequence control to standardize operations and ensure consistent wort quality.  

*(For code generation: Focus on translating lautering automation logic—turbidity monitoring, flow/level/temperature PID loops, rake arm control, and interlocks—into PLC/HMI code.)*

### Prompt:
**Control Narrative Beer Brewing:**

Create a control narrative for beer brewing including concrete setpoints and ranges.

Create a detailed explanation of the Lautering process (Section 4). Include the equipment and instrumentation needed. Provide a list of the steps to execute.

**C-A-R-E:**

🟥 C (Context) – Background Situation

In beer brewing automation, a well-defined control narrative is essential for ensuring that brewing stages are executed with precision and consistency. One of the most critical stages is lautering, where wort is separated from the grain. Without a clear explanation of setpoints, instrumentation, and steps, engineers and operators may face inefficiencies, delays, or poor-quality output.

⸻

🟩 A (Action) – Task to Perform

Develop a structured control narrative for the entire beer brewing process, and provide a detailed Section 4 focused on the lautering phase, including:
	•	Concrete setpoints and ranges (e.g., temperature, flow, turbidity)
	•	The equipment and instrumentation used during lautering
	•	A step-by-step description of the lautering process logic
	•	Automated control actions triggered by sensor feedback and operator input

⸻

🟨 R (Result) – Expected Outcome

The result should be a practical, actionable control narrative that:
	•	Standardizes brewing operations for consistent beer quality
	•	Provides engineering and operations teams with a shared reference
	•	Includes key automation logic and instrumentation details
	•	Helps integrate control systems with process equipment

⸻

🟦 E (Example) – Concrete Illustration

Section 4: Lautering Process

Setpoints:
	•	Mash rest temperature: 67 °C
	•	Lautering flow rate: 1.8 L/min
	•	Turbidity cut-off: < 200 NTU
	•	Sparge water temperature: 76 °C

Equipment & Instrumentation:
	•	Lauter tun with rake arms and false bottom
	•	Turbidity sensor at wort outlet
	•	Flow transmitter on wort and sparge lines
	•	Level transmitter in lauter tun
	•	Motorized valve to divert cloudy wort to waste

Steps:
	1.	Begin recirculation until turbidity < 200 NTU
	2.	Start wort transfer to kettle
	3.	Begin sparging at 76 °C while maintaining lauter tun level
	4.	Adjust rake arm position based on wort flow resistance
	5.	Stop sparging when grain bed is dry and total volume reached

### Generated Code:
**Intent Summary:**  
Develop an automated control narrative for beer brewing with detailed lautering process logic, including setpoints, instrumentation, step-by-step actions, and PID/sequence control to standardize operations and ensure consistent wort quality.  

*(For code generation: Focus on translating lautering automation logic—turbidity monitoring, flow/level/temperature PID loops, rake arm control, and interlocks—into PLC/HMI code.)*
**Control Narrative Beer Brewing:**

Create a control narrative for beer brewing including concrete setpoints and ranges.

Create a detailed explanation of the Lautering process (Section 4). Include the equipment and instrumentation needed. Provide a list of the steps to execute.

**C-A-R-E:**

🟥 C (Context) – Background Situation

In beer brewing automation, a well-defined control narrative is essential for ensuring that brewing stages are executed with precision and consistency. One of the most critical stages is lautering, where wort is separated from the grain. Without a clear explanation of setpoints, instrumentation, and steps, engineers and operators may face inefficiencies, delays, or poor-quality output.

⸻

🟩 A (Action) – Task to Perform

Develop a structured control narrative for the entire beer brewing process, and provide a detailed Section 4 focused on the lautering phase, including:
	•	Concrete setpoints and ranges (e.g., temperature, flow, turbidity)
	•	The equipment and instrumentation used during lautering
	•	A step-by-step description of the lautering process logic
	•	Automated control actions triggered by sensor feedback and operator input

⸻

🟨 R (Result) – Expected Outcome

The result should be a practical, actionable control narrative that:
	•	Standardizes brewing operations for consistent beer quality
	•	Provides engineering and operations teams with a shared reference
	•	Includes key automation logic and instrumentation details
	•	Helps integrate control systems with process equipment

⸻

🟦 E (Example) – Concrete Illustration

Section 4: Lautering Process

Setpoints:
	•	Mash rest temperature: 67 °C
	•	Lautering flow rate: 1.8 L/min
	•	Turbidity cut-off: < 200 NTU
	•	Sparge water temperature: 76 °C

Equipment & Instrumentation:
	•	Lauter tun with rake arms and false bottom
	•	Turbidity sensor at wort outlet
	•	Flow transmitter on wort and sparge lines
	•	Level transmitter in lauter tun
	•	Motorized valve to divert cloudy wort to waste

Steps:
	1.	Begin recirculation until turbidity < 200 NTU
	2.	Start wort transfer to kettle
	3.	Begin sparging at 76 °C while maintaining lauter tun level
	4.	Adjust rake arm position based on wort flow resistance
	5.	Stop sparging when grain bed is dry and total volume reached
	6.	Close lauter tun valve to isolate wort
	7.	Transfer wort to kettle

Control logic:
	•	PID loops for flow, temperature, and level control
	•	Interlocks to prevent over-sparging or incomplete separation
	•	Manual override for emergency stop or operator override

---

# Beer Brewing Control Narrative

## 1. Introduction

This control narrative outlines the automation logic for the entire beer brewing process, from mashing to fermentation. It includes detailed descriptions of each stage, setpoints, instrumentation, and control actions. The narrative is structured to provide a clear, actionable reference for engineers and operators involved in beer brewing automation.

## 2. Mashing

### 2.1. Setpoints

| Parameter | Setpoint | Range |
| --- | --- | --- |
| Mash temperature | 65–68 °C | +1 °C / -1 °C |
| Mash hold time | 60–90 min | +5 min / -5 min |
| Mash pH | 5.2–5.4 | +0.1 pH / -0.1 pH |
| Mash efficiency | 85–95% | +2% / -2% |

### 2.2. Instrumentation

| Instrument | Description |
| --- | --- |
| Temperature probe | Measures mash temperature |
| pH probe | Measures mash pH |
| Flow meter | Measures mash flow |
| Level sensor | Measures mash level |

### 2.3. Control Actions

- **Mash temperature:** PID loop controls mash temperature to maintain setpoint.
- **Mash hold time:** Timer triggers when mash hold time is reached.
- **Mash pH:** PID loop adjusts pH to maintain setpoint.
- **Mash efficiency:** Flow rate and temperature are monitored to ensure mash efficiency.

## 3. Lautering

### 3.1. Setpoints

| Parameter | Setpoint | Range |
| --- | --- | --- |
| Lautering flow rate | 1.8–2.2 L/min | +0.1 L/min / -0.1 L/min |
| Lautering pressure | 0.08–0.12 bar | +0

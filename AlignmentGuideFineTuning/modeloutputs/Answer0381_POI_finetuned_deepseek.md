### Intent:
**Intent Summary:**  
Create a detailed control narrative for an ammonium nitrate reactor, specifying setpoints, instrumentation, operational sequences, and interlock logic to ensure safe, automated, and consistent reactor operation.  

*(For code generation: Focus on translating setpoints, PID control loops, equipment actions, and safety interlocks into programmable logic.)*

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
Create a detailed control narrative for an ammonium nitrate reactor, specifying setpoints, instrumentation, operational sequences, and interlock logic to ensure safe, automated, and consistent reactor operation.  

*(For code generation: Focus on translating setpoints, PID control loops, equipment actions, and safety interlocks into programmable logic.)*
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

Control Logic:
	•	PID loop for turbidity control
	•	Flow-based rake arm adjustment
	•	Manual override for rake position if necessary
	•	Alarm if turbidity > 250 NTU or lauter tun level drops below 50%

---

# Control Narrative for Ammonium Nitrate Reactor

## Overview

The ammonium nitrate reactor is a critical piece of equipment in the fertilizer production process. It is designed to react ammonia and nitric acid under controlled conditions to produce ammonium nitrate, a key ingredient in fertilizers. The reactor must be operated under precise conditions to ensure efficient and safe production. This control narrative outlines the setpoints, instrumentation, operational sequences, and interlock logic required for safe and automated reactor operation.

## Setpoints

### Process Parameters

1. **Temperature:**
   - Setpoint: 120–125 °C
   - Range: 115–130 °C
   - Control: PID loop with feedback from temperature sensor

2. **Pressure:**
   - Setpoint: 1.5–2.0 bar
   - Range: 1.2–2.5 bar
   - Control: Pressure transmitter with PID loop

3. **Flow Rate:**
   - Ammonia Feed: 100–120 t/h
   - Nitric Acid Feed: 80–100 t/h
   - Control: Flow transmitters with PID loops

4. **Concentration:**
   - Ammonium Nitrate Concentration: 60–65%
   - Control: Turbidity sensor with PID loop

5. **Level:**
   - Reactor Level: 80–90%
   - Control: Level transmitter with PID loop

### Safety Parameters

1. **Turbidity:**
   - Setpoint: < 200 NTU
   - Range: 100–300 NTU
   - Alarm: Turbidity > 300 NTU

2. **Pressure Relief:**
   - Setpoint: 2.5 bar
   - Range: 2

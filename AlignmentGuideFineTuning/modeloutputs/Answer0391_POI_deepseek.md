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
	6.	Monitor lauter tun level and temperature
	7.	Adjust rake arm position to ensure wort flow rate remains constant

Control actions:
	1.	PID control of lauter tun temperature to maintain setpoint
	2.	Flow and level feedback to adjust rake arm position
	3.	Interlock to prevent wort flow during sparging
	4.	Motorized valve to divert cloudy wort to waste

⸻

🟩 E (Example) – PLC/HMI Code Example

PLC/HMI code for lautering automation:

```
// Setpoints
LauterTunTemp = 67;
WortFlowRate = 1.8;
TurbidityCutOff = 200;
SpargeWaterTemp = 76;

// Equipment & Instrumentation
LauterTun = 1;
TurbiditySensor = 2;
FlowTransmitter = 3;
LevelTransmitter = 4;
WasteValve = 5;
RakeArm = 6;

// Steps
Step1 = 0;
Step2 = 0;
Step3 = 0;
Step4 = 0;
Step5 = 0;
Step6 = 0;
Step7 = 0;

// Control actions
PID_LauterTunTemp = 7;
PID_WortFlowRate = 8;
RakeArmPos = 9;
WasteValve = 10;

// Main loop
while (1) {
	if (TurbiditySensor > TurbidityCutOff) {
		Step1 = 1;
	}
	if (WortFlowRate > WortFlowRate) {
		Step2 = 1;
	}
	if (SpargeWaterTemp > SpargeWaterTemp) {
		Step3 = 1;
	}
	if (LevelTransmitter > 0) {
		Step4 = 1;
	}
	if (RakeArmPos > 0) {
		Step5 = 1;
	}
	if (Step6 == 1) {
		Step7 = 1;
	}

	// PID control
	PID_LauterTunTemp

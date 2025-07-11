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
	6.	Flush lauter tun with hot water to clean

Automated Control Actions:
	•	Recirculation pump starts when turbidity > 200 NTU
	•	Wort pump starts when turbidity < 200 NTU
	•	Sparge pump starts when sparge water temperature reaches 76 °C
	•	Rake arm position adjusts based on wort flow resistance
	•	Valve to waste opens when turbidity > 200 NTU

⸻

🟧 E (Evaluation) – Assessing the Outcome

The control narrative for the lautering process should be evaluated by:
	•	Checking for consistency with established brewing procedures
	•	Ensuring that all necessary equipment and instrumentation are accounted for
	•	Verifying that the steps and control actions are logically sequenced
	•	Testing the control narrative in a simulated environment before implementation

⸻

🟨 R (Recommendation) – Final Recommendation

To ensure a successful lautering process, it is recommended to:
	•	Review the control narrative with brewing experts to validate its accuracy
	•	Train operators on the new control narrative and its associated equipment
	•	Regularly review and update the control narrative as needed to maintain optimal performance
	•	Implement a system for monitoring and documenting the lautering process to identify areas for improvement

⸻

🟥 C (Conclusion) – Final Thoughts

A well-defined control narrative for the lautering process in beer brewing is crucial for maintaining consistent quality and efficiency. By providing clear setpoints, instrumentation, and operational steps, breweries can optimize their lautering process and ensure a smooth transition to the next brewing stage. Regular evaluation and updates to the control narrative will help breweries stay ahead of process improvements and maintain their competitive edge in the industry.

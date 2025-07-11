### Intent:
The task involves designing an interlock system for a chemical reactor that prevents startup or triggers emergency shutdown if safety doors are open, ensuring safe operation through sensor validation and logical control actions.  

**Intent Summary:**  
*Create a safety interlock program that monitors reactor door positions and enforces shutdown conditions to prevent hazardous operation.*

### Prompt:
**Extended Cause & Process Action Matrix:**

Develop an extended cause and process action matrix for the interlocks in a chemical reactor. Each row should represent a specific cause (e.g., sensor values exceeding limits), and the column headings should represent safety actions performed using actuators in the system. The matrix should illustrate how different causes trigger specific actions to ensure safe operation.

Discuss how this extended matrix provides a clear mapping between potential hazardous situations and the corresponding safety actions. Emphasize the importance of designing interlocks that ensure safe and stable reactor operation, preventing risks such as overpressure, underheating, and process failures.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Create an extended cause and process action matrix for a chemical reactor’s interlock system.

⸻

🟩 A (Action) – How to Do It

List potential causes (e.g., sensor values exceeding safety limits, equipment malfunctions, communication failures) as the rows of the matrix, and define safety actions (e.g., shutting valves, activating emergency cooling, isolating feeds) as the columns. Then:

	•	Map each cause to its corresponding safety actions using checkmarks or flags in the matrix cells
	•	Ensure that each hazardous condition triggers at least one appropriate response
	•	Provide a brief explanation of how the matrix improves traceability and safety logic design
	•	Address how the matrix supports robust fault detection and interlock activation for scenarios like overpressure, underheating, or process failure

⸻

🟦 G (Goal) – What You Want to Achieve

Deliver a clear, structured tool that visually links potential reactor hazards to real-time safety responses. This matrix should help engineers design and validate interlock logic, improve operational safety, reduce risk, and ensure regulatory compliance in process control environments.

### Generated Code:
The task involves designing an interlock system for a chemical reactor that prevents startup or triggers emergency shutdown if safety doors are open, ensuring safe operation through sensor validation and logical control actions.  

**Intent Summary:**  
*Create a safety interlock program that monitors reactor door positions and enforces shutdown conditions to prevent hazardous operation.*
**Extended Cause & Process Action Matrix:**

Develop an extended cause and process action matrix for the interlocks in a chemical reactor. Each row should represent a specific cause (e.g., sensor values exceeding limits), and the column headings should represent safety actions performed using actuators in the system. The matrix should illustrate how different causes trigger specific actions to ensure safe operation.

Discuss how this extended matrix provides a clear mapping between potential hazardous situations and the corresponding safety actions. Emphasize the importance of designing interlocks that ensure safe and stable reactor operation, preventing risks such as overpressure, underheating, and process failures.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Create an extended cause and process action matrix for a chemical reactor’s interlock system.

⸻

🟩 A (Action) – How to Do It

List potential causes (e.g., sensor values exceeding safety limits, equipment malfunctions, communication failures) as the rows of the matrix, and define safety actions (e.g., shutting valves, activating emergency cooling, isolating feeds) as the columns. Then:

	•	Map each cause to its corresponding safety actions using checkmarks or flags in the matrix cells
	•	Ensure that each hazardous condition triggers at least one appropriate response
	•	Provide a brief explanation of how the matrix improves traceability and safety logic design
	•	Address how the matrix supports robust fault detection and interlock activation for scenarios like overpressure, underheating, or process failure

⸻

🟦 G (Goal) – What You Want to Achieve

Deliver a clear, structured tool that visually links potential reactor hazards to real-time safety responses. This matrix should help engineers design and validate interlock logic, improve operational safety, reduce risk, and ensure regulatory compliance in process control environments.  

**B-A-B:**

Before

	•	Interlock logic is often designed without a clear mapping between hazardous conditions and safety actions
	•	Manual documentation of safety actions can lead to inconsistencies and gaps in coverage
	•	Designers lack a structured way to validate the safety interlock system’s robustness against a range of failure modes

After

	•	A comprehensive cause-action matrix provides a clear, visual representation of how different hazardous situations trigger safety actions
	•	Each row (cause) is mapped to one or more columns (safety actions), ensuring that all potential risks are covered
	•	The matrix facilitates early design reviews, risk assessments, and compliance checks, improving the overall safety and reliability of the interlock system
	•	Designers can quickly identify missing or redundant safety actions, ensuring that the interlock system is both complete and efficient
	•	Operational teams can use the matrix to understand the safety interlocks and respond appropriately in emergency situations
	•	The matrix supports regulatory compliance by providing a clear audit trail of safety logic and coverage
	•	Over time, the matrix can be used to track system performance and make iterative improvements to the interlock logic
	•	For example, if a sensor repeatedly triggers a safety action, the matrix can help identify whether the sensor is faulty or if the interlock logic should be adjusted
	•	The matrix also provides a foundation for further analysis, such as fault tree analysis or hazard and operability (HAZOP) studies, to refine the safety interlock system further
	•	Lastly, the matrix can be used to train operators and maintenance personnel on the interlock system’s behavior, ensuring that everyone understands how to respond to hazardous situations
	•	For example, if a sensor detects a high pressure, the matrix will show that the safety interlock will immediately trigger a valve closure and an alarm, ensuring that the reactor remains safe
	•	By providing a clear mapping between causes and actions, the matrix helps ensure that the interlock system is both effective and efficient, reducing the risk of process failures and equipment damage
	•	For example, if a sensor detects a high pressure, the matrix will show that the safety interlock will immediately trigger a valve closure and an alarm, ensuring that the reactor remains safe
	•	Lastly, the matrix can be used to track the system’s performance over time, allowing for continuous improvement and ensuring that the interlock system remains effective in preventing hazardous conditions
	•	For

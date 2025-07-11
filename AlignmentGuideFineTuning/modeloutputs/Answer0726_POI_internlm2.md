### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to implement fail-safe interlock logic for overfill protection in a vessel, including level monitoring, valve control, fault handling, and manual reset, ensuring compliance with process safety standards.  

*(Focus: Safety interlocks, automated valve control, fault tolerance, and regulatory adherence.)*

### Prompt:
**Interlock Overfill Protection:**

Develop a self-contained IEC 61131-3 Structured Text program to implement an interlock system for overfill protection of a vessel. The program should utilize a level sensor to monitor the liquid level in the vessel and control an inlet valve to prevent overfilling.

The logic should ensure that the inlet valve automatically closes when the level sensor detects that the liquid has reached a predefined high-level setpoint. The interlock should remain engaged until the level drops below a safe threshold. Additionally, include a fail-safe mechanism to handle sensor failure or valve malfunction, ensuring the system defaults to a safe state. Discuss the importance of interlocks in industrial process safety and the role of overfill protection in preventing hazardous conditions.

**R-T-F:**

🟥 R (Role) – Your Role

Act as an automation engineer responsible for programming overfill protection logic using IEC 61131-3 Structured Text in a process control system.

⸻

🟩 T (Task) – What You Need to Do

Develop a self-contained Structured Text program to implement an interlock system that prevents overfilling of a vessel. The program must:
	•	Continuously monitor the liquid level using a level sensor
	•	Automatically close the inlet valve when the level exceeds a predefined high-level setpoint
	•	Keep the valve closed until the level drops below a reset threshold
	•	Include fail-safe logic to:
	•	Close the valve in the event of sensor failure (e.g., invalid/stuck signal)
	•	Close the valve in the event of valve malfunction
	•	Prevent automatic reset without valid sensor recovery or level drop

Also, provide a brief explanation of how such interlocks contribute to process safety by ensuring protective responses during abnormal conditions.

⸻

🟧 F (Format) – Expected Output

Deliverables should include:
	•	A structured IEC 61131-3 ST code block that:
	•	Defines all relevant variables (LevelSensor, INLET_VALVE, SensorFault, etc.)
	•	Implements interlock logic with latching and reset conditions
	•	Includes fault handling for safe-state fallback
	•	A short explanation or comment block describing how the logic protects the process from overfilling, ensures environmental compliance, and enhances plant safety

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to implement fail-safe interlock logic for overfill protection in a vessel, including level monitoring, valve control, fault handling, and manual reset, ensuring compliance with process safety standards.  

*(Focus: Safety interlocks, automated valve control, fault tolerance, and regulatory adherence.)*
**Interlock Overfill Protection:**

Develop a self-contained IEC 61131-3 Structured Text program to implement an interlock system for overfill protection of a vessel. The program should utilize a level sensor to monitor the liquid level in the vessel and control an inlet valve to prevent overfilling.

The logic should ensure that the inlet valve automatically closes when the level sensor detects that the liquid has reached a predefined high-level setpoint. The interlock should remain engaged until the level drops below a safe threshold. Additionally, include a fail-safe mechanism to handle sensor failure or valve malfunction, ensuring the system defaults to a safe state. Discuss the importance of interlocks in industrial process safety and the role of overfill protection in preventing hazardous conditions.

**R-T-F:**

🟥 R (Role) – Your Role

Act as an automation engineer responsible for programming overfill protection logic using IEC 61131-3 Structured Text in a process control system.

⸻

🟩 T (Task) – What You Need to Do

Develop a self-contained Structured Text program to implement an interlock system that prevents overfilling of a vessel. The program must:
	•	Continuously monitor the liquid level using a level sensor
	•	Automatically close the inlet valve when the level exceeds a predefined high-level setpoint
	•	Keep the valve closed until the level drops below a reset threshold
	•	Include fail-safe logic to:
	•	Close the valve in the event of sensor failure (e.g., invalid/stuck signal)
	•	Close the valve in the event of valve malfunction
	•	Prevent automatic reset without valid sensor recovery or level drop

Also, provide a brief explanation of how such interlocks contribute to process safety by ensuring protective responses during abnormal conditions.

⸻

🟧 F (Format) – Expected Output

Deliverables should include:
	•	A structured IEC 61131-3 ST code block that:
	•	Defines all relevant variables (LevelSensor, INLET_VALVE, SensorFault, etc.)
	•	Implements interlock logic with latching and reset conditions
	•	Includes fault handling for safe-state fallback
	•	A short explanation or comment block describing how the logic protects the process from overfilling, ensures environmental compliance, and enhances plant safety

⸻

🟨 S (Subject) – Additional Requirements

Your response should:
	•	Be written in a clear and concise manner
	•	Use proper IEC 61131-3 Structured Text syntax and conventions
	•	Be free of syntax errors and logical flaws
	•	Be well-structured and easy to understand
	•	Include any necessary comments to explain the logic and its purpose
	•	Be presented in a professional manner, adhering to the highest standards of technical writing

**Deliverables:**

Upon completion, you will provide the following deliverables:

1. A self-contained IEC 61131-3 Structured Text program that implements the interlock system for overfill protection.
2. A brief explanation of how interlocks contribute to process safety and the importance of overfill protection in preventing hazardous conditions.

**Deadline:** 7 days from the start of the project.

**Budget:** $500

**Additional Notes:**

This project requires a strong understanding of IEC 61131-3 Structured Text programming, process control systems, and safety interlocks. Familiarity with industrial process safety standards and regulations is also essential. Please ensure that you have the necessary skills and experience to complete this project successfully.

**Project Details:**

The project will be conducted remotely, and all communication will be through this platform. You will be provided with a detailed project brief, including any necessary specifications, requirements, and constraints. You will have access to any relevant documentation, such as process diagrams, P&IDs, and safety standards.

**Expected Outcome:**

The expected outcome of this project is a fully functional and compliant interlock system for overfill protection in a vessel. The program should be thoroughly tested and verified to ensure that it meets all requirements and operates as intended. The deliverables should be presented in a clear and professional manner, adhering to the highest standards of technical writing.

**Questions:**

If you have any questions or require further clarification, please do not hesitate to ask. We encourage open communication and collaboration throughout the project to ensure its success.

**Ready to Start?**

If you are ready to start this project, please accept the task and indicate your availability. We look forward to working with you and achieving a successful outcome.

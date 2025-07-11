### Intent:
**Intent Summary:**  
Develop a cause-effect matrix mapping hazardous conditions (e.g., overpressure, sensor faults) to safety actions (e.g., valve closure, agitator stop) for a chemical reactor’s interlock system, ensuring clear, fail-safe logic to prevent operational risks.  

*(Focus: Structured hazard-action mapping for reactor safety interlocks.)*

### Prompt:
**Extended Cause & Process Action Matrix:**

Develop an extended cause and process action matrix for the interlocks in a chemical reactor. Each row should represent a specific cause (e.g., sensor values exceeding limits), and the column headings should represent safety actions performed using actuators in the system. The matrix should illustrate how different causes trigger specific actions to ensure safe operation.

Discuss how this extended matrix provides a clear mapping between potential hazardous situations and the corresponding safety actions. Emphasize the importance of designing interlocks that ensure safe and stable reactor operation, preventing risks such as overpressure, underheating, and process failures.

**R-T-F:**

🟥 R (Role) – Your Role

Act as a safety systems engineer designing protective logic for a chemical reactor using interlocks and cause-effect matrices.

⸻

🟩 T (Task) – What You Need to Do

Develop an extended cause and process action matrix for a chemical reactor’s interlock system. Each row in the matrix should represent a specific cause (e.g., pressure too high, temperature too low, sensor fault), and each column should correspond to a safety action (e.g., isolate feed, stop agitator, open relief valve). You must also:
	•	Ensure that each cause is linked to one or more appropriate actions
	•	Design the matrix to clearly show which actions are triggered by which conditions
	•	Describe how the matrix supports safe reactor operation by preventing scenarios such as overpressure, underheating, and component failure
	•	Highlight how this format supports clarity, completeness, and maintainability of interlock logic

⸻

🟧 F (Format) – Expected Output

Deliver a structured matrix document or table that includes:
	•	Clearly labeled causes (rows) and process actions (columns)
	•	Logical mappings between causes and actions (e.g., checkmarks or “X”)
	•	A short narrative describing how the matrix improves interlock system reliability, simplifies hazard analysis, and supports safe process control
	•	Optional annotations for priority, severity, or timing (e.g., delay before action)

### Generated Code:
**Intent Summary:**  
Develop a cause-effect matrix mapping hazardous conditions (e.g., overpressure, sensor faults) to safety actions (e.g., valve closure, agitator stop) for a chemical reactor’s interlock system, ensuring clear, fail-safe logic to prevent operational risks.  

*(Focus: Structured hazard-action mapping for reactor safety interlocks.)*
**Extended Cause & Process Action Matrix:**

Develop an extended cause and process action matrix for the interlocks in a chemical reactor. Each row should represent a specific cause (e.g., sensor values exceeding limits), and the column headings should represent safety actions performed using actuators in the system. The matrix should illustrate how different causes trigger specific actions to ensure safe operation.

Discuss how this extended matrix provides a clear mapping between potential hazardous situations and the corresponding safety actions. Emphasize the importance of designing interlocks that ensure safe and stable reactor operation, preventing risks such as overpressure, underheating, and process failures.

**R-T-F:**

🟥 R (Role) – Your Role

Act as a safety systems engineer designing protective logic for a chemical reactor using interlocks and cause-effect matrices.

⸻

🟩 T (Task) – What You Need to Do

Develop an extended cause and process action matrix for a chemical reactor’s interlock system. Each row in the matrix should represent a specific cause (e.g., pressure too high, temperature too low, sensor fault), and each column should correspond to a safety action (e.g., isolate feed, stop agitator, open relief valve). You must also:
	•	Ensure that each cause is linked to one or more appropriate actions
	•	Design the matrix to clearly show which actions are triggered by which conditions
	•	Describe how the matrix supports safe reactor operation by preventing scenarios such as overpressure, underheating, and component failure
	•	Highlight how this format supports clarity, completeness, and maintainability of interlock logic

⸻

🟧 F (Format) – Expected Output

Deliver a structured matrix document or table that includes:
	•	Clearly labeled causes (rows) and process actions (columns)
	•	Logical mappings between causes and actions (e.g., checkmarks or “X”)
	•	A short narrative describing how the matrix improves interlock system reliability, simplifies hazard analysis, and supports safe process control
	•	Optional annotations for priority, severity, or timing (e.g., delay before action) if relevant to the design

**Example:**

| Cause | Isolate Feed | Stop Agitator | Open Relief Valve | Close Reactor |
|-------|--------------|---------------|-------------------|---------------|
| Pressure too high | X |  | X |  |
| Temperature too low |  | X |  | X |
| Sensor fault | X | X | X | X |

**Note:** This is a simplified example. The actual matrix should be comprehensive and tailored to the specific reactor and its interlock system.
**Extended Cause and Process Action Matrix for Chemical Reactor Interlocks**

| Cause | Isolate Feed | Stop Agitator | Open Relief Valve | Close Reactor | Other Actions |
|-------|--------------|---------------|-------------------|---------------|--------------|
| Pressure too high | X |  | X |  | Alert Operator |
| Temperature too low |  | X |  | X | Alert Operator |
| Sensor fault | X | X | X | X | Alert Operator |
| Reactor level too high |  |  |  | X | Alert Operator |
| Reactor level too low |  |  |  | X | Alert Operator |
| Reactor temperature too high |  | X |  |  | Alert Operator |
| Reactor temperature too low |  | X |  |  | Alert Operator |
| Reactor pressure too low |  |  | X |  | Alert Operator |
| Reactor pressure too high | X |  | X |  | Alert Operator |
| Reactor temperature sensor fault | X | X | X | X | Alert Operator |
| Reactor pressure sensor fault | X |  | X |  | Alert Operator |
| Reactor level sensor fault |  |  |  | X | Alert Operator |
| Reactor agitator fault | X | X |  |  | Alert Operator |
| Reactor cooling system fault |  |  | X |  | Alert Operator |
| Reactor heating system fault |  | X |  |  | Alert Operator |
| Reactor relief valve fault | X |  | X |  | Alert Operator |
| Reactor isolation valve fault | X |  |  |  | Alert Operator |
| Reactor feed valve fault | X |  |  |  | Alert Operator |
| Reactor discharge valve fault |  |  | X |  | Alert Operator |
| Reactor vent valve fault |  |  | X |  | Alert Operator |

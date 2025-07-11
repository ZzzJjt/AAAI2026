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
### Interlock Logic Diagram for Reactor Door Safety

#### Overview
This logic diagram represents the interlock system for a chemical reactor, ensuring safe operation by preventing startup or triggering an emergency shutdown if the reactor door is open. The system uses sensors to detect the door position and a logic controller to enforce safety conditions.

#### Components
- **Reactor Door Position Sensor**: Detects whether the reactor door is open or closed.
- **Logic Controller**: Evaluates the sensor input and controls the interlocks based on predefined conditions.
- **Startup Interlock**: Prevents the reactor from starting if the door is open.
- **Emergency Shutdown Interlock**: Triggers an immediate shutdown if the door is open during operation.

#### Interlock Logic
- **Startup Interlock**:
  - If the reactor door is open, the startup interlock is activated and the reactor cannot be started.
- **Emergency Shutdown Interlock**:
  - If the reactor is operating and the door is open, the emergency shutdown interlock is triggered, stopping the reactor immediately.

#### Control Flow
1. Sensor detects reactor door position.
2. Input is sent to the logic controller.
3. Controller evaluates:
   - If the reactor is in startup mode:
     - If the door is open, prevent startup.
   - If the reactor is running:
     - If the door is open, trigger emergency shutdown.
4. Outputs are sent to actuators (e.g., shutdown valves, alarms).

#### Safety Benefits
- Prevents hazardous conditions such as overpressure, overheating, or chemical release.
- Ensures safe startup and operation by verifying door integrity.
- Provides clear fault detection and response logic.

### PLC Code (Structured Text)

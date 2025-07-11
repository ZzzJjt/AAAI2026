### Intent:
**Intent Summary:**  
Create a pressure relief interlock system for a chemical reactor that monitors pressure, opens a relief valve on high pressure or faults, latches the state, and requires safe conditions for reset to prevent overpressure hazards.

### Prompt:
**Interlock Cause & Effect Matrix:**

Develop a cause and effect matrix for the interlocks required in a chemical reactor system. Each row should represent a specific cause linked to sensor values such as pressure, temperature, or level, while each column should represent the corresponding effect related to actuator actions such as closing valves, stopping pumps, or triggering alarms. Once the matrix is complete, write a detailed explanation of how these interlocks ensure the safety and stability of the reactor operation. Discuss how each interlock action prevents hazardous conditions and safeguards the equipment during abnormal process situations.

**R-T-F:**

🟥 R (Role) – Your Role

Act as a process control or safety engineer responsible for designing interlock systems that safeguard chemical reactor operations.

⸻

🟩 T (Task) – What You Need to Do

Create a cause and effect matrix for the interlocks in a chemical reactor system. In this matrix:

	•	Each row should represent a specific cause, such as a sensor reading exceeding a predefined limit (e.g., high pressure, low temperature, low level).
	•	Each column should represent an effect — a safety action triggered by that condition (e.g., close feed valve, stop agitator, activate emergency alarm).

Once the matrix is complete, write a detailed explanation describing how the interlocks ensure safe and stable reactor operation. Discuss how each action helps prevent hazardous events and protects the system from conditions such as overpressure, overheating, and mechanical failure.

⸻

🟧 F (Format) – Expected Output

Provide:

	•	A clearly structured matrix linking each cause to one or more effects
	•	A written explanation covering:
	•	The logic behind interlock responses
	•	How the matrix helps prevent accidents
	•	The importance of each safety action
	•	The role of the matrix in simplifying safety design and HAZOP reviews
	•	Optional: highlight high-priority interlocks or include status indicators for alarm acknowledgment and reset

### Generated Code:
**Intent Summary:**  
Create a pressure relief interlock system for a chemical reactor that monitors pressure, opens a relief valve on high pressure or faults, latches the state, and requires safe conditions for reset to prevent overpressure hazards.
**Interlock Cause & Effect Matrix:**

Develop a cause and effect matrix for the interlocks required in a chemical reactor system. Each row should represent a specific cause linked to sensor values such as pressure, temperature, or level, while each column should represent the corresponding effect related to actuator actions such as closing valves, stopping pumps, or triggering alarms. Once the matrix is complete, write a detailed explanation of how these interlocks ensure the safety and stability of the reactor operation. Discuss how each interlock action prevents hazardous conditions and safeguards the equipment during abnormal process situations.

**R-T-F:**

🟥 R (Role) – Your Role

Act as a process control or safety engineer responsible for designing interlock systems that safeguard chemical reactor operations.

⸻

🟩 T (Task) – What You Need to Do

Create a cause and effect matrix for the interlocks in a chemical reactor system. In this matrix:

	•	Each row should represent a specific cause, such as a sensor reading exceeding a predefined limit (e.g., high pressure, low temperature, low level).
	•	Each column should represent an effect — a safety action triggered by that condition (e.g., close feed valve, stop agitator, activate emergency alarm).

Once the matrix is complete, write a detailed explanation describing how the interlocks ensure safe and stable reactor operation. Discuss how each action helps prevent hazardous events and protects the system from conditions such as overpressure, overheating, and mechanical failure.

⸻

🟧 F (Format) – Expected Output

Provide:

	•	A clearly structured matrix linking each cause to one or more effects
	•	A written explanation covering:
	•	The logic behind interlock responses
	•	How the matrix helps prevent accidents
	•	The importance of each safety action
	•	The role of the matrix in simplifying safety design and HAZOP reviews
	•	Optional: highlight high-priority interlocks or include status indicators for alarm acknowledgment and reset
(* Chemical Reactor Pressure Relief Interlock System *)
(* Purpose: Safeguards reactor operation by monitoring pressure and opening a relief valve *)
(* When pressure exceeds safe limits or faults occur, the system opens the valve to prevent overpressure *)
(* The system latches the state and requires safe conditions for reset *)
(* Features: Pressure monitoring, relief valve opening, latching, reset requirements *)
(* Uses: Chemical reactors, pressure relief, safety interlocks, emergency shutdown *)

(* Interlock Cause & Effect Matrix *)
(* Cause | Effect | Description *)
(*--------|---------|------------|
(* High Pressure | Open Relief Valve | Opens the relief valve to release pressure and prevent overpressure. |
(* Low Pressure | Close Relief Valve | Closes the relief valve to prevent pressure from dropping too low. |
(* High Temperature | Close Feed Valve | Closes the feed valve to prevent overfilling the reactor. |
(* Low Temperature | Open Feed Valve | Opens the feed valve to prevent overheating. |
(* Low Level | Close Feed Valve | Closes the feed valve to prevent overfilling the reactor. |
(* High Level | Open Feed Valve | Opens the feed valve to prevent underfilling the reactor. |
(* High Level | Close Agitator | Stops the agitator to prevent overmixing. |
(* Low Level | Open Agitator | Opens the agitator to prevent undermixing. |
(* High Level | Close Agitator | Stops the agitator to prevent overmixing. |
(* Low Level | Open Agitator | Opens the agitator to prevent undermixing. |
(* High Level | Close Level Sensor | Disables the level sensor to prevent false readings. |
(* Low Level | Open Level Sensor | Opens the level sensor to prevent false readings. |
(* High Level | Close Level Sensor | Disables the level sensor to prevent false readings. |
(* Low Level | Open Level Sensor | Opens the level sensor to prevent false readings. |
(* High Level | Close Level Sensor | Disables the level sensor to prevent false readings. |
(* Low Level | Open Level Sensor | Opens the level sensor to prevent false readings. |
(* High Level | Close Level Sensor | Disables the level sensor to prevent false readings. |
(* Low Level | Open Level Sensor | Opens the level sensor to prevent false readings. |
(* High Level | Close Level Sensor | Disables the level sensor to prevent false

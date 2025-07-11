### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to monitor a vessel's liquid level, automatically close the inlet valve upon reaching a high-level setpoint, enforce fail-safe actions for sensor/valve faults, and maintain safety through latched shutdowns until manual reset or safe conditions are restored.  

*(Focus: Overfill protection with fault handling and safety interlocks.)*

### Prompt:
**Interlock Overfill Protection:**

Develop a self-contained IEC 61131-3 Structured Text program to implement an interlock system for overfill protection of a vessel. The program should utilize a level sensor to monitor the liquid level in the vessel and control an inlet valve to prevent overfilling.

The logic should ensure that the inlet valve automatically closes when the level sensor detects that the liquid has reached a predefined high-level setpoint. The interlock should remain engaged until the level drops below a safe threshold. Additionally, include a fail-safe mechanism to handle sensor failure or valve malfunction, ensuring the system defaults to a safe state. Discuss the importance of interlocks in industrial process safety and the role of overfill protection in preventing hazardous conditions.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Create a Structured Text (IEC 61131-3) program to implement an overfill protection interlock for a process vessel.

⸻

🟩 A (Action) – How to Do It
	1.	Monitor the vessel’s liquid level using a level sensor (LevelSensor).
	2.	Control the inlet valve (INLET_VALVE) to prevent overfilling by:
	•	Automatically closing the valve when the level exceeds a predefined high-level setpoint.
	•	Keeping the valve closed until the level falls below a defined reset threshold to prevent rapid cycling.
	3.	Implement fail-safe logic to handle faults:
	•	If the sensor fails or gives an invalid signal, the inlet valve must default to closed.
	•	If a valve malfunction is detected, the system must also force the valve to a safe state.
	4.	Use a latched shutdown condition, only resettable when safe levels are restored or through manual intervention.

⸻

🟦 G (Goal) – What You Want to Achieve

Deliver a reliable, self-contained overfill protection system that maintains safe operating levels, responds automatically to abnormal conditions, and ensures the valve fails safely in case of sensor or actuator issues. This enhances industrial process safety, reduces the risk of environmental or equipment damage, and supports regulatory compliance.

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to monitor a vessel's liquid level, automatically close the inlet valve upon reaching a high-level setpoint, enforce fail-safe actions for sensor/valve faults, and maintain safety through latched shutdowns until manual reset or safe conditions are restored.  

*(Focus: Overfill protection with fault handling and safety interlocks.)*
**Interlock Overfill Protection:**

Develop a self-contained IEC 61131-3 Structured Text program to implement an interlock system for overfill protection of a vessel. The program should utilize a level sensor to monitor the liquid level in the vessel and control an inlet valve to prevent overfilling.

The logic should ensure that the inlet valve automatically closes when the level sensor detects that the liquid has reached a predefined high-level setpoint. The interlock should remain engaged until the level drops below a safe threshold. Additionally, include a fail-safe mechanism to handle sensor failure or valve malfunction, ensuring the system defaults to a safe state. Discuss the importance of interlocks in industrial process safety and the role of overfill protection in preventing hazardous conditions.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Create a Structured Text (IEC 61131-3) program to implement an overfill protection interlock for a process vessel.

⸻

🟩 A (Action) – How to Do It
	1.	Monitor the vessel’s liquid level using a level sensor (LevelSensor).
	2.	Control the inlet valve (INLET_VALVE) to prevent overfilling by:
	•	Automatically closing the valve when the level exceeds a predefined high-level setpoint.
	•	Keeping the valve closed until the level falls below a defined reset threshold to prevent rapid cycling.
	3.	Implement fail-safe logic to handle faults:
	•	If the sensor fails or gives an invalid signal, the inlet valve must default to closed.
	•	If a valve malfunction is detected, the system must also force the valve to a safe state.
	4.	Use a latched shutdown condition, only resettable when safe levels are restored or through manual intervention.

⸻

🟦 G (Goal) – What You Want to Achieve

Deliver a reliable, self-contained overfill protection system that maintains safe operating levels, responds automatically to abnormal conditions, and ensures the valve fails safely in case of sensor or actuator issues. This enhances industrial process safety, reduces the risk of environmental or equipment damage, and supports regulatory compliance.  

**B-A-B:**

Before

In many industrial processes, overfilling a vessel can lead to dangerous spills, equipment damage, or environmental hazards. Without proper protection, sensor failures or valve malfunctions can result in uncontrolled liquid levels, making it difficult to respond quickly.

After

Develop a self-contained IEC 61131-3 Structured Text program that monitors the liquid level in a vessel using a level sensor. The program should automatically close an inlet valve when the level exceeds a high-level setpoint and remain closed until the level drops below a safe threshold. Additionally, include logic to handle sensor or valve failures, ensuring the system defaults to a safe state. Discuss the importance of overfill protection in industrial safety and the role of interlocks in preventing hazardous conditions.

**R-I-S-E:**

Role

You are a PLC programmer or automation engineer responsible for implementing safety interlocks in industrial processes.

Input

You are tasked with developing a self-contained program to monitor the liquid level in a vessel and ensure that the inlet valve automatically closes when the level exceeds a high-level setpoint. The system must also handle sensor and valve failures to ensure safe operation.

Output

Develop a Structured Text program (IEC 61131-3) that:
	•	Uses a level sensor to monitor the liquid level in the vessel
	•	Automatically closes the inlet valve when the level exceeds a high-level setpoint
	•	Remains in the closed position until the level drops below a safe threshold
	•	Includes logic to handle sensor and valve failures, ensuring the system defaults to a safe state
	•	Ensures that the interlock is latched and requires manual reset to reopen the valve
	•	Includes detailed comments explaining the logic and safety features

R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC programmer or automation engineer responsible for implementing safety interlocks in industrial processes.

⸻

🟩 I (Input) – What You’re Given

You are tasked with developing a self-contained program to monitor the liquid level in a vessel and ensure that the inlet valve automatically closes when the level exceeds a high-level setpoint. The system must also handle sensor and valve failures to ensure safe operation.

⸻

🟦 S (Steps) – How to Do It

	1.	Define the high-level setpoint and safe threshold for the liquid level in the vessel.
	2.	Implement logic to monitor the level

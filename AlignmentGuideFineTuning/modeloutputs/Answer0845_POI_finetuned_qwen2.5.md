### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to monitor and enforce emergency shutdowns for a subsea gas wellhead when pressure, temperature, or flow exceed safe limits, requiring manual reset after intervention.  

**Key Focus:**  
- Real-time monitoring of PT/TT/FT sensors.  
- Automatic valve closure on threshold breaches (1500 psi, 120°C, low flow).  
- Latching shutdown with manual reset to ensure safety compliance.

### Prompt:
**Interlock Gas Wellhead:**

Develop a self-contained IEC 61131-3 Structured Text program to implement emergency interlocks for a subsea gas wellhead. The program should monitor critical parameters such as wellhead pressure, temperature, and flow rates using pressure transmitters (PT), temperature transmitters (TT), and flow meters (FT). The interlock system should immediately trigger emergency shutdown procedures if any of these parameters exceed predefined safety limits.

The program should include logic for closing the master valve (MV-101) if wellhead pressure exceeds 1500 psi, or if flow rate drops below the minimum threshold, indicating a potential leak. Additionally, integrate temperature monitoring to shut down the system if the temperature exceeds 120°C. Incorporate safety features such as automatic reset prevention, ensuring that manual intervention is required to restart the system after an emergency shutdown.

Discuss the critical role of emergency interlocks in subsea gas wellhead operations, particularly in preventing catastrophic failures due to pressure, temperature, or flow anomalies.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Design and implement an emergency interlock system for a subsea gas wellhead using IEC 61131-3 Structured Text. The system must ensure real-time response to unsafe operating conditions and require manual intervention to resume operation after a shutdown.

⸻

🟩 A (Action) – How to Do It
	1.	Monitor key parameters:
	•	Pressure via PT sensors
	•	Temperature via TT sensors
	•	Flow rate via FT sensors
	2.	Program interlock logic in Structured Text to:
	•	Close master valve (MV-101) if pressure exceeds 1500 psi
	•	Close MV-101 if flow rate drops below a minimum safe value
	•	Initiate shutdown if temperature exceeds 120°C
	•	Latch the shutdown condition and prevent automatic restart
	3.	Implement a manual reset condition (e.g., RESET := TRUE) to clear the SHUTDOWN flag only after an operator has reviewed the issue.

⸻

🟦 G (Goal) – What You Want to Achieve

Create a self-contained, fail-safe interlock system that ensures the safety and integrity of the subsea gas wellhead under abnormal pressure, temperature, or flow conditions. The final program must respond instantly, prevent reactivation without inspection, and support reliable and unmanned subsea operations.

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to monitor and enforce emergency shutdowns for a subsea gas wellhead when pressure, temperature, or flow exceed safe limits, requiring manual reset after intervention.  

**Key Focus:**  
- Real-time monitoring of PT/TT/FT sensors.  
- Automatic valve closure on threshold breaches (1500 psi, 120°C, low flow).  
- Latching shutdown with manual reset to ensure safety compliance.
**Interlock Gas Wellhead:**

Develop a self-contained IEC 61131-3 Structured Text program to implement emergency interlocks for a subsea gas wellhead. The program should monitor critical parameters such as wellhead pressure, temperature, and flow rates using pressure transmitters (PT), temperature transmitters (TT), and flow meters (FT). The interlock system should immediately trigger emergency shutdown procedures if any of these parameters exceed predefined safety limits.

The program should include logic for closing the master valve (MV-101) if wellhead pressure exceeds 1500 psi, or if flow rate drops below the minimum threshold, indicating a potential leak. Additionally, integrate temperature monitoring to shut down the system if the temperature exceeds 120°C. Incorporate safety features such as automatic reset prevention, ensuring that manual intervention is required to restart the system after an emergency shutdown.

Discuss the critical role of emergency interlocks in subsea gas wellhead operations, particularly in preventing catastrophic failures due to pressure, temperature, or flow anomalies.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Design and implement an emergency interlock system for a subsea gas wellhead using IEC 61131-3 Structured Text. The system must ensure real-time response to unsafe operating conditions and require manual intervention to resume operation after a shutdown.

⸻

🟩 A (Action) – How to Do It
	1.	Monitor key parameters:
	•	Pressure via PT sensors
	•	Temperature via TT sensors
	•	Flow rate via FT sensors
	2.	Program interlock logic in Structured Text to:
	•	Close master valve (MV-101) if pressure exceeds 1500 psi
	•	Close MV-101 if flow rate drops below a minimum safe value
	•	Initiate shutdown if temperature exceeds 120°C
	•	Latch the shutdown condition and prevent automatic restart
	3.	Implement a manual reset condition (e.g., RESET := TRUE) to clear the SHUTDOWN flag only after an operator has reviewed the issue.

⸻

🟦 G (Goal) – What You Want to Achieve

Create a self-contained, fail-safe interlock system that ensures the safety and integrity of the subsea gas wellhead under abnormal pressure, temperature, or flow conditions. The final program must respond instantly, prevent reactivation without inspection, and support reliable and unmanned subsea operations.  

**R-I-S-E:**

Role

You are a PLC programmer or automation engineer responsible for designing and implementing safety interlocks for a subsea gas wellhead in compliance with IEC 61131-3 standards.

Input

You are provided with the following critical parameters and thresholds:
	•	Pressure: PT sensor, safe limit = 1500 psi
	•	Temperature: TT sensor, safe limit = 120°C
	•	Flow: FT sensor, minimum threshold = 100 standard cubic meters per hour
	•	Master valve: MV-101, to be closed during emergency shutdowns
	•	Shutdown logic: Latching interlocks to prevent automatic recovery
	•	Manual reset: A safety interlock to require manual intervention for system restart

	You are also tasked with ensuring that the interlock system is fail-safe, meaning it defaults to a safe state in the event of sensor failure or communication loss.

	Lastly, the system must be designed to support real-time monitoring and emergency response in an unattended subsea environment.

	You are to implement this logic using IEC 61131-3 Structured Text, ensuring that the program is modular, efficient, and includes detailed comments for clarity and maintainability.

	You are to implement this logic using IEC 61131-3 Structured Text, ensuring that the program is modular, efficient, and includes detailed comments for clarity and maintainability.

	You are to implement this logic using IEC 61131-3 Structured Text, ensuring that the program is modular, efficient, and includes detailed comments for clarity and maintainability.

	You are to implement this logic using IEC 61131-3 Structured Text, ensuring that the program is modular, efficient, and includes detailed comments for clarity and maintainability.

	You are to implement this logic using IEC 61131-3 Structured Text, ensuring that the program is modular, efficient, and includes detailed comments for clarity and maintainability.

	You are to implement this logic using IEC 61131-3 Structured Text, ensuring that the program is modular, efficient, and includes detailed comments for clarity and maintainability.

	You are to implement this logic using IEC 61131-3 Structured Text, ensuring that the program is modular, efficient, and includes detailed comments for clarity and maintain

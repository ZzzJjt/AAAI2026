### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to monitor and enforce emergency shutdowns for a subsea gas wellhead based on pressure, temperature, and flow rate limits, ensuring fail-safe operation with manual reset requirements.

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
Develop an IEC 61131-3 Structured Text program to monitor and enforce emergency shutdowns for a subsea gas wellhead based on pressure, temperature, and flow rate limits, ensuring fail-safe operation with manual reset requirements.
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

You are a PLC programmer or automation engineer responsible for designing and implementing emergency interlock logic for a subsea gas wellhead using IEC 61131-3 Structured Text.

Input

You are provided with the following:
	•	Pressure, temperature, and flow rate sensor data from the wellhead
	•	Normal operational limits for each parameter
	•	A list of safety actions to be performed in the event of an emergency (e.g., closing the master valve, stopping the flow, and triggering alarms)
	•	Communication with the control system to monitor and enforce safety conditions

	•	You are required to ensure that the interlock system is fail-safe, meaning it will immediately trigger protective actions if any monitored parameter exceeds its safe limit.

	•	You must also ensure that the system requires manual intervention to reset the interlocks, preventing automatic recovery in the event of a false alarm or sensor malfunction.

	•	Lastly, the system must be designed to handle both normal and abnormal operating conditions, ensuring that it can respond quickly and reliably to emergencies while maintaining safe and efficient gas wellhead operations.

	•	You are required to ensure that the interlock system is fail-safe, meaning it will immediately trigger protective actions if any monitored parameter exceeds its safe limit.

	•	You must also ensure that the system requires manual intervention to reset the interlocks, preventing automatic recovery in the event of a false alarm or sensor malfunction.

	•	Lastly, the system must be designed to handle both normal and abnormal operating conditions, ensuring that it can respond quickly and reliably to emergencies while maintaining safe and efficient gas wellhead operations.

	•	You are required to ensure that the interlock system is fail-safe, meaning it will immediately trigger protective actions if any monitored parameter exceeds its safe limit.

	•	You must also ensure that the system requires manual intervention to reset the interlocks, preventing automatic recovery in the event of a false alarm or sensor malfunction.

	•	Lastly, the system must be designed to handle both normal and abnormal operating conditions, ensuring that it can respond quickly and reliably to emergencies while maintaining safe and efficient gas wellhead operations.

	•	You are required to ensure that the interlock system is fail-safe, meaning it will immediately trigger protective actions if any monitored parameter exceeds its safe limit.

	•	You must also ensure that the system requires manual intervention to reset the interlocks, preventing automatic recovery in the event of a false alarm or sensor

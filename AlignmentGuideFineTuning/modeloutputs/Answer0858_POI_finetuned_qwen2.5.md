### Intent:
**Intent Summary:**  
Develop a pressure relief interlock system for a prilling station handling ammonium nitrate, ensuring automatic valve activation, process shutdown, and alarms if pressure exceeds 15 bar, with fail-safe defaults and manual reset only under safe conditions.  

*(Focus: Safety-critical pressure control with validation, latching, and compliance)*

### Prompt:
**Interlock Prilling Station:**

Develop a complete list of interlocks required for a prilling station handling ammonium nitrates. The interlocks should cover critical safety and operational aspects to ensure the safe and efficient operation of the prilling process. Discuss the importance of implementing these interlocks in ammonium nitrate production for both safety and compliance with regulatory standards.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Create a comprehensive list of interlocks for a prilling station that processes ammonium nitrate, focusing on ensuring safe and compliant operation of the facility.

⸻

🟩 A (Action) – How to Do It
	1.	Identify critical safety and operational risks in the prilling process—such as overheating, overpressure, mechanical failure, and ventilation loss.
	2.	For each identified risk, define an interlock that includes:
	•	The monitored condition (e.g., temperature, pressure, air flow, feed rate)
	•	A specific trigger threshold (e.g., temperature > 180 °C, airflow < minimum safe value)
	•	The corresponding automated response (e.g., shut down feed system, activate emergency vent, sound alarm)
	3.	Include a mix of automated and manual interlocks, including Emergency Stop (E-Stop).
	4.	Ensure each interlock is designed to default to a safe state and is clearly documented for implementation and audit.

⸻

🟦 G (Goal) – What You Want to Achieve

Deliver a complete safety interlock plan for the prilling station that provides real-time protection against hazardous conditions, supports regulatory compliance, and enhances the overall reliability and safety of ammonium nitrate production operations.

### Generated Code:
**Intent Summary:**  
Develop a pressure relief interlock system for a prilling station handling ammonium nitrate, ensuring automatic valve activation, process shutdown, and alarms if pressure exceeds 15 bar, with fail-safe defaults and manual reset only under safe conditions.  

*(Focus: Safety-critical pressure control with validation, latching, and compliance)*
**Interlock Prilling Station:**

Develop a complete list of interlocks required for a prilling station handling ammonium nitrates. The interlocks should cover critical safety and operational aspects to ensure the safe and efficient operation of the prilling process. Discuss the importance of implementing these interlocks in ammonium nitrate production for both safety and compliance with regulatory standards.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Create a comprehensive list of interlocks for a prilling station that processes ammonium nitrate, focusing on ensuring safe and compliant operation of the facility.

⸻

🟩 A (Action) – How to Do It
	1.	Identify critical safety and operational risks in the prilling process—such as overheating, overpressure, mechanical failure, and ventilation loss.
	2.	For each identified risk, define an interlock that includes:
	•	The monitored condition (e.g., temperature, pressure, air flow, feed rate)
	•	A specific trigger threshold (e.g., temperature > 180 °C, airflow < minimum safe value)
	•	The corresponding automated response (e.g., shut down feed system, activate emergency vent, sound alarm)
	3.	Include a mix of automated and manual interlocks, including Emergency Stop (E-Stop).
	4.	Ensure each interlock is designed to default to a safe state and is clearly documented for implementation and audit.

⸻

🟦 G (Goal) – What You Want to Achieve

Deliver a complete safety interlock plan for the prilling station that provides real-time protection against hazardous conditions, supports regulatory compliance, and enhances the overall reliability and safety of ammonium nitrate production operations.  

**Interlock Prilling Station:**

Develop a complete list of interlocks required for a prilling station handling ammonium nitrates. The interlocks should cover critical safety and operational aspects to ensure the safe and efficient operation of the prilling process.

	•	Overheating Interlock: Shutdown the prilling process if the temperature exceeds a predefined limit (e.g., 180 °C) to prevent thermal runaway and material degradation.
	•	Overpressure Interlock: Open a pressure relief valve if the pressure in the prilling vessel exceeds a safe threshold (e.g., 15 bar) to prevent vessel failure and ensure safe pressure levels.
	•	Mechanical Interlock: Trigger an emergency stop if a critical component (e.g., prilling drum) fails or malfunctions, ensuring the system defaults to a safe state.
	•	Feed Control Interlock: Stop the material feed if the prilling process is not running or if the material flow rate drops below a minimum threshold to prevent overloading the system.
	•	Airflow Interlock: Open a safety valve if the airflow in the prilling area falls below a minimum level, indicating a ventilation failure that could lead to hazardous conditions.
	•	Overfill Interlock: Trigger an alarm and prevent further material addition if the prilling vessel exceeds its maximum fill level, ensuring safe operation and preventing overflow.
	•	Manual Override Interlock: Implement a fail-safe mechanism that defaults to a safe state (e.g., shutdown) if manual control is lost or if the system detects an unsafe condition, ensuring the prilling process remains under control.
	•	Communication Interlock: Trigger an alarm if communication with critical sensors or control systems is lost, indicating a potential failure in the monitoring and control system.
	•	Overheating Interlock: Shutdown the prilling process if the temperature exceeds a predefined limit (e.g., 180 °C) to prevent thermal runaway and material degradation.
	•	Overpressure Interlock: Open a pressure relief valve if the pressure in the prilling vessel exceeds a safe threshold (e.g., 15 bar) to prevent vessel failure and ensure safe pressure levels.
	•	Mechanical Interlock: Trigger an emergency stop if a critical component (e.g., prilling drum) fails or malfunctions, ensuring the system defaults to a safe state.
	•	Feed Control Interlock: Stop the material feed if the prilling process is not running or if the material flow

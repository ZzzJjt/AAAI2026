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

---

**Pressure Relief Interlock System:**

Design a pressure relief interlock system for the prilling station that automatically activates valves, shuts down the process, and sounds alarms when the pressure exceeds 15 bar. The system should also include fail-safe defaults and manual reset only under safe conditions.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Design a pressure relief interlock system for the prilling station that ensures safe and efficient operation by automatically responding to overpressure conditions.

⸻

🟩 A (Action) – How to Do It
	1.	Identify the pressure sensors and valves required for the system.
	2.	Define the pressure threshold (15 bar) at which the system should activate.
	3.	Design the logic for the interlock system:
	•	When pressure exceeds 15 bar, the system should automatically activate the pressure relief valve(s) to reduce pressure.
	•	The system should also shut down the prilling process and sound an alarm.
	4.	Ensure the system defaults to a safe state (e.g., valves closed, process off) in case of power failure or other malfunctions.
	5.	Implement a manual reset mechanism that can only be activated under safe conditions (e.g., pressure below 15 bar, process shut down).
	6.	Document the system design, including wiring diagrams, flowcharts, and safety protocols, for implementation and audit.

⸻

🟦 G (Goal) – What You Want to Achieve

Develop a pressure relief interlock system that provides automatic protection against overpressure conditions, ensures safe and efficient operation of the prilling station, and meets regulatory requirements for ammonium nitrate production facilities.

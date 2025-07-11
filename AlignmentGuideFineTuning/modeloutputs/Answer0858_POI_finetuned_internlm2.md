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

**▸▸▸ INTERLOCK LIST ◁◁◁**

**Interlock 1: Overpressure Protection**

•	Condition: Pressure in the prilling chamber
•	Trigger: Pressure exceeds 15 bar
•	Response: Automatically open pressure relief valve to reduce pressure to safe levels
•	Default: Pressure relief valve remains open until pressure drops below 15 bar
•	Manual Reset: Only possible when pressure is below 15 bar and all other interlocks are in a safe state

**Interlock 2: Overheating Protection**

•	Condition: Temperature in the prilling chamber
•	Trigger: Temperature exceeds 180°C
•	Response: Automatically shut down the prilling process and activate emergency cooling
•	Default: Process remains shut down until temperature drops below 180°C
•	Manual Reset: Only possible when temperature is below 180°C and all other interlocks are in a safe state

**Interlock 3: Mechanical Failure Protection**

•	Condition: Failure of critical equipment (e.g., pump, agitator)
•	Trigger: Equipment failure detected
•	Response: Automatically shut down the prilling process and activate emergency backup systems
•	Default: Process remains shut down until the failed equipment is repaired or replaced
•	Manual Reset: Not applicable, as the interlock is designed to prevent manual reset until the equipment is operational

**Interlock 4: Ventilation Loss Protection**

•	Condition: Loss of ventilation in the prilling chamber
•	Trigger: Ventilation levels fall below safe limits
•	Response: Automatically shut down the prilling process and activate emergency ventilation
•	Default: Process remains shut down until ventilation levels return to safe levels
•	Manual Reset: Only possible when ventilation levels are within safe limits and all other interlocks are in a safe state

**Interlock 5: Emergency Stop (E-Stop)**

•	Condition: Emergency stop signal
•	Trigger: E-Stop button pressed or signal received
•	Response: Immediately shut down all prilling processes and activate emergency safety measures
•	Default: Process remains shut down until the E-Stop signal is released
•	Manual Reset: Not applicable, as the E-Stop interlock is designed to prevent manual reset until the emergency situation is resolved

**▸▸▸ CONCLUSION ◁

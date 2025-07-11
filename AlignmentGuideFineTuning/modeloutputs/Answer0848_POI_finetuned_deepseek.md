### Intent:
**Intent Summary:**  
Generate a cause-and-action matrix for a chemical reactor's interlock system, mapping hazardous conditions (e.g., overpressure, sensor failures) to predefined safety responses (e.g., valve shutdowns, alarms) to ensure traceability, regulatory compliance, and robust fault mitigation.  

*(Focus: Structured safety logic design for automated process control.)*

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
Generate a cause-and-action matrix for a chemical reactor's interlock system, mapping hazardous conditions (e.g., overpressure, sensor failures) to predefined safety responses (e.g., valve shutdowns, alarms) to ensure traceability, regulatory compliance, and robust fault mitigation.  

*(Focus: Structured safety logic design for automated process control.)*
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
Ammonium Nitrate Prilling Station Interlocks

### 1. Overpressure Interlock

**Interlock:**
- Condition: Pressure > 10 bar
- Trigger Threshold: Pressure > 10 bar
- Response:
  - Emergency venting
  - Stop feed system
  - Activate pressure relief valve
  - Sound alarm
- Manual Override: No
- Documentation: Yes

### 2. Overheating Interlock

**Interlock:**
- Condition: Temperature > 180°C
- Trigger Threshold: Temperature > 180°C
- Response:
  - Stop feed system
  - Activate cooling system
  - Sound alarm
  - Activate emergency stop (E-Stop)
- Manual Override: No
- Documentation: Yes

### 3. Low Airflow Interlock

**Interlock:**
- Condition: Airflow < 1000 m³/h
- Trigger Threshold: Airflow < 1000 m³/h
- Response:
  - Stop feed system
  - Activate emergency vent
  - Sound alarm
  - Activate emergency stop (E-Stop)
- Manual Override: No
- Documentation: Yes

### 4. Feed Rate Interlock

**Interlock:**
- Condition: Feed Rate > 100 kg/min
- Trigger Threshold: Feed Rate > 100 kg/min
- Response:
  - Stop feed system
  - Activate emergency vent
  - Sound alarm
  - Activate emergency stop (E-Stop)
- Manual Override: No
- Documentation: Yes

### 5. Emergency Stop (E-Stop)

**Interlock:**
- Condition: Manual Override
- Trigger Threshold: Manual Override
- Response:
  - Stop all systems
  - Activate emergency vent
  - Sound alarm
  - Activate emergency stop (E-Stop)
- Manual Override: Yes
- Documentation: Yes

### 6. Ventilation Interlock

**Interlock:**
- Condition: Ventilation Failure
- Trigger Threshold: Ventilation Failure
- Response:
  - Activate emergency vent
  - Sound alarm
  - Activate emergency stop (E-Stop)
- Manual Override: No
- Documentation: Yes

### 7.

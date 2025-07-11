### Intent:
**Intent Summary:**  
Design a set of safety interlocks for an ammonium nitrate prilling station to automatically detect and respond to critical faults (e.g., overpressure, sensor failures) by triggering shutdowns or relief actions, ensuring compliance with safety standards and preventing hazardous incidents.  

*(Focus: Safety interlock logic for high-risk chemical handling, prioritizing automated fault detection and mitigation.)*

### Prompt:
**Interlock Prilling Station:**

Develop a complete list of interlocks required for a prilling station handling ammonium nitrates. The interlocks should cover critical safety and operational aspects to ensure the safe and efficient operation of the prilling process. Discuss the importance of implementing these interlocks in ammonium nitrate production for both safety and compliance with regulatory standards.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a process safety or automation engineer responsible for designing interlock protection systems for a prilling station handling ammonium nitrate, ensuring operational safety and regulatory compliance.

⸻

🟩 I (Input) – What You’re Given

You are to develop a complete list of interlocks for a prilling station. The system processes molten ammonium nitrate, a highly energetic compound that requires tight control of pressure, temperature, and material flow. Your interlocks should address:
	•	Overtemperature
	•	Overpressure
	•	Cooling air flow failure
	•	Melt pump/feed failure
	•	Product accumulation
	•	Scrubber/emission failure
	•	Inert gas supply loss (if applicable)
	•	Emergency stop conditions

Each interlock should have a clearly defined trigger condition and response action (e.g., shut down equipment, open relief, stop melt feed).

⸻

🟧 S (Steps) – What You Need to Do
	1.	Identify critical risks in prilling station operations, focusing on temperature, pressure, emissions, and flow control.
	2.	Define interlock conditions:
	•	For each fault scenario (e.g., high temperature > limit), specify the sensor input and setpoint
	•	Define the automated response (e.g., shutdown prill tower, close feed valve, activate emergency venting)
	3.	List at least 8–10 interlocks, including both automatic and manual (E-stop) options
	4.	Document the interlocks for use in programming logic and safety audits
	5.	Optionally, implement the logic using IEC 61131-3 code or draw a cause-and-effect matrix

⸻

🟦 E (Expectation) – What Success Looks Like

You deliver a well-structured interlock system that:
	•	Automatically protects the process during unsafe or abnormal conditions
	•	Minimizes explosion or release risks
	•	Supports compliance with ammonium nitrate handling standards (e.g., OSHA, ATEX, NFPA)
	•	Enhances operator safety and system reliability

The result is a comprehensive, practical safety layer embedded into the prilling station’s automation system.

### Generated Code:
**Intent Summary:**  
Design a set of safety interlocks for an ammonium nitrate prilling station to automatically detect and respond to critical faults (e.g., overpressure, sensor failures) by triggering shutdowns or relief actions, ensuring compliance with safety standards and preventing hazardous incidents.  

*(Focus: Safety interlock logic for high-risk chemical handling, prioritizing automated fault detection and mitigation.)*
**Interlock Prilling Station:**

Develop a complete list of interlocks required for a prilling station handling ammonium nitrates. The interlocks should cover critical safety and operational aspects to ensure the safe and efficient operation of the prilling process. Discuss the importance of implementing these interlocks in ammonium nitrate production for both safety and compliance with regulatory standards.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a process safety or automation engineer responsible for designing interlock protection systems for a prilling station handling ammonium nitrate, ensuring operational safety and regulatory compliance.

⸻

🟩 I (Input) – What You’re Given

You are to develop a complete list of interlocks for a prilling station. The system processes molten ammonium nitrate, a highly energetic compound that requires tight control of pressure, temperature, and material flow. Your interlocks should address:
	•	Overtemperature
	•	Overpressure
	•	Cooling air flow failure
	•	Melt pump/feed failure
	•	Product accumulation
	•	Scrubber/emission failure
	•	Inert gas supply loss (if applicable)
	•	Emergency stop conditions

Each interlock should have a clearly defined trigger condition and response action (e.g., shut down equipment, open relief, stop melt feed).

⸻

🟧 S (Steps) – What You Need to Do
	1.	Identify critical risks in prilling station operations, focusing on temperature, pressure, emissions, and flow control.
	2.	Define interlock conditions:
	•	For each fault scenario (e.g., high temperature > limit), specify the sensor input and setpoint
	•	Define the automated response (e.g., shutdown prill tower, close feed valve, activate emergency venting)
	3.	List at least 8–10 interlocks, including both automatic and manual (E-stop) options
	4.	Document the interlocks for use in programming logic and safety audits
	5.	Optionally, implement the logic using IEC 61131-3 code or draw a cause-and-effect matrix

⸻

🟦 E (Expectation) – What Success Looks Like

You deliver a well-structured interlock system that:
	•	Automatically protects the process during unsafe or abnormal conditions
	•	Minimizes explosion or release risks
	•	Supports compliance with ammonium nitrate handling standards (e.g., OSHA, ATEX, NFPA)
	•	Enhances operator safety and system reliability

The result is a comprehensive, practical safety layer embedded into the prilling station’s automation system. Your interlock design will be a critical component of the overall safety management system for the facility.

**Interlock Prilling Station:**

1. **Overtemperature Interlock:**
	- Trigger condition: Temperature sensor detects a temperature above the setpoint
	- Response action: Shutdown prill tower, stop melt feed, activate emergency cooling system
2. **Overpressure Interlock:**
	- Trigger condition: Pressure sensor detects a pressure above the setpoint
	- Response action: Shutdown prill tower, open relief valve, activate emergency venting system
3. **Cooling Air Flow Failure Interlock:**
	- Trigger condition: Flow sensor detects a cooling air flow below the setpoint
	- Response action: Shutdown prill tower, stop melt feed, activate emergency cooling system
4. **Melt Pump/Feed Failure Interlock:**
	- Trigger condition: Pump or feed failure detected
	- Response action: Shutdown prill tower, stop melt feed, activate emergency cooling system
5. **Product Accumulation Interlock:**
	- Trigger condition: Product level sensor detects a level above the setpoint
	- Response action: Shutdown prill tower, stop melt feed, activate emergency venting system
6. **Scrubber/Emission Failure Interlock:**
	- Trigger condition: Emission or scrubber failure detected
	- Response action: Shutdown prill tower, stop melt feed, activate emergency venting system
7. **Inert Gas Supply Loss Interlock:**
	- Trigger condition: Inert gas flow sensor detects a flow below the setpoint
	- Response action: Shutdown prill tower, stop melt feed, activate emergency cooling system
8. **Emergency Stop Interlock:**
	- Trigger condition: Manual emergency stop button pressed
	- Response action: Shutdown prill tower, stop melt feed, activate emergency venting system
9. **Fire Detection Interlock:**
	- Trigger condition: Fire detection system activated
	- Response action: Shutdown prill tower, stop melt feed, activate emergency venting system
10. **Power Failure Interlock:**
	- Trigger condition: Power failure detected
	- Response action: Shutdown prill tower, stop melt feed, activate emergency cooling system

**Interlock Prilling Station:**

The interlock system for the prilling station is a critical safety layer that ensures the safe and efficient operation of the process.

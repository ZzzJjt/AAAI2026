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

The result is a comprehensive, practical safety layer embedded into the prilling station’s automation system.
Ammonium Nitrate Prilling Station Interlocks

The ammonium nitrate prilling station is a critical process in the production of ammonium nitrate fertilizers. The process involves melting ammonium nitrate in a furnace, and then prilling it into small pellets for further processing. The process is highly hazardous due to the explosive nature of ammonium nitrate, and requires strict safety measures to prevent accidents.

To ensure the safe and efficient operation of the prilling station, a set of interlocks is required to monitor and control key parameters such as temperature, pressure, and material flow. The interlocks should be designed to detect and respond to critical faults, and should be capable of triggering shutdowns or relief actions in the event of an emergency.

List of Interlocks

1. Overpressure Interlock

The overpressure interlock is designed to detect when the pressure in the prilling tower exceeds the set limit. If the pressure exceeds the limit, the interlock will trigger a shutdown of the melt pump and feed valve, and open the emergency venting system to relieve the pressure.

2. Overtemperature Interlock

The overtemperature interlock is designed to detect when the temperature in the prilling tower exceeds the set limit. If the temperature exceeds the limit, the interlock will trigger a shutdown of the melt pump and feed valve, and open the emergency cooling system to reduce the temperature.

3. Cooling Air Flow Interlock

The cooling air flow interlock is designed to detect when the cooling air flow to the prilling tower is below the set limit. If the cooling air flow is below the limit, the interlock will trigger a shutdown of the melt pump and feed valve, and open the emergency venting system to relieve the pressure.

4. Melt Pump/Feed Failure Interlock

The melt pump/feed failure interlock is designed to detect when the melt pump or feed valve fails. If the pump or valve fails, the interlock will trigger a shutdown of the melt pump and feed valve, and open the emergency venting system to relieve the pressure.

5. Product Accumulation Interlock

The product accumulation interlock is designed to detect when the prilling tower becomes overfilled. If the tower becomes overfilled, the interlock will trigger a shutdown of the melt pump and feed valve, and open the emergency venting system to relieve the pressure.

6. Scrubber/Emission Failure Interlock

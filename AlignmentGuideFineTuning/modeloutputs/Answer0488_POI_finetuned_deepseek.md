### Intent:
**Intent Summary:**  
Design a set of safety interlocks for an ammonium nitrate prilling station to automatically mitigate hazards (e.g., overpressure, temperature deviations) by triggering predefined shutdowns, alarms, or corrective actions, ensuring compliance with safety standards.  

*(Focus: Automated hazard response via interlocks in a high-risk process.)*

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
Design a set of safety interlocks for an ammonium nitrate prilling station to automatically mitigate hazards (e.g., overpressure, temperature deviations) by triggering predefined shutdowns, alarms, or corrective actions, ensuring compliance with safety standards.  

*(Focus: Automated hazard response via interlocks in a high-risk process.)*
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

The ammonium nitrate prilling station is a critical process in the production of fertilizers and explosives. It involves melting ammonium nitrate in a furnace, agitating it to form prills, and cooling the prills before packaging. The process is highly hazardous due to the explosive nature of the material and the potential for overpressure, overheating, and material spills. To ensure the safe and efficient operation of the prilling station, a set of interlocks is required to monitor and control critical parameters.

List of Interlocks

1. Overpressure Interlock

The overpressure interlock is triggered when the pressure in the furnace exceeds the maximum allowable pressure. The interlock shuts down the furnace and opens the relief valve to vent excess pressure.

2. Overtemperature Interlock

The overtemperature interlock is activated when the temperature in the furnace exceeds the maximum allowable temperature. The interlock shuts down the furnace and opens the cooling water valve to reduce the temperature.

3. Cooling Air Flow Interlock

The cooling air flow interlock is activated when the cooling air flow rate falls below the minimum required flow rate. The interlock shuts down the furnace and opens the emergency vent to vent the furnace.

4. Melt Pump Failure Interlock

The melt pump failure interlock is activated when the melt pump fails to pump molten ammonium nitrate. The interlock shuts down the furnace and opens the emergency vent to vent the furnace.

5. Feed Valve Failure Interlock

The feed valve failure interlock is activated when the feed valve fails to open or close. The interlock shuts down the furnace and opens the emergency vent to vent the furnace.

6. Product Accumulation Interlock

The product accumulation interlock is activated when the product accumulates in the furnace. The interlock shuts down the furnace and opens the emergency vent to vent the furnace.

7. Scrubber/Emission Failure Interlock

The scrubber/emission failure interlock is activated when the scrubber or emission system fails to operate. The interlock shuts down the furnace and opens the emergency vent to vent the furnace.

8. Inert Gas Supply Loss Interlock

The inert gas supply loss interlock is activated when the inert gas supply fails. The interlock shuts down the furnace and opens the emergency vent to vent the furnace.

9. Emergency Stop Interlock

### Intent:
**Intent Summary:**  
Design a safety interlock system for an ammonium nitrate prilling station that automatically triggers shutdowns and protective actions based on critical process parameters (temperature, pressure, flow) to prevent hazards and ensure regulatory compliance.  

*(Focus: Safety automation, fault detection, and emergency response for explosive material handling.)*

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
Design a safety interlock system for an ammonium nitrate prilling station that automatically triggers shutdowns and protective actions based on critical process parameters (temperature, pressure, flow) to prevent hazards and ensure regulatory compliance.  

*(Focus: Safety automation, fault detection, and emergency response for explosive material handling.)*
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

The ammonium nitrate prilling station is a critical process in the production of ammonium nitrate fertilizers. The process involves melting ammonium nitrate in a furnace, and then prilling it into small pellets for further processing. The process is highly sensitive to temperature, pressure, and flow conditions, and any deviation from the safe operating limits can lead to catastrophic consequences.

To ensure the safe and efficient operation of the prilling station, a comprehensive interlock system is required to monitor and control critical process parameters. The interlocks should cover both safety and operational aspects, and should be designed to comply with relevant safety and regulatory standards.

List of Interlocks

1. Overtemperature Interlock

The system should monitor the temperature of the molten ammonium nitrate and trigger an interlock if it exceeds the setpoint. The interlock should shut down the furnace and stop the melt feed, and open the emergency venting system to release excess pressure.

2. Overpressure Interlock

The system should monitor the pressure of the melt tank and trigger an interlock if it exceeds the setpoint. The interlock should shut down the melt feed and open the venting system to release excess pressure.

3. Cooling Air Flow Interlock

The system should monitor the flow of cooling air to the melt tank and trigger an interlock if it falls below the setpoint. The interlock should shut down the melt feed and open the venting system to release excess pressure.

4. Melt Pump/Feed Failure Interlock

The system should monitor the melt pump and feed valve and trigger an interlock if they fail. The interlock should shut down the melt feed and open the venting system to release excess pressure.

5. Product Accumulation Interlock

The system should monitor the melt tank level and trigger an interlock if it reaches the setpoint. The interlock should shut down the melt feed and open the venting system to release excess pressure.

6. Scrubber/Emission Failure Interlock

The system should monitor the scrubber and emission system and trigger an interlock if they fail. The interlock should shut down the melt feed and open the venting system to release excess pressure.

7. Inert Gas Supply Loss Interlock

The system should monitor the inert gas supply and trigger an interlock if it fails. The interlock should

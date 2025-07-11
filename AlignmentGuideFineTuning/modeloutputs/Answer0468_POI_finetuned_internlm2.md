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

The result is a comprehensive, practical safety layer embedded into the prilling station’s automation system. Your interlock design ensures that critical safety checks are in place to prevent accidents and maintain regulatory compliance.
**R-I-S-E:**

🟩 I (Input) – What You’re Given

You are a process safety engineer responsible for designing interlock protection systems for a prilling station handling ammonium nitrate. The prilling process involves the cooling and solidification of molten ammonium nitrate into small pellets. The interlock system must ensure the safe operation of the prilling process by automatically shutting down the system in response to critical process parameters, such as temperature, pressure, and flow.

Your task is to develop a complete list of interlocks for the prilling station, including the following:

•	Overtemperature interlock: Trigger a shutdown if the temperature of the molten ammonium nitrate exceeds a specified limit.

•	Overpressure interlock: Stop the prilling process if the pressure in the system exceeds a safe operating limit.

•	Cooling air flow failure interlock: Automatically shut down the prilling process if the cooling air flow fails, preventing overheating and potential hazards.

•	Melt pump/feed failure interlock: Stop the prilling process if the melt pump or feed system fails, preventing overheating and potential hazards.

•	Product accumulation interlock: Automatically shut down the prilling process if the product accumulation in the system exceeds a safe limit, preventing overheating and potential hazards.

•	Scrubber/emission failure interlock: Stop the prilling process if the scrubber or emission control system fails, preventing the release of hazardous gases.

•	Inert gas supply loss interlock (if applicable): Automatically shut down the prilling process if the inert gas supply fails, preventing the release of hazardous gases.

•	Emergency stop conditions interlock: Stop the prilling process in response to manual emergency stop signals or other critical safety conditions.

For each interlock, provide a clear description of the trigger condition and the automated response, including any safety-critical actions taken by the system.

**R-I-S-E:**

🟩 I (Input) – What You’re Given

You are a process safety engineer responsible for designing interlock protection systems for a prilling station handling ammonium nitrate. The prilling process involves the cooling and solidification of molten ammonium nitrate into small pellets. The interlock system must ensure the safe operation of the prilling process by automatically

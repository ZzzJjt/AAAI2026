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

The result is a comprehensive, practical safety layer embedded into the prilling station’s automation system. To design a comprehensive interlock system for a prilling station handling ammonium nitrate, we need to consider the critical risks associated with the process and develop interlocks that address these risks. Here's a detailed list of interlocks, including their trigger conditions and response actions:

### Interlock List

#### 1. **Overtemperature Interlock**
- **Trigger Condition:** Temperature exceeds a set limit (e.g., 150°C).
- **Response Action:** 
  - Close the feed valve to the prill tower.
  - Activate the emergency venting system.
  - Stop the melt pump.
  - Alert operators via alarms and display messages.

#### 2. **Overpressure Interlock**
- **Trigger Condition:** Pressure exceeds a set limit (e.g., 10 bar).
- **Response Action:** 
  - Open the relief valve to vent excess pressure.
  - Close the feed valve to the prill tower.
  - Stop the melt pump.
  - Alert operators via alarms and display messages.

#### 3. **Cooling Air Flow Failure Interlock**
- **Trigger Condition:** Cooling air flow drops below a set limit (e.g., 500 m³/h).
- **Response Action:** 
  - Close the feed valve to the prill tower.
  - Stop the melt pump.
  - Alert operators via alarms and display messages.

#### 4. **Melt Pump/Feed Failure Interlock**
- **Trigger Condition:** Melt pump stops or feed flow drops below a set limit (e.g., 100 kg/min).
- **Response Action:** 
  - Close the feed valve to the prill tower.
  - Stop the melt pump.
  - Alert operators via alarms and display messages.

#### 5. **Product Accumulation Interlock**
- **Trigger Condition:** Product level in the prill tower exceeds a set limit (e.g., 80% capacity).
- **Response Action:** 
  - Close the feed valve to the prill tower.
  - Stop the melt pump.
  - Alert operators via alarms and display messages.

#### 6. **Scrubber/Emission Failure Interlock**
- **Trigger Condition:** Scrubber efficiency drops below a set limit (e.g., 90%).
- **Response Action:** 
  - Close the feed valve to the prill tower.
  - Stop the melt pump.
  - Alert operators via alarms and display messages.

#### 7. **Inert Gas Supply Loss

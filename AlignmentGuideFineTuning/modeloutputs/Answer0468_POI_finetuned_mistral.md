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
FUNCTION_BLOCK FB_AmmoniumNitratePrillingInterlock
VAR_INPUT
    Execute : BOOL; // Trigger interlock evaluation on rising edge
    Temp_PT100 : REAL; // Prill tower temperature (°C)
    Pressure_PV : REAL; // Tower pressure (bar)
    Melt_Flow_PV : REAL; // Melt flow rate (kg/h)
    Cooling_Air_Flow_PV : REAL; // Cooling air flow (m³/h)
    Scrubber_Status : BOOL; // Scrubber status (ON/OFF)
    Inert_Gas_Supply : BOOL; // Inert gas supply (ON/OFF)
    Emergency_Stop : BOOL; // Manual emergency stop
END_VAR

VAR_OUTPUT
    Tower_Shutdown : BOOL; // Prill tower shutdown interlock
    Melt_Feed_Stop : BOOL; // Melt feed interlock
    Cooling_Air_Stop : BOOL; // Cooling air interlock
    Scrubber_Manual_Override : BOOL; // Scrubber manual override interlock
    Inert_Gas_Manual_Override : BOOL; // Inert gas manual override interlock
    Alarm_HighTemp : BOOL; // High temperature alarm
    Alarm_HighPressure : BOOL; // High pressure alarm
    Alarm_LowCoolingAir : BOOL; // Low cooling air alarm
    Alarm_MeltFlowLoss : BOOL; // Melt flow loss alarm
    Alarm_ScrubberFailure : BOOL; // Scrubber failure alarm
    Alarm_InertGasLoss : BOOL; // Inert gas loss alarm
    Alarm_EmergencyStop : BOOL; // Emergency stop alarm
END_VAR

VAR
    Temp_High_Limit : REAL := 180.0; // High temperature limit (°C)
    Pressure_High_Limit : REAL := 2.5; // High pressure limit (bar)
    Melt_Flow_Min_Limit : REAL := 95.0; // Melt flow minimum limit (kg/h)

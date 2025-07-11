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
FUNCTION_BLOCK FB_AmmoniumNitratePrillingStationInterlocks
VAR_INPUT
    Execute : BOOL; // Trigger interlock evaluation on rising edge
    CoolingAirFlow_PT100 : REAL; // Cooling air flow in m³/min
    MeltPumpPressure_PT100 : REAL; // Melt pump pressure in bar
    MeltPumpFlow_PT100 : REAL; // Melt flow rate in kg/min
    ScrubberEmission_PT100 : REAL; // Scrubber emission in ppm
    InertGasSupply_PT100 : REAL; // Inert gas supply in m³/min
    EmergencyStop : BOOL; // Manual emergency stop
END_VAR

VAR_OUTPUT
    PrillTowerShutdown : BOOL; // Shutdown prill tower
    MeltFeedStop : BOOL; // Stop melt feed
    ReliefValveOpen : BOOL; // Open relief valve
    ScrubberShutdown : BOOL; // Shutdown scrubber
    InertGasShutdown : BOOL; // Shutdown inert gas
    Alarm : BOOL; // Safety alarm
    LogEntry : STRING; // Log entry for interlock event
END_VAR

VAR
    MaxCoolingAirFlow : REAL := 1000.0; // Max cooling air flow in m³/min
    MaxMeltPumpPressure : REAL := 150.0; // Max melt pump pressure in bar
    MaxMeltPumpFlow : REAL := 1000.0; // Max melt flow rate in kg/min
    MaxScrubberEmission : REAL := 100.0; // Max scrubber emission in ppm
    MaxInertGasSupply : REAL := 1000.0; // Max inert gas supply in m³/min
    EmergencyStopActive : BOOL;
    Overpressure : BOOL;
    Overtemperature : BOOL;
    CoolingAirFlowFailure : BOOL;
    MeltPumpFailure : BOOL;
    ProductAccumulation : BOOL;
    Scrub

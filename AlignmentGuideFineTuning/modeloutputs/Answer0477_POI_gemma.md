### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to monitor a distillation column's pressure and temperature, triggering safety interlocks (pressure relief valve, feed valve closure, and reboiler shutdown) upon overpressure, underpressure, or overtemperature conditions, with fail-safe defaults for sensor/valve faults.

### Prompt:
**Interlock Pressure Relief:**

Develop a self-contained IEC 61131-3 Structured Text program to implement an interlock system for opening a pressure relief valve in a vessel upon detecting overpressure. The program should monitor the vessel pressure using a pressure sensor and trigger the opening of the relief valve when the pressure exceeds a predefined safe limit.

The logic should ensure that the pressure relief valve remains open until the vessel pressure drops below a safe threshold. Additionally, incorporate safety checks to account for sensor failures or valve malfunctions, ensuring that the system defaults to a safe state in the event of a fault. Discuss the significance of pressure relief systems in protecting industrial processes from overpressure hazards and ensuring operational safety.

**R-I-S-E:**

🟥 R (Role) – Your Role

Act as an industrial automation engineer responsible for implementing automated pressure relief interlock logic using IEC 61131-3 Structured Text to ensure safe operation of a pressurized vessel.

⸻

🟩 I (Input) – What You’re Given

You are tasked with developing a self-contained Structured Text program to protect a vessel from overpressure. The system must:
	•	Monitor pressure using a pressure transmitter (PT)
	•	Open a pressure relief valve when the pressure exceeds a defined high limit (e.g., 15 bar)
	•	Keep the valve open until the pressure drops below a reset threshold (e.g., 12 bar)
	•	Include fail-safe logic that activates the relief valve in case of:
	•	Sensor failure (e.g., invalid or stuck reading)
	•	Valve malfunction
	•	Ensure the system defaults to a safe state (valve open) when faults are detected

⸻

🟧 S (Steps) – What You Need to Do
	1.	Declare variables for the pressure sensor (PT_101), relief valve (RELIEF_VALVE), fault inputs (SensorFault, ValveFault), and latching logic (SHUTDOWN_LATCH).
	2.	Implement interlock logic that:
	•	Opens the relief valve when PT_101 > HIGH_LIMIT
	•	Maintains the open state until PT_101 < RESET_LIMIT
	•	Sets RELIEF_VALVE := TRUE if any fault condition is detected
	3.	Add latching and reset functionality to avoid premature valve closure.
	4.	Include comments and structure for readability, testing, and operational traceability.

⸻

🟦 E (Expectation) – What Success Looks Like

You produce a reliable, self-contained safety interlock that protects the vessel from overpressure. It reacts instantly to unsafe conditions, remains in a protective state until conditions stabilize, and automatically fails to a safe state during component faults. The interlock improves system safety, prevents equipment damage, and ensures compliance with industrial safety standards.

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to monitor a distillation column's pressure and temperature, triggering safety interlocks (pressure relief valve, feed valve closure, and reboiler shutdown) upon overpressure, underpressure, or overtemperature conditions, with fail-safe defaults for sensor/valve faults.
**Interlock Pressure Relief:**

Develop a self-contained IEC 61131-3 Structured Text program to implement an interlock system for opening a pressure relief valve in a vessel upon detecting overpressure. The program should monitor the vessel pressure using a pressure sensor and trigger the opening of the relief valve when the pressure exceeds a predefined safe limit.

The logic should ensure that the pressure relief valve remains open until the vessel pressure drops below a safe threshold. Additionally, incorporate safety checks to account for sensor failures or valve malfunctions, ensuring that the system defaults to a safe state in the event of a fault. Discuss the significance of pressure relief systems in protecting industrial processes from overpressure hazards and ensuring operational safety.

**R-I-S-E:**

🟥 R (Role) – Your Role

Act as an industrial automation engineer responsible for implementing automated pressure relief interlock logic using IEC 61131-3 Structured Text to ensure safe operation of a pressurized vessel.

⸻

🟩 I (Input) – What You’re Given

You are tasked with developing a self-contained Structured Text program to protect a vessel from overpressure. The system must:
	•	Monitor pressure using a pressure transmitter (PT)
	•	Open a pressure relief valve when the pressure exceeds a defined high limit (e.g., 15 bar)
	•	Keep the valve open until the pressure drops below a reset threshold (e.g., 12 bar)
	•	Include fail-safe logic that activates the relief valve in case of:
	•	Sensor failure (e.g., invalid or stuck reading)
	•	Valve malfunction
	•	Ensure the system defaults to a safe state (valve open) when faults are detected

⸻

🟧 S (Steps) – What You Need to Do
	1.	Declare variables for the pressure sensor (PT_101), relief valve (RELIEF_VALVE), fault inputs (SensorFault, ValveFault), and latching logic (SHUTDOWN_LATCH).
	2.	Implement interlock logic that:
	•	Opens the relief valve when PT_101 > HIGH_LIMIT
	•	Maintains the open state until PT_101 < RESET_LIMIT
	•	Sets RELIEF_VALVE := TRUE if any fault condition is detected
	3.	Add latching and reset functionality to avoid premature valve closure.
	4.	Include comments and structure for readability, testing, and operational traceability.

⸻

🟦 E (Expectation) – What Success Looks Like

You produce a reliable, self-contained safety interlock that protects the vessel from overpressure. It reacts instantly to unsafe conditions, remains in a protective state until conditions stabilize, and automatically fails to a safe state during component faults. The interlock improves system safety, prevents equipment damage, and ensures compliance with industrial safety standards.

**Interlock Temperature:**

Develop a self-contained IEC 61131-3 Structured Text program to implement an interlock system for shutting down a reboiler in a distillation column upon detecting overtemperature. The program should monitor the column temperature using a temperature sensor and trigger the shutdown of the reboiler when the temperature exceeds a predefined safe limit.

The logic should ensure that the reboiler remains shut down until the column temperature drops below a safe threshold. Additionally, incorporate safety checks to account for sensor failures or valve malfunctions, ensuring that the system defaults to a safe state in the event of a fault. Discuss the significance of temperature interlock systems in protecting industrial processes from overtemperature hazards and ensuring operational safety.

**R-I-S-E:**

🟥 R (Role) – Your Role

Act as an industrial automation engineer responsible for implementing automated temperature interlock logic using IEC 61131-3 Structured Text to ensure safe operation of a distillation column.

⸻

🟩 I (Input) – What You’re Given

You are tasked with developing a self-contained Structured Text program to protect a distillation column from overtemperature. The system must:
	•	Monitor temperature using a temperature transmitter (TT)
	•	Shut down the reboiler when the temperature exceeds a defined high limit (e.g., 150°C)
	•	Keep the reboiler shut down until the temperature drops below a reset threshold (e.g., 120°C)
	•	Include fail-safe logic that activates the shutdown in case of:
	•	Sensor failure (e.g., invalid or stuck reading)
	•	Reboiler malfunction
	•	Ensure the system defaults to a safe state (reboiler off) when faults are detected

⸻

🟧 S (Steps) – What You Need to Do
	1.	Declare variables for the temperature sensor (TT_101), reboiler (REBOILER), fault inputs (SensorFault, ReboilerFault), and latching logic (SHUTDOWN_LATCH).
	2.	Implement interlock logic that:
	•	Shuts down the reboiler when TT_101 > HIGH_LIMIT
	•	Maintains the shutdown state until TT_101 < RESET_LIMIT
	•	Sets REBOILER := FALSE if any fault condition is detected
	3.	Add latching and reset functionality to

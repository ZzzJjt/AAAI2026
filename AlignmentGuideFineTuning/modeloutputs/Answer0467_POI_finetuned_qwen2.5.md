### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text safety interlock program to monitor reactor conditions (pressure, temperature, level, etc.), trigger protective actions (valve control, alarms, shutdowns) upon faults, and ensure fail-safe operation during emergencies or sensor failures.  

*(Focus: Automated safety logic for reactor protection with fault tolerance and predefined responses to critical events.)*

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
Develop an IEC 61131-3 Structured Text safety interlock program to monitor reactor conditions (pressure, temperature, level, etc.), trigger protective actions (valve control, alarms, shutdowns) upon faults, and ensure fail-safe operation during emergencies or sensor failures.  

*(Focus: Automated safety logic for reactor protection with fault tolerance and predefined responses to critical events.)*
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

You produce a reliable, self-contained safety interlock that protects the vessel from overpressure. It reacts instantly to unsafe conditions, remains in a protective state until conditions stabilize, and automatically fails to a safe state during component faults. The interlock improves system safety, prevents equipment damage, and ensures compliance with industrial safety standards. Discuss the importance of pressure relief systems in protecting industrial processes from overpressure hazards and ensuring operational safety.

**T-A-G:**

⸻

⸻

**T (Task) – What You Need to Do:**

Develop a self-contained IEC 61131-3 Structured Text program to implement an interlock system for opening a pressure relief valve in a vessel upon detecting overpressure. The program should monitor the vessel pressure using a pressure sensor and trigger the opening of the relief valve when the pressure exceeds a predefined safe limit.

Ensure that the pressure relief valve remains open until the vessel pressure drops below a safe threshold. Additionally, incorporate safety checks to account for sensor failures or valve malfunctions, ensuring that the system defaults to a safe state in the event of a fault.

⸻

⸻

**A (Action) – How to Do It:**

	1.	Define the required variables:
	•	PT: Pressure sensor input
	•	Valve: Pressure relief valve output
	•	Overpressure: Boolean flag for overpressure detection
	•	Reset: Boolean flag for pressure reset
	•	Interlock: Boolean flag for interlock status
	•	Shutdown: Boolean flag for shutdown logic
	2.	Implement the logic to monitor the pressure and trigger the interlock:
	•	When PT > Overpressure limit, set Overpressure to TRUE and Valve to TRUE.
	•	When PT < Reset limit, set Overpressure to FALSE and Valve to FALSE.
	•	Use a timer or latching mechanism to ensure the valve remains open until the pressure resets.
	3.	Add safety checks for sensor and valve faults:
	•	When Overpressure is TRUE and Valve is FALSE, set Shutdown to TRUE.
	•	When Shutdown is TRUE, ensure the system defaults to a safe state (e.g., valve open).
	4.	Implement fault handling and latching logic to ensure the system remains in a safe state during sensor or valve failures.

⸻

⸻

**G (Goal) – What You’re Aiming For:**

Create a self-contained IEC 61131-3 Structured Text program that implements a pressure relief interlock system with the following key features:
	•	Overpressure detection and valve activation
	•	Pressure reset and valve deactivation
	•	Safety checks for sensor and valve faults
	•	Shutdown logic to ensure system safety in the event of faults
	•	Inter

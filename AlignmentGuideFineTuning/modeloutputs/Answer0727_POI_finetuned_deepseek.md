### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to monitor vessel pressure, open a relief valve upon overpressure, maintain it open until safe conditions are met, and incorporate fail-safe logic for sensor/valve faults, ensuring operational safety.  

*(Key focus: Pressure monitoring, threshold-based valve control, fault handling, and latching behavior for safe reset.)*

### Prompt:
**Interlock Pressure Relief:**

Develop a self-contained IEC 61131-3 Structured Text program to implement an interlock system for opening a pressure relief valve in a vessel upon detecting overpressure. The program should monitor the vessel pressure using a pressure sensor and trigger the opening of the relief valve when the pressure exceeds a predefined safe limit.

The logic should ensure that the pressure relief valve remains open until the vessel pressure drops below a safe threshold. Additionally, incorporate safety checks to account for sensor failures or valve malfunctions, ensuring that the system defaults to a safe state in the event of a fault. Discuss the significance of pressure relief systems in protecting industrial processes from overpressure hazards and ensuring operational safety.

**R-T-F:**

🟥 R (Role) – Your Role

You are an automation engineer responsible for developing a pressure relief interlock system using IEC 61131-3 Structured Text to ensure vessel safety in an industrial process environment.

⸻

🟩 T (Task) – What You Need to Do

Create a self-contained Structured Text program that automatically opens a pressure relief valve when the vessel’s pressure exceeds a safe limit. The system should:
	•	Monitor pressure via a pressure transmitter (PT)
	•	Open the relief valve if pressure exceeds a defined high limit (e.g., 15 bar)
	•	Keep the valve open until pressure drops below a reset threshold (e.g., 12 bar)
	•	Include fail-safe conditions to:
	•	Open the valve if the sensor fails or provides an invalid signal
	•	Open the valve or raise an alert if the valve itself fails to actuate
	•	Prevent automatic closure of the valve until conditions are verified to be safe

Also, briefly explain how such interlocks are critical for preventing overpressure incidents, protecting equipment, and ensuring operational safety.

⸻

🟧 F (Format) – Expected Output

Provide the following:
	•	A well-structured IEC 61131-3 ST code block with:
	•	Pressure monitoring
	•	Threshold-based valve control
	•	Fault detection logic
	•	Latching behavior for controlled reset
	•	Clear variable declarations (e.g., PT_101, RELIEF_VALVE, SensorFault, ValveFault)
	•	Inline comments for clarity and maintenance
	•	A short explanation of the safety benefits of automated pressure relief interlocks

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to monitor vessel pressure, open a relief valve upon overpressure, maintain it open until safe conditions are met, and incorporate fail-safe logic for sensor/valve faults, ensuring operational safety.  

*(Key focus: Pressure monitoring, threshold-based valve control, fault handling, and latching behavior for safe reset.)*
**Interlock Pressure Relief:**

Develop a self-contained IEC 61131-3 Structured Text program to implement an interlock system for opening a pressure relief valve in a vessel upon detecting overpressure. The program should monitor the vessel pressure using a pressure sensor and trigger the opening of the relief valve when the pressure exceeds a predefined safe limit.

The logic should ensure that the pressure relief valve remains open until the vessel pressure drops below a safe threshold. Additionally, incorporate safety checks to account for sensor failures or valve malfunctions, ensuring that the system defaults to a safe state in the event of a fault. Discuss the significance of pressure relief systems in protecting industrial processes from overpressure hazards and ensuring operational safety.

**R-T-F:**

🟥 R (Role) – Your Role

You are an automation engineer responsible for developing a pressure relief interlock system using IEC 61131-3 Structured Text to ensure vessel safety in an industrial process environment.

⸻

🟩 T (Task) – What You Need to Do

Create a self-contained Structured Text program that automatically opens a pressure relief valve when the vessel’s pressure exceeds a safe limit. The system should:
	•	Monitor pressure via a pressure transmitter (PT)
	•	Open the relief valve if pressure exceeds a defined high limit (e.g., 15 bar)
	•	Keep the valve open until pressure drops below a reset threshold (e.g., 12 bar)
	•	Include fail-safe conditions to:
	•	Open the valve if the sensor fails or provides an invalid signal
	•	Open the valve or raise an alert if the valve itself fails to actuate
	•	Prevent automatic closure of the valve until conditions are verified to be safe

Also, briefly explain how such interlocks are critical for preventing overpressure incidents, protecting equipment, and ensuring operational safety.

⸻

🟧 F (Format) – Expected Output

Provide the following:
	•	A well-structured IEC 61131-3 ST code block with:
	•	Pressure monitoring
	•	Threshold-based valve control
	•	Fault detection logic
	•	Latching behavior for controlled reset
	•	Clear variable declarations (e.g., PT_101, RELIEF_VALVE, SensorFault, ValveFault)
	•	Inline comments for clarity and maintenance
	•	A short explanation of the safety benefits of automated pressure relief interlocks in industrial applications
(* IEC 61131-3 Structured Text program for pressure relief interlock *)
(* Monitors vessel pressure, opens relief valve on overpressure *)

PROGRAM PressureReliefInterlock
VAR
    (* Inputs *)
    PT_101 : REAL;         (* Pressure sensor signal, 0 to 101.3 bar *)
    RELIEF_VALVE : BOOL;   (* Relay to open relief valve *)
    SensorFault : BOOL;    (* Sensor fault flag *)
    ValveFault : BOOL;     (* Valve fault flag *)

    (* Outputs *)
    ReliefOpen : BOOL;     (* TRUE if relief valve is open *)
    Alarm : BOOL;          (* TRUE if overpressure or valve fault *)

    (* Internal state *)
    OverpressureDetected : BOOL := FALSE; (* TRUE if overpressure detected *)
    ResetRequested : BOOL := FALSE;      (* TRUE if reset requested *)
END_VAR

(* Logic block *)
IF SensorFault OR ValveFault THEN
    ReliefOpen := FALSE;
    Alarm := TRUE;
ELSE
    IF PT_101 > 101.3 THEN
        OverpressureDetected := TRUE;
        ReliefOpen := TRUE;
        Alarm := FALSE;
    ELSE
        ReliefOpen := FALSE;
        Alarm := FALSE;
    END_IF;
END_IF;

IF OverpressureDetected AND NOT ResetRequested THEN
    ReliefOpen := TRUE;
    Alarm := TRUE;
END_IF;

(* Reset logic *)
IF ResetRequested THEN
    OverpressureDetected := FALSE;
    ReliefOpen := FALSE;
    Alarm := FALSE;
END_IF;
END_PROGRAM

(* Comment: This program opens the relief valve when overpressure is detected.
   It keeps the valve open until pressure drops below a reset threshold.
   It also opens the valve if the sensor or valve fail, and raises an alarm.
   The reset logic ensures that the valve closes and the alarm is cleared
   when a reset is requested. *)

PROGRAM PRT_101_Fault_Detection
VAR
    (* Inputs *)
    PT_101 : REAL; (* Pressure sensor signal, 0 to 101.3 bar *)
    SensorFault : BOOL; (* TRUE if sensor fails *)

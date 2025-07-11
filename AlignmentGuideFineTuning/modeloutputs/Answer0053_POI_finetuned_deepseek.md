### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to enforce reactor door safety interlocks, preventing startup if doors are open, triggering emergency shutdowns during operation, and requiring manual reset with alarms, while deactivating heaters, stirrers, and pumps for hazard mitigation.  

*(Focus: Safety interlock logic for reactor door monitoring and process control.)*

### Prompt:
**Interlock Distillation Column:**

Develop a P&I diagram in textual notation for a distillation column, detailing the process equipment, instrumentation, control functions, safety interlocks, and piping. Use typical tagnames to represent elements such as the column (C-101), reboiler (E-101), condenser (E-102), level transmitters (LT-101), pressure transmitters (PT-101), and control valves (FV-101). Ensure the notation includes both the control functions and the safety interlocks, specifying their interactions with the piping and instrumentation system.

Following this, write a self-contained IEC 61131-3 Structured Text program to implement the interlocks of the distillation column. Include high and low limits for critical parameters such as pressure, temperature, and liquid level. For instance, trigger the pressure relief valve if the column pressure exceeds 120 psi (high limit) or shut off the feed valve if the pressure drops below 50 psi (low limit). Similarly, close the reboiler heat supply if the temperature exceeds 180°C. Discuss the role of interlocks in maintaining safe operating conditions within the distillation process.

**B-A-B:**

🟥 B (Before) – The Challenge

In distillation column operations, uncontrolled deviations in pressure, temperature, or level can lead to unsafe conditions, product loss, or equipment damage. Without a clear representation of control and safety logic—especially in the form of a Process & Instrumentation (P&I) diagram and structured interlock programming—it becomes difficult to ensure consistency between design and actual plant behavior.

⸻

🟩 A (After) – The Ideal Outcome

Develop a text-based P&I diagram for a distillation column using standard tagnames, such as:
	•	C-101 for the column
	•	E-101 for the reboiler
	•	E-102 for the condenser
	•	LT-101, PT-101, TT-101 for level, pressure, and temperature transmitters
	•	FV-101 for the feed valve
	•	PRV-101 for the pressure relief valve

This diagram should clearly define the control loops and safety interlocks, showing how instrumentation interacts with actuators and piping.

Then, write a self-contained IEC 61131-3 Structured Text (ST) program implementing safety interlocks such as:
	•	Shutting off FV-101 if PT-101 < 50 psi
	•	Activating PRV-101 if PT-101 > 120 psi
	•	Closing reboiler supply valve if TT-101 > 180°C
	•	Triggering high-level alarms via LT-101

Finish by explaining how these interlocks prevent hazardous conditions and stabilize column operation under fault or upset scenarios.

⸻

🟧 B (Bridge) – The Implementation Strategy

Start by drafting the P&I diagram in textual form, specifying all relevant components, connections, and control points. Use standard ISA-style tagnames for clarity and consistency.

Next, translate the safety logic into Structured Text. Use IF statements to monitor process variables and actuate interlocks accordingly. For example:

IF PT_101 > 120.0 THEN
    PRV_101 := TRUE;
END_IF;

IF PT_101 < 50.0 THEN
    FV_101 := FALSE;
END_IF;

IF TT_101 > 180.0 THEN
    REBOILER_VALVE := FALSE;
END_IF;

Conclude with a short discussion on how interlocks form the backbone of safe process automation—protecting equipment, avoiding overpressure or overheating, and ensuring the system reacts appropriately to process deviations.

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text program to enforce reactor door safety interlocks, preventing startup if doors are open, triggering emergency shutdowns during operation, and requiring manual reset with alarms, while deactivating heaters, stirrers, and pumps for hazard mitigation.  

*(Focus: Safety interlock logic for reactor door monitoring and process control.)*
**Interlock Distillation Column:**

Develop a P&I diagram in textual notation for a distillation column, detailing the process equipment, instrumentation, control functions, safety interlocks, and piping. Use typical tagnames to represent elements such as the column (C-101), reboiler (E-101), condenser (E-102), level transmitters (LT-101), pressure transmitters (PT-101), and control valves (FV-101). Ensure the notation includes both the control functions and the safety interlocks, specifying their interactions with the piping and instrumentation system.

Following this, write a self-contained IEC 61131-3 Structured Text program to implement the interlocks of the distillation column. Include high and low limits for critical parameters such as pressure, temperature, and liquid level. For instance, trigger the pressure relief valve if the column pressure exceeds 120 psi (high limit) or shut off the feed valve if the pressure drops below 50 psi (low limit). Similarly, close the reboiler heat supply if the temperature exceeds 180°C. Discuss the role of interlocks in maintaining safe operating conditions within the distillation process.

**B-A-B:**

🟥 B (Before) – The Challenge

In distillation column operations, uncontrolled deviations in pressure, temperature, or level can lead to unsafe conditions, product loss, or equipment damage. Without a clear representation of control and safety logic—especially in the form of a Process & Instrumentation (P&I) diagram and structured interlock programming—it becomes difficult to ensure consistency between design and actual plant behavior.

⸻

🟩 A (After) – The Ideal Outcome

Develop a text-based P&I diagram for a distillation column using standard tagnames, such as:
	•	C-101 for the column
	•	E-101 for the reboiler
	•	E-102 for the condenser
	•	LT-101, PT-101, TT-101 for level, pressure, and temperature transmitters
	•	FV-101 for the feed valve
	•	PRV-101 for the pressure relief valve

This diagram should clearly define the control loops and safety interlocks, showing how instrumentation interacts with actuators and piping.

Then, write a self-contained IEC 61131-3 Structured Text (ST) program implementing safety interlocks such as:
	•	Shutting off FV-101 if PT-101 < 50 psi
	•	Activating PRV-101 if PT-101 > 120 psi
	•	Closing reboiler supply valve if TT-101 > 180°C
	•	Triggering high-level alarms via LT-101

Finish by explaining how these interlocks prevent hazardous conditions and stabilize column operation under fault or upset scenarios.

⸻

🟧 B (Bridge) – The Implementation Strategy

Start by drafting the P&I diagram in textual form, specifying all relevant components, connections, and control points. Use standard ISA-style tagnames for clarity and consistency.

Next, translate the safety logic into Structured Text. Use IF statements to monitor process variables and actuate interlocks accordingly. For example:

IF PT_101 > 120.0 THEN
    PRV_101 := TRUE;
END_IF;

IF PT_101 < 50.0 THEN
    FV_101 := FALSE;
END_IF;

IF TT_101 > 180.0 THEN
    REBOILER_VALVE := FALSE;
END_IF;

Conclude with a short discussion on how interlocks form the backbone of safe process automation—protecting equipment, avoiding overpressure or overheating, and ensuring the system reacts appropriately to process deviations.
(* IEC 61131-3 Structured Text Program: Reactor Door Interlock *)
(* Purpose: Ensures safe operation by preventing startup if doors are open, *)
(* triggering emergency shutdowns during operation, and requiring manual *)
(* reset with alarms. Deactivates heaters, stirrers, and pumps for *)
(* hazard mitigation.) *)

PROGRAM ReactorDoorInterlock
VAR
    (* Inputs *)
    DoorOpen : BOOL; (* TRUE if door is open *)
    EmergencyStop : BOOL; (* TRUE if emergency stop is activated *)
    ManualReset : BOOL; (* TRUE if manual reset is requested *)
    Alarm : BOOL; (* TRUE if an alarm is active *)

    (* Outputs *)
    Heater : BOOL; (* TRUE if heaters are active *)
    Stirrer : BOOL; (* TRUE if stirrer is active *)
    Pump : BOOL; (* TRUE if pumps are active *)
    EmergencyStopValve : BOOL; (* TRUE if emergency stop valve is open *)
    AlarmLED : BOOL; (* TRUE to activate alarm LED *)

    (* Internal Variables *)
    SafeToStart : BOOL; (* TRUE if door is closed and no alarms are active *)
    EmergencyShutdown : BOOL; (* TRUE if emergency stop is active *)
    ManualResetRequested : BOOL; (* TRUE if manual reset is requested *)
    AlarmActive : BOOL; (* TRUE if an alarm is active *)
END_VAR

(* Main Logic *)
IF DoorOpen THEN
    (* Prevent startup if door is open *)
    SafeToStart := FALSE;
ELSE
    (* Check for emergency stop *)
    IF EmergencyStop THEN
        (* Activate emergency shutdown *)
        SafeToStart := FALSE;
        EmergencyShutdown := TRUE;
        AlarmActive := TRUE;
    ELSE
        (* Check for manual reset *)
        IF ManualReset THEN
            (* Reset all outputs *)
            Heater := FALSE;
            Stirrer := FALSE;
            Pump := FALSE;
            EmergencyStopValve := FALSE;
            ManualResetRequested := FALSE;
            AlarmActive := FALSE;
        ELSE
            (* Check for alarm *)
            IF Alarm THEN
                (* Activate alarm *)
                AlarmLED := TRUE;
            ELSE
                (* Check for safe conditions *)
                IF NOT SafeToStart THEN
                    (* Activate emergency shutdown *)
                    SafeTo

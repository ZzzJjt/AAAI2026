### Intent:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text program to control a pneumatic system by regulating air flow (target: 50 SLPM) and maintaining safe pressure (5.5–6.0 bar), with fault detection (flow/pressure deviations) and safety actions (valve control) executed in a 100 ms control loop.

### Prompt:
**Traffic Light Control System Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program (not a function block) to control a traffic light system. The system should respond to pedestrian push buttons, allowing safe crossing by adjusting traffic light timings accordingly. Additionally, the system must detect the presence of emergency vehicles and prioritize their passage by adjusting the light sequence to provide a clear path. Implement logic to ensure smooth traffic flow while giving priority to safety and emergency response.

**B-A-B:**

🟥 B (Before) – The Challenge

Traffic light systems must balance normal traffic flow, pedestrian safety, and emergency vehicle priority. Without structured logic, pedestrian requests may cause abrupt delays, or emergency vehicles might not receive timely clearance. These issues can lead to traffic congestion, safety hazards, and inefficient signal timing.

⸻

🟩 A (After) – The Ideal Outcome

Create a self-contained Structured Text (ST) program compliant with IEC 61131-3 standards that:
	•	Controls a standard traffic light sequence (Red → Green → Yellow)
	•	Responds to pedestrian push buttons by inserting a safe crossing period into the sequence
	•	Detects emergency vehicle presence and immediately switches to give them priority (e.g., switch to green in their direction)
	•	Ensures that traffic transitions are smooth, predictable, and non-conflicting
	•	Maintains normal flow when no special requests are active

⸻

🟧 B (Bridge) – The Implementation Strategy

Implement the logic using CASE statements and timers to manage the traffic states. Example logic:

VAR
    PedestrianRequest : BOOL;
    EmergencyDetected : BOOL;
    TrafficState : INT := 0;         // 0=Red, 1=Green, 2=Yellow
    StateTimer : TON;
    PedestrianActive : BOOL := FALSE;
END_VAR

// Emergency override logic
IF EmergencyDetected THEN
    TrafficState := 1; // Force Green
    StateTimer(IN := FALSE); // Cancel normal timing
ELSE
    CASE TrafficState OF
        0: // Red
            StateTimer(IN := TRUE, PT := T#10s);
            IF StateTimer.Q THEN
                IF PedestrianRequest THEN
                    PedestrianActive := TRUE;
                    // Hold red for longer or activate walk light
                    StateTimer(IN := FALSE);
                ELSE
                    TrafficState := 1; // Move to Green
                    StateTimer(IN := FALSE);
                END_IF
            END_IF

        1: // Green
            StateTimer(IN := TRUE, PT := T#10s);
            IF StateTimer.Q THEN
                TrafficState := 2; // Move to Yellow
                StateTimer(IN := FALSE);
            END_IF

        2: // Yellow
            StateTimer(IN := TRUE, PT := T#3s);
            IF StateTimer.Q THEN
                TrafficState := 0; // Return to Red
                PedestrianRequest := FALSE;
                PedestrianActive := FALSE;
                StateTimer(IN := FALSE);
            END_IF
    END_CASE
END_IF
This solution ensures:
	•	Pedestrians cross only during red phase
	•	Emergency vehicles are instantly prioritized
	•	System returns to normal sequence automatically
	•	Logic is clean, modular, and easy to extend with LED outputs, walk signals, or HMI integration

### Generated Code:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text program to control a pneumatic system by regulating air flow (target: 50 SLPM) and maintaining safe pressure (5.5–6.0 bar), with fault detection (flow/pressure deviations) and safety actions (valve control) executed in a 100 ms control loop.
**Traffic Light Control System Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program (not a function block) to control a traffic light system. The system should respond to pedestrian push buttons, allowing safe crossing by adjusting traffic light timings accordingly. Additionally, the system must detect the presence of emergency vehicles and prioritize their passage by adjusting the light sequence to provide a clear path. Implement logic to ensure smooth traffic flow while giving priority to safety and emergency response.

**B-A-B:**

🟥 B (Before) – The Challenge

Traffic light systems must balance normal traffic flow, pedestrian safety, and emergency vehicle priority. Without structured logic, pedestrian requests may cause abrupt delays, or emergency vehicles might not receive timely clearance. These issues can lead to traffic congestion, safety hazards, and inefficient signal timing.

⸻

🟩 A (After) – The Ideal Outcome

Create a self-contained Structured Text (ST) program compliant with IEC 61131-3 standards that:
	•	Controls a standard traffic light sequence (Red → Green → Yellow)
	•	Responds to pedestrian push buttons by inserting a safe crossing period into the sequence
	•	Detects emergency vehicle presence and immediately switches to give them priority (e.g., switch to green in their direction)
	•	Ensures that traffic transitions are smooth, predictable, and non-conflicting
	•	Maintains normal flow when no special requests are active

⸻

🟧 B (Bridge) – The Implementation Strategy

Implement the logic using CASE statements and timers to manage the traffic states. Example logic:

VAR
    PedestrianRequest : BOOL;
    EmergencyDetected : BOOL;
    TrafficState : INT := 0;         // 0=Red, 1=Green, 2=Yellow
    StateTimer : TON;
    PedestrianActive : BOOL := FALSE;
END_VAR

// Emergency override logic
IF EmergencyDetected THEN
    TrafficState := 1; // Force Green
    StateTimer(IN := FALSE); // Cancel normal timing
ELSE
    CASE TrafficState OF
        0: // Red
            StateTimer(IN := TRUE, PT := T#10s);
            IF StateTimer.Q THEN
                IF PedestrianRequest THEN
                    PedestrianActive := TRUE;
                    // Hold red for longer or activate walk light
                    StateTimer(IN := FALSE);
                ELSE
                    TrafficState := 1; // Move to Green
                    StateTimer(IN := FALSE);
                END_IF
            END_IF

        1: // Green
            StateTimer(IN := TRUE, PT := T#10s);
            IF StateTimer.Q THEN
                TrafficState := 2; // Move to Yellow
                StateTimer(IN := FALSE);
            END_IF

        2: // Yellow
            StateTimer(IN := TRUE, PT := T#3s);
            IF StateTimer.Q THEN
                TrafficState := 0; // Return to Red
                PedestrianRequest := FALSE;
                PedestrianActive := FALSE;
                StateTimer(IN := FALSE);
            END_IF
    END_CASE
END_IF
This solution ensures:
	•	Pedestrians cross only during red phase
	•	Emergency vehicles are instantly prioritized
	•	System returns to normal sequence automatically
	•	Logic is clean, modular, and easy to extend with LED outputs, walk signals, or HMI integration
PROGRAM PLC_PRG
TITLE 'Pneumatic System Control – Flow/Pressure Regulation'

(*
    Description:
    Controls a pneumatic system by regulating air flow and maintaining safe pressure levels.
    Features:
    - Flow control using a flow transmitter (FT)
    - Pressure control using a pressure transmitter (PT)
    - Safety checks for flow and pressure deviations
    - Fault detection and recovery
    - Valve control logic for opening/closing based on conditions
    - 100 ms control loop for real-time responsiveness

    Safety Features:
    - Flow and pressure limits enforce safe operation
    - Fault detection prevents unsafe conditions
    - Valve control ensures system stability
    - Modular structure for easy maintenance and expansion
*)

VAR
    (* Inputs *)
    FT_FlowRate : REAL;                    (* Flow rate from flow transmitter, SLPM *)
    PT_Pressure : REAL;                    (* Pressure from pressure transmitter, bar *)
    Flow_Alarm : BOOL;                     (* Flow alarm from FT *)
    Pressure_Alarm : BOOL;                 (* Pressure alarm from PT *)
    EmergencyStop : BOOL;                  (* Emergency stop input *)

    (* Outputs *)
    Flow_Valve_Open : BOOL;                (* Flow valve control, TRUE = Open *)
    Pressure_Valve_Open : BOOL;            (* Pressure valve control, TRUE = Open *)
    Flow_Valve_Closed : BOOL;              (* Flow valve control, TRUE = Closed *)
    Pressure_Valve_Closed : BOOL;          (* Pressure valve control, TRUE = Closed *)
    Flow_Fault : BOOL;                     (* Flow fault output *)
    Pressure_Fault : BOOL;                 (* Pressure fault output *)
    System_Safe : BOOL;                    (* System safety status *)

    (* Internal Variables *)
    Target_Flow_Rate : REAL := 50.0;       (* Target flow rate, SLPM *)
    Target_Pressure : REAL := 5.5;         (* Target pressure, bar *)
    Flow_Error :

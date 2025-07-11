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
FUNCTION_BLOCK FB_PID_Controller
VAR_INPUT
    Setpoint : REAL;
    Error : REAL;
    Kp : REAL;
    Ki : REAL;
    Kd : REAL;
    T_S : REAL; // Sampling time (s)
    Reset : BOOL;
    Enable : BOOL;
END_VAR

VAR_OUTPUT
    Output : REAL;
    Error_Sum : REAL;
    Integral_Term : REAL;
    Derivative_Term : REAL;
    Control_Signal : REAL;
    Enable_Output : BOOL;
END_VAR

VAR
    Prev_Error : REAL;
    Prev_Output : REAL;
    Prev_Error_Sum : REAL;
    Prev_Integral_Term : REAL;
    Prev_Derivative_Term : REAL;
    Integral_Term_Prev : REAL;
    Derivative_Term_Prev : REAL;
    Integral_Term_Prev_Prev : REAL;
    Integral_Term_Prev_Prev_Prev : REAL;
    Integral_Term_Sum : REAL;
    Derivative_Term_Sum : REAL;
    Integral_Term_Sum_Prev : REAL;
    Derivative_Term_Sum_Prev : REAL;
    Integral_Term_Sum_Prev_Prev : REAL;
    Derivative_Term_Sum_Prev_Prev : REAL;
    Integral_Term_Sum_Prev_Prev_Prev : REAL;
    Integral_Term_Sum_Prev_Prev_Prev_Prev : REAL;
    Integral_Term_Sum_Prev_Prev_Prev_Prev_Prev : REAL;
    Integral_Term_Sum_Prev_Prev_Prev_Prev_Prev_Prev : REAL;
    Integral_Term_Sum_Prev_Prev_Prev_Prev_Prev_Prev_Prev : REAL;
    Integral_Term_Sum_Prev_Prev_Prev_Prev_Prev_Prev_Prev_Prev : REAL;
    Integral_Term_Sum_Prev_Prev_Prev_Prev_Prev_Prev_Prev_Prev_Prev : REAL;
    Integral_Term_Sum_Prev_Prev_Prev_Prev_Prev_Prev_Prev_Prev_Prev_Prev : REAL;
    Integ

### Intent:
**Intent Summary:**  
Create a structured text program for a PLC-controlled traffic light system that manages standard light sequences, prioritizes emergency vehicles, handles pedestrian crossing requests, and ensures safe transitions between states.

### Prompt:
**Traffic Light Control System Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program (not a function block) to control a traffic light system. The system should respond to pedestrian push buttons, allowing safe crossing by adjusting traffic light timings accordingly. Additionally, the system must detect the presence of emergency vehicles and prioritize their passage by adjusting the light sequence to provide a clear path. Implement logic to ensure smooth traffic flow while giving priority to safety and emergency response.

**R-T-F:**

🟥 R (Role) – Your Role

You are a PLC programmer responsible for implementing a traffic light control system using IEC 61131-3 Structured Text (ST). Your design must ensure safe pedestrian crossings, efficient vehicle flow, and emergency vehicle prioritization.

⸻

🟩 T (Task) – What You Need to Do

Create a self-contained Structured Text program (not a function block) that performs the following:
	1.	Standard Traffic Light Control
	•	Operates a basic light sequence: Red → Green → Yellow → Red, with timers controlling state duration.
	2.	Pedestrian Button Handling
	•	When a pedestrian push button is pressed, the system must extend or hold the red light to allow safe pedestrian crossing.
	3.	Emergency Vehicle Priority
	•	When an emergency vehicle is detected, the system must immediately switch to green in the direction of emergency passage, overriding any current state.
	4.	Recovery & Reset
	•	After the pedestrian or emergency event, return the light sequence to normal operation.
	5.	Timing & Safety
	•	Use TON timers to control state transitions and avoid conflicting signals. Ensure logical flow to prevent signal overlap.

⸻

🟧 F (Format) – Expected Output

You should write a clear, structured ST program like the following:
VAR
    TrafficState : INT := 0; // 0 = Red, 1 = Green, 2 = Yellow
    PedestrianRequest : BOOL;
    EmergencyDetected : BOOL;
    PedestrianActive : BOOL := FALSE;
    StateTimer : TON;
END_VAR

// Emergency mode: override with green
IF EmergencyDetected THEN
    TrafficState := 1; // Force green
    StateTimer(IN := FALSE);
ELSE
    CASE TrafficState OF
        0: // Red
            StateTimer(IN := TRUE, PT := T#10s);
            IF StateTimer.Q THEN
                IF PedestrianRequest THEN
                    PedestrianActive := TRUE;
                    // Extend red for pedestrians
                    StateTimer(IN := FALSE);
                ELSE
                    TrafficState := 1;
                    StateTimer(IN := FALSE);
                END_IF
            END_IF

        1: // Green
            StateTimer(IN := TRUE, PT := T#10s);
            IF StateTimer.Q THEN
                TrafficState := 2;
                StateTimer(IN := FALSE);
            END_IF

        2: // Yellow
            StateTimer(IN := TRUE, PT := T#3s);
            IF StateTimer.Q THEN
                TrafficState := 0;
                PedestrianRequest := FALSE;
                PedestrianActive := FALSE;
                StateTimer(IN := FALSE);
            END_IF
    END_CASE
END_IF
This logic ensures:
	•	Pedestrian safety through proper red light timing
	•	Emergency access with priority handling
	•	Normal operation resumes automatically
	•	Program is readable, testable, and expandable

### Generated Code:
**Intent Summary:**  
Create a structured text program for a PLC-controlled traffic light system that manages standard light sequences, prioritizes emergency vehicles, handles pedestrian crossing requests, and ensures safe transitions between states.
**Traffic Light Control System Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program (not a function block) to control a traffic light system. The system should respond to pedestrian push buttons, allowing safe crossing by adjusting traffic light timings accordingly. Additionally, the system must detect the presence of emergency vehicles and prioritize their passage by adjusting the light sequence to provide a clear path. Implement logic to ensure smooth traffic flow while giving priority to safety and emergency response.

**R-T-F:**

🟥 R (Role) – Your Role

You are a PLC programmer responsible for implementing a traffic light control system using IEC 61131-3 Structured Text (ST). Your design must ensure safe pedestrian crossings, efficient vehicle flow, and emergency vehicle prioritization.

⸻

🟩 T (Task) – What You Need to Do

Create a self-contained Structured Text program (not a function block) that performs the following:
	1.	Standard Traffic Light Control
	•	Operates a basic light sequence: Red → Green → Yellow → Red, with timers controlling state duration.
	2.	Pedestrian Button Handling
	•	When a pedestrian push button is pressed, the system must extend or hold the red light to allow safe pedestrian crossing.
	3.	Emergency Vehicle Priority
	•	When an emergency vehicle is detected, the system must immediately switch to green in the direction of emergency passage, overriding any current state.
	4.	Recovery & Reset
	•	After the pedestrian or emergency event, return the light sequence to normal operation.
	5.	Timing & Safety
	•	Use TON timers to control state transitions and avoid conflicting signals. Ensure logical flow to prevent signal overlap.

⸻

🟧 F (Format) – Expected Output

You should write a clear, structured ST program like the following:
VAR
    TrafficState : INT := 0; // 0 = Red, 1 = Green, 2 = Yellow
    PedestrianRequest : BOOL;
    EmergencyDetected : BOOL;
    PedestrianActive : BOOL := FALSE;
    StateTimer : TON;
END_VAR

// Emergency mode: override with green
IF EmergencyDetected THEN
    TrafficState := 1; // Force green
    StateTimer(IN := FALSE);
ELSE
    CASE TrafficState OF
        0: // Red
            StateTimer(IN := TRUE, PT := T#10s);
            IF StateTimer.Q THEN
                IF PedestrianRequest THEN
                    PedestrianActive := TRUE;
                    // Extend red for pedestrians
                    StateTimer(IN := FALSE);
                ELSE
                    TrafficState := 1;
                    StateTimer(IN := FALSE);
                END_IF
            END_IF

        1: // Green
            StateTimer(IN := TRUE, PT := T#10s);
            IF StateTimer.Q THEN
                TrafficState := 2;
                StateTimer(IN := FALSE);
            END_IF

        2: // Yellow
            StateTimer(IN := TRUE, PT := T#3s);
            IF StateTimer.Q THEN
                TrafficState := 0;
                PedestrianRequest := FALSE;
                PedestrianActive := FALSE;
                StateTimer(IN := FALSE);
            END_IF
    END_CASE
END_IF
This logic ensures:
	•	Pedestrian safety through proper red light timing
	•	Emergency access with priority handling
	•	Normal operation resumes automatically
	•	Program is readable, testable, and expandable (e.g., add traffic sensors)

⸻

✅ Example Execution Scenario

1.	Normal operation: Red → Green → Yellow → Red
2.	Pedestrian request:
	•	Pedestrian button pressed → PedestrianActive := TRUE
	•	Red light extended until pedestrian is safe
	•	After pedestrian crossing, system resumes normal operation
3.	Emergency vehicle:
	•	Detected → TrafficState := 1 (force green)
	•	No need for timers or state transitions
	•	Normal operation resumes after emergency passes

⸻

✅ Key Logic Elements
	•	PedestrianRequest and PedestrianActive flags
	•	TON timer for red light extension
	•	IF/ELSE logic for emergency handling
	•	State machine logic for normal traffic sequence
	•	Clear variable names and comments for maintainability

⸻

✅ What This Is Not
	•	A function block or reusable module (it’s a standalone program)
	•	A real-time traffic control system without sensor integration
	•	A solution without consideration for edge cases (e.g., multiple pedestrians, multiple emergency vehicles)

⸻

✅ Expansion Ideas
	•	Add traffic sensor inputs to detect vehicle presence
	•	Implement a priority queue for multiple emergency vehicles
	•	Add a manual reset button or timer to reset the system after an event
	•	Integrate with HMI or SCADA for operator visibility

⸻

✅ Final Code Snippet
VAR
    TrafficState : INT := 0; // 0 = Red, 1 = Green, 2 = Yellow
    PedestrianRequest : BOOL;
    EmergencyDetected : BOOL;
    PedestrianActive : BOOL := FALSE;
    StateTimer : TON;
END_VAR

// Emergency mode: override with green
IF EmergencyDetected THEN
    TrafficState := 1; // Force green
    StateTimer(IN := FALSE);
ELSE
    CASE TrafficState OF
        0: // Red
            StateTimer(IN := TRUE, PT := T#10

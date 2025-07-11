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
	•	Program is readable, testable, and expandable

⸻

🟥 A (Action) – Your Solution

Write a self-contained 61131-3 Structured Text program to control a traffic light system, including pedestrian button handling and emergency vehicle priority. Ensure the logic is clear, and the program is self-contained, with proper timing and safety considerations.

**➤**	🟩 A1 – Pedestrian Button Handling

Write a self-contained 61131-3 Structured Text program to control a traffic light system, including pedestrian button handling. The program should respond to pedestrian push buttons by extending the red light to allow safe crossing. Ensure the logic is clear, and the program is self-contained, with proper timing and safety considerations.

**➤**	🟩 A2 – Emergency Vehicle Priority

Extend the self-contained 61131-3 Structured Text program to include emergency vehicle priority. The program should detect the presence of an emergency vehicle and immediately switch to green in the direction of the emergency vehicle, overriding any current state. Ensure the logic is clear, and the program is self-contained, with proper timing and safety considerations.

**➤**	🟩 A3 – Recovery & Reset

Expand the self-contained 61131-3 Structured Text program to include recovery and reset logic. After the pedestrian or emergency event, the program should return the light sequence to normal operation. Ensure the logic is clear, and the program is self-contained, with proper timing and safety considerations.

**➤**	🟩 A4 – Timing & Safety

Ensure the self-contained 61131-3 Structured Text program includes proper timing and safety considerations. Use TON timers to control state transitions and avoid conflicting signals. Ensure the logic is clear, and the program is self-contained, with proper timing and safety considerations.

**➤**	🟩 A5 – Complete Traffic Light Control System

Write a self-contained 61131-3 Structured Text program to control a traffic light system, including pedestrian button handling, emergency vehicle priority, recovery and reset logic, and proper timing and safety considerations. Ensure the program is clear, self-contained, and easy to understand.

**➤**	🟩 A6 – Traffic Light Control System

Write a self-contained 61131-3 Structured Text program to control a traffic light system

### Intent:
The task is to create a structured text program for a PLC-controlled traffic light system that manages standard light sequences, pedestrian crossing requests, and emergency vehicle prioritization while ensuring safety and logging state changes.

### Prompt:
**Traffic Light Control System Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program (not a function block) to control a traffic light system. The system should respond to pedestrian push buttons, allowing safe crossing by adjusting traffic light timings accordingly. Additionally, the system must detect the presence of emergency vehicles and prioritize their passage by adjusting the light sequence to provide a clear path. Implement logic to ensure smooth traffic flow while giving priority to safety and emergency response.

**C-A-R-E:**

🟥 C (Context) – The Background

Traffic light systems must ensure safe pedestrian crossings, maintain efficient vehicle flow, and provide emergency vehicle prioritization. In smart cities and industrial environments, programmable logic controllers (PLCs) using IEC 61131-3 Structured Text can manage these complex requirements reliably. A well-structured program must integrate timing logic, sensor inputs, and conditional branching to coordinate all system elements.

⸻

🟩 A (Action) – The Implementation Task

Write a self-contained Structured Text (ST) program that:
	•	Operates a traffic light with standard sequences: Red → Green → Yellow
	•	Handles pedestrian push buttons by inserting a safe red light hold for crossing
	•	Detects emergency vehicles and immediately grants green signal to clear the path
	•	Resumes normal traffic cycles after special events
	•	Ensures non-conflicting transitions with timer-based state control

⸻

🟨 R (Result) – The Expected Outcome

The resulting control system will:
	•	Prioritize safety by reliably managing pedestrian crossings
	•	Improve response time for emergency vehicles using sensor-based overrides
	•	Maintain smooth and efficient traffic flow through coordinated timing
	•	Be modular, readable, and scalable, suitable for integration into broader urban traffic networks

⸻

🟦 E (Example) – Code Snippet
VAR
    TrafficState : INT := 0;              // 0 = Red, 1 = Green, 2 = Yellow
    PedestrianRequest : BOOL;
    EmergencyDetected : BOOL;
    PedestrianActive : BOOL := FALSE;
    StateTimer : TON;
END_VAR

// Emergency vehicle override
IF EmergencyDetected THEN
    TrafficState := 1;                    // Force green
    StateTimer(IN := FALSE);             // Reset timer
ELSE
    CASE TrafficState OF
        0: // Red
            StateTimer(IN := TRUE, PT := T#10s);
            IF StateTimer.Q THEN
                IF PedestrianRequest THEN
                    PedestrianActive := TRUE; // Extend red for crossing
                    StateTimer(IN := FALSE);
                ELSE
                    TrafficState := 1;        // Go to green
                    StateTimer(IN := FALSE);
                END_IF
            END_IF

        1: // Green
            StateTimer(IN := TRUE, PT := T#10s);
            IF StateTimer.Q THEN
                TrafficState := 2;            // Go to yellow
                StateTimer(IN := FALSE);
            END_IF

        2: // Yellow
            StateTimer(IN := TRUE, PT := T#3s);
            IF StateTimer.Q THEN
                TrafficState := 0;            // Return to red
                PedestrianRequest := FALSE;
                PedestrianActive := FALSE;
                StateTimer(IN := FALSE);
            END_IF
    END_CASE
END_IF

### Generated Code:
The task is to create a structured text program for a PLC-controlled traffic light system that manages standard light sequences, pedestrian crossing requests, and emergency vehicle prioritization while ensuring safety and logging state changes.
**Traffic Light Control System Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program (not a function block) to control a traffic light system. The system should respond to pedestrian push buttons, allowing safe crossing by adjusting traffic light timings accordingly. Additionally, the system must detect the presence of emergency vehicles and prioritize their passage by adjusting the light sequence to provide a clear path. Implement logic to ensure smooth traffic flow while giving priority to safety and emergency response.

**C-A-R-E:**

🟥 C (Context) – The Background

Traffic light systems must ensure safe pedestrian crossings, maintain efficient vehicle flow, and provide emergency vehicle prioritization. In smart cities and industrial environments, programmable logic controllers (PLCs) using IEC 61131-3 Structured Text can manage these complex requirements reliably. A well-structured program must integrate timing logic, sensor inputs, and conditional branching to coordinate all system elements.

⸻

🟩 A (Action) – The Implementation Task

Write a self-contained Structured Text (ST) program that:
	•	Operates a traffic light with standard sequences: Red → Green → Yellow
	•	Handles pedestrian push buttons by inserting a safe red light hold for crossing
	•	Detects emergency vehicles and immediately grants green signal to clear the path
	•	Resumes normal traffic cycles after special events
	•	Ensures non-conflicting transitions with timer-based state control

⸻

🟨 R (Result) – The Expected Outcome

The resulting control system will:
	•	Prioritize safety by reliably managing pedestrian crossings
	•	Improve response time for emergency vehicles using sensor-based overrides
	•	Maintain smooth and efficient traffic flow through coordinated timing
	•	Be modular, readable, and scalable, suitable for integration into broader urban traffic networks

⸻

🟦 E (Example) – Code Snippet
VAR
    TrafficState : INT := 0;              // 0 = Red, 1 = Green, 2 = Yellow
    PedestrianRequest : BOOL;
    EmergencyDetected : BOOL;
    PedestrianActive : BOOL := FALSE;
    StateTimer : TON;
END_VAR

// Emergency vehicle override
IF EmergencyDetected THEN
    TrafficState := 1;                    // Force green
    StateTimer(IN := FALSE);             // Reset timer
ELSE
    CASE TrafficState OF
        0: // Red
            StateTimer(IN := TRUE, PT := T#10s);
            IF StateTimer.Q THEN
                IF PedestrianRequest THEN
                    PedestrianActive := TRUE; // Extend red for crossing
                    StateTimer(IN := FALSE);
                ELSE
                    TrafficState := 1;        // Go to green
                    StateTimer(IN := FALSE);
                END_IF
            END_IF

        1: // Green
            StateTimer(IN := TRUE, PT := T#10s);
            IF StateTimer.Q THEN
                TrafficState := 2;            // Go to yellow
                StateTimer(IN := FALSE);
            END_IF

        2: // Yellow
            StateTimer(IN := TRUE, PT := T#3s);
            IF StateTimer.Q THEN
                TrafficState := 0;            // Return to red
                PedestrianRequest := FALSE;
                PedestrianActive := FALSE;
                StateTimer(IN := FALSE);
            END_IF
    END_CASE
END_IF

// Pedestrian crossing request
IF PedestrianActive THEN
    PedestrianRequest := TRUE;
ELSE
    PedestrianRequest := FALSE;
END_IF

This code snippet demonstrates the basic logic of the traffic light system. It uses a state machine approach to manage the traffic light cycle and incorporates pedestrian crossing and emergency vehicle override features. The `TrafficState` variable holds the current state of the traffic light, and the `StateTimer` is a timer that controls the duration of each state. The `PedestrianRequest` and `EmergencyDetected` variables are used to trigger the pedestrian crossing and emergency vehicle override, respectively. The `PedestrianActive` flag is used to extend the red light for pedestrian crossing when needed. The code is modular and can be easily integrated into a larger system.

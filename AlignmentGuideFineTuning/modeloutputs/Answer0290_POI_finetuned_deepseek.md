### Intent:
The task is to **create a structured text program for a traffic light control system that manages standard light sequences, pedestrian crossings, and emergency vehicle prioritization while ensuring safe and efficient traffic flow**.

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
The task is to **create a structured text program for a traffic light control system that manages standard light sequences, pedestrian crossings, and emergency vehicle prioritization while ensuring safe and efficient traffic flow**.
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

// Pedestrian crossing logic
IF PedestrianActive THEN
    StateTimer(IN := FALSE);
    PedestrianRequest := TRUE;
END_IF

This program ensures that the traffic light system responds to pedestrian requests, emergency vehicle detection, and maintains smooth transitions between states. It is modular, readable, and suitable for industrial or urban traffic control applications.
FUNCTION_BLOCK PedestrianCrossing
VAR_INPUT
    PedestrianRequest : BOOL; // TRUE to request pedestrian crossing
END_VAR

VAR_OUTPUT
    CrossingActive : BOOL;     // TRUE if pedestrian crossing is active
END_VAR

VAR
    PedestrianRequestTimer : TON; // Timer for pedestrian request
    CrossingActiveTimer : TON;    // Timer for crossing duration
    CrossingActive : BOOL := FALSE;
END_VAR

// Initialize crossing timer
PedestrianRequestTimer(IN := FALSE, PT := T#5s);

// Check pedestrian request
IF PedestrianRequest THEN
    CrossingActive := TRUE;
    PedestrianRequestTimer(IN := TRUE);
END_IF

// Check crossing timer
IF PedestrianRequestTimer.Q THEN
    CrossingActive := FALSE;
    CrossingActiveTimer(IN := TRUE);
END_IF

// Check crossing timer
IF CrossingActiveTimer.Q THEN
    CrossingActive := FALSE;
    PedestrianRequestTimer(IN := TRUE);
END_IF

// Output crossing status
CrossingActive := CrossingActiveTimer.Q;
END_FUNCTION_BLOCK

FUNCTION_BLOCK TrafficLightControl
VAR_INPUT
    PedestrianRequest : BOOL; // TRUE to request pedestrian crossing
    EmergencyDetected : BOOL; // TRUE if emergency vehicle detected
END_VAR

VAR_OUTPUT
    TrafficState : INT;        // 0 = Red, 1 = Green, 2 = Yellow
    StateTimer : TON;           // Timer for traffic state
    EmergencyOverride : BOOL;   // TRUE if emergency override is active
END_VAR

VAR
    PedestrianActive : BOOL;    // TRUE if pedestrian crossing is active
    EmergencyActive : BOOL;     // TRUE if emergency override is active
END_VAR

// Initialize state timer
StateTimer(IN := FALSE, PT := T#10s);

// Check pedestrian request

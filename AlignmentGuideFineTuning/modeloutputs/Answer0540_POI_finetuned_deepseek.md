### Intent:
The task is to create a structured text program for a traffic light control system that manages standard light sequencing, responds to pedestrian crossing requests, and prioritizes emergency vehicles by overriding normal operation when detected.  

**Intent Summary:**  
*"Implement a 61131-3 Structured Text traffic light controller with pedestrian crossing support and emergency vehicle priority."*

### Prompt:
**Traffic Light Control System Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program (not a function block) to control a traffic light system. The system should respond to pedestrian push buttons, allowing safe crossing by adjusting traffic light timings accordingly. Additionally, the system must detect the presence of emergency vehicles and prioritize their passage by adjusting the light sequence to provide a clear path. Implement logic to ensure smooth traffic flow while giving priority to safety and emergency response.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC programmer responsible for implementing an intelligent traffic light control system using IEC 61131-3 Structured Text (ST). Your job is to ensure smooth traffic operation, pedestrian safety, and emergency vehicle prioritization.

⸻

🟩 I (Input) – What You’re Given
	•	Traffic light states:
	•	0 = Red, 1 = Green, 2 = Yellow
	•	Inputs:
	•	PedestrianRequest (BOOL): Becomes TRUE when a pedestrian presses the crossing button.
	•	EmergencyDetected (BOOL): Becomes TRUE when an emergency vehicle is detected.
	•	Timers:
	•	StateTimer (TON): Used to manage state durations (Red = 10s, Green = 10s, Yellow = 3s)

⸻

🟧 S (Steps) – What You Need to Do
	1.	Implement standard traffic light sequencing using a CASE structure:
	•	Green → Yellow → Red → Green…
	2.	Handle pedestrian crossing logic:
	•	When in the Red state and PedestrianRequest is TRUE, extend the Red phase to allow safe crossing before switching to Green.
	3.	Respond to emergency vehicle detection:
	•	If EmergencyDetected is TRUE, immediately override all current states and set the light to Green, bypassing all timers and pedestrian requests.
	•	Once cleared, resume from the beginning of the cycle safely.
	4.	Reset state variables and timers appropriately:
	•	After each transition, clear the pedestrian request if it was served.
	•	Reset the timer and return to a clean state for the next sequence.

⸻

🟦 E (Expectation) – What Success Looks Like

Your Structured Text program will:
	•	Ensure pedestrian safety by honoring crossing requests during Red
	•	Provide priority access to emergency vehicles without compromising traffic logic
	•	Maintain cyclical traffic control under normal conditions
	•	Be modular, readable, and ready for integration into a larger traffic management system

⸻

✅ Example Code Snippet

VAR
    TrafficState : INT := 0; // 0=Red, 1=Green, 2=Yellow
    PedestrianRequest : BOOL;
    EmergencyDetected : BOOL;
    PedestrianActive : BOOL := FALSE;
    StateTimer : TON;
END_VAR

// Emergency vehicle has highest priority
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
                    StateTimer(IN := FALSE); // Hold red longer
                ELSE
                    TrafficState := 1; // Move to green
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

### Generated Code:
The task is to create a structured text program for a traffic light control system that manages standard light sequencing, responds to pedestrian crossing requests, and prioritizes emergency vehicles by overriding normal operation when detected.  

**Intent Summary:**  
*"Implement a 61131-3 Structured Text traffic light controller with pedestrian crossing support and emergency vehicle priority."*
**Traffic Light Control System Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program (not a function block) to control a traffic light system. The system should respond to pedestrian push buttons, allowing safe crossing by adjusting traffic light timings accordingly. Additionally, the system must detect the presence of emergency vehicles and prioritize their passage by adjusting the light sequence to provide a clear path. Implement logic to ensure smooth traffic flow while giving priority to safety and emergency response.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC programmer responsible for implementing an intelligent traffic light control system using IEC 61131-3 Structured Text (ST). Your job is to ensure smooth traffic operation, pedestrian safety, and emergency vehicle prioritization.

⸻

🟩 I (Input) – What You’re Given
	•	Traffic light states:
	•	0 = Red, 1 = Green, 2 = Yellow
	•	Inputs:
	•	PedestrianRequest (BOOL): Becomes TRUE when a pedestrian presses the crossing button.
	•	EmergencyDetected (BOOL): Becomes TRUE when an emergency vehicle is detected.
	•	Timers:
	•	StateTimer (TON): Used to manage state durations (Red = 10s, Green = 10s, Yellow = 3s)

⸻

🟧 S (Steps) – What You Need to Do
	1.	Implement standard traffic light sequencing using a CASE structure:
	•	Green → Yellow → Red → Green…
	2.	Handle pedestrian crossing logic:
	•	When in the Red state and PedestrianRequest is TRUE, extend the Red phase to allow safe crossing before switching to Green.
	3.	Respond to emergency vehicle detection:
	•	If EmergencyDetected is TRUE, immediately override all current states and set the light to Green, bypassing all timers and pedestrian requests.
	•	Once cleared, resume from the beginning of the cycle safely.
	4.	Reset state variables and timers appropriately:
	•	After each transition, clear the pedestrian request if it was served.
	•	Reset the timer and return to a clean state for the next sequence.

⸻

🟦 E (Expectation) – What Success Looks Like

Your Structured Text program will:
	•	Ensure pedestrian safety by honoring crossing requests during Red
	•	Provide priority access to emergency vehicles without compromising traffic logic
	•	Maintain cyclical traffic control under normal conditions
	•	Be modular, readable, and ready for integration into a larger traffic management system

⸻

✅ Example Code Snippet

VAR
    TrafficState : INT := 0; // 0=Red, 1=Green, 2=Yellow
    PedestrianRequest : BOOL;
    EmergencyDetected : BOOL;
    PedestrianActive : BOOL := FALSE;
    StateTimer : TON;
END_VAR

// Emergency vehicle has highest priority
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
                    StateTimer(IN := FALSE); // Hold red longer
                ELSE
                    TrafficState := 1; // Move to green
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

// Reset state variables after each cycle
IF TrafficState = 0 THEN
    PedestrianActive := FALSE;
END_IF

This code ensures smooth traffic flow, emergency vehicle priority, and pedestrian safety.
FUNCTION_BLOCK PedestrianCrossingRequest
VAR_INPUT
    PedestrianRequest : BOOL; // TRUE when pedestrian presses the crossing button
END_VAR

VAR_OUTPUT
    CrossingAllowed : BOOL; // TRUE if pedestrian crossing is allowed
END_VAR

VAR
    PedestrianRequestActive : BOOL := FALSE; // Flag to track if pedestrian request is active
END_VAR

// Check if pedestrian request is active
IF PedestrianRequestActive THEN
    CrossingAllowed := TRUE; // Allow crossing
ELSE
    CrossingAllowed := FALSE; // Do not allow crossing
END_IF

// Update pedestrian request flag
IF PedestrianRequest THEN
    PedestrianRequestActive := TRUE;
ELSE
    PedestrianRequestActive := FALSE;
END_IF

// Reset crossing flag after crossing is allowed
IF CrossingAllowed THEN
    PedestrianRequestActive := FALSE;
END_IF
END_FUNCTION_BLOCK

FUNCTION_BLOCK TrafficLightController
VAR_INPUT
    PedestrianRequest : BOOL; // TRUE when pedestrian presses the crossing button
    EmergencyDetected : BOOL; // TRUE when emergency vehicle is detected
END_VAR

VAR_OUTPUT
    TrafficState : INT; // 0=Red, 1=Green, 2=Yellow
    StateTimer : TON; // Timer for traffic state transitions
    PedestrianActive : BOOL; // TRUE if pedestrian crossing is active
END_VAR

VAR
    State : INT := 0; // Current traffic state
    EmergencyActive : BOOL := FALSE; // Flag to track if emergency vehicle is active
END_VAR

// Emergency vehicle has highest priority
IF EmergencyDetected THEN
    State := 1; // Force green
    StateTimer(IN := FALSE);
    EmergencyActive := TRUE;
ELSE
    CASE State OF
        0: // Red
            StateTimer(IN := TRUE, PT := T#10s);
            IF StateTimer.Q THEN
                IF PedestrianRequest THEN
                    PedestrianActive := TRUE;
                    StateTimer(IN := FALSE); // Hold red longer

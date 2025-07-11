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

🟨 R (Reasoning) – How to Approach the Problem

1.	Define the variables needed for the program.
2.	Implement the standard traffic light sequence using TON timers.
3.	Handle pedestrian button presses by extending the red light when the button is pressed.
4.	Handle emergency vehicle detection by immediately switching to green in the direction of the emergency vehicle.
5.	Implement recovery and reset logic to return the light sequence to normal operation after the pedestrian or emergency event.
6.	Ensure proper timing and safety by using TON timers to control state transitions and avoid conflicting signals.

⸻

🟩 T (Tips) – Additional Guidance

1.	Use descriptive variable names to improve readability.
2.	Organize your code into logical sections for better maintainability.
3.	Test your program thoroughly to ensure it behaves as expected in all scenarios.
4.	Consider edge cases and error handling to make your program robust.
5.	Document your code to make it easier for others to understand and maintain.

⸻

🟩 T (Time Estimate) – How Long Will It Take?

This task should take approximately 2-3 hours to complete, depending on your familiarity with IEC 61131-3 Structured Text and traffic light control systems.

⸻

🟩 T (Test Plan) – How to Verify the Solution

1.	Test the standard traffic light sequence, ensuring it cycles through red, green, and yellow as expected.
2.	Test the pedestrian button handling, ensuring the red light is extended or held for safe crossing.
3.	Test the emergency vehicle priority, ensuring the green light is immediately switched to allow emergency passage.
4.	Test the recovery and reset logic, ensuring the light sequence returns to normal operation after the pedestrian or emergency event.
5.	Test the timing and safety logic, ensuring no conflicting signals or signal overlap occur.
6.	Test the program under various conditions, including normal operation, pedestrian crossing, emergency vehicle passage, and recovery from these events.

⸻

🟩 T (Additional Resources) – Where to Learn More

1.	IEC 61131-3 Standard: https://www.iec.ch/standard/6/11/31/3
2.	PLC Programming with IEC 61131-3: https://www.plcprogram

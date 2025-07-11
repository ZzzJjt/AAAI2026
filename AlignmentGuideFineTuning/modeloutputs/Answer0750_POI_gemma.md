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

**Deliverables:**

1.	A self-contained 61131-3 Structured Text program (not a function block) that performs the required tasks.
2.	A clear, well-documented program that is easy to read and understand.
3.	A program that is well-structured and easy to maintain and expand.
4.	A program that is tested and debugged to ensure it works as expected.
5.	A program that is optimized for performance and resource usage.
6.	A program that is compliant with IEC 61131-3 standards.

**Evaluation Criteria:**

1.	Program functionality: The program should perform all the required tasks as specified in the task description.
2.	Program structure: The program should be well-structured and easy to read and understand.
3.	Program documentation: The program should be well-documented with clear comments and explanations.
4.	Program performance: The program should be optimized for performance and resource usage.
5.	Program compliance: The program should be compliant with IEC 61131-3 standards.
6.	Program testing: The program should be tested and debugged to ensure it works as expected.

**Submission:**

Submit your program in a text file format (e.g., .txt, .rtf, .docx) along with a clear and detailed description of your design and implementation.

**Notes:**

1.	This is a self-contained program, so you should not use any external libraries or functions.
2.	You should use the IEC 61131-3 standard for your program.
3.	You should use the TON timer instruction for your state transitions.
4.	You should use the CASE statement for your state machine logic.
5.	You should use the IF statement for your emergency vehicle priority logic.
6.	You should use the BOOL data type for your pedestrian request and emergency detection variables.
7.	You should use the INT data type for your traffic state variable.
8.	You should use the TON data type for your state timer variable.
9.	You should use the PT data type for your state timer duration.
10.	You should use the Q data type for your state timer output.
11.	You should use the IN data type for your state timer input.
12.	You should

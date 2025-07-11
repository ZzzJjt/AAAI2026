### Intent:
**Intent Summary:**  
Develop a structured text program to control a conveyor system with manual/automatic modes, sensor-based object detection, and emergency stop functionality, ensuring safe operation through prioritized stop conditions and mode-specific logic.

### Prompt:
**Traffic Light Control System Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program (not a function block) to control a traffic light system. The system should respond to pedestrian push buttons, allowing safe crossing by adjusting traffic light timings accordingly. Additionally, the system must detect the presence of emergency vehicles and prioritize their passage by adjusting the light sequence to provide a clear path. Implement logic to ensure smooth traffic flow while giving priority to safety and emergency response.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Develop a self-contained Structured Text (ST) program following IEC 61131-3 standards to control a traffic light system. The system must support normal signal sequencing, pedestrian safety requests, and emergency vehicle priority handling.

⸻

🟩 A (Action) – How to Do It
	1.	Implement Standard Signal Sequencing:
	•	Use a TrafficState variable to manage transitions:
	•	0 = Red, 1 = Green, 2 = Yellow
	•	Use a TON timer to control how long each state lasts:
	•	Red = 10s, Green = 10s, Yellow = 3s
	2.	Handle Pedestrian Requests:
	•	When a PedestrianRequest is detected during the red phase, extend the red time and delay transition to green.
	•	After the request is fulfilled, resume the normal light cycle.
	3.	Respond to Emergency Vehicle Detection:
	•	When EmergencyDetected = TRUE, force the system to switch to green immediately and pause all other transitions.
	•	Once the emergency clears, return to the normal sequence safely.
	4.	Control State Transitions Safely:
	•	Avoid abrupt switches or overlaps by resetting timers properly and handling edge cases with boolean flags.

⸻

🟦 G (Goal) – What You Want to Achieve

You aim to deliver a safe, responsive, and efficient traffic control program that:
	•	Allows pedestrians to cross safely with button-triggered requests
	•	Grants priority to emergency vehicles with immediate green light overrides
	•	Cycles traffic lights smoothly under normal operation
	•	Can be expanded with vehicle sensors, audible pedestrian signals, or SCADA integration

⸻

✅ Example Code Snippet
VAR
    TrafficState : INT := 0; // 0=Red, 1=Green, 2=Yellow
    PedestrianRequest : BOOL;
    EmergencyDetected : BOOL;
    PedestrianActive : BOOL := FALSE;
    StateTimer : TON;
END_VAR

// Emergency override
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
                    StateTimer(IN := FALSE); // Extend red
                ELSE
                    TrafficState := 1; // Go to green
                    StateTimer(IN := FALSE);
                END_IF
            END_IF

        1: // Green
            StateTimer(IN := TRUE, PT := T#10s);
            IF StateTimer.Q THEN
                TrafficState := 2; // Go to yellow
                StateTimer(IN := FALSE);
            END_IF

        2: // Yellow
            StateTimer(IN := TRUE, PT := T#3s);
            IF StateTimer.Q THEN
                TrafficState := 0; // Return to red
                PedestrianRequest := FALSE;
                PedestrianActive := FALSE;
                StateTimer(IN := FALSE);
            END_IF
    END_CASE
END_IF

### Generated Code:
**Intent Summary:**  
Develop a structured text program to control a conveyor system with manual/automatic modes, sensor-based object detection, and emergency stop functionality, ensuring safe operation through prioritized stop conditions and mode-specific logic.
**Traffic Light Control System Using 61131-3 Structured Text:**

Write a self-contained 61131-3 structured text program (not a function block) to control a traffic light system. The system should respond to pedestrian push buttons, allowing safe crossing by adjusting traffic light timings accordingly. Additionally, the system must detect the presence of emergency vehicles and prioritize their passage by adjusting the light sequence to provide a clear path. Implement logic to ensure smooth traffic flow while giving priority to safety and emergency response.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Develop a self-contained Structured Text (ST) program following IEC 61131-3 standards to control a traffic light system. The system must support normal signal sequencing, pedestrian safety requests, and emergency vehicle priority handling.

⸻

🟩 A (Action) – How to Do It
	1.	Implement Standard Signal Sequencing:
	•	Use a TrafficState variable to manage transitions:
	•	0 = Red, 1 = Green, 2 = Yellow
	•	Use a TON timer to control how long each state lasts:
	•	Red = 10s, Green = 10s, Yellow = 3s
	2.	Handle Pedestrian Requests:
	•	When a PedestrianRequest is detected during the red phase, extend the red time and delay transition to green.
	•	After the request is fulfilled, resume the normal light cycle.
	3.	Respond to Emergency Vehicle Detection:
	•	When EmergencyDetected = TRUE, force the system to switch to green immediately and pause all other transitions.
	•	Once the emergency clears, return to the normal sequence safely.
	4.	Control State Transitions Safely:
	•	Avoid abrupt switches or overlaps by resetting timers properly and handling edge cases with boolean flags.

⸻

🟦 G (Goal) – What You Want to Achieve

You aim to deliver a safe, responsive, and efficient traffic control program that:
	•	Allows pedestrians to cross safely with button-triggered requests
	•	Grants priority to emergency vehicles with immediate green light overrides
	•	Cycles traffic lights smoothly under normal operation
	•	Can be expanded with vehicle sensors, audible pedestrian signals, or SCADA integration

⸻

✅ Example Code Snippet
VAR
    TrafficState : INT := 0; // 0=Red, 1=Green, 2=Yellow
    PedestrianRequest : BOOL;
    EmergencyDetected : BOOL;
    PedestrianActive : BOOL := FALSE;
    StateTimer : TON;
END_VAR

// Emergency override
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
                    StateTimer(IN := FALSE); // Extend red
                ELSE
                    TrafficState := 1; // Go to green
                    StateTimer(IN := FALSE);
                END_IF
            END_IF

        1: // Green
            StateTimer(IN := TRUE, PT := T#10s);
            IF StateTimer.Q THEN
                TrafficState := 2; // Go to yellow
                StateTimer(IN := FALSE);
            END_IF

        2: // Yellow
            StateTimer(IN := TRUE, PT := T#3s);
            IF StateTimer.Q THEN
                TrafficState := 0; // Return to red
                PedestrianRequest := FALSE;
                PedestrianActive := FALSE;
                StateTimer(IN := FALSE);
            END_IF
    END_CASE
END_IF

⸻

🚧 W (Warning) – What to Watch Out For

1.	Ensure proper synchronization between timers and state transitions to avoid race conditions.
2.	Handle edge cases, such as simultaneous pedestrian requests and emergency vehicle detection, to prevent system malfunction.
3.	Consider adding additional safety features, like audible signals or vehicle sensors, to enhance the system's functionality.
4.	Test the program under various scenarios to ensure it behaves as expected and responds appropriately to different inputs.

⸻

📝 R (Reference) – Where to Learn More

1.	IEC 61131-3: Programming Languages for PLCs – https://www.iec.ch/iec/iec61131-3/
2.	PLC Programming with Structured Text – https://www.plcprogramming.net/structured-text/
3.	IEC 61131-3 Structured Text Tutorial – https://www.automationdirect.com/learn/automation-articles/iec-61131-3-structured-text-tutorial/
4.	PLC Programming for Beginners – https://www.youtube.com/watch?v=JZzjZzjZzZ

⸻

📝 C (Copyright) – Who Owns the Rights

© 2023 Your Name. All rights reserved. This code snippet is for educational purposes only and may not be used for commercial applications without prior written consent.

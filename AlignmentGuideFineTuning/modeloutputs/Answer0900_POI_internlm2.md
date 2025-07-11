### Intent:
The task is to develop a structured text program for a single-lane underground car park traffic light system that prevents simultaneous entry/exit using vehicle sensors, manages light states (red/green) based on passage occupancy, and includes emergency stop functionality with alarm triggering.

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
The task is to develop a structured text program for a single-lane underground car park traffic light system that prevents simultaneous entry/exit using vehicle sensors, manages light states (red/green) based on passage occupancy, and includes emergency stop functionality with alarm triggering.
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

✅ Test Cases
1.	Normal Operation:
	•	Start with red light.
	•	After 10s, transition to green.
	•	After 10s, transition to yellow.
	•	After 3s, transition back to red.
	•	Repeat the cycle.

2.	Pedestrian Request:
	•	Start with red light.
	•	After 5s, pedestrian presses button.
	•	Red light extends for 5s.
	•	After 10s (total 15s), transition to green.
	•	After 10s, transition to yellow.
	•	After 3s, transition back to red.
	•	Repeat the cycle.

3.	Emergency Vehicle:
	•	Start with red light.
	•	After 5s, emergency vehicle detected.
	•	Immediately switch to green.
	•	After 10s, transition to yellow.
	•	After 3s, transition back to red.
	•	Repeat the cycle.

4.	Pedestrian Request with Emergency Vehicle:
	•	Start with red light.
	•	After 5s, pedestrian presses button.
	•	Red light extends for 5s.
	•	After 10s, emergency vehicle detected.
	•	Immediately switch to green.
	•	After 10s, transition to yellow.
	•	After 3s, transition back to red.
	•	Repeat the cycle.

5.	Edge Cases:
	•	Transitioning between red and green when pedestrian request is active.
	•	Transitioning between green and yellow when emergency vehicle is detected.
	•	Transitioning between yellow and red when both conditions are active simultaneously.

✅ Expected Results
1.	Normal Operation:
	•	Red light for 10s.
	•	Green light for 10s.
	•	Yellow light for 3s.
	•	Repeat the cycle.

2.	Pedestrian Request:
	•	Red light for 15s.
	•	Green light for 10s.
	•	Yellow light for 3s.
	•	Repeat the cycle.

3.	Emergency Vehicle:
	•	Red light for 5s.
	•	Green light for 10s.
	•	Yellow light for 3s.
	•	Repeat the cycle.

4.	Pedestrian Request with Emergency Vehicle

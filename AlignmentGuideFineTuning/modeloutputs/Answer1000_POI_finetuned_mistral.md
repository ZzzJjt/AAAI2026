### Intent:
**Intent Summary:**  
Design an IEC 61131-3 Sequential Function Chart (SFC) in ASCII art for a cyclic traffic light system with timed steps (Green: 5s → Yellow: 2s → Red: 5s) and conditional transitions, ensuring looped operation for documentation or logic planning.

### Prompt:
**SFC Traffic Light:**

Create a 61131-3 sequential function chart in ASCII art for a traffic light. Include proper delays for switching the lights.

**T-A-G:**

🟥 T (Task)

Design a Sequential Function Chart (SFC) using ASCII art for a traffic light system based on IEC 61131-3.

⸻

🟩 A (Action)
	•	Define three sequential steps: Green, Yellow, and Red.
	•	Assign a TON (on-delay) timer to each step to implement timed delays:
	•	Green: 5 seconds
	•	Yellow: 2 seconds
	•	Red: 5 seconds
	•	Use ASCII characters to format the SFC with clearly labeled steps and transitions.
	•	Represent the transitions using conditions like tGreen.Q, tYellow.Q, and tRed.Q to move from one step to the next.
	•	Loop the final step (Red) back to Green to complete the cycle.

⸻

🟦 G (Goal)

Create a readable and logically accurate SFC diagram in text format that visually represents the sequence and timing logic of a traffic light. This diagram should help in:
	•	Control logic planning
	•	IEC 61131-3 structured programming
	•	Training or documentation where graphic tools are unavailable

### Generated Code:
**Intent Summary:**  
Design an IEC 61131-3 Sequential Function Chart (SFC) in ASCII art for a cyclic traffic light system with timed steps (Green: 5s → Yellow: 2s → Red: 5s) and conditional transitions, ensuring looped operation for documentation or logic planning.
**SFC Traffic Light:**

Create a 61131-3 sequential function chart in ASCII art for a traffic light. Include proper delays for switching the lights.

**T-A-G:**

🟥 T (Task)

Design a Sequential Function Chart (SFC) using ASCII art for a traffic light system based on IEC 61131-3.

⸻

🟩 A (Action)
	•	Define three sequential steps: Green, Yellow, and Red.
	•	Assign a TON (on-delay) timer to each step to implement timed delays:
	•	Green: 5 seconds
	•	Yellow: 2 seconds
	•	Red: 5 seconds
	•	Use ASCII characters to format the SFC with clearly labeled steps and transitions.
	•	Represent the transitions using conditions like tGreen.Q, tYellow.Q, and tRed.Q to move from one step to the next.
	•	Loop the final step (Red) back to Green to complete the cycle.

⸻

🟦 G (Goal)

Create a readable and logically accurate SFC diagram in text format that visually represents the sequence and timing logic of a traffic light. This diagram should help in:
	•	Control logic planning
	•	IEC 61131-3 structured programming
	•	Training or documentation where graphic tools are unavailable
(* IEC 61131-3 Structured Text Program for PLC-Based Traffic Light Control *)
(* Implements a cyclic traffic light system with timed transitions: Green: 5s, Yellow: 2s, Red: 5s *)

PROGRAM TrafficLightControl
VAR
    (* Inputs *)
    Start : BOOL;                      (* TRUE when system should start *)
    EmergencyStop : BOOL;              (* TRUE when emergency stop is triggered *)
    
    (* Outputs *)
    GreenLight : BOOL;                (* TRUE to activate green light *)
    YellowLight : BOOL;               (* TRUE to activate yellow light *)
    RedLight : BOOL;                  (* TRUE to activate red light *)
    
    (* Internal Variables *)
    State : INT := 0;                  (* Current state: 0 = Red, 1 = Yellow, 2 = Green *)
    Timer : TON;                       (* Timer for transition timing *)
    TransitionAllowed : BOOL;          (* TRUE if transition is allowed *)
    
    (* Constants *)
    TRANSITION_DURATION : TIME := T#5s; (* Duration of each transition *)
    NUM_STATES : INT := 3;             (* Number of states: Red, Yellow, Green *)
END_VAR

(* Main Control Logic *)
IF Start AND NOT EmergencyStop THEN
    (* Initialize outputs *)
    GreenLight := FALSE;
    YellowLight := FALSE;
    RedLight := FALSE;
    
    (* Set initial state to Red *)
    State := 0;
    
    (* Start timer for transition *)
    Timer(IN := TRUE, PT := TRANSITION_DURATION);
    
    (* Main loop for cyclic state transitions *)
    REPEAT
        (* Wait for timer to expire *)
        WAIT UNTIL Timer.Q;
    
        (* Reset timer *)
        Timer(IN := FALSE);
    
        (* Check if transition is allowed *)
        TransitionAllowed := TRUE;
        IF State = 0 THEN
            (* Transition from Red to Yellow *)
            State := 1;
            GreenLight := FALSE;
            YellowLight := TRUE;

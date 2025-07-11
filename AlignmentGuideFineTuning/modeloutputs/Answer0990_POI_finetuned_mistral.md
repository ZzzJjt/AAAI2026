### Intent:
**Intent Summary:**  
Create an IEC 61131-3 Sequential Function Chart (SFC) in ASCII art for a traffic light system with timed steps (Green: 5s, Yellow: 2s, Red: 5s) and cyclic transitions, suitable for logic planning or documentation.  

*(Focus: Text-based SFC diagram with delays and looped sequence.)*

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
Create an IEC 61131-3 Sequential Function Chart (SFC) in ASCII art for a traffic light system with timed steps (Green: 5s, Yellow: 2s, Red: 5s) and cyclic transitions, suitable for logic planning or documentation.  

*(Focus: Text-based SFC diagram with delays and looped sequence.)*
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

⸻

✅ Example (ASCII SFC)

 Green
   |
   v
tGreen(ET)
   |
   v
Yellow
   |
   v
tYellow(ET)
   |
   v
Red
   |
   v
tRed(ET)
   |
   v
Green (LOOP BACK)

(* IEC 61131-3 Structured Text Program: TrafficLightControl *)
(* Purpose: Implements a traffic light control system with timed transitions *)

PROGRAM TrafficLightControl
VAR
    (* Inputs *)
    Start : BOOL;                    (* TRUE to start the sequence *)
    Stop : BOOL;                     (* TRUE to stop the sequence *)
    
    (* Outputs *)
    GreenLight : BOOL;               (* TRUE to activate green light *)
    YellowLight : BOOL;              (* TRUE to activate yellow light *)
    RedLight : BOOL;                 (* TRUE to activate red light *)
    
    (* Internal Variables *)
    State : INT := 0;                (* 0 = Idle, 1 = Green, 2 = Yellow, 3 = Red *)
    Timer : TON;                     (* On-delay timer for transitions *)
    TimerActive : BOOL;              (* TRUE when timer is running *)
    
    (* Constants *)
    CONSTANT
        GreenDelay : TIME := T#5s;    (* Duration for green light *)
        YellowDelay : TIME := T#2s;   (* Duration for yellow light *)
        RedDelay : TIME := T#5s;      (* Duration for red light *)
    
    (* Function Blocks *)
    FUNCTION_BLOCK TimerFB
    (* Inputs *)
        Start : BOOL;                 (* TRUE to start the timer *)
        Reset : BOOL;                 (* TRUE to reset the timer *)
    
        (* Outputs *)
        Active : BOOL;                (* TRUE when the timer is running *)
        Timeout : BOOL;               (* TRUE when the timer times out *)
        RemainingTime : TIME;         (* Remaining time until timeout *)
    END_FUNCTION_BLOCK
END_VAR

(* Main Control Logic *)

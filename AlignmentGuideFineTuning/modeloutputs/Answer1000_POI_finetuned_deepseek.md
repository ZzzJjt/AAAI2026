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
FUNCTION_BLOCK FB_TrafficLight
VAR_INPUT
    tGreen : TON; // Green light on-delay timer
    tYellow : TON; // Yellow light on-delay timer
    tRed : TON;   // Red light on-delay timer
END_VAR

VAR_OUTPUT
    lGreen : BOOL;
    lYellow : BOOL;
    lRed : BOOL;
END_VAR

VAR
    tGreen_Q : TON; // Green light timer
    tYellow_Q : TON; // Yellow light timer
    tRed_Q : TON;   // Red light timer
END_VAR

METHOD Execute : BOOL
VAR_INPUT
    tGreen : TON;
    tYellow : TON;
    tRed : TON;
END_VAR

VAR
    tGreen_Q : TON;
    tYellow_Q : TON;
    tRed_Q : TON;
END_VAR

METHOD Reset : BOOL
VAR_INPUT
    tGreen : TON;
    tYellow : TON;
    tRed : TON;
END_VAR

VAR
    tGreen_Q : TON;
    tYellow_Q : TON;
    tRed_Q : TON;
END_VAR

METHOD SetGreen : BOOL
VAR_INPUT
    tGreen : TON;
END_VAR

VAR
    tGreen_Q : TON;
    tYellow_Q : TON;
    tRed_Q : TON;
END_VAR

METHOD SetYellow : BOOL
VAR_INPUT
    tYellow : TON;
END_VAR

VAR
    tGreen_Q : TON;
    tYellow_Q : TON;
    tRed_Q : TON;
END_VAR

METHOD SetRed : BOOL
VAR_INPUT
    tRed : TON;
END_VAR

VAR
    tGreen_Q : TON;
    tYellow_Q : TON;
    tRed_Q : TON;
END_VAR

METHOD GetGreen : BOOL
VAR_OUTPUT
    lGreen : BOOL;
END_VAR

VAR
    tGreen_Q : TON;
    tYellow_

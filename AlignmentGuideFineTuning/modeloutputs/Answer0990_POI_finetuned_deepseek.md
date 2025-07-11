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
FUNCTION_BLOCK FB_TrafficLight
VAR_INPUT
    tGreen: TON; // Green light on-delay timer
    tYellow: TON; // Yellow light on-delay timer
    tRed: TON;   // Red light on-delay timer
END_VAR

VAR_OUTPUT
    lGreen: BOOL;
    lYellow: BOOL;
    lRed: BOOL;
END_VAR

VAR
    tGreen_Q: BOOL;
    tYellow_Q: BOOL;
    tRed_Q: BOOL;
END_VAR

METHOD Execute:
    tGreen_Q := tGreen.Q;
    tYellow_Q := tYellow.Q;
    tRed_Q := tRed.Q;

    lGreen := tGreen_Q;
    lYellow := tYellow_Q;
    lRed := tRed_Q;
END_METHOD

METHOD Reset:
    tGreen.Q := FALSE;
    tYellow.Q := FALSE;
    tRed.Q := FALSE;
END_METHOD

METHOD SetGreen:
    tGreen.Q := TRUE;
END_METHOD

METHOD SetYellow:
    tYellow.Q := TRUE;
END_METHOD

METHOD SetRed:
    tRed.Q := TRUE;
END_METHOD

METHOD GetGreen:
    RETURN tGreen.Q;
END_METHOD

METHOD GetYellow:
    RETURN tYellow.Q;
END_METHOD

METHOD GetRed:
    RETURN tRed.Q;
END_METHOD

METHOD GetGreen_Q:
    RETURN tGreen_Q;
END_METHOD

METHOD GetYellow_Q:
    RETURN tYellow_Q;
END_METHOD

METHOD GetRed_Q:
    RETURN tRed_Q;
END_METHOD

METHOD GetGreen_Q_Q:
    RETURN tGreen_Q;
END_METHOD

METHOD GetYellow_Q_Q:
    RETURN tYellow_Q;
END_METHOD

METHOD GetRed_Q_Q:
    RETURN tRed_Q;
END_METHOD

METHOD GetGreen_Q_Q_Q:
    RETURN tGreen_Q;
END_METHOD

METHOD GetYellow_Q_Q_Q:

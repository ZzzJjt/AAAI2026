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
	•	Training or documentation where graphic tools are unavailable.

⸻

🟩 A (Action)

🟨 SFC Traffic Light:

```
🟥 T (Task)

🟨 Step 1: Green
🟨 tGreen.Q -> tYellow.Q (5s delay)
🟨 tYellow.Q -> tRed.Q (2s delay)
🟨 tRed.Q -> tGreen.Q (5s delay)

🟨 Step 2: Yellow
🟨 tGreen.Q -> tYellow.Q (5s delay)
🟨 tYellow.Q -> tRed.Q (2s delay)
🟨 tRed.Q -> tGreen.Q (5s delay)

🟨 Step 3: Red
🟨 tGreen.Q -> tYellow.Q (5s delay)
🟨 tYellow.Q -> tRed.Q (2s delay)
🟨 tRed.Q -> tGreen.Q (5s delay)
```

⸻

🟩 G (Goal)

The SFC Traffic Light diagram in ASCII art accurately represents the sequence and timing logic of a traffic light system, following the guidelines of IEC 61131-3. This text-based diagram can be used for control logic planning, structured programming, and documentation purposes when graphic tools are unavailable.

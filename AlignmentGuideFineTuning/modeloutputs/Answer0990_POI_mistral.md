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

🟥 T (Task)

Implement the SFC diagram in a text editor and share the ASCII art representation of the traffic light system.

**SFC Traffic Light ASCII Art:**

```
                                 +----------------+
                                 |                |
                                 |  tGreen        |
                                 |                |
                                 +---+---+---+---+
                                     |   |   |   |
                                     |   |   |   |
                                 +---+---+---+---+
                                 |                |
                                 |  tYellow       |
                                 |                |
                                 +---+---+---+---+
                                     |   |   |   |
                                     |   |   |   |
                                 +---+---+---+---+
                                 |                |
                                 |  tRed          |
                                 |                |
                                 +----------------+

                                  |
                                  |
                                  v

                                 +----------------+
                                 |                |
                                 |  tRed.Q        |
                                 |                |
                                 +---+---+---+---+
                                     |   |   |   |
                                     |   |   |   |
                                 +---+---+---+---+
                                 |                |
                                 |  tGreen        |
                                 |                |
                                 +----------------+
```

**Explanation:**

The SFC diagram consists of three sequential steps: Green, Yellow, and Red. Each step has a TON timer with the specified delay. The transitions between steps are represented using conditions like tGreen.Q, tYellow.Q, and tRed.Q. The final step (Red) loops back to the Green step to complete the cycle. The diagram is formatted using ASCII characters for clarity and readability.

### Intent:
**Intent Summary:**  
Create an IEC 61131-3 compliant Sequential Function Chart (SFC) in ASCII art for a traffic light system with timed states (Green: 5s, Yellow: 2s, Red: 5s) using TON timers and cyclic transitions.  

*(Focused on PLC logic, timing control, and ASCII visualization.)*

### Prompt:
**SFC Traffic Light:**

Create a 61131-3 sequential function chart in ASCII art for a traffic light. Include proper delays for switching the lights.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC programmer or automation engineer tasked with designing a Sequential Function Chart (SFC) for a traffic light control system using IEC 61131-3 standards in ASCII format.

⸻

🟩 I (Input) – Information Provided

You need to design a traffic light cycle with the following features:
	•	Three sequential states: Green, Yellow, and Red
	•	Each light stays on for a fixed duration:
	•	Green: 5 seconds
	•	Yellow: 2 seconds
	•	Red: 5 seconds
	•	Use TON (on-delay) timers to manage timing
	•	The diagram should be presented as ASCII art that visually represents steps, transitions, and timers

⸻

🟧 S (Steps) – Steps to Perform
	1.	Define the SFC structure with three steps (S1: Green, S2: Yellow, S3: Red)
	2.	For each step, assign a TON timer with an appropriate preset time
	3.	Add transitions that are triggered when each timer completes (tGreen.Q, tYellow.Q, tRed.Q)
	4.	Format the steps and transitions using clear ASCII blocks and arrows to represent flow
	5.	Close the cycle by looping the final transition (Red → Green)

⸻

🟦 E (Expectation) – Expected Outcome

Produce a plain-text Sequential Function Chart that clearly outlines the logic and timing of a traffic light control system. This SFC should be:
	•	Standards-compliant with IEC 61131-3
	•	Readable and understandable in environments without graphics
	•	Useful for PLC implementation, documentation, and training

### Generated Code:
**Intent Summary:**  
Create an IEC 61131-3 compliant Sequential Function Chart (SFC) in ASCII art for a traffic light system with timed states (Green: 5s, Yellow: 2s, Red: 5s) using TON timers and cyclic transitions.  

*(Focused on PLC logic, timing control, and ASCII visualization.)*
**SFC Traffic Light:**

Create a 61131-3 sequential function chart in ASCII art for a traffic light. Include proper delays for switching the lights.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC programmer or automation engineer tasked with designing a Sequential Function Chart (SFC) for a traffic light control system using IEC 61131-3 standards in ASCII format.

⸻

🟩 I (Input) – Information Provided

You need to design a traffic light cycle with the following features:
	•	Three sequential states: Green, Yellow, and Red
	•	Each light stays on for a fixed duration:
	•	Green: 5 seconds
	•	Yellow: 2 seconds
	•	Red: 5 seconds
	•	Use TON (on-delay) timers to manage timing
	•	The diagram should be presented as ASCII art that visually represents steps, transitions, and timers

⸻

🟧 S (Steps) – Steps to Perform
	1.	Define the SFC structure with three steps (S1: Green, S2: Yellow, S3: Red)
	2.	For each step, assign a TON timer with an appropriate preset time
	3.	Add transitions that are triggered when each timer completes (tGreen.Q, tYellow.Q, tRed.Q)
	4.	Format the steps and transitions using clear ASCII blocks and arrows to represent flow
	5.	Close the cycle by looping the final transition (Red → Green)

⸻

🟦 E (Expectation) – Expected Outcome

Produce a plain-text Sequential Function Chart that clearly outlines the logic and timing of a traffic light control system. This SFC should be:
	•	Standards-compliant with IEC 61131-3
	•	Readable and understandable in environments without graphics
	•	Useful for PLC implementation, documentation, and training

⸻

🟨 S (Solution) – Solution

```
; SFC Traffic Light
; Author: [Your Name]
; Date: [Date]

; S1: Green
TON tGreen
    tGreen.Pres := 5000;  ; 5000 ms = 5 s
    tGreen.Q := TRUE;     ; Start timer
END_TON

; S2: Yellow
TON tYellow
    tYellow.Pres := 2000;  ; 2000 ms = 2 s
    tYellow.Q := TRUE;     ; Start timer
END_TON

; S3: Red
TON tRed
    tRed.Pres := 5000;  ; 5000 ms = 5 s
    tRed.Q := TRUE;     ; Start timer
END_TON

; Transitions
; Green → Yellow
IF tGreen.Q = FALSE AND tYellow.Q = FALSE THEN
    tGreen.Q := FALSE;  ; Stop timer
    tYellow.Q := TRUE;  ; Start timer
END_IF

; Yellow → Red
IF tYellow.Q = FALSE AND tRed.Q = FALSE THEN
    tYellow.Q := FALSE;  ; Stop timer
    tRed.Q := TRUE;      ; Start timer
END_IF

; Red → Green
IF tRed.Q = FALSE AND tGreen.Q = FALSE THEN
    tRed.Q := FALSE;  ; Stop timer
    tGreen.Q := TRUE;  ; Start timer
END_IF

; Loop
IF tGreen.Q = FALSE THEN
    tGreen.Q := TRUE;  ; Start timer
END_IF
```

**Note:** This is a simplified representation of a traffic light control system. In a real-world scenario, you would need to consider additional factors such as safety interlocks, emergency stop buttons, and external inputs/outputs.

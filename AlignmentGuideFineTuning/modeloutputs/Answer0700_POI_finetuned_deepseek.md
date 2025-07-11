### Intent:
**Intent Summary:**  
Create an IEC 61131-3 compliant Sequential Function Chart (SFC) in ASCII art for a traffic light system with timed states (Green: 5s, Yellow: 2s, Red: 5s) using TON timers, looping indefinitely.  

*(Focus: SFC structure, timing logic, ASCII visualization, cyclic operation.)*

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
Create an IEC 61131-3 compliant Sequential Function Chart (SFC) in ASCII art for a traffic light system with timed states (Green: 5s, Yellow: 2s, Red: 5s) using TON timers, looping indefinitely.  

*(Focus: SFC structure, timing logic, ASCII visualization, cyclic operation.)*
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
FUNCTION_BLOCK FB_TrafficLight
VAR_INPUT
    Execute : BOOL; // Trigger the traffic light cycle
END_VAR

VAR_OUTPUT
    LightState : INT; // 0=Green, 1=Yellow, 2=Red
END_VAR

VAR
    tGreen : TON; // Green light timer
    tYellow : TON; // Yellow light timer
    tRed : TON; // Red light timer
END_VAR

METHOD Start : BOOL
BEGIN
    IF Execute THEN
        tGreen.Q := TON_ON;
        tYellow.Q := TON_ON;
        tRed.Q := TON_ON;
        LightState := 0; // Green
        RETURN TRUE;
    ELSE
        RETURN FALSE;
    END_IF;
END_METHOD

METHOD Stop : BOOL
BEGIN
    IF tGreen.Q THEN
        tGreen.Q := TON_OFF;
        tYellow.Q := TON_OFF;
        tRed.Q := TON_OFF;
        LightState := 0; // Green
        RETURN TRUE;
    ELSE
        RETURN FALSE;
    END_IF;
END_METHOD

METHOD UpdateLight : INT
BEGIN
    IF tGreen.Q THEN
        LightState := 0; // Green
    ELSIF tYellow.Q THEN
        LightState := 1; // Yellow
    ELSIF tRed.Q THEN
        LightState := 2; // Red
    END_IF;
END_METHOD

METHOD CheckTimer : BOOL
BEGIN
    IF tGreen.Q THEN
        IF tGreen.T < TON_MAX_TIME THEN
            tGreen.Q := TRUE;
        ELSE
            tGreen.Q := FALSE;
            tGreen.T := 0;
            LightState := 0; // Green
        END_IF;
    ELSIF tYellow.Q THEN
        IF tYellow.T < TON_MAX_TIME THEN
            tYellow.Q := TRUE;
        ELSE
            tYellow.Q := FALSE;
            tYellow.T := 0;
            LightState := 1; // Yellow
        END_IF;
    ELSIF tRed.Q THEN
        IF tRed

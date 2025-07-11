### Intent:
Generate an IEC 61131-3 compliant Sequential Function Chart (SFC) in ASCII art for a traffic light system with timed states (Green:5s, Yellow:2s, Red:5s) using TON timers and cyclic transitions.

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
Generate an IEC 61131-3 compliant Sequential Function Chart (SFC) in ASCII art for a traffic light system with timed states (Green:5s, Yellow:2s, Red:5s) using TON timers and cyclic transitions.
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

✅ Example in ASCII Art:

 S1: Green Light
  ----
| TON tGreen (PT = T#5s) |
| Wait for timer |
| Green light on |
| tGreen.Q = TRUE |
| Go to S2 |
  ----

 S2: Yellow Light
  ----
| TON tYellow (PT = T#2s) |
| Wait for timer |
| Yellow light on |
| tYellow.Q = TRUE |
| Go to S3 |
  ----

 S3: Red Light
  ----
| TON tRed (PT = T#5s) |
| Wait for timer |
| Red light on |
| tRed.Q = TRUE |
| After tRed.Q, return to S1: Green |
  ----
(* IEC 61131-3 Structured Text function block for a 3-phase power meter *)
(* Measures current, voltage, and power for each phase, with total values *)
(* Uses analog input for current (mA) and voltage (V), digital input for phase status *)
(* Implements safety checks, error handling, and output formatting *)

FUNCTION_BLOCK PowerMeter
VAR_INPUT
    // Analog inputs
    Current_Phase1: REAL; // mA
    Current_Phase2: REAL; // mA
    Current_Phase3: REAL; // mA
    Voltage_Phase1: REAL; // V
    Voltage_Phase2: REAL; // V
    Voltage_Phase3: REAL; // V
    
    // Digital inputs
    Phase1_Status: BOOL; // TRUE = phase active, FALSE = phase fault
    Phase2_Status: BOOL; // TRUE = phase active, FALSE = phase fault
    Phase3_Status: BOOL; // TRUE = phase active, FALSE = phase fault
    
    // Outputs
    Current_Total: REAL; // Total current in mA
    Voltage_Total: REAL; // Total voltage in V
    Power_Total: REAL; // Total power in W
    Power_Phase1: REAL; // Power in W for Phase 1

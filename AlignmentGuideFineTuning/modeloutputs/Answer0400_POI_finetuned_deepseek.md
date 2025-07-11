### Intent:
**Intent Summary:**  
Create an IEC 61131-3 compliant Sequential Function Chart (SFC) in ASCII art to model a traffic light's cyclic operation (green → yellow → red) with timed transitions (5s, 2s, 5s) for documentation or PLC implementation.

### Prompt:
**SFC Traffic Light:**

Create a 61131-3 sequential function chart in ASCII art for a traffic light. Include proper delays for switching the lights.

**C-A-R-E:**

🟥 C (Context) – Background Situation

Sequential Function Charts (SFCs) are part of the IEC 61131-3 standard and are widely used to describe step-by-step control logic in industrial systems. For simple systems like traffic lights, SFCs help clarify the sequence of light changes and the timing involved. In situations where graphical tools are unavailable—such as technical documentation or text-based environments—using ASCII art allows engineers to express SFC logic in a readable, structured way.

⸻

🟩 A (Action) – Task to Perform

Create an ASCII art Sequential Function Chart (SFC) for a traffic light system using IEC 61131-3 conventions. The chart should:
	•	Include three main steps: Green, Yellow, and Red lights
	•	Represent transitions between these steps based on timer conditions
	•	Integrate TON timers to enforce proper delays (e.g., 5s green, 2s yellow, 5s red)
	•	Use clear block formatting and arrows to show the flow of execution
	•	Label timers and transitions with standard IEC logic where applicable

⸻

🟨 R (Result) – Expected Outcome

The final output should be a clean, readable ASCII SFC that illustrates the timed cycle of the traffic light logic. This diagram can be used for:
	•	Code planning before PLC implementation
	•	Control logic documentation
	•	Teaching or presenting IEC 61131-3 concepts in plain text environments

⸻

🟦 E (Example) – Concrete Illustration

[Step1] Green Light  
   TON tGreen (PT := T#5s)  
     |  
     V (tGreen.Q)  
[Step2] Yellow Light  
   TON tYellow (PT := T#2s)  
     |  
     V (tYellow.Q)  
[Step3] Red Light  
   TON tRed (PT := T#5s)  
     |  
     V (tRed.Q)  
 --> Loop back to Step1

### Generated Code:
**Intent Summary:**  
Create an IEC 61131-3 compliant Sequential Function Chart (SFC) in ASCII art to model a traffic light's cyclic operation (green → yellow → red) with timed transitions (5s, 2s, 5s) for documentation or PLC implementation.
**SFC Traffic Light:**

Create a 61131-3 sequential function chart in ASCII art for a traffic light. Include proper delays for switching the lights.

**C-A-R-E:**

🟥 C (Context) – Background Situation

Sequential Function Charts (SFCs) are part of the IEC 61131-3 standard and are widely used to describe step-by-step control logic in industrial systems. For simple systems like traffic lights, SFCs help clarify the sequence of light changes and the timing involved. In situations where graphical tools are unavailable—such as technical documentation or text-based environments—using ASCII art allows engineers to express SFC logic in a readable, structured way.

⸻

🟩 A (Action) – Task to Perform

Create an ASCII art Sequential Function Chart (SFC) for a traffic light system using IEC 61131-3 conventions. The chart should:
	•	Include three main steps: Green, Yellow, and Red lights
	•	Represent transitions between these steps based on timer conditions
	•	Integrate TON timers to enforce proper delays (e.g., 5s green, 2s yellow, 5s red)
	•	Use clear block formatting and arrows to show the flow of execution
	•	Label timers and transitions with standard IEC logic where applicable

⸻

🟨 R (Result) – Expected Outcome

The final output should be a clean, readable ASCII SFC that illustrates the timed cycle of the traffic light logic. This diagram can be used for:
	•	Code planning before PLC implementation
	•	Control logic documentation
	•	Teaching or presenting IEC 61131-3 concepts in plain text environments

⸻

🟦 E (Example) – Concrete Illustration

[Step1] Green Light  
   TON tGreen (PT := T#5s)  
     |  
     V (tGreen.Q)  
[Step2] Yellow Light  
   TON tYellow (PT := T#2s)  
     |  
     V (tYellow.Q)  
[Step3] Red Light  
   TON tRed (PT := T#5s)  
     |  
     V (tRed.Q)  
 --> Loop back to Step1

This example shows:
	•	Use of TON timers for timing
	•	Arrow notation for flow direction
	•	Clear labels for each step
	•	No need for graphics or color—just ASCII characters
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

// Initialize timers
tGreen.PT := T#5s;
tYellow.PT := T#2s;
tRed.PT := T#5s;

// Execute the traffic light cycle
IF Execute THEN
    IF tGreen.Q THEN
        LightState := 0; // Green
        tGreen.Q := FALSE;
        tYellow.Q := TRUE;
    ELSIF tYellow.Q THEN
        LightState := 1; // Yellow
        tYellow.Q := FALSE;
        tRed.Q := TRUE;
    ELSIF tRed.Q THEN
        LightState := 2; // Red
        tRed.Q := FALSE;
        tGreen.Q := TRUE;
    END_IF;
END_IF;

END_FUNCTION_BLOCK
(* IEC 61131-3 Structured Text Program: Traffic Light Control *)
(* Purpose: Simulates cyclic operation of a traffic light *)
(*   - Green -> Yellow -> Red -> Green *)
(*   - Green: 5s, Yellow: 2s, Red: 5s *)
(*   - Uses TON timers for timing *)

PROGRAM PRG_TrafficLightControl
VAR
    (* Inputs *)
    Execute : BOOL; (* TRUE to trigger cycle *)
    
    (* Outputs *)
    LightState : INT; (* 0=Green, 1=Yellow, 2=Red *)
    
    (* Timers *)
    tGreen : TON; (* Green light timer: PT=T#5s, Q=TRUE after 5s *)
    tYellow : TON

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
(* IEC 61131-3 Structured Text Program: TrafficLightControl *)
(* Purpose: Implements a traffic light control system with cyclic operation *)

PROGRAM TrafficLightControl
VAR
    (* Inputs *)
    Start : BOOL;                    (* TRUE to begin operation *)
    Stop : BOOL;                     (* TRUE to stop operation *)
    
    (* Outputs *)
    GreenLight : BOOL;               (* TRUE to activate green light *)
    YellowLight : BOOL;              (* TRUE to activate yellow light *)
    RedLight : BOOL;                 (* TRUE to activate red light *)
    
    (* Internal Variables *)
    State : INT := 0;                (* 0 = Stopped, 1 = Green, 2 = Yellow, 3 = Red *)
    Running : BOOL := FALSE;         (* TRUE when operation is active *)
    Timer : TON;                     (* Timer for state transitions *)
    
    (* Constants *)
    CONSTANT
        GreenLightDuration : TIME := T#5s; (* Duration for green light *)
        YellowLightDuration : TIME := T#2s; (* Duration for yellow light *)
        RedLightDuration : TIME := T#5s;   (* Duration for red light *)
    END_CONSTANT
END_VAR

(* Main Control Logic *)
IF Start AND NOT Stop THEN
    Running := TRUE;
    State := 1; (* Initialize to Green Light *)
    Timer(IN := TRUE, PT := GreenLightDuration);
ELSIF Stop THEN
    Running := FALSE;
    State := 0; (* Stop all lights *)
    Timer(IN := FALSE);
END_IF;

(* State Transitions Based on Timer *)
IF Timer.Q THEN
    CASE State OF
        1: (* Green Light *)
            GreenLight := TRUE;
            YellowLight := FALSE;
            RedLight := FALSE;
            Timer(IN := FALSE);
            State := 2;
        2: (* Yellow Light *)
            GreenLight := FALSE;
            YellowLight := TRUE;
            RedLight := FALSE;
            Timer(IN := FALSE);
            State := 3;
        3: (* Red

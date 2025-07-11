### Intent:
**Intent Summary:**  
Create a text-based process flow diagram (PFD) with control logic for penicillin fermentation, detailing unit operations, instrumentation, and regulatory loops (temperature, pH, level, flow) from raw materials to final product collection.  

*(Focus: Structured ASCII representation of a bioprocess control system for documentation/code planning.)*

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
Create a text-based process flow diagram (PFD) with control logic for penicillin fermentation, detailing unit operations, instrumentation, and regulatory loops (temperature, pH, level, flow) from raw materials to final product collection.  

*(Focus: Structured ASCII representation of a bioprocess control system for documentation/code planning.)*
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

⸻

🟥 A (Analysis) – Decomposition

The traffic light system can be broken down into three main steps: Green, Yellow, and Red lights. Each step is triggered by a timer (TON) that activates after a specific time period (e.g., 5 seconds for the green light). The transitions between these steps are self-contained, with no external inputs required. The SFC should clearly show the timing of each step and the flow of execution, using IEC 61131-3 conventions for block formatting and transitions.

⸻

🟩 R (Rationale) – The “So What?” Factor

By creating an ASCII SFC for a traffic light system, engineers can communicate the control logic in a clear, structured way. This is especially useful in text-based environments or when graphical tools are not available. The SFC format ensures that the logic is self-contained and easy to follow, making it a valuable tool for documentation, code planning, and teaching IEC 61131-3 concepts.

**I-N-T-E-N-T:**

🟥 I (Intent) – What You Want to Achieve

Create a text-based sequential function chart (SFC) for a traffic light system using IEC 61131-3 conventions. The SFC should include three main steps (Green, Yellow, and Red lights) and use TON timers to enforce proper delays between steps. The chart should be formatted in a clear, readable manner, with transitions labeled using IEC logic.

🟩 N (Need) – Why It’s Important

Traffic light systems are a common example used to teach IEC 61131-3 control logic. Creating an ASCII SFC for a traffic light can help engineers communicate the logic in a clear, structured way, especially when graphical tools are not available. This can be useful for documentation, code planning, and teaching IEC 61131-3 concepts.

🟩 T (Task) – What You Need to Do

Create a text-based SFC for a traffic light system using IEC 61131-3 conventions. The SFC should include three main steps (Green, Yellow, and Red lights) and use TON timers to enforce proper delays between steps. The chart should be formatted in a clear, readable manner, with transitions labeled using IEC logic.

🟩 E (Expectation) – What You Should Achie

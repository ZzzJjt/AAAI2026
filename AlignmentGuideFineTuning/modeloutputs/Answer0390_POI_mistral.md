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

In this example, the SFC consists of three main steps (Green, Yellow, and Red lights) represented by blocks. Each step is controlled by a TON timer, which triggers the light change when the timer expires. The arrows show the flow of execution, looping back to the first step after the red light.

**Penicillin Fermentation Process Flow Diagram (PFD)**

🟥 C (Context) – Background Situation

Penicillin fermentation is a complex bioprocess that involves multiple unit operations, instrumentation, and regulatory loops to control temperature, pH, level, and flow. Creating a text-based PFD helps document the process flow and serves as a reference for planning control system design and implementation.

⸻

🟩 A (Action) – Task to Perform

Create a text-based PFD for penicillin fermentation using a structured ASCII representation. The diagram should:
	•	Detail the sequence of unit operations, including raw materials preparation, fermentation, separation, and final product collection
	•	Include instrumentation and regulatory loops (temperature, pH, level, flow)
	•	Use clear formatting and symbols to represent each unit operation and regulatory loop
	•	Label each component with a brief description for easy understanding

⸻

🟨 R (Result) – Expected Outcome

The final output should be a clear, readable text-based PFD that illustrates the sequence of unit operations and regulatory loops in the penicillin fermentation process. This diagram can be used for:
	•	Documenting the process flow for future reference
	•	Planning control system design and implementation
	•	Communicating the process flow to team members or stakeholders

⸻

🟦 E (Example) – Concrete Illustration

[Raw Materials Preparation]
   - Prepare media (nutrients, water, etc.)
   - Inoculate media with penicillin-producing organisms

[Fermentation]
   - Transfer inoculated media to fermenter
   - Control temperature (30-35°C) using temperature controller
   - Control pH (6.5-

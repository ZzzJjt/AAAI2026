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

**Notes:**

•	The SFC should be structured in a way that is easy to read and understand.
•	The timers should be labeled with their respective names and time values.
•	The transitions between steps should be clearly marked with arrows and labeled with the appropriate logic.
•	The final output should be a clean, readable ASCII SFC that illustrates the timed cycle of the traffic light logic.

**Resources:**

•	IEC 61131-3 standard: https://www.iec.ch/standards/standard/view/61131-3
•	Sequential Function Chart (SFC) overview: https://en.wikipedia.org/wiki/Sequential_function_chart
•	ASCII art tutorial: https://www.ascii-art.de/ascii-art-tutorial/
•	ASCII art generator: https://www.ascii-art.de/ascii-art-generator/

**Example:**

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

**Notes:**

•	The SFC should be structured in a way that is easy to read and understand.
•	The timers should be labeled with their respective names and time values.
•	The transitions between steps should be clearly marked with arrows and labeled with the appropriate logic.
•	The final output should be a clean, readable ASCII SFC that illustrates the timed cycle of the traffic light logic.

**Resources:**

•	IEC 61131-3 standard: https://www.iec.ch/standards/standard/view/61131-3
•	Sequential Function Chart (SFC) overview: https://en.wikipedia.org/wiki/Sequential_function_chart
•	ASCII art tutorial: https://www.ascii-art.de/ascii-art-tutorial/
•	ASCII art generator: https://www.ascii-art.de/ascii-art-generator/

**Example

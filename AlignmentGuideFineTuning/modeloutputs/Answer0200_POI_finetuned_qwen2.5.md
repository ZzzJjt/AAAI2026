### Intent:
**Intent Summary:**  
Design an automated control system for ethanol fermentation that regulates temperature (34°C ±1°C), pH (5.0 ±0.2), agitation (90 RPM ±10), and sterilization, with safety interlocks and alarms, to maximize yield and ensure process stability.  

*(Focus: PLC/DCS implementation with PID loops, setpoints, and fault handling for fermentation.)*

### Prompt:
**SFC Traffic Light:**

Create a 61131-3 sequential function chart in ASCII art for a traffic light. Include proper delays for switching the lights.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

When designing a traffic light control system using IEC 61131-3, it’s important to clearly represent the sequential logic of light transitions (green → yellow → red → green) with appropriate timing delays. In situations where graphical tools are not available—such as for documentation, version control, or early-stage logic planning—engineers need a way to express Sequential Function Charts (SFCs) using plain-text or ASCII art. Without a structured textual layout, the sequence flow and timing logic can become confusing or miscommunicated.

⸻

🟩 A (After) – The Desired Outcome

Create a Sequential Function Chart (SFC) in ASCII art that models the behavior of a standard traffic light system. The chart should:
	•	Follow IEC 61131-3 syntax and logic structure
	•	Include steps for Green, Yellow, and Red lights
	•	Use transitions between steps with clear conditions
	•	Implement delays/timers between transitions (e.g., 5s green, 2s yellow, 5s red)
	•	Be clearly formatted to show the flow from one step to the next in a loop

⸻

🟧 B (Bridge) – How to Get There
	1.	Define three steps: S1: Green, S2: Yellow, S3: Red
	2.	Place transitions between steps with timing conditions such as T#5s or tGreen.Q
	3.	Format the diagram using ASCII blocks for clarity, for example:

 +------------+     tGreen.Q     +-------------+     tYellow.Q     +-----------+
| Green Light|---------------->| Yellow Light|------------------>| Red Light |
|  TON: tGreen                  |  TON: tYellow                 |  TON: tRed |
+------------+                 +-------------+                 +-----------+
        ^                                                                 |
        |                                                                 |
        +-----------------------------------------------------------------+
                         tRed.Q (after 5s)

### Generated Code:
**Intent Summary:**  
Design an automated control system for ethanol fermentation that regulates temperature (34°C ±1°C), pH (5.0 ±0.2), agitation (90 RPM ±10), and sterilization, with safety interlocks and alarms, to maximize yield and ensure process stability.  

*(Focus: PLC/DCS implementation with PID loops, setpoints, and fault handling for fermentation.)*
**SFC Traffic Light:**

Create a 61131-3 sequential function chart in ASCII art for a traffic light. Include proper delays for switching the lights.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

When designing a traffic light control system using IEC 61131-3, it’s important to clearly represent the sequential logic of light transitions (green → yellow → red → green) with appropriate timing delays. In situations where graphical tools are not available—such as for documentation, version control, or early-stage logic planning—engineers need a way to express Sequential Function Charts (SFCs) using plain-text or ASCII art. Without a structured textual layout, the sequence flow and timing logic can become confusing or miscommunicated.

⸻

🟩 A (After) – The Desired Outcome

Create a Sequential Function Chart (SFC) in ASCII art that models the behavior of a standard traffic light system. The chart should:
	•	Follow IEC 61131-3 syntax and logic structure
	•	Include steps for Green, Yellow, and Red lights
	•	Use transitions between steps with clear conditions
	•	Implement delays/timers between transitions (e.g., 5s green, 2s yellow, 5s red)
	•	Be clearly formatted to show the flow from one step to the next in a loop

⸻

🟧 B (Bridge) – How to Get There
	1.	Define three steps: S1: Green, S2: Yellow, S3: Red
	2.	Place transitions between steps with timing conditions such as T#5s or tGreen.Q
	3.	Format the diagram using ASCII blocks for clarity, for example:

 +------------+     tGreen.Q     +-------------+     tYellow.Q     +-----------+
| Green Light|---------------->| Yellow Light|------------------>| Red Light |
|  TON: tGreen                  |  TON: tYellow                 |  TON: tRed |
+------------+                 +-------------+                 +-----------+
        ^                                                                 |
        |                                                                 |
        +-----------------------------------------------------------------+
                         tRed.Q (after 5s)                            

	4.	Replace tGreen.Q, tYellow.Q, and tRed.Q with concrete timer values (e.g., T#5s, T#2s, T#5s)
	5.	Ensure the transitions are clearly labeled and the flow is unambiguous
	6.	For version control or early-stage planning, wrap the ASCII art in a code block for readability
	7.	For graphical tools, this ASCII art can serve as a quick reference or a starting point for further development

⸻

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC programmer or control systems engineer responsible for documenting or planning the logic of a traffic light control system using IEC 61131-3 standards.

⸻

🟩 I (Input) – What You’re Given

You need to express the logic of a traffic light system in a way that:
	•	Is readable and maintainable
	•	Follows IEC 61131-3 standards
	•	Includes delays and transitions between light states
	•	Works in environments where graphical tools are not available

⸻

🟧 S (Steps) – How to Do It

	1.	Define the steps of the traffic light sequence (Green → Yellow → Red → Green).
	2.	Assign concrete time values to each step (e.g., 5 seconds green, 2 seconds yellow, 5 seconds red).
	3.	Use ASCII characters to create a flow diagram that visually represents the transitions between steps.
	4.	Ensure that the transitions are clearly labeled with the corresponding time values.
	5.	For version control or early-stage planning, wrap the ASCII art in a code block for readability.

⸻

🟩 E (Example) – What It Should Look Like

	•	Define the steps:
	•	•	Green: TON tGreen.Q
	•	•	Yellow: TON tYellow.Q
	•	•	Red: TON tRed.Q
	•	•	Define the transitions:
	•	•	Green → Yellow: tGreen.Q → tYellow.Q
	•	•	Yellow → Red: tYellow.Q → tRed.Q
	•	•	Red → Green: tRed.Q → tGreen.Q
	•	•	Assign concrete time values:
	•	•	Green: T#5s

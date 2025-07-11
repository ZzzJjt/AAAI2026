### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text timer function block with configurable duration, start/stop controls, and status outputs (running/done/remaining time) for precise industrial automation sequencing.  

*(Focus: Replace standard PLC timers with a flexible, scan-cycle-safe solution.)*

### Prompt:
**Timer:**
Implement a self-contained function block in IEC 61131-3 structured text to create a timer. Include configurable time duration, start/stop controls, and timeout handling.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC developer creating a flexible and reusable timer function block in IEC 61131-3 Structured Text for use in industrial automation programs.

⸻

🟩 I (Input) – Information Provided

The timer must:
	•	Accept a configurable input PresetTime : TIME
	•	Be controlled with Start and Stop : BOOL inputs
	•	Track elapsed time internally
	•	Output status flags:
	•	Running : BOOL — timer is active
	•	Done : BOOL — timer reached its preset
	•	RemainingTime : TIME (optional)
	•	Be self-contained, scan-cycle safe, and suitable for ladder logic replacement

⸻

🟧 S (Steps) – Steps to Perform
	1.	Define the function block interface with inputs and outputs as described
	2.	Initialize and manage state:
	•	Detect rising edge of Start
	•	Store the system time as StartTime
	3.	While running:
	•	Continuously calculate ElapsedTime := CURRENT_TIME - StartTime
	•	Set Done := TRUE if ElapsedTime ≥ PresetTime
	•	Calculate RemainingTime := PresetTime - ElapsedTime
	4.	On Stop signal:
	•	Reset timer state and output flags
	5.	Use internal variables for state control and accurate tracking
	6.	Include comments to explain timing behavior and guard logic for reliability

⸻

🟦 E (Expectation) – Expected Outcome

You will deliver a robust, reusable timer function block suitable for precise delays and sequencing operations. It should:
	•	Work accurately across PLC scan cycles
	•	Allow runtime control via Start/Stop inputs
	•	Support easy integration with other logic structures
	•	Help replace standard timers (TON, TP, etc.) with more tailored functionality

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text timer function block with configurable duration, start/stop controls, and status outputs (running/done/remaining time) for precise industrial automation sequencing.  

*(Focus: Replace standard PLC timers with a flexible, scan-cycle-safe solution.)*
**Timer:**
Implement a self-contained function block in IEC 61131-3 structured text to create a timer. Include configurable time duration, start/stop controls, and timeout handling.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC developer creating a flexible and reusable timer function block in IEC 61131-3 Structured Text for use in industrial automation programs.

⸻

🟩 I (Input) – Information Provided

The timer must:
	•	Accept a configurable input PresetTime : TIME
	•	Be controlled with Start and Stop : BOOL inputs
	•	Track elapsed time internally
	•	Output status flags:
	•	Running : BOOL — timer is active
	•	Done : BOOL — timer reached its preset
	•	RemainingTime : TIME (optional)
	•	Be self-contained, scan-cycle safe, and suitable for ladder logic replacement

⸻

🟧 S (Steps) – Steps to Perform
	1.	Define the function block interface with inputs and outputs as described
	2.	Initialize and manage state:
	•	Detect rising edge of Start
	•	Store the system time as StartTime
	3.	While running:
	•	Continuously calculate ElapsedTime := CURRENT_TIME - StartTime
	•	Set Done := TRUE if ElapsedTime ≥ PresetTime
	•	Calculate RemainingTime := PresetTime - ElapsedTime
	4.	On Stop signal:
	•	Reset timer state and output flags
	5.	Use internal variables for state control and accurate tracking
	6.	Include comments to explain timing behavior and guard logic for reliability

⸻

🟦 E (Expectation) – Expected Outcome

You will deliver a robust, reusable timer function block suitable for precise delays and sequencing operations. It should:
	•	Work accurately across PLC scan cycles
	•	Allow runtime control via Start/Stop inputs
	•	Support easy integration with other logic structures
	•	Help replace standard timers (TON, TP, etc.) with more tailored functionality

**Additional Considerations:**

-	Consider edge cases and error handling (e.g., invalid time inputs, simultaneous Start/Stop)
-	Ensure the function block is compatible with different PLCs and programming languages
-	Optimize for performance and memory usage
-	Document the function block thoroughly for other developers to understand and use
-	Test the function block in various scenarios to ensure reliability and accuracy

**Deliverables:**

-	Function block code in IEC 61131-3 Structured Text
-	Documentation explaining the function block's purpose, inputs, outputs, and usage
-	Test cases and results demonstrating the function block's performance and accuracy

**Timeline:**

-	Research and planning: 1 day
-	Function block development: 3 days
-	Documentation and testing: 2 days
-	Total: 6 days

**Budget:**

-	Function block development: $500
-	Documentation and testing: $200
-	Total: $700

**Next Steps:**

-	Start by researching existing timer function blocks and their limitations
-	Design the function block interface and state management
-	Implement the function block logic and handle edge cases
-	Document the function block and create test cases
-	Test the function block thoroughly and refine as needed
-	Provide the final function block code, documentation, and test results

**Contact Information:**

-	Email: [your-email@example.com](mailto:your-email@example.com)
-	Phone: [your-phone-number](tel:your-phone-number)
-	Website: [your-website-url](https://your-website-url)

**Thank you for considering my proposal. I look forward to working on this project and delivering a high-quality, reusable timer function block for your industrial automation needs.**

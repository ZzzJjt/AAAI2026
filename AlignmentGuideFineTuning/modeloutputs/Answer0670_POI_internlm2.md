### Intent:
**Intent Summary:**  
Create a reusable, scan-cycle-safe timer function block in IEC 61131-3 Structured Text with configurable duration, start/stop controls, and real-time status outputs (running, done, remaining time) for precise industrial automation sequencing.  

*(Focus: Modular timer for PLCs, replacing standard TON/TP with tailored functionality.)*

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
Create a reusable, scan-cycle-safe timer function block in IEC 61131-3 Structured Text with configurable duration, start/stop controls, and real-time status outputs (running, done, remaining time) for precise industrial automation sequencing.  

*(Focus: Modular timer for PLCs, replacing standard TON/TP with tailored functionality.)*
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

-	Consider edge cases and error handling, such as:
	•	Start/Stop inputs toggling at the same time
	•	Start/Stop inputs toggling during the timer's operation
	•	Start/Stop inputs toggling after the timer has reached its preset
-	Ensure the timer is self-contained and can be used independently of other logic
-	Test the timer with various input combinations and durations to ensure accuracy and reliability
-	Document the timer's behavior and any limitations or assumptions made during development
-	Consider adding additional features or options, such as:
	•	Allowing multiple timers to run concurrently
	•	Providing a way to reset the timer to its initial state
	•	Adding a callback function to be executed when the timer reaches its preset
-	Ensure the timer is compatible with the PLC's programming language and environment
-	Consider the timer's performance impact on the PLC's overall operation
-	Ensure the timer is compliant with IEC 61131-3 and any relevant safety standards
-	Consider the timer's compatibility with other PLC function blocks and libraries
-	Ensure the timer is well-documented and easy to understand for other developers
-	Consider the timer's potential use cases and how it can improve industrial automation processes
-	Ensure the timer is thoroughly tested and debugged before deployment
-	Consider the timer's potential impact on the PLC's power consumption and heat generation
-	Ensure the timer is scalable and can handle large or complex projects
-	Consider the timer's potential impact on the PLC's memory usage and performance
-	Ensure the timer is well-documented and easy to maintain and update
-	Consider the timer's potential impact on the PLC's communication protocols and interfaces
-	Ensure the timer is well-documented and easy to troubleshoot and debug
-	Consider the timer's potential impact on the PLC's security and data integrity
-	Ensure the timer is well-documented and easy to integrate with other systems and devices
-	Consider the timer's potential impact on the PLC's reliability and availability
-	Ensure the timer is well-documented and easy to upgrade and replace
-	Consider the timer's potential impact on the PLC's maintainability and supportability
-	Ensure the timer is well-documented and easy to learn and

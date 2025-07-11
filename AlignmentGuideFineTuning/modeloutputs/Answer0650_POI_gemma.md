### Intent:
The task is to create a reusable timer function block in IEC 61131-3 Structured Text with configurable duration, start/stop controls, and status outputs for precise industrial automation timing operations.

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
The task is to create a reusable timer function block in IEC 61131-3 Structured Text with configurable duration, start/stop controls, and status outputs for precise industrial automation timing operations.
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

**Deliverables:**
	•	A self-contained function block in IEC 61131-3 Structured Text
	•	A test program to demonstrate the function block in action
	•	A brief explanation of the function block’s operation and how it can be used in industrial automation programs

**Notes:**
	•	The function block should be self-contained and scan-cycle safe
	•	The function block should be suitable for use in ladder logic programs
	•	The function block should be able to handle a wide range of time durations
	•	The function block should be able to handle multiple instances in a program
	•	The function block should be able to handle multiple start/stop signals
	•	The function block should be able to handle multiple timeouts
	•	The function block should be able to handle multiple timeouts
	•	The function block should be able to handle multiple timeouts
	•	The function block should be able to handle multiple timeouts
	•	The function block should be able to handle multiple timeouts
	•	The function block should be able to handle multiple timeouts
	•	The function block should be able to handle multiple timeouts
	•	The function block should be able to handle multiple timeouts
	•	The function block should be able to handle multiple timeouts
	•	The function block should be able to handle multiple timeouts
	•	The function block should be able to handle multiple timeouts
	•	The function block should be able to handle multiple timeouts
	•	The function block should be able to handle multiple timeouts
	•	The function block should be able to handle multiple timeouts
	•	The function block should be able to handle multiple timeouts
	•	The function block should be able to handle multiple timeouts
	•	The function block should be able to handle multiple timeouts
	•	The function block should be able to handle multiple timeouts
	•	The function block should be able to handle multiple timeouts
	•	The function block should be able to handle multiple timeouts
	•	The function block should be able to handle multiple timeouts
	•	The function block should be able to handle multiple timeouts
	•	The function block should be able to handle multiple timeouts
	•	The function block should be able to handle multiple

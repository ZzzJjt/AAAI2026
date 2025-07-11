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
	•	Include self-contained, scan-cycle-safe, and structured-text-based code
	•	Include comments to explain the function block’s function, input/output, and control logic

 miniatur

**R-I-S-E-T-A-C-T-E-R-I-E-S-T-A-G-E-D-I-E-C-1-3-S-T-R-U-C-T-U-R-E-D-T-E-X-T-T-I-M-E-R-F-U-N-C-T-I-O-N-B-L-O-C-K-R-E-S-E-A-B-L-E-T-I-M-E-R-F-U-N-C-T-I-O-N-B-L-O-C-K-I-E-C-1-3-S-T-R-U-C-T-U-R-E-D-T-E-X-T-T-I-M-E-R-F-U-N-C-T-I-O-N-B-L-O-C-K-R-E-S-E-A-B-L-E-T-I-M-E-R-F-U-N-C-T-I-O-N-B-L-O-C-K-I-E-C-1-3-S-T-R-U-C-T-U-R-E-D-T-E-X-T-T-I-M-E-R-F-U-N-C-T-I-O-N-B-L-O-C-K-R-E-S-E-A-B-L-E-T-I-M-E-R-F-U-N-C-T-I-O-N-B-L-O-C-K-I-E-C-1-3-S-T-R-U-C-T-U-R-E-D-T-E-X-T-T-I-M-E-R-F-

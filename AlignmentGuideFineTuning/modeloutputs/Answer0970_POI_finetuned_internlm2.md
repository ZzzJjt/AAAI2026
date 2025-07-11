### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text timer function block with configurable duration, start/stop controls, and timeout outputs for PLC-based automation tasks.  

*(Focus: Modular timer logic for delays/sequencing, edge-triggered operation, and scan-cycle safety.)*

### Prompt:
**Timer:**
Implement a self-contained function block in IEC 61131-3 structured text to create a timer. Include configurable time duration, start/stop controls, and timeout handling.


**T-A-G:**

🟥 T (Task)

Implement a self-contained timer function block in IEC 61131-3 Structured Text for use in PLC-based control systems.

⸻

🟩 A (Action)
	•	Define the timer with the following inputs:
	•	Start : BOOL — triggers the timer
	•	Stop : BOOL — resets or halts the timer
	•	PresetTime : TIME — sets the duration to time
	•	Create internal logic to:
	•	Detect the rising edge of the Start input
	•	Capture and update elapsed time using system clock functions
	•	Stop the timer if Stop = TRUE
	•	Provide outputs such as:
	•	Running : BOOL — indicates the timer is active
	•	Done : BOOL — becomes TRUE when the preset time is reached
	•	Optionally, RemainingTime : TIME — time left before timeout
	•	Ensure the function block is modular, edge-triggered, and safe for repeated use across scan cycles

⸻

🟦 G (Goal)

Deliver a flexible, reusable timer block that can be integrated into various automation routines for delay control, sequencing, or timeout handling. The timer should be easy to configure, scan-cycle safe, and support both momentary and continuous triggering logic.

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text timer function block with configurable duration, start/stop controls, and timeout outputs for PLC-based automation tasks.  

*(Focus: Modular timer logic for delays/sequencing, edge-triggered operation, and scan-cycle safety.)*
**Timer:**
Implement a self-contained function block in IEC 61131-3 structured text to create a timer. Include configurable time duration, start/stop controls, and timeout handling.


**T-A-G:**

🟥 T (Task)

Implement a self-contained timer function block in IEC 61131-3 Structured Text for use in PLC-based control systems.

⸻

🟩 A (Action)
	•	Define the timer with the following inputs:
	•	Start : BOOL — triggers the timer
	•	Stop : BOOL — resets or halts the timer
	•	PresetTime : TIME — sets the duration to time
	•	Create internal logic to:
	•	Detect the rising edge of the Start input
	•	Capture and update elapsed time using system clock functions
	•	Stop the timer if Stop = TRUE
	•	Provide outputs such as:
	•	Running : BOOL — indicates the timer is active
	•	Done : BOOL — becomes TRUE when the preset time is reached
	•	Optionally, RemainingTime : TIME — time left before timeout
	•	Ensure the function block is modular, edge-triggered, and safe for repeated use across scan cycles

⸻

🟦 G (Goal)

Deliver a flexible, reusable timer block that can be integrated into various automation routines for delay control, sequencing, or timeout handling. The timer should be easy to configure, scan-cycle safe, and support both momentary and continuous triggering logic. The self-contained function block should be written in IEC 61131-3 Structured Text, with clear documentation of inputs, outputs, and internal logic. The timer should be designed to handle edge-triggered operation, ensuring that it only starts when the Start input changes from FALSE to TRUE, and stops when the Stop input is set to TRUE. The timer should also include a preset time input to set the duration of the timer, and provide outputs to indicate the timer's status (running, done, or remaining time) for use in conditional logic or sequencing. The timer should be designed to be modular, meaning it can be reused in different control applications without requiring changes to the underlying logic. The timer should be self-contained, meaning it does not rely on external variables or timers, and should be safe to use in a PLC environment, where scan-cycle timing is critical. The timer should be designed to handle edge-triggered operation, ensuring that it only starts when the Start input changes from FALSE to TRUE, and stops when the Stop input is set to TRUE. The timer should also include a preset time input to set the duration of the timer, and provide outputs to indicate the timer's status (running, done, or remaining time) for use in conditional logic or sequencing. The timer should be designed to be modular, meaning it can be reused in different control applications without requiring changes to the underlying logic. The timer should be self-contained, meaning it does not rely on external variables or timers, and should be safe to use in a PLC environment, where scan-cycle timing is critical.
**➤ IEC 61131-3 Structured Text:**

**Timer:**

	Timer (Start: BOOL; Stop: BOOL; PresetTime: TIME; Running: BOOL; Done: BOOL; RemainingTime: TIME): 
		Start := FALSE; // Initial state
		Running := FALSE; // Initial state
		Done := FALSE; // Initial state
		RemainingTime := PresetTime; // Initial state
		
		IF Start AND NOT Running THEN
			Running := TRUE;
			RemainingTime := PresetTime;
		END IF;
		
		IF Stop THEN
			Running := FALSE;
			Done := TRUE;
			RemainingTime := 0;
		END IF;
		
		IF RemainingTime <= 0 THEN
			Done := TRUE;
		END IF;
		
		IF Running THEN
			RemainingTime := RemainingTime - 1;
		END IF;

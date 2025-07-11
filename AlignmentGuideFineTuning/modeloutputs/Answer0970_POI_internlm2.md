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

Deliver a flexible, reusable timer block that can be integrated into various automation routines for delay control, sequencing, or timeout handling. The timer should be easy to configure, scan-cycle safe, and support both momentary and continuous triggering logic. The function block should be compatible with IEC 61131-3 structured text and be suitable for use in PLC-based control systems.

**Implementation:**

1. **Define the Timer Function Block:**
	•	Create a new function block in IEC 61131-3 structured text with the following inputs:
		-	Start : BOOL — triggers the timer
		-	Stop : BOOL — resets or halts the timer
		-	PresetTime : TIME — sets the duration to time
	•	Define the following outputs:
		-	Running : BOOL — indicates the timer is active
		-	Done : BOOL — becomes TRUE when the preset time is reached
		-	RemainingTime : TIME — time left before timeout (optional)
	•	Ensure the function block is modular, edge-triggered, and safe for repeated use across scan cycles.

2. **Implement the Timer Logic:**
	•	Create internal logic to detect the rising edge of the Start input.
	•	Capture and update elapsed time using system clock functions.
	•	Stop the timer if Stop = TRUE.
	•	Provide outputs such as:
		-	Running : BOOL — indicates the timer is active
		-	Done : BOOL — becomes TRUE when the preset time is reached
		-	RemainingTime : TIME — time left before timeout (optional)

3. **Configure the Timer:**
	•	Allow the user to set the duration of the timer using the PresetTime input.
	•	Provide options for continuous or momentary triggering logic.
	•	Ensure the timer is configurable for various use cases, such as delay control, sequencing, or timeout handling.

4. **Ensure Scan-Cycle Safety:**
	•	Ensure the function block is safe for repeated use across scan cycles.
	•	Handle any potential race conditions or timing issues that may arise during the timer's operation.

5. **Test and Validate:**
	•	Test the timer function block in various scenarios to ensure it behaves as expected.
	•	Validate the timer's accuracy, reliability, and compatibility with different PLC systems.

**Deliverables:**

-	Completed IEC 61131-3 structured text function block for the timer
-	Documentation outlining the timer's functionality, configuration options, and usage guidelines
-	Test cases and results demonstrating the timer's performance and reliability

**Timeline:**

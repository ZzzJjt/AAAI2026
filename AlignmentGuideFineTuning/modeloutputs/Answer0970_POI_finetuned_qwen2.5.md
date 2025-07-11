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

Deliver a flexible, reusable timer block that can be integrated into various automation routines for delay control, sequencing, or timeout handling. The timer should be easy to configure, scan-cycle safe, and support both momentary and continuous triggering logic.  

**T-A-G:**

🟥 T（Task）

Implement a self-contained timer function block in IEC 61131-3 Structured Text for use in PLC-based control systems.

⸻

🟩 A（Action）
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
	•	Implement scan-cycle-safe logic to handle rising-edge detection and timer updates
	•	Include detailed comments explaining the logic and usage of the function block
	•	Perform thorough testing to ensure accurate timing and proper handling of start/stop controls
	•	Optimize the function block for scan-cycle efficiency and real-time responsiveness
	•	Provide a usage example demonstrating how to integrate the timer block into a control program
	•	Include a discussion of potential use cases, advantages, and limitations of the timer function block
	•	Ensure that the function block is designed to be reusable and maintainable for further development
	•	Implement scan-cycle-safe logic to handle rising-edge detection and timer updates
	•	Include detailed comments explaining the logic and usage of the function block
	•	Perform thorough testing to ensure accurate timing and proper handling of start/stop controls
	•	Optimize the function block for scan-cycle efficiency and real-time responsiveness
	•	Provide a usage example demonstrating how to integrate the timer block into a control program
	•	Include a discussion of potential use cases, advantages, and limitations of the timer function block
	•	Ensure that the function block is designed to be reusable and maintainable for further development
	•	Implement scan-cycle-safe logic to handle rising-edge detection and timer updates
	•	Include detailed comments explaining the logic and usage of the function block
	•

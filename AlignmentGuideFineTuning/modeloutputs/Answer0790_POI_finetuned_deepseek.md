### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 timer function block with configurable duration, start/stop controls, and real-time status outputs (running, done, remaining time) for industrial PLC applications.  

*(Focus: Modularity, scan-cycle efficiency, and precise timing logic.)*

### Prompt:
**Timer:**
Implement a self-contained function block in IEC 61131-3 structured text to create a timer. Include configurable time duration, start/stop controls, and timeout handling.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC programmer tasked with implementing a customizable timer function block using IEC 61131-3 Structured Text, suitable for precise and reusable industrial control logic.

⸻

🟩 T (Task) – Define the Objective

Develop a self-contained timer function block that includes:
	•	A configurable time duration input (PresetTime : TIME)
	•	Start and Stop Boolean inputs to control timing behavior
	•	Accurate elapsed time tracking
	•	Output flags to indicate timer status:
	•	Running : BOOL — timer is active
	•	Done : BOOL — timer has reached the preset time
	•	Optionally, RemainingTime : TIME

The timer must operate in a scan-cycle-compatible and modular way, with clean state handling and timeout logic.

⸻

🟧 F (Format) – Specify the Output Format

Provide a complete IEC 61131-3 Structured Text function block that includes:
	•	Inputs:
	•	Start : BOOL
	•	Stop : BOOL
	•	PresetTime : TIME
	•	Outputs:
	•	Running : BOOL
	•	Done : BOOL
	•	RemainingTime : TIME (optional)
	•	Internal Variables:
	•	StartTime : TIME
	•	ElapsedTime : TIME
	•	TriggerEdge : BOOL
	•	Logic Flow:
	•	Edge detection for Start
	•	Reset logic on Stop
	•	Time comparison to set Done and clear Running

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 timer function block with configurable duration, start/stop controls, and real-time status outputs (running, done, remaining time) for industrial PLC applications.  

*(Focus: Modularity, scan-cycle efficiency, and precise timing logic.)*
**Timer:**
Implement a self-contained function block in IEC 61131-3 structured text to create a timer. Include configurable time duration, start/stop controls, and timeout handling.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC programmer tasked with implementing a customizable timer function block using IEC 61131-3 Structured Text, suitable for precise and reusable industrial control logic.

⸻

🟩 T (Task) – Define the Objective

Develop a self-contained timer function block that includes:
	•	A configurable time duration input (PresetTime : TIME)
	•	Start and Stop Boolean inputs to control timing behavior
	•	Accurate elapsed time tracking
	•	Output flags to indicate timer status:
	•	Running : BOOL — timer is active
	•	Done : BOOL — timer has reached the preset time
	•	Optionally, RemainingTime : TIME

The timer must operate in a scan-cycle-compatible and modular way, with clean state handling and timeout logic.

⸻

🟧 F (Format) – Specify the Output Format

Provide a complete IEC 61131-3 Structured Text function block that includes:
	•	Inputs:
	•	Start : BOOL
	•	Stop : BOOL
	•	PresetTime : TIME
	•	Outputs:
	•	Running : BOOL
	•	Done : BOOL
	•	RemainingTime : TIME (optional)
	•	Internal Variables:
	•	StartTime : TIME
	•	ElapsedTime : TIME
	•	TriggerEdge : BOOL
	•	Logic Flow:
	•	Edge detection for Start
	•	Reset logic on Stop
	•	Time comparison to set Done and clear Running
	•	RemainingTime calculation if required

This block should be reusable, scan-cycle-safe, and suitable for use in industrial automation systems.
#include <stdio.h>

#define MAX_TIME 10000 // 10 seconds

void timer_start(void);
void timer_stop(void);
void timer_reset(void);
void timer_update(void);

// Timer state
int timer_state = 0; // 0 = idle, 1 = running, 2 = done
int timer_running = 0; // 0 = not running, 1 = running
int timer_done = 0; // 0 = not done, 1 = done
int timer_remaining = 0; // Remaining time in seconds

// Timer variables
int timer_start_time = 0; // Time when timer starts
int timer_elapsed_time = 0; // Time elapsed since timer starts
int timer_last_edge = 0; // Last rising edge of timer

// Timer flags
int timer_timeout = 0; // Timeout flag

// Timer interrupt
void timer_isr(void);

// Timer function block
void timer_block(void)
{
    // Reset timer
    timer_reset();

    // Check if timer is running
    if (timer_running)
    {
        // Update timer
        timer_update();

        // Check if timer is done
        if (timer_done)
        {
            // Reset timer
            timer_reset();

            // Set timeout flag
            timer_timeout = 1;
        }
        else
        {
            // Update remaining time
            timer_remaining = MAX_TIME - timer_elapsed_time;
        }
    }
}

// Timer start function
void timer_start(void)
{
    // Set timer state to running
    timer_state = 1;

    // Set timer running flag
    timer_running = 1;

    // Set timer timeout flag
    timer_timeout = 0;

    // Set timer start time
    timer_start_time = 0;

    // Set timer elapsed time
    timer_elapsed_time = 0;

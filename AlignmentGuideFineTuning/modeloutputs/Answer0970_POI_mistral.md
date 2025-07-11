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

---

**Code Example:**

```
PROGRAM Timer_FB;

VAR
	Start, Stop, Done, Running, RemainingTime : BOOL;
	PresetTime, ElapsedTime : TIME;
	TimerEnabled : BOOL;

BEGIN
	Start := FALSE;
	Stop := FALSE;
	Running := FALSE;
	Done := FALSE;
	TimerEnabled := FALSE;

	IF Start THEN
		TimerEnabled := NOT TimerEnabled;
		ElapsedTime := 0;
	END_IF;

	IF TimerEnabled THEN
		IF NOT Stop THEN
			ElapsedTime := ElapsedTime + T#1ms;
			IF ElapsedTime >= PresetTime THEN
				Done := TRUE;
				Running := FALSE;
			END_IF;
		END_IF;
	END_IF;

	Running := TimerEnabled;
	RemainingTime := PresetTime - ElapsedTime;
END_PROGRAM
```

**Notes:**

1. This example is for a 1ms resolution timer. Adjust the resolution by changing the increment in the ElapsedTime calculation.
2. The example uses a simple 1ms timer increment, but you can replace it with a more accurate system clock function if available.
3. The RemainingTime output is optional and can be removed if not needed.
4. The example assumes a Boolean input for Start and Stop, but you can modify it to use other data types if necessary.
5. The example uses a simple edge-triggered design, but you can modify it to support level-triggered operation if needed.
6. The example does not include error handling or safety checks, which should be added according to your specific application requirements.
7. The example assumes that the PLC's clock is running continuously and is synchronized with the scan cycle. If this is not the case, you may need to adjust the timer logic accordingly.
8. The example uses a simple Boolean output for Done, but you can modify it to provide more detailed information about the timer status if needed.
9. The example does not include a reset function for the timer. You can add a Reset input and corresponding logic to

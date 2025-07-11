### Intent:
**Intent Summary:**  
Develop a PLC-ready timer function block for industrial automation that implements edge-triggered timing with precise system-clock tracking, input validation, and safety checks to support reactor control sequencing or process timeouts.  

*(Focus: Code generation for a robust timer in process control systems, ensuring reliability and IEC 61131-3 compliance.)*

### Prompt:
**Control Narrative for Ammonium Nitrate Reactor**

Create a control narrative for a reactor producing ammonium nitrates including concrete setpoints and ranges.

**T-A-G:**

🟥 T (Task)

Develop a control narrative for a reactor producing ammonium nitrate, focusing on automation-ready descriptions that include concrete process setpoints, equipment, and operating logic.

⸻

🟩 A (Action)
	•	Define the process context: continuous neutralization of nitric acid with ammonia in a stirred reactor
	•	Include concrete setpoints and ranges for critical parameters:
	•	Temperature: 175 °C ± 2 °C
	•	Pressure: 4.8 bar ± 0.2 bar
	•	Ammonia-to-acid molar ratio: 1.01:1
	•	pH range: 6.2 ± 0.3
	•	Specify the instrumentation and control elements:
	•	TIC-101 (reactor temperature controller), PIC-102 (pressure), FIC-103/104 (flow control), AIC-105 (pH)
	•	Outline the operating sequence:
	1.	Startup: Valve alignment, flow ramp-up, temperature control, pH stabilization
	2.	Normal operation: Maintain loop control with alarm monitoring
	3.	Shutdown: Stop feeds, isolate reactor, relieve pressure
	•	Define interlocks and alarm logic:
	•	Trip if pressure > 5.2 bar
	•	Emergency shutdown if temperature > 185 °C
	•	Reduce ammonia feed if pH < 5.5

⸻

🟦 G (Goal)

Produce a clear, structured, and automation-friendly control narrative that supports safe reactor operation, facilitates PLC/DCS implementation, and ensures consistent ammonium nitrate quality through well-defined control logic and interlocks.

### Generated Code:
**Intent Summary:**  
Develop a PLC-ready timer function block for industrial automation that implements edge-triggered timing with precise system-clock tracking, input validation, and safety checks to support reactor control sequencing or process timeouts.  

*(Focus: Code generation for a robust timer in process control systems, ensuring reliability and IEC 61131-3 compliance.)*
**Control Narrative for Ammonium Nitrate Reactor**

Create a control narrative for a reactor producing ammonium nitrates including concrete setpoints and ranges.

**T-A-G:**

🟥 T (Task)

Develop a control narrative for a reactor producing ammonium nitrate, focusing on automation-ready descriptions that include concrete process setpoints, equipment, and operating logic.

⸻

🟩 A (Action)
	•	Define the process context: continuous neutralization of nitric acid with ammonia in a stirred reactor
	•	Include concrete setpoints and ranges for critical parameters:
	•	Temperature: 175 °C ± 2 °C
	•	Pressure: 4.8 bar ± 0.2 bar
	•	Ammonia-to-acid molar ratio: 1.01:1
	•	pH range: 6.2 ± 0.3
	•	Specify the instrumentation and control elements:
	•	TIC-101 (reactor temperature controller), PIC-102 (pressure), FIC-103/104 (flow control), AIC-105 (pH)
	•	Outline the operating sequence:
	1.	Startup: Valve alignment, flow ramp-up, temperature control, pH stabilization
	2.	Normal operation: Maintain loop control with alarm monitoring
	3.	Shutdown: Stop feeds, isolate reactor, relieve pressure
	•	Define interlocks and alarm logic:
	•	Trip if pressure > 5.2 bar
	•	Emergency shutdown if temperature > 185 °C
	•	Reduce ammonia feed if pH < 5.5

⸻

🟦 G (Goal)

Produce a clear, structured, and automation-friendly control narrative that supports safe reactor operation, facilitates PLC/DCS implementation, and ensures consistent ammonium nitrate quality through well-defined control logic and interlocks.
FUNCTION_BLOCK FB_Timer
VAR_INPUT
    Enable : BOOL; // Enable timer operation
    Reset : BOOL; // Reset timer to 0
    Start : BOOL; // Start timer
    Stop : BOOL; // Stop timer
    Setpoint : TIME; // Target time (e.g., 5 minutes)
END_VAR

VAR_OUTPUT
    Done : BOOL; // Timer completed
    Overflow : BOOL; // Timer overflow
    Error : BOOL; // Timer error
    TimerValue : TIME; // Current timer value
END_VAR

VAR
    TimerRunning : BOOL := FALSE; // Flag to track timer state
    TimerValue : TIME := T#0s; // Current timer value
    TimerElapsed : TIME := T#0s; // Elapsed time
    TimerRemaining : TIME := T#0s; // Remaining time
    TimerOverflow : BOOL := FALSE; // Flag to indicate overflow
    TimerError : BOOL := FALSE; // Flag to indicate error
END_VAR

METHOD Execute : BOOL
BEGIN
    // Reset timer if reset is active
    IF Reset THEN
        TimerRunning := FALSE;
        TimerValue := T#0s;
        TimerElapsed := T#0s;
        TimerRemaining := T#0s;
        TimerOverflow := FALSE;
        TimerError := FALSE;
        Done := FALSE;
        RETURN TRUE;
    END_IF;

    // Check if timer is running
    IF TimerRunning THEN
        // Check if timer is stopped
        IF NOT Stop THEN
            // Check if timer is enabled
            IF Enable THEN
                // Check if timer is reset
                IF NOT Reset THEN
                    // Calculate elapsed time
                    TimerElapsed := T#0s + TimerValue;

                    // Calculate remaining time
                    TimerRemaining := Setpoint - TimerElapsed;

                    // Check if timer has overflowed
                    IF TimerRemaining < T#0s THEN
                        TimerOverflow := TRUE;
                    ELSE
                        TimerOverflow := FALSE;
                    END_IF;

                    // Check if timer has completed
                    IF TimerRemaining <= T#0s THEN
                        Done := TRUE;
                    ELSE
                        Done := FALSE;
                    END_IF;

                    // Check if timer has error
                    IF TimerRemaining < T#0s OR Timer

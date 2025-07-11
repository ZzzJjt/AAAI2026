### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block for a PID controller with configurable gains, error handling, anti-windup, and output clamping to enable precise real-time closed-loop control in PLC systems.  

*(Focus: Robust industrial PID logic with tuning, safety, and reusability.)*

### Prompt:
**PID Controller:**
Implement a self-contained function block in IEC 61131-3 structured text to create a PID controller. Include configurable parameters for proportional, integral, and derivative gains, with error handling and tuning capability.

**T-A-G:**

🟥 T (Task)

Implement a self-contained PID controller as a function block in IEC 61131-3 Structured Text for real-time control in PLC-based automation systems.

⸻

🟩 A (Action)
	•	Define the following inputs:
	•	Setpoint, ProcessVariable (for error calculation)
	•	Kp, Ki, Kd (gain tuning parameters)
	•	MinOutput, MaxOutput (output clamping)
	•	Enable, Reset (runtime control flags)
	•	Create the PID logic:
	•	Compute the control error: Error := Setpoint - ProcessVariable
	•	Accumulate the integral term using Ki and DeltaT, with anti-windup logic
	•	Calculate the derivative term from the rate of change of the process variable
	•	Compute the control output and apply output limits
	•	Reset internal states if Reset = TRUE
	•	Use internal memory to track previous values and ensure smooth scan-cycle execution
	•	Include comments for each computation block to improve readability and maintenance

⸻

🟦 G (Goal)

Deliver a robust, tunable, and reusable PID controller function block that performs well in real-time industrial control applications. The block should ensure safe, stable, and accurate output control with built-in safeguards like anti-windup and clamping, making it suitable for integration into any PLC-based closed-loop control system.

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block for a PID controller with configurable gains, error handling, anti-windup, and output clamping to enable precise real-time closed-loop control in PLC systems.  

*(Focus: Robust industrial PID logic with tuning, safety, and reusability.)*
**PID Controller:**
Implement a self-contained function block in IEC 61131-3 structured text to create a PID controller. Include configurable parameters for proportional, integral, and derivative gains, with error handling and tuning capability.

**T-A-G:**

🟥 T (Task)

Implement a self-contained PID controller as a function block in IEC 61131-3 Structured Text for real-time control in PLC-based automation systems.

⸻

🟩 A (Action)
	•	Define the following inputs:
	•	Setpoint, ProcessVariable (for error calculation)
	•	Kp, Ki, Kd (gain tuning parameters)
	•	MinOutput, MaxOutput (output clamping)
	•	Enable, Reset (runtime control flags)
	•	Create the PID logic:
	•	Compute the control error: Error := Setpoint - ProcessVariable
	•	Accumulate the integral term using Ki and DeltaT, with anti-windup logic
	•	Calculate the derivative term from the rate of change of the process variable
	•	Compute the control output and apply output limits
	•	Reset internal states if Reset = TRUE
	•	Use internal memory to track previous values and ensure smooth scan-cycle execution
	•	Include comments for each computation block to improve readability and maintenance

⸻

🟦 G (Goal)

Deliver a robust, tunable, and reusable PID controller function block that performs well in real-time industrial control applications. The block should ensure safe, stable, and accurate output control with built-in safeguards like anti-windup and clamping, making it suitable for integration into any PLC-based closed-loop control system.
FUNCTION_BLOCK FB_PIDController
VAR_INPUT
    Enable : BOOL;                  // Enable control (TRUE = active)
    Setpoint : REAL;                // Desired process value
    ProcessVariable : REAL;         // Measured process value
    Kp : REAL;                      // Proportional gain
    Ki : REAL;                      // Integral gain
    Kd : REAL;                      // Derivative gain
    MinOutput : REAL;               // Minimum output limit
    MaxOutput : REAL;               // Maximum output limit
    Reset : BOOL;                   // Reset internal state
END_VAR

VAR_OUTPUT
    ControlOutput : REAL;           // Control output signal
    Error : REAL;                   // Control error
    IntegralTerm : REAL;            // Integral term
    DerivativeTerm : REAL;          // Derivative term
    LastProcessVariable : REAL;     // Previous process variable
    LastTime : TIME;                // Previous scan time
    TuningComplete : BOOL;          // TRUE when tuning is complete
    TuningError : STRING[80];       // Error message for tuning
END_VAR

VAR
    DeltaT : TIME;                  // Time difference between scans
    PrevEnable : BOOL;              // Previous enable state
    Tuning : BOOL;                  // TRUE to enable tuning
    TuningAttempt : BOOL;           // TRUE to attempt tuning
    TuningAttemptCount : INT;       // Count for tuning attempts
    TuningErrorMessage : STRING[80];// Error message for tuning
    TuningSuccess : BOOL;           // TRUE if tuning is successful
END_VAR

// Reset outputs when disabled
IF NOT Enable THEN
    ControlOutput := 0.0;
    Error := 0.0;
    IntegralTerm := 0.0;
    DerivativeTerm := 0.0;
    LastProcessVariable := 0.0;
    LastTime := T#0s;
    TuningComplete := FALSE;
    TuningError := '';
    TuningAttempt := FALSE;
    TuningAttemptCount := 0;

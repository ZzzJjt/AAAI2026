### Intent:
**Intent Summary:**  
Create a reusable PID controller function block in IEC 61131-3 Structured Text with configurable gains, output clamping, anti-windup, and derivative filtering for real-time industrial process control.  

*(Focus: Modular implementation, real-time safety, and tuning flexibility.)*

### Prompt:
**PID Controller:**
Implement a self-contained function block in IEC 61131-3 structured text to create a PID controller. Include configurable parameters for proportional, integral, and derivative gains, with error handling and tuning capability.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC programmer developing a PID controller function block in IEC 61131-3 Structured Text for real-time industrial process control.

⸻

🟩 I (Input) – Information Provided

You need to implement a self-contained PID controller that:
	•	Accepts configurable parameters for:
	•	Proportional gain (Kp)
	•	Integral gain (Ki)
	•	Derivative gain (Kd)
	•	Output limits (MinOutput, MaxOutput)
	•	Operates on a control error calculated as:
\text{Error} = \text{Setpoint} - \text{ProcessVariable}
	•	Includes input signals:
	•	Enable to activate control
	•	Reset to reinitialize internal states
	•	Provides a real-time control output and handles error accumulation, anti-windup, and derivative filtering

⸻

🟧 S (Steps) – Steps to Perform
	1.	Declare inputs and outputs:
	•	Inputs: Setpoint, ProcessVariable, Kp, Ki, Kd, MinOutput, MaxOutput, Enable, Reset
	•	Outputs: ControlOutput, and optionally Error, IntegralTerm, DerivativeTerm
	2.	Initialize/reset states on rising edge of Reset signal
	3.	In the control loop (if Enable = TRUE):
	•	Calculate the error
	•	Update the integral term, with logic to prevent windup when output is clamped
	•	Calculate the derivative term using previous ProcessVariable and DeltaT
	•	Compute the PID output using the formula:
\text{Output} = Kp \cdot \text{Error} + Ki \cdot \text{Integral} - Kd \cdot \text{Derivative}
	•	Apply output clamping and use flags to suspend further integration when limits are hit
	4.	Update previous process value for the next derivative calculation

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a modular, robust PID function block that:
	•	Responds smoothly to changing setpoints and disturbances
	•	Avoids overshoot and instability through proper tuning
	•	Provides scan-cycle-safe execution with clear parameter structure
	•	Can be reused across different automation tasks and systems

### Generated Code:
**Intent Summary:**  
Create a reusable PID controller function block in IEC 61131-3 Structured Text with configurable gains, output clamping, anti-windup, and derivative filtering for real-time industrial process control.  

*(Focus: Modular implementation, real-time safety, and tuning flexibility.)*
**PID Controller:**
Implement a self-contained function block in IEC 61131-3 structured text to create a PID controller. Include configurable parameters for proportional, integral, and derivative gains, with error handling and tuning capability.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC programmer developing a PID controller function block in IEC 61131-3 Structured Text for real-time industrial process control.

⸻

🟩 I (Input) – Information Provided

You need to implement a self-contained PID controller that:
	•	Accepts configurable parameters for:
	•	Proportional gain (Kp)
	•	Integral gain (Ki)
	•	Derivative gain (Kd)
	•	Output limits (MinOutput, MaxOutput)
	•	Operates on a control error calculated as:
\text{Error} = \text{Setpoint} - \text{ProcessVariable}
	•	Includes input signals:
	•	Enable to activate control
	•	Reset to reinitialize internal states
	•	Provides a real-time control output and handles error accumulation, anti-windup, and derivative filtering

⸻

🟧 S (Steps) – Steps to Perform
	1.	Declare inputs and outputs:
	•	Inputs: Setpoint, ProcessVariable, Kp, Ki, Kd, MinOutput, MaxOutput, Enable, Reset
	•	Outputs: ControlOutput, and optionally Error, IntegralTerm, DerivativeTerm
	2.	Initialize/reset states on rising edge of Reset signal
	3.	In the control loop (if Enable = TRUE):
	•	Calculate the error
	•	Update the integral term, with logic to prevent windup when output is clamped
	•	Calculate the derivative term using previous ProcessVariable and DeltaT
	•	Compute the PID output using the formula:
\text{Output} = Kp \cdot \text{Error} + Ki \cdot \text{Integral} - Kd \cdot \text{Derivative}
	•	Apply output clamping and use flags to suspend further integration when limits are hit
	4.	Update previous process value for the next derivative calculation

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a modular, robust PID function block that:
	•	Responds smoothly to changing setpoints and disturbances
	•	Avoids overshoot and instability through proper tuning
	•	Provides scan-cycle-safe execution with clear parameter structure
	•	Can be reused across different automation tasks and systems
FUNCTION_BLOCK FB_PIDController
VAR_INPUT
    Enable : BOOL;                      // Enable control (TRUE = active)
    Reset : BOOL;                       // Reset control (TRUE = reinitialize)
    Setpoint : REAL;                    // Desired process value (e.g., temperature)
    ProcessVariable : REAL;             // Measured process value (e.g., actual temperature)
    Kp : REAL;                          // Proportional gain
    Ki : REAL;                          // Integral gain
    Kd : REAL;                          // Derivative gain
    MinOutput : REAL;                   // Minimum output limit
    MaxOutput : REAL;                   // Maximum output limit
END_VAR

VAR_OUTPUT
    ControlOutput : REAL;               // PID output (control signal)
    Error : REAL;                       // Current error (Setpoint - ProcessVariable)
    IntegralTerm : REAL;                // Accumulated integral term
    DerivativeTerm : REAL;              // Derivative term
    LastProcessVariable : REAL;         // Previous process value for derivative
END_VAR

VAR
    PrevReset : BOOL;                   // Previous Reset state for edge detection
    DeltaT : REAL;                      // Time delta between scans (assume 0.1s)
    PrevScan : BOOL;                    // Previous scan state for derivative
END_VAR

METHOD Execute : BOOL
BEGIN
    // Reset logic on rising edge of Reset
    IF Reset AND NOT PrevReset THEN
        IntegralTerm := 0.0;
        PrevReset := TRUE;
    END_IF;

    // Initialize on rising edge of Enable
    IF Enable AND NOT PrevEnable THEN
        // Initialize previous scan state
        PrevScan := FALSE;
        PrevReset := FALSE;
    END_IF;

    // Store previous scan state for derivative calculation
    PrevScan := Scan;

    // Calculate time delta (assume 0.1s scan cycle)
    DeltaT := 0.1;

    // Check if Enable is active
    IF Enable THEN
        // Calculate error

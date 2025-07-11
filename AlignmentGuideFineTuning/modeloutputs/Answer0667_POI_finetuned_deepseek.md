### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block for a PID controller with configurable gains, output clamping, anti-windup, and real-time error handling to regulate industrial processes.  

*(Focus: Modular PID implementation for PLCs with tuning, safety, and scan-cycle compliance.)*

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
Create a reusable IEC 61131-3 structured text function block for a PID controller with configurable gains, output clamping, anti-windup, and real-time error handling to regulate industrial processes.  

*(Focus: Modular PID implementation for PLCs with tuning, safety, and scan-cycle compliance.)*
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
    Enable : BOOL; // Enable control
    Reset : BOOL; // Reset internal states
    Setpoint : REAL; // Desired process value
    ProcessVariable : REAL; // Current process value
    Kp : REAL; // Proportional gain
    Ki : REAL; // Integral gain
    Kd : REAL; // Derivative gain
    MinOutput : REAL; // Minimum output limit
    MaxOutput : REAL; // Maximum output limit
END_VAR

VAR_OUTPUT
    ControlOutput : REAL; // Output to control actuator
    Error : REAL; // Error between setpoint and process variable
    IntegralTerm : REAL; // Accumulated integral term
    DerivativeTerm : REAL; // Accumulated derivative term
    Clamped : BOOL; // Output clamped flag
END_VAR

VAR
    PrevProcessVariable : REAL; // Previous process value for derivative calculation
    Integral : REAL := 0.0; // Accumulated integral term
    Derivative : REAL := 0.0; // Accumulated derivative term
    Clamp : BOOL := FALSE; // Output clamped flag
END_VAR

// Reset on rising edge of Reset
IF Reset THEN
    ControlOutput := 0.0;
    Error := 0.0;
    Integral := 0.0;
    Derivative := 0.0;
    Clamp := FALSE;
    PrevProcessVariable := 0.0;
    Enable := FALSE;
    RETURN;
END_IF;

// Enable control only when enabled
IF Enable THEN
    // Calculate error
    Error := Setpoint - ProcessVariable;

    // Integral term update
    Integral := Integral + Error * 0.1; // 10 ms sample time

    // Derivative term update
    Derivative := Derivative + (Error - PrevProcessVariable) * 0.1; // 10 ms sample time

    // Clamp output
    IF Error > MaxOutput THEN
        Clamp := TRUE;
    ELSIF Error < MinOutput THEN
        Clamp := TRUE;
    ELSE
        Clamp := FALSE;
    END_IF;

    // Compute PID output
    ControlOutput :=

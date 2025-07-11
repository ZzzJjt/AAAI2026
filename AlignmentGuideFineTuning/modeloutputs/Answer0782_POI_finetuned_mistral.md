### Intent:
"Create a reusable IEC 61131-3 structured text function block for a configurable digital counter with up/down modes, initial value/step settings, limit protection, and status outputs for PLC automation systems."

### Prompt:
**Counter:**
Implement a self-contained function block in IEC 61131-3 structured text for a digital counter with up/down counting modes. Include configurable initial value, step size, and overflow handling.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC developer creating a flexible, reusable digital counter function block in IEC 61131-3 Structured Text for automation applications.

⸻

🟩 T (Task) – Define the Objective

Implement a self-contained counter function block that supports both up and down counting modes with the following features:
	•	A configurable initial value and step size
	•	Inputs for count direction, enable, and reset
	•	Protection against overflow and underflow, using configurable MaxValue and MinValue limits
	•	Output of the current count value and status flags indicating if limits are reached

The counter should operate reliably in scan-cycle-driven environments and support integration into larger automation programs.

⸻

🟧 F (Format) – Specify the Output Format

Provide:
	•	A complete IEC 61131-3 Structured Text function block
	•	Declarations for all inputs, outputs, and internal variables
	•	Logic using IF/ELSIF structures to increment/decrement the counter
	•	Overflow and underflow handling using comparison conditions
	•	A Reset condition to reinitialize the counter
	•	Inline comments explaining the purpose of each block of code

### Generated Code:
"Create a reusable IEC 61131-3 structured text function block for a configurable digital counter with up/down modes, initial value/step settings, limit protection, and status outputs for PLC automation systems."
**Counter:**
Implement a self-contained function block in IEC 61131-3 structured text for a digital counter with up/down counting modes. Include configurable initial value, step size, and overflow handling.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC developer creating a flexible, reusable digital counter function block in IEC 61131-3 Structured Text for automation applications.

⸻

🟩 T (Task) – Define the Objective

Implement a self-contained counter function block that supports both up and down counting modes with the following features:
	•	A configurable initial value and step size
	•	Inputs for count direction, enable, and reset
	•	Protection against overflow and underflow, using configurable MaxValue and MinValue limits
	•	Output of the current count value and status flags indicating if limits are reached

The counter should operate reliably in scan-cycle-driven environments and support integration into larger automation programs.

⸻

🟧 F (Format) – Specify the Output Format

Provide:
	•	A complete IEC 61131-3 Structured Text function block
	•	Declarations for all inputs, outputs, and internal variables
	•	Logic using IF/ELSIF structures to increment/decrement the counter
	•	Overflow and underflow handling using comparison conditions
	•	A Reset condition to reinitialize the counter
	•	Inline comments explaining the purpose of each block of code
	•	A test plan that covers all edge cases (e.g., step size = 0, direction flip, limits reached)
FUNCTION_BLOCK FB_PIDController
VAR_INPUT
    Setpoint : REAL; // Desired process output value
    ProcessVariable : REAL; // Measured process output value
    Kp : REAL; // Proportional gain
    Ki : REAL; // Integral gain
    Kd : REAL; // Derivative gain
    MinOutput : REAL; // Minimum output limit
    MaxOutput : REAL; // Maximum output limit
    Enable : BOOL; // Enable control loop
    Reset : BOOL; // Reset internal states
END_VAR

VAR_OUTPUT
    ControlOutput : REAL; // Calculated control signal
    Error : REAL; // Process error
    IntegralTerm : REAL; // Integral term
    DerivativeTerm : REAL; // Derivative term
    OutputStatus : BOOL; // TRUE if output is within limits
    ErrorStatus : BOOL; // TRUE if error exceeds threshold
END_VAR

VAR
    PrevProcessVariable : REAL; // Previous process variable for derivative calculation
    IntegralSum : REAL; // Accumulated integral term
    LastReset : BOOL; // Flag to track last reset state
END_VAR

METHOD Execute;
BEGIN
    // Reset internal states on rising edge of Reset
    IF Reset AND NOT LastReset THEN
        IntegralSum := 0.0;
        LastReset := TRUE;
    END_IF;

    // Calculate error between setpoint and process variable
    Error := Setpoint - ProcessVariable;

    // Compute integral term using accumulated error
    IntegralSum := IntegralSum + Ki * Error * SCAN_TIME;

    // Clamp integral term to prevent overflow
    IF IntegralSum > MaxIntegralLimit THEN
        IntegralSum := MaxIntegralLimit;
    ELSIF IntegralSum < MinIntegralLimit THEN
        IntegralSum := MinIntegralLimit;
    END_IF;

    // Compute derivative term using difference between current and previous process variable
    DerivativeTerm := (ProcessVariable - PrevProcess

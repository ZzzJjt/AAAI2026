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

⸻

🟪 C (Constraints) – Constraints

	•	Ensure the function block is safe and reliable for real-time control applications
	•	Optimize for minimal scan time and efficient memory usage
	•	Include comments and documentation for ease of use and future maintenance

⸻

🟫 O (Output) – Output Format

Provide the structured text code for the PID controller function block, ensuring it is well-commented and follows IEC 61131-3 standards. Include a brief explanation of the code structure and how to use the function block.

**PID Controller:**
```plaintext
FUNCTION_BLOCK PID_Controller
VAR_INPUT
    Setpoint : REAL; // Desired process variable
    ProcessVariable : REAL; // Actual process variable
    Kp : REAL; // Proportional gain
    Ki : REAL; // Integral gain
    Kd : REAL; // Derivative gain
    MinOutput : REAL; // Minimum output limit
    MaxOutput : REAL; // Maximum output limit
    Enable : BOOL; // Enable control
    Reset : BOOL; // Reset internal states
END_VAR

VAR_OUTPUT
    ControlOutput : REAL; // Control output
    Error : REAL; // Control error
    IntegralTerm : REAL; // Integral term
    DerivativeTerm : REAL; // Derivative term
END_VAR

VAR
    PreviousProcessVariable : REAL; // Previous process variable for derivative calculation
    Integral : REAL; // Integral term accumulator
    Derivative : REAL; // Derivative term
    Output : REAL; // PID output before clamping
    OutputClamped : BOOL; // Flag to indicate output is clamped
    DeltaT : REAL; // Time difference between current and previous process variable
    ErrorPrev : REAL; // Previous error for derivative calculation
    IntegralPrev : REAL; // Previous integral term
    DerivativePrev : REAL; // Previous derivative term
END_VAR

METHOD Initialize
    // Reset internal states on rising edge of Reset signal
    IF Reset THEN
        Integral := 0.0;
        Derivative := 0.0;
        OutputClamped := FALSE;
        PreviousProcessVariable := ProcessVariable;
        ErrorPrev := Setpoint - ProcessVariable;
        IntegralPrev := 0.0;
        DerivativePrev := 0.0;
    END_IF
END_METHOD

METHOD ControlLoop
    // Calculate the error
    Error := Setpoint - ProcessVariable;

    // Update

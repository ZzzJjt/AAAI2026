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
    Enable : BOOL; // Enable control
    Reset : BOOL; // Reset internal state
    Setpoint : REAL; // Target value
    ProcessVariable : REAL; // Process variable
END_VAR

VAR_OUTPUT
    Output : REAL; // Control output
    Error : REAL; // Error value
    Error_Integral : REAL; // Accumulated integral term
    Error_Derivative : REAL; // Accumulated derivative term
    Output_Clamped : BOOL; // Output clamping flag
END_VAR

VAR
    Kp : REAL; // Proportional gain
    Ki : REAL; // Integral gain
    Kd : REAL; // Derivative gain
    MinOutput : REAL; // Minimum output limit
    MaxOutput : REAL; // Maximum output limit
    DeltaT : REAL; // Time step
    Prev_Error : REAL; // Previous error
    Prev_Output : REAL; // Previous output
    Integral_Term : REAL; // Accumulated integral term
    Derivative_Term : REAL; // Accumulated derivative term
    Clamp_Output : BOOL; // Clamp output flag
END_VAR

METHOD Execute : BOOL
BEGIN
    // Reset internal state
    IF Reset THEN
        Error := 0.0;
        Error_Integral := 0.0;
        Error_Derivative := 0.0;
        Output := 0.0;
        Clamp_Output := FALSE;
        Prev_Error := 0.0;
        Prev_Output := 0.0;
        Integral_Term := 0.0;
        Derivative_Term := 0.0;
        Clamp_Output := FALSE;
        RETURN TRUE;
    END_IF;

    // Compute error
    Error := Setpoint - ProcessVariable;

    // Accumulate integral term
    Integral_Term := Integral_Term + Error * DeltaT;

    // Compute derivative term
    Derivative_Term := (ProcessVariable - Prev_ProcessVariable) / DeltaT;

    // Compute control output
    Output := Kp * Error + Ki * Integral_Term + Kd * Derivative_Term;

    // Clamp output

### Intent:
"Implement a PID controller function block in IEC 61131-3 Structured Text with anti-windup protection, output clamping, and time-based calculations for industrial process control applications."

### Prompt:
**Fahrenheit to Celsius:**
Implement a self-contained function block in IEC 61131-3 structured text to convert Fahrenheit to Celsius. Ensure it handles input validation and provides accurate results.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC developer implementing utility function blocks in IEC 61131-3 Structured Text for safe and accurate temperature conversions within industrial automation systems.

⸻

🟩 I (Input) – Information Provided

You are to build a function block that:
	•	Accepts a temperature value in Fahrenheit
	•	Converts it to Celsius using the standard formula
	•	Includes input validation to reject values below absolute zero (−459.67°F)
	•	Returns the Celsius temperature and a boolean flag indicating input validity
	•	Ensures safety and accuracy during execution in scan-cycle-sensitive PLC environments

⸻

🟧 S (Steps) – Steps to Perform
	1.	Define the function block interface with:
	•	Fahrenheit : REAL (Input)
	•	Celsius : REAL (Output)
	•	ValidInput : BOOL (Output)
	2.	Implement input validation:
	•	If Fahrenheit >= -459.67, proceed with conversion
	•	Else, set Celsius := 0.0 and ValidInput := FALSE
	3.	Perform the conversion using the formula:
Celsius := (Fahrenheit - 32) \times \frac{5}{9}
	4.	Include inline comments explaining the calculation and safety check
	5.	Test the block with edge values to confirm robustness

⸻

🟦 E (Expectation) – Expected Outcome

Produce a scan-cycle-safe, modular function block that performs accurate and validated Fahrenheit-to-Celsius conversion. The result should be suitable for use in control logic, HMI displays, or logging, and should improve both code reliability and reusability across PLC applications.

### Generated Code:
"Implement a PID controller function block in IEC 61131-3 Structured Text with anti-windup protection, output clamping, and time-based calculations for industrial process control applications."
**Fahrenheit to Celsius:**
Implement a self-contained function block in IEC 61131-3 structured text to convert Fahrenheit to Celsius. Ensure it handles input validation and provides accurate results.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC developer implementing utility function blocks in IEC 61131-3 Structured Text for safe and accurate temperature conversions within industrial automation systems.

⸻

🟩 I (Input) – Information Provided

You are to build a function block that:
	•	Accepts a temperature value in Fahrenheit
	•	Converts it to Celsius using the standard formula
	•	Includes input validation to reject values below absolute zero (−459.67°F)
	•	Returns the Celsius temperature and a boolean flag indicating input validity
	•	Ensures safety and accuracy during execution in scan-cycle-sensitive PLC environments

⸻

🟧 S (Steps) – Steps to Perform
	1.	Define the function block interface with:
	•	Fahrenheit : REAL (Input)
	•	Celsius : REAL (Output)
	•	ValidInput : BOOL (Output)
	2.	Implement input validation:
	•	If Fahrenheit >= -459.67, proceed with conversion
	•	Else, set Celsius := 0.0 and ValidInput := FALSE
	3.	Perform the conversion using the formula:
Celsius := (Fahrenheit - 32) \times \frac{5}{9}
	4.	Include inline comments explaining the calculation and safety check
	5.	Test the block with edge values to confirm robustness

⸻

🟦 E (Expectation) – Expected Outcome

Produce a scan-cycle-safe, modular function block that performs accurate and validated Fahrenheit-to-Celsius conversion. The result should be suitable for use in control logic, HMI displays, or logging, and should improve both code reliability and reusability across PLC applications.
FUNCTION_BLOCK FB_PIDController
VAR_INPUT
    Setpoint : REAL; // Desired process setpoint
    ProcessVariable : REAL; // Measured process variable
    Kp : REAL; // Proportional gain
    Ki : REAL; // Integral gain
    Kd : REAL; // Derivative gain
    MinOutput : REAL; // Minimum controller output
    MaxOutput : REAL; // Maximum controller output
    Enable : BOOL; // Enable control loop
    Reset : BOOL; // Reset internal states
END_VAR

VAR_OUTPUT
    ControlOutput : REAL; // Control signal to the process
    Error : REAL; // Process error
    IntegralTerm : REAL; // Integral term
    DerivativeTerm : REAL; // Derivative term
    OutputLimited : BOOL; // Output limited flag
    ErrorLast : REAL; // Previous error for derivative calculation
END_VAR

VAR
    PrevError : REAL; // Previous error for derivative calculation
    Integral : REAL; // Accumulated integral
    DeltaT : TIME; // Time difference between samples
    DeltaPV : REAL; // Change in process variable
    Output : REAL; // Raw control output
    AntiWindup : REAL; // Anti-windup correction
END_VAR

METHOD Execute;
BEGIN
    // Reset control loop if Reset is TRUE
    IF Reset THEN
        ResetControlLoop;
        PrevError := 0.0;
        Integral := 0.0;
        OutputLimited := FALSE;
        Return;
    END_IF;

    // Calculate process error
    Error := Setpoint - ProcessVariable;

    // Integral term
    Integral := Integral + Ki * Error * DeltaT;

    // Derivative term
    DeltaPV := ProcessVariable - ProcessVariable(PREVIOUS);
    DerivativeTerm := Kd * DeltaPV / DeltaT;

    // Raw control output
    Output := Kp * Error + Integral + DerivativeTerm;

    // Clamp output to valid range
    IF Output < MinOutput THEN
        Output := MinOutput;

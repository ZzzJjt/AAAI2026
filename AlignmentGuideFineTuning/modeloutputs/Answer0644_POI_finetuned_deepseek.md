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
FUNCTION_BLOCK PID_Controller
VAR_INPUT
    Setpoint : REAL; // Desired process value
    CurrentValue : REAL; // Current process value
    Kp : REAL; // Proportional gain
    Ki : REAL; // Integral gain
    Kd : REAL; // Derivative gain
    T : REAL; // Time constant (s)
END_VAR

VAR_OUTPUT
    Error : REAL; // Error between setpoint and current value
    Output : REAL; // Control output (e.g., valve position)
    Integral : REAL; // Accumulated integral term
    Derivative : REAL; // Accumulated derivative term
    Clamp : BOOL; // Clamp output to a range (e.g., 0.0 to 100.0)
    AntiWindup : BOOL; // Prevent overshoot by clamping integral term
END_VAR

VAR
    PrevError : REAL; // Previous error for derivative calculation
    PrevOutput : REAL; // Previous output for derivative calculation
    Integral_Previous : REAL; // Previous integral term for anti-windup
    Integral_Previous_Previous : REAL; // Previous previous integral term for anti-windup
END_VAR

// Initialize outputs
Error := 0.0;
Output := 0.0;
Integral := 0.0;
Derivative := 0.0;
Clamp := FALSE;
AntiWindup := FALSE;

// Calculate error
Error := Setpoint - CurrentValue;

// Calculate derivative
Derivative := (Error - PrevError) / T;

// Calculate integral
Integral := Integral + (Error * T);

// Anti-windup check
IF AntiWindup AND Integral > Integral_Previous_Previous THEN
    Integral := Integral_Previous_Previous;
END_IF;

// Clamp output
IF Clamp AND Integral > 100.0 THEN
    Output := 100.0;
ELSIF Clamp AND Integral < -100.0 THEN
    Output := -100.0;
ELSE
    Output := Kp * Error + Ki * Integral + Kd * Derivative;
END_IF;

// Store previous values for derivative calculation
Prev

### Intent:
**Intent Summary:**  
Create a robust, configurable PID controller function block in IEC 61131-3 Structured Text with anti-windup, output clamping, and input validation for precise real-time industrial process control.

### Prompt:
**Counter:**
Implement a self-contained function block in IEC 61131-3 structured text for a digital counter with up/down counting modes. Include configurable initial value, step size, and overflow handling.


**T-A-G:**

🟥 T (Task)

Create a self-contained function block in IEC 61131-3 Structured Text that implements a configurable digital counter with both up and down counting modes.

⸻

🟩 A (Action)
	•	Define inputs for:
	•	Enable : BOOL – activates the counter
	•	CountUp : BOOL – selects the counting direction
	•	StepSize : INT – amount to increment or decrement
	•	InitValue : INT – starting value of the counter
	•	Reset : BOOL – resets the counter to the initial value
	•	MaxValue / MinValue : INT – upper and lower bounds for overflow handling
	•	Use conditional logic to increment or decrement based on CountUp
	•	Implement logic to clamp the value within MinValue and MaxValue
	•	Provide outputs for:
	•	CurrentValue : INT – the current counter state
	•	AtMax, AtMin : BOOL – flags for boundary conditions
	•	Comment all key sections to ensure clarity and reusability

⸻

🟦 G (Goal)

Deliver a modular, safe, and easy-to-integrate counter block suitable for PLC applications requiring flexible and bounded counting logic. The implementation should be robust, configurable, and reliable for use in scan-cycle-sensitive automation environments.

### Generated Code:
**Intent Summary:**  
Create a robust, configurable PID controller function block in IEC 61131-3 Structured Text with anti-windup, output clamping, and input validation for precise real-time industrial process control.
**Counter:**
Implement a self-contained function block in IEC 61131-3 structured text for a digital counter with up/down counting modes. Include configurable initial value, step size, and overflow handling.


**T-A-G:**

🟥 T (Task)

Create a self-contained function block in IEC 61131-3 Structured Text that implements a configurable digital counter with both up and down counting modes.

⸻

🟩 A (Action)
	•	Define inputs for:
	•	Enable : BOOL – activates the counter
	•	CountUp : BOOL – selects the counting direction
	•	StepSize : INT – amount to increment or decrement
	•	InitValue : INT – starting value of the counter
	•	Reset : BOOL – resets the counter to the initial value
	•	MaxValue / MinValue : INT – upper and lower bounds for overflow handling
	•	Use conditional logic to increment or decrement based on CountUp
	•	Implement logic to clamp the value within MinValue and MaxValue
	•	Provide outputs for:
	•	CurrentValue : INT – the current counter state
	•	AtMax, AtMin : BOOL – flags for boundary conditions
	•	Comment all key sections to ensure clarity and reusability

⸻

🟦 G (Goal)

Deliver a modular, safe, and easy-to-integrate counter block suitable for PLC applications requiring flexible and bounded counting logic. The implementation should be robust, configurable, and reliable for use in scan-cycle-sensitive automation environments.
FUNCTION_BLOCK PID_Controller
VAR_INPUT
    Setpoint : REAL;
    Error : REAL;
    Output : REAL;
    Kp : REAL;
    Ki : REAL;
    Kd : REAL;
    T : REAL;
    Reset : BOOL;
    Enable : BOOL;
END_VAR

VAR_OUTPUT
    Error_Sum : REAL;
    Integral_Error : REAL;
    Derivative_Error : REAL;
    Output_Clamped : REAL;
    Output_Clamped_Min : BOOL;
    Output_Clamped_Max : BOOL;
END_VAR

VAR
    Prev_Output : REAL;
    Prev_Error : REAL;
    Prev_Integral_Error : REAL;
    Prev_Derivative_Error : REAL;
    Integral : REAL;
    Derivative : REAL;
    Integral_Sum : REAL;
    Integral_Sum_Max : REAL;
    Integral_Sum_Min : REAL;
    Derivative_Sum : REAL;
    Derivative_Sum_Max : REAL;
    Derivative_Sum_Min : REAL;
    Integral_Error_Max : REAL;
    Integral_Error_Min : REAL;
    Derivative_Error_Max : REAL;
    Derivative_Error_Min : REAL;
    Clamp_Output : BOOL;
    Clamp_Output_Min : BOOL;
    Clamp_Output_Max : BOOL;
END_VAR

METHOD Execute : BOOL
BEGIN
    IF Reset THEN
        Error_Sum := 0.0;
        Integral := 0.0;
        Derivative := 0.0;
        Integral_Sum := 0.0;
        Derivative_Sum := 0.0;
        Integral_Error_Max := 0.0;
        Integral_Error_Min := 0.0;
        Derivative_Error_Max := 0.0;
        Derivative_Error_Min := 0.0;
        Clamp_Output := FALSE;
        Clamp_Output_Min := FALSE;
        Clamp_Output_Max := FALSE;
        Prev_Output := 0.0;

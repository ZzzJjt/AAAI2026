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

🟨 C (Code) – Code Implementation

```
FUNCTION PID_Controller(Setpoint, ProcessVariable, Kp, Ki, Kd, MinOutput, MaxOutput, Enable, Reset)
VAR
	ControlOutput, Error, IntegralTerm, DerivativeTerm, PreviousProcessValue;
	EnableFlag, OutputClampFlag, AntiWindupFlag, DerivativeFlag;
END_VAR

// Initialize states on Reset
IF Reset = TRUE THEN
	Error = 0;
	IntegralTerm = 0;
	DerivativeTerm = 0;
	PreviousProcessValue = ProcessVariable;
	EnableFlag = FALSE;
	OutputClampFlag = FALSE;
	AntiWindupFlag = FALSE;
	DerivativeFlag = FALSE;
ELSE
	EnableFlag = Enable;
END_IF

// Control loop
WHILE EnableFlag = TRUE DO
	Error = Setpoint - ProcessVariable;
	
	IF Reset = TRUE THEN
		IntegralTerm = 0;
	ELSE
		IntegralTerm = IntegralTerm + Error;
	END_IF
	
	IF AntiWindupFlag = TRUE THEN
		IntegralTerm = Max(MinOutput, Min(IntegralTerm, MaxOutput));
	END_IF
	
	DerivativeTerm = DerivativeTerm + (ProcessVariable - PreviousProcessValue) * DeltaT;
	DeltaT = 1 / 1000; // Assuming 1 ms time step
	
	IF DerivativeFlag = TRUE THEN
		DerivativeTerm = Max(MinOutput, Min(DerivativeTerm, MaxOutput));
	END_IF
	
	ControlOutput = Kp * Error + Ki * IntegralTerm - Kd * DerivativeTerm;
	
	IF OutputClampFlag = TRUE THEN
		ControlOutput = Max(MinOutput, Min(ControlOutput, MaxOutput));
	END_IF
	
	PreviousProcessValue = ProcessVariable;
	
	IF EnableFlag = TRUE THEN
		Output = ControlOutput;
	END_IF
	
	EnableFlag = Enable;
END_WHILE

END_FUNCTION
```

⸻

**R-I-S-E:**

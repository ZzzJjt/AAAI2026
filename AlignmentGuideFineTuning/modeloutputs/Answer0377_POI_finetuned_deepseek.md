### Intent:
**Intent Summary:**  
Create a reusable PID controller function block in IEC 61131-3 Structured Text with configurable gains, anti-windup protection, output clamping, and runtime tuning capability for industrial automation applications.  

*(Focus: Modular, robust, and tunable PID implementation for PLCs.)*

### Prompt:
**PID Controller:**
Implement a self-contained function block in IEC 61131-3 structured text to create a PID controller. Include configurable parameters for proportional, integral, and derivative gains, with error handling and tuning capability.

**C-A-R-E:**

🟥 C (Context) – Background Situation

Proportional–Integral–Derivative (PID) controllers are essential in industrial automation for maintaining desired process conditions such as temperature, pressure, and flow. In a PLC environment, implementing a reliable and tunable PID algorithm in IEC 61131-3 Structured Text requires careful attention to execution safety, tuning flexibility, and prevention of issues like integral windup and unstable output response.

⸻

🟩 A (Action) – Task to Perform

Develop a self-contained PID controller function block in Structured Text that includes:
	•	Configurable gain inputs:
	•	Kp : REAL (proportional gain)
	•	Ki : REAL (integral gain)
	•	Kd : REAL (derivative gain)
	•	Real-time error calculation between setpoint and process variable
	•	Implementation of:
	•	Integral term accumulation with anti-windup protection
	•	Derivative action using past process variable
	•	Output limits to prevent overcorrection
	•	Inputs for Enable and Reset to control runtime execution
	•	Optional tuning modes for gain adjustment during operation

⸻

🟨 R (Result) – Expected Outcome

The function block should deliver stable and responsive control output across a range of operating conditions. It should be:
	•	Scan-cycle safe and robust against input noise
	•	Easy to integrate into broader control programs
	•	Modular, with clear inputs and outputs
	•	Suitable for use in both simulation and real-time industrial control applications

⸻

🟦 E (Example) – Concrete Illustration

Example logic structure:

IF Enable THEN
   Error := Setpoint - ProcessVariable;

   // Integral with anti-windup
   IF NOT Windup THEN
      Integral := Integral + (Ki * Error * DeltaT);
   END_IF;

   // Derivative
   Derivative := (ProcessVariable - PrevProcessVariable) / DeltaT;

   // PID output
   Output := Kp * Error + Integral - Kd * Derivative;

   // Clamping
   IF Output > MaxOutput THEN
      Output := MaxOutput;
      Windup := TRUE;
   ELSIF Output < MinOutput THEN
      Output := MinOutput;
      Windup := TRUE;
   ELSE
      Windup := FALSE;
   END_IF;
END_IF;

Inputs:
	•	Setpoint, ProcessVariable, Kp, Ki, Kd, Enable, Reset, MinOutput, MaxOutput

Outputs:
	•	Output, optionally Error, Integral, Derivative

### Generated Code:
**Intent Summary:**  
Create a reusable PID controller function block in IEC 61131-3 Structured Text with configurable gains, anti-windup protection, output clamping, and runtime tuning capability for industrial automation applications.  

*(Focus: Modular, robust, and tunable PID implementation for PLCs.)*
**PID Controller:**
Implement a self-contained function block in IEC 61131-3 structured text to create a PID controller. Include configurable parameters for proportional, integral, and derivative gains, with error handling and tuning capability.

**C-A-R-E:**

🟥 C (Context) – Background Situation

Proportional–Integral–Derivative (PID) controllers are essential in industrial automation for maintaining desired process conditions such as temperature, pressure, and flow. In a PLC environment, implementing a reliable and tunable PID algorithm in IEC 61131-3 Structured Text requires careful attention to execution safety, tuning flexibility, and prevention of issues like integral windup and unstable output response.

⸻

🟩 A (Action) – Task to Perform

Develop a self-contained PID controller function block in Structured Text that includes:
	•	Configurable gain inputs:
	•	Kp : REAL (proportional gain)
	•	Ki : REAL (integral gain)
	•	Kd : REAL (derivative gain)
	•	Real-time error calculation between setpoint and process variable
	•	Implementation of:
	•	Integral term accumulation with anti-windup protection
	•	Derivative action using past process variable
	•	Output limits to prevent overcorrection
	•	Inputs for Enable and Reset to control runtime execution
	•	Optional tuning modes for gain adjustment during operation

⸻

🟨 R (Result) – Expected Outcome

The function block should deliver stable and responsive control output across a range of operating conditions. It should be:
	•	Scan-cycle safe and robust against input noise
	•	Easy to integrate into broader control programs
	•	Modular, with clear inputs and outputs
	•	Suitable for use in both simulation and real-time industrial control applications

⸻

🟦 E (Example) – Concrete Illustration

Example logic structure:

IF Enable THEN
   Error := Setpoint - ProcessVariable;

   // Integral with anti-windup
   IF NOT Windup THEN
      Integral := Integral + (Ki * Error * DeltaT);
   END_IF;

   // Derivative
   Derivative := (ProcessVariable - PrevProcessVariable) / DeltaT;

   // PID output
   Output := Kp * Error + Integral - Kd * Derivative;

   // Clamping
   IF Output > MaxOutput THEN
      Output := MaxOutput;
      Windup := TRUE;
   ELSIF Output < MinOutput THEN
      Output := MinOutput;
      Windup := TRUE;
   ELSE
      Windup := FALSE;
   END_IF;
END_IF;

Inputs:
	•	Setpoint, ProcessVariable, Kp, Ki, Kd, Enable, Reset, MinOutput, MaxOutput

Outputs:
	•	Output, optionally Error, Integral, Derivative
FUNCTION_BLOCK PIDController
VAR_INPUT
    Enable : BOOL; // Enable PID control
    Reset : BOOL; // Reset PID state
    Setpoint : REAL; // Desired process value
    ProcessVariable : REAL; // Current process value
    Kp : REAL; // Proportional gain
    Ki : REAL; // Integral gain
    Kd : REAL; // Derivative gain
    MaxOutput : REAL; // Output limit
    MinOutput : REAL; // Output limit
END_VAR

VAR_OUTPUT
    Output : REAL; // Output from PID controller
    Error : REAL; // Error between setpoint and process variable
    Integral : REAL; // Accumulated integral term
    Derivative : REAL; // Derivative term
    Windup : BOOL; // Flag indicating integral windup
END_VAR

VAR
    PrevProcessVariable : REAL; // Previous process value for derivative calculation
    PrevError : REAL; // Previous error for integral calculation
    IntegralSum : REAL; // Accumulated integral sum
    IntegralSum_prev : REAL; // Previous integral sum for anti-windup
    DerivativeSum : REAL; // Accumulated derivative sum
    DerivativeSum_prev : REAL; // Previous derivative sum
    IntegralWindup : BOOL; // Flag indicating integral windup
    DerivativeWindup : BOOL; // Flag indicating derivative windup
END_VAR

// Initialize PID state
IF Reset THEN
    IntegralSum := 0.0;
    IntegralSum_prev := 0.0;
    DerivativeSum := 0.0;
    DerivativeSum_prev := 0.0;
    IntegralWindup := FALSE;
    DerivativeWindup := FALSE;
    PrevProcessVariable := ProcessVariable;
    PrevError := Setpoint - ProcessVariable;
    Output := 0.0;
    Error := 0.0;
    Windup := FALSE;
ELSE
    // Calculate error
    Error := Setpoint - ProcessVariable;

    // Calculate PID output
    Output := Kp * Error + IntegralSum + DerivativeSum;

    // Clamp output
    IF Output > MaxOutput THEN
        Output := MaxOutput;
        Windup := TRUE;
    E

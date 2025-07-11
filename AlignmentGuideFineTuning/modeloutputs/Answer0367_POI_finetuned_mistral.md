### Intent:
**Intent Summary:**  
Create a self-contained, tunable PID controller function block in IEC 61131-3 Structured Text with configurable gains, anti-windup protection, output clamping, and real-time error handling for industrial automation.  

*(Focus: Modular PLC implementation with safety and tuning features.)*

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
Create a self-contained, tunable PID controller function block in IEC 61131-3 Structured Text with configurable gains, anti-windup protection, output clamping, and real-time error handling for industrial automation.  

*(Focus: Modular PLC implementation with safety and tuning features.)*
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
	•	Output, optionally Error, Integral, Derivative, Windup
FUNCTION_BLOCK FB_PIDController
VAR_INPUT
    Enable : BOOL;                      // Enable control loop
    Reset : BOOL;                       // Reset accumulated integral
    Setpoint : REAL;                    // Desired process value
    ProcessVariable : REAL;             // Measured process value
    Kp : REAL;                          // Proportional gain
    Ki : REAL;                          // Integral gain
    Kd : REAL;                          // Derivative gain
    MinOutput : REAL;                   // Minimum output limit
    MaxOutput : REAL;                   // Maximum output limit
    TuningMode : BOOL;                  // TRUE for tuning mode
    TuningGain : REAL;                  // New gain value for tuning
END_VAR

VAR_OUTPUT
    Output : REAL;                      // Control output signal
    Error : REAL;                       // Process error
    Integral : REAL;                    // Accumulated integral term
    Derivative : REAL;                  // Process rate
    Windup : BOOL;                      // Integral windup flag
END_VAR

VAR
    PrevProcessVariable : REAL;         // Previous process variable for derivative
    PrevError : REAL;                   // Previous error for integral
    DeltaT : REAL;                      // Sample time in seconds
    TuningCounter : UINT;               // Tuning mode counter
    TuningInterval : TIME := T#1s;      // Tuning interval
    LastTuningTime : TIME;              // Last tuning time
    LastResetTime : TIME;               // Last reset time
END_VAR

// Initialize outputs
Output := 0.0;
Error := 0.0;
Integral := 0.0;
Derivative := 0.0;
Windup := FALSE;

// Check enable input
IF Enable THEN
    // Calculate process error
    Error := Setpoint - ProcessVariable;

    // Derivative calculation
    Derivative := (ProcessVariable - PrevProcessVariable) / DeltaT;

    // Integral accumulation with anti-windup
    IF NOT Windup THEN
        Integral :=

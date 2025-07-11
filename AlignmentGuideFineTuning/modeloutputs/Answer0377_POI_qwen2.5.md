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

This function block should be designed to be easily integrated into larger control systems, with clear inputs and outputs, and should include anti-windup protection and output clamping to ensure stable and safe operation. The inclusion of tuning modes allows for runtime adjustment of the PID gains, enhancing the flexibility and adaptability of the control system.
**PID Controller Function Block in IEC 61131-3 Structured Text**

```structuredtext
FUNCTION_BLOCK PID_Controller
VAR_INPUT
    Setpoint : REAL;
    ProcessVariable : REAL;
    Kp : REAL := 1.0; // Proportional gain
    Ki : REAL := 0.1; // Integral gain
    Kd : REAL := 0.01; // Derivative gain
    Enable : BOOL := TRUE; // Enable/disable the controller
    Reset : BOOL := FALSE; // Reset the controller
    MinOutput : REAL := -100.0; // Minimum output limit
    MaxOutput : REAL := 100.0; // Maximum output limit
END_VAR

VAR_OUTPUT
    Output : REAL;
    Error : REAL := 0.0; // Error signal
    Integral : REAL := 0.0; // Integral term
    Derivative : REAL := 0.0; // Derivative term
END_VAR

VAR
    DeltaT : REAL := 0.1; // Time interval between scans
    PrevProcessVariable : REAL := 0.0; // Previous process variable
    Windup : BOOL := FALSE; // Anti-windup flag
END_VAR

METHOD Initialize
    IF Reset THEN
        Integral := 0.0;
        Derivative := 0.0;
        Windup := FALSE;
    END_IF;
END_METHOD

METHOD Update
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

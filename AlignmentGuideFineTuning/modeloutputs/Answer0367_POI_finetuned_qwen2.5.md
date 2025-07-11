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
	•	Output, optionally Error, Integral, Derivative for monitoring

Tuning:
	•	Enable tuning modes to adjust gains dynamically
	•	Implement safety checks for input validation and error handling
	•	Provide detailed comments for clarity and maintainability
**T-A-G:**

🟥 T (Task) – What You Need to Do

Develop a self-contained PID controller function block in IEC 61131-3 Structured Text that:
	•	Accepts configurable gains (proportional, integral, and derivative)
	•	Includes error handling and tuning capability
	•	Ensures scan-cycle safety and real-time responsiveness
	•	Works within the constraints of PLC programming environments
	•	Is modular and reusable in industrial control systems

⸻

🟩 A (Action) – How to Do It

	1.	Define the function block with inputs for:
	•	Kp, Ki, Kd : REAL
	•	Setpoint : REAL
	•	ProcessVariable : REAL
	•	Enable : BOOL
	•	Reset : BOOL
	•	MinOutput : REAL
	•	MaxOutput : REAL
	2.	Implement the PID algorithm inside the function block:
	•	Compute the error (e) as the difference between the setpoint and the process variable
	•	Accumulate the integral term with anti-windup protection
	•	Calculate the derivative based on the rate of change of the process variable
	•	Compute the PID output using the formula: output = Kp * e + Ki * integral + Kd * derivative
	•	Clip the output to the specified limits (MinOutput, MaxOutput)
	3.	Add logic to handle the enable and reset inputs:
	•	Enable the PID control only when the enable input is TRUE
	•	Reset the integral and error terms when the reset input is TRUE
	4.	Include detailed comments explaining the function block’s inputs, outputs, and the PID control process
	5.	Perform thorough testing to ensure scan-cycle safety, real-time responsiveness, and proper handling of edge cases
	6.	Optimize the function block for performance and memory usage, considering the constraints of PLC environments
	7.	Provide examples of how to integrate the function block into a control system, including tuning and parameter selection
	8.	Ensure that the function block is modular and reusable, with clear documentation for integration and maintenance
	9.	Implement safety checks and error handling

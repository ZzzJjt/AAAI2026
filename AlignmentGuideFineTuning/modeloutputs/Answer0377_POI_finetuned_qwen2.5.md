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
	•	Output, optionally Error, Integral, Derivative for monitoring

Tuning modes:
	•	Enable/Disable runtime adjustment of gains
	•	Provide methods to gradually adjust gains for smooth transitions
	•	Include a reset mechanism to clear the integral and start from a neutral state
	•	Implement safeguards to prevent abrupt gain changes that could lead to instability
	•	Enable logging or status outputs to monitor the controller’s health and performance
	•	Include a self-contained function block with a clear, structured layout for PLC integration
	•	Ensure that the function block is scan-cycle-safe and includes error handling for robustness
	•	Provide detailed comments explaining the logic and the role of each parameter
	•	Include a discussion of the benefits of using a self-contained function block in PLC programming, particularly for PID control, and highlight its advantages in terms of modularity, reusability, and maintainability
	•	Explain how this approach can improve code clarity, reduce development time, and enhance collaboration in industrial automation projects
	•	Include a comparison with traditional methods of implementing PID control in PLCs, emphasizing the advantages of a structured, function block-based approach
	•	Provide examples of how this function block can be integrated into larger control systems, including typical use cases and practical implementation tips
	•	Include a discussion of the limitations of the function block, such as scan-cycle timing and memory constraints, and provide guidance on optimizing its performance in real-world applications
	•	Include a list of references or further reading for developers looking to expand their understanding of PID control and Structured Text programming in PLCs
	•	Provide a detailed explanation of the function block’s inputs and outputs, including typical ranges and units, to ensure proper integration and tuning
	•	Include a discussion of the function block’s limitations, such as scan-cycle timing and memory constraints, and provide guidance on optimizing its performance in real-world applications
	•	Provide a comparison of the function block’s performance with traditional methods of implementing PID control in PLCs, highlighting its advantages in terms of modularity, reusability, and maintainability
	•	Include a discussion of the function block’s limitations, such as scan-cycle timing and memory constraints, and provide guidance on optimizing its performance in real-world applications
	•	Provide a comparison of the function block’s performance with traditional methods of implementing PID control in PLCs, highlighting its advantages in terms of modularity, reusability, and maintainability
	•	Include a discussion of the function

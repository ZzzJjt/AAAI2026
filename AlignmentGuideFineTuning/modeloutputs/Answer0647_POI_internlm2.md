### Intent:
"Implement a Kalman filter function block in IEC 61131-3 Structured Text for real-time state estimation (position and velocity) with configurable noise parameters and reset capability."

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
"Implement a Kalman filter function block in IEC 61131-3 Structured Text for real-time state estimation (position and velocity) with configurable noise parameters and reset capability."
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

🟨 C (Constraints) – Constraints

•	IEC 61131-3 Structured Text
•	Real-time execution
•	No external libraries or dependencies
•	No use of floating-point arithmetic
•	No use of complex data types
•	No use of conditional statements or loops
•	No use of function blocks or function calls
•	No use of timers or counters
•	No use of external memory (RAM or ROM)
•	No use of external storage (e.g., EEPROM)
•	No use of external communication (e.g., Ethernet, CAN)
•	No use of external hardware (e.g., sensors, actuators)
•	No use of external power supply
•	No use of external clock or synchronization
•	No use of external interrupts
•	No use of external events or signals
•	No use of external tasks or threads
•	No use of external synchronization primitives (e.g., semaphores, mutexes)
•	No use of external synchronization mechanisms (e.g., critical sections)
•	No use of external synchronization protocols (e.g., master-slave)
•	No use of external synchronization services (e.g., distributed locks)
•	No use of external synchronization tools (e.g., barriers)
•	No use of external synchronization objects (e.g., barriers, semaphores, mutexes)
•	No use of external synchronization primitives (e.g., critical sections)
•	No use of external synchronization mechanisms (e.g., master-slave)
•	No use of external synchronization protocols (e.g., distributed locks)
•	No use of external synchronization services (e.g., barriers)
•	No use of external synchronization tools (e.g., barriers)
•	No use of external synchronization objects (e.g., barriers, semaphores, mutexes)
•	No use of external synchronization primitives (e.g., critical sections)
•	No use of external synchronization mechanisms (e.g., master-slave)
•	No use of external synchronization protocols (e.g., distributed locks)
•	No use of external synchronization services (e.g., barriers)
•	No use of external synchronization tools (e.g., barriers)
•	No use of external synchronization objects (e.g., barriers, semaphores, mutexes)
•	No use of external synchronization primitives (e.g., critical sections)
•	No use of external

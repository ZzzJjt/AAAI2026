### Intent:
**Intent Summary:**  
Create a reusable Quicksort function block in IEC 61131-3 Structured Text to sort integer arrays iteratively (using stack-based bounds tracking) for PLC applications, with configurable execution control and completion signaling.  

*(Focus: Industrial sorting utility for PLCs, emphasizing iterative implementation, input/output handling, and deterministic execution.)*

### Prompt:
**PID Controller:**
Implement a self-contained function block in IEC 61131-3 structured text to create a PID controller. Include configurable parameters for proportional, integral, and derivative gains, with error handling and tuning capability.

**T-A-G:**

🟥 T (Task)

Implement a self-contained PID controller as a function block in IEC 61131-3 Structured Text for real-time control in PLC-based automation systems.

⸻

🟩 A (Action)
	•	Define the following inputs:
	•	Setpoint, ProcessVariable (for error calculation)
	•	Kp, Ki, Kd (gain tuning parameters)
	•	MinOutput, MaxOutput (output clamping)
	•	Enable, Reset (runtime control flags)
	•	Create the PID logic:
	•	Compute the control error: Error := Setpoint - ProcessVariable
	•	Accumulate the integral term using Ki and DeltaT, with anti-windup logic
	•	Calculate the derivative term from the rate of change of the process variable
	•	Compute the control output and apply output limits
	•	Reset internal states if Reset = TRUE
	•	Use internal memory to track previous values and ensure smooth scan-cycle execution
	•	Include comments for each computation block to improve readability and maintenance

⸻

🟦 G (Goal)

Deliver a robust, tunable, and reusable PID controller function block that performs well in real-time industrial control applications. The block should ensure safe, stable, and accurate output control with built-in safeguards like anti-windup and clamping, making it suitable for integration into any PLC-based closed-loop control system.

### Generated Code:
**Intent Summary:**  
Create a reusable Quicksort function block in IEC 61131-3 Structured Text to sort integer arrays iteratively (using stack-based bounds tracking) for PLC applications, with configurable execution control and completion signaling.  

*(Focus: Industrial sorting utility for PLCs, emphasizing iterative implementation, input/output handling, and deterministic execution.)*
**PID Controller:**
Implement a self-contained function block in IEC 61131-3 structured text to create a PID controller. Include configurable parameters for proportional, integral, and derivative gains, with error handling and tuning capability.

**T-A-G:**

🟥 T (Task)

Implement a self-contained PID controller as a function block in IEC 61131-3 Structured Text for real-time control in PLC-based automation systems.

⸻

🟩 A (Action)
	•	Define the following inputs:
	•	Setpoint, ProcessVariable (for error calculation)
	•	Kp, Ki, Kd (gain tuning parameters)
	•	MinOutput, MaxOutput (output clamping)
	•	Enable, Reset (runtime control flags)
	•	Create the PID logic:
	•	Compute the control error: Error := Setpoint - ProcessVariable
	•	Accumulate the integral term using Ki and DeltaT, with anti-windup logic
	•	Calculate the derivative term from the rate of change of the process variable
	•	Compute the control output and apply output limits
	•	Reset internal states if Reset = TRUE
	•	Use internal memory to track previous values and ensure smooth scan-cycle execution
	•	Include comments for each computation block to improve readability and maintenance

⸻

🟦 G (Goal)

Deliver a robust, tunable, and reusable PID controller function block that performs well in real-time industrial control applications. The block should ensure safe, stable, and accurate output control with built-in safeguards like anti-windup and clamping, making it suitable for integration into any PLC-based closed-loop control system.

⸻

🟩 A (Action)
	•	Define the following outputs:
	•	ControlSignal (proportional and integral components)
	•	DerivativeSignal (derivative component)
	•	ErrorSignal (error value)
	•	Enable the function block and implement the following features:
	•	Stack-based bounds tracking for iterative execution
	•	Input/output handling for error calculation and control signal generation
	•	Completion signaling for successful execution
	•	Configurable execution control for runtime parameter tuning and reset
	•	Include comments for each output block to improve readability and maintenance

⸻

🟥 T (Task)

Implement a Quicksort function block in IEC 61131-3 Structured Text for iterative array sorting. Include configurable execution control and completion signaling.

⸻

🟩 A (Action)
	•	Define the following inputs:
	•	Array (input array to be sorted)
	•	MinIndex, MaxIndex (bounds for stack-based bounds tracking)
	•	Enable, Reset (runtime control flags)
	•	Create the Quicksort logic:
	•	Compute the pivot element and partition the array around it
	•	Push the elements smaller than the pivot to the stack and the elements larger than the pivot to the stack
	•	Pop elements from the stack and recursively sort them
	•	Merge the sorted sub-arrays and return the sorted array
	•	Include comments for each computation block to improve readability and maintenance

⸻

🟦 G (Goal)

Deliver a robust, configurable, and reusable Quicksort function block that performs well in real-time industrial control applications. The block should ensure safe, stable, and accurate output control with built-in safeguards like stack-based bounds tracking and completion signaling, making it suitable for integration into any PLC-based closed-loop control system.

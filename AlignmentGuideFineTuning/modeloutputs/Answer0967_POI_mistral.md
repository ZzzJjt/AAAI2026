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

---

**Quicksort Function Block:**

🟥 T (Task)

Develop a reusable Quicksort function block in IEC 61131-3 Structured Text for PLC applications, utilizing an iterative, stack-based bounds tracking approach to sort integer arrays efficiently.

⸻

🟩 A (Action)
	•	Define the following inputs:
	•	Array (the array to be sorted)
	•	StartIndex, EndIndex (bounds of the array segment to be sorted)
	•	Swap (a function to swap two elements in the array)
	•	Compare (a function to compare two elements in the array)
	•	Create the Quicksort logic:
	•	If the array segment has only one element or is empty, return
	•	Choose a pivot element and partition the array into three segments: left, equal, and right
	•	Recursively call the Quicksort function for the left and right segments
	•	Use a stack to track the bounds of the unsorted segments
	•	Include comments for each computation block to improve readability and maintenance

⸻

🟦 G (Goal)

Deliver a high-performance, efficient, and reusable Quicksort function block that can be easily integrated into PLC-based applications for sorting integer arrays. The block should ensure deterministic execution, minimize stack usage, and provide a simple interface for custom comparison and swapping functions, making it suitable for a wide range of industrial sorting tasks.

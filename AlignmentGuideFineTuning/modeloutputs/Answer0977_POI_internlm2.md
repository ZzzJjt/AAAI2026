### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block for a PID controller with configurable gains, error handling, anti-windup, and output clamping to enable precise real-time closed-loop control in PLC systems.  

*(Focus: Robust industrial PID logic with tuning, safety, and reusability.)*

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
Create a reusable IEC 61131-3 structured text function block for a PID controller with configurable gains, error handling, anti-windup, and output clamping to enable precise real-time closed-loop control in PLC systems.  

*(Focus: Robust industrial PID logic with tuning, safety, and reusability.)*
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

Deliver a robust, tunable, and reusable PID controller function block that performs well in real-time industrial control applications. The block should ensure safe, stable, and accurate output control with built-in safeguards like anti-windup and clamping, making it suitable for integration into any PLC-based closed-loop control system. The function block should be well-documented, with clear comments and a concise design that promotes easy integration and maintenance.

**Additional Considerations:**

- **Safety:** Ensure that the PID controller is safe to use in industrial applications by implementing safeguards like anti-windup and output clamping. These features will prevent the controller from driving the process variable beyond safe limits, protecting the system from damage and ensuring reliable operation.
- **Tuning:** Provide a mechanism for tuning the PID gains (Kp, Ki, Kd) to achieve optimal performance for the specific process being controlled. This may include a user interface or a set of guidelines for manual tuning.
- **Reusability:** Design the function block to be easily reusable in different control systems, with minimal configuration required for each application. This can be achieved by using standard data types, well-defined input/output parameters, and clear documentation.
- **Documentation:** Include detailed comments and documentation within the function block to explain the purpose of each component, the expected behavior, and any limitations or assumptions. This will make it easier for other developers to understand and integrate the PID controller into their projects.
- **Testing:** Thoroughly test the PID controller in various scenarios to ensure its accuracy, stability, and robustness. This may include testing with different process dynamics, gain settings, and disturbances to validate the controller's performance and behavior.
- **Performance:** Optimize the function block for real-time execution in PLC systems, considering factors like memory usage, processing time, and scan cycle requirements. This will ensure that the PID controller can be used in high-speed control applications without causing performance issues or delays.
- **Maintenance:** Design the function block with maintainability in mind, using modular and well-structured code that is easy to modify and extend. This will make it easier to update the controller in the future, as new features or improvements are required.

**Deliverables:**

- **Function Block:** A complete IEC 61131-3 structured text function block for the PID controller, including all necessary input/output parameters, logic, and comments.
- **Documentation:** Detailed comments and documentation within the function block, explaining the purpose of each component, expected behavior, and any limitations or assumptions.
- **Test Cases:** A set of test cases to validate the PID controller's accuracy, stability, and robustness in various scenarios.
- **Performance Analysis:** A report analyzing the function block's performance in terms of

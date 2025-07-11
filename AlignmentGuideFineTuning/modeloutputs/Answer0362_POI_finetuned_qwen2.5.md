### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block for a configurable digital counter with up/down modes, step size, overflow handling, and reset functionality.  

*(Focus: Modularity, safety, and clarity for industrial PLC applications.)*

### Prompt:
**Counter:**
Implement a self-contained function block in IEC 61131-3 structured text for a digital counter with up/down counting modes. Include configurable initial value, step size, and overflow handling.

**C-A-R-E:**

🟥 C (Context) – Background Situation

Digital counters are commonly used in industrial control systems to track quantities such as parts, pulses, or process cycles. However, many basic implementations lack configurable options like up/down mode, step size control, and overflow protection. In a PLC environment governed by scan cycles, a flexible, reusable counter function block can improve both functionality and system safety.

⸻

🟩 A (Action) – Task to Perform

Implement a self-contained function block in IEC 61131-3 Structured Text that performs as a versatile digital counter, supporting:
	•	Up and down counting modes based on a direction input
	•	A configurable initial value and custom step size
	•	Handling of overflow and underflow conditions using max and min limits
	•	An optional reset function to reinitialize the counter
	•	Clearly defined input/output variables and readable internal logic

⸻

🟨 R (Result) – Expected Outcome

The result should be a modular, reliable function block that can be easily reused across projects requiring counting logic. It should integrate seamlessly into existing PLC programs, provide accurate state tracking, and protect against boundary violations. The implementation should enhance maintainability, safety, and clarity in industrial automation systems.

⸻

🟦 E (Example) – Concrete Illustration

Example functionality:

IF Enable THEN
   IF Reset THEN
      CurrentValue := InitValue;
   ELSIF CountUp THEN
      CurrentValue := CurrentValue + StepSize;
   ELSE
      CurrentValue := CurrentValue - StepSize;
   END_IF;

   // Handle overflow and underflow
   IF CurrentValue >= MaxValue THEN
      CurrentValue := MaxValue;
      AtMax := TRUE;
   ELSIF CurrentValue <= MinValue THEN
      CurrentValue := MinValue;
      AtMin := TRUE;
   END_IF;
END_IF;

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block for a configurable digital counter with up/down modes, step size, overflow handling, and reset functionality.  

*(Focus: Modularity, safety, and clarity for industrial PLC applications.)*
**Counter:**
Implement a self-contained function block in IEC 61131-3 structured text for a digital counter with up/down counting modes. Include configurable initial value, step size, and overflow handling.

**C-A-R-E:**

🟥 C (Context) – Background Situation

Digital counters are commonly used in industrial control systems to track quantities such as parts, pulses, or process cycles. However, many basic implementations lack configurable options like up/down mode, step size control, and overflow protection. In a PLC environment governed by scan cycles, a flexible, reusable counter function block can improve both functionality and system safety.

⸻

🟩 A (Action) – Task to Perform

Implement a self-contained function block in IEC 61131-3 Structured Text that performs as a versatile digital counter, supporting:
	•	Up and down counting modes based on a direction input
	•	A configurable initial value and custom step size
	•	Handling of overflow and underflow conditions using max and min limits
	•	An optional reset function to reinitialize the counter
	•	Clearly defined input/output variables and readable internal logic

⸻

🟨 R (Result) – Expected Outcome

The result should be a modular, reliable function block that can be easily reused across projects requiring counting logic. It should integrate seamlessly into existing PLC programs, provide accurate state tracking, and protect against boundary violations. The implementation should enhance maintainability, safety, and clarity in industrial automation systems.

⸻

🟦 E (Example) – Concrete Illustration

Example functionality:

IF Enable THEN
   IF Reset THEN
      CurrentValue := InitValue;
   ELSIF CountUp THEN
      CurrentValue := CurrentValue + StepSize;
   ELSE
      CurrentValue := CurrentValue - StepSize;
   END_IF;

   // Handle overflow and underflow
   IF CurrentValue >= MaxValue THEN
      CurrentValue := MaxValue;
      AtMax := TRUE;
   ELSIF CurrentValue <= MinValue THEN
      CurrentValue := MinValue;
      AtMin := TRUE;
   END_IF;
END_IF;  

This example shows how to create a self-contained function block that manages both up and down counting modes, with configurable step sizes and limits, while ensuring proper handling of edge cases like overflow and underflow. It also includes a reset capability to clear the counter to its initial value.

⸻

Incorporate this function block into your PLC programs to enable precise and flexible counting operations, improving system responsiveness and safety in industrial automation tasks.

**B-A-B-E:**

🟥 B (Before) – The Challenge

In industrial automation, especially with PLCs, basic counters often lack flexibility and safety features. Without configurable options for up/down counting, custom step sizes, and overflow protection, engineers face limitations in implementing precise control logic. This can lead to inefficiencies, safety risks, and increased development time.

⸻

🟩 A (After) – The Desired Outcome

After implementing a self-contained function block in IEC 61131-3 Structured Text for a configurable digital counter, the following benefits are achieved:

	•	Up and down counting modes: The function block supports both incrementing and decrementing operations, allowing for bidirectional counting.
	•	Configurable step size: Users can define the amount by which the counter value changes with each step, providing flexibility in applications where precise control is needed.
	•	Overflow and underflow protection: The block includes logic to handle scenarios where the counter value exceeds its maximum or minimum limits, ensuring safe operation and preventing system failures.
	•	Reset functionality: A dedicated input allows for the counter to be reset to an initial value, providing a mechanism for reinitializing the counting process when required.

⸻

🟨 R (Result) – The Value Provided

The result of implementing this function block is a reusable, modular, and configurable digital counter that enhances the capabilities of industrial control systems. It provides a standardized approach to counting logic, improving system flexibility, safety, and maintainability. This leads to more efficient and reliable automation solutions, with reduced development time and lower risk of errors or system failures.

⸻

🟦 E (Example) – A Real-World Application

In a packaging line, a configurable counter could be used to track the number of bottles filled, with the ability to adjust the counting step size based on the bottle size or packaging speed. The up/down modes could be used to account for missing bottles or overfilling, while overflow protection ensures that the system remains stable under abnormal conditions.

	•	Inputs:
	•	Enable:

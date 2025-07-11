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

Example usage:

VAR
   Counter: BOOL;
   Direction: BOOL;
   StepSize: INT;
   InitValue: INT;
   MaxValue: INT;
   MinValue: INT;
   AtMax: BOOL;
   AtMin: BOOL;
   CurrentValue: INT;

CALL Counter_Up_Down(
   Counter := TRUE,
   Direction := TRUE,
   StepSize := 1,
   InitValue := 0,
   MaxValue := 100,
   MinValue := -100,
   AtMax := FALSE,
   AtMin := FALSE,
   CurrentValue := 0
);

END_VAR;

⸻

🟪 A (Analysis) – Decomposition into Smaller Steps

•	Define the input and output variables for the function block, including the enable, direction, step size, initial value, and limits for the counter.
•	Implement the logic for counting up or down based on the direction input, with the step size applied to the current value.
•	Handle overflow and underflow conditions by setting the current value to the maximum or minimum limit, respectively.
•	Include a reset function to initialize the counter to the initial value.
•	Ensure the function block is self-contained, with clear comments and variable naming for easy integration into PLC programs.

⸻

🟩 I (Insight) – Key Point or Concept

The key insight is to create a modular, self-contained function block for a digital counter in IEC 61131-3 Structured Text. This allows for flexible counting logic with configurable parameters, while maintaining safety and clarity in industrial automation systems.

⸻

🟥 C (Conclusion) – Final Thoughts

By implementing a reusable function block for a digital counter with up/down modes, step size control, and overflow handling, you can enhance the flexibility and safety of your PLC-based automation systems. This modular approach ensures that counting logic is self-contained and easily integrated into existing code, while also providing clear documentation and input/output definitions for seamless integration.

### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block for a configurable digital counter with up/down modes, step size, limits, and overflow/underflow protection.  

*(Focus: Modular, safe, and flexible counting logic for PLCs.)*

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
Create a reusable IEC 61131-3 structured text function block for a configurable digital counter with up/down modes, step size, limits, and overflow/underflow protection.  

*(Focus: Modular, safe, and flexible counting logic for PLCs.)*
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

Example I/O:

Inputs:
   •	Enable: Boolean (start/stop counter)
   •	CountUp: Boolean (up/down mode)
   •	StepSize: Integer (increment/decrement)
   •	Reset: Boolean (reset counter)

Outputs:
   •	CurrentValue: Integer (current counter value)
   •	AtMax: Boolean (counter reached maximum)
   •	AtMin: Boolean (counter reached minimum)

⸻

🟪 A (Analysis) – Breakdown

The function block should handle the following:
	•	Input validation: Ensure that the enable, count up/down, and step size signals are valid and within expected ranges.
	•	State tracking: Maintain the current counter value, updating it based on the count up/down mode and step size.
	•	Limit handling: Implement logic to detect and handle overflow and underflow conditions, setting the counter to the maximum or minimum value when necessary.
	•	Output signals: Provide clear and self-explanatory outputs, including the current counter value and flags indicating whether the counter has reached its maximum or minimum limits.

⸻

🟩 T (Tips) – Suggestions

	•	Ensure that the function block is self-contained, with all necessary logic and state tracking encapsulated within the block.
	•	Use clear variable names and comments to improve readability and maintainability.
	•	Consider adding a reset input to allow for easy reinitialization of the counter.
	•	Handle edge cases, such as the transition between up and down modes, to ensure smooth operation.
	•	Implement input validation to prevent unexpected behavior due to invalid signals.

**Counter:**
Implement a self-contained function block in IEC 61131-3 Structured Text that performs as a versatile digital counter, supporting:
	•	Up and down counting modes based on a direction input
	•	A configurable initial value and custom step size
	•	Handling of overflow and underflow conditions using max and min limits
	•	An optional reset function to reinitialize the counter
	•	Clearly defined input/output variables and readable internal logic.

**C-A-R-E:**

🟥 C (Context) – Background Situation

Digital counters are commonly used in industrial control systems to track quantities such as parts, pulses, or process cycles. However, many basic implementations lack configurable options like up/down mode,

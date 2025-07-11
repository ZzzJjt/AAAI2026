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
END_IF; To create a reusable IEC 61131-3 structured text function block for a configurable digital counter, follow these steps:

1. **Define Inputs and Outputs:**
   - `Enable`: Boolean input to enable/disable the counter.
   - `Reset`: Boolean input to reset the counter.
   - `CountUp`: Boolean input to set the counting direction (up or down).
   - `InitValue`: Integer input for the initial value of the counter.
   - `StepSize`: Integer input for the step size of the counter.
   - `MaxValue`: Integer input for the maximum value of the counter.
   - `MinValue`: Integer input for the minimum value of the counter.
   - `CurrentValue`: Integer output for the current value of the counter.
   - `AtMax`: Boolean output indicating if the counter has reached its maximum value.
   - `AtMin`: Boolean output indicating if the counter has reached its minimum value.

2. **Implement the Counter Logic:**
   - Initialize the counter with the `InitValue`.
   - Update the counter based on the `CountUp` input and the `StepSize`.
   - Check for overflow and underflow conditions and handle them using the `MaxValue` and `MinValue`.
   - Set the `AtMax` and `AtMin` outputs accordingly.

Here is the structured text implementation:

```structuredtext
FUNCTION_BLOCK Counter
VAR_INPUT
   Enable : BOOL;
   Reset : BOOL;
   CountUp : BOOL;
   InitValue : INT;
   StepSize : INT;
   MaxValue : INT;
   MinValue : INT;
END_VAR

VAR_OUTPUT
   CurrentValue : INT;
   AtMax : BOOL;
   AtMin : BOOL;
END_VAR

VAR
   CurrentValueInternal : INT := InitValue;
   AtMaxInternal : BOOL := FALSE;
   AtMinInternal : BOOL := FALSE;
END_VAR

IF Enable THEN
   IF Reset THEN
      CurrentValueInternal := InitValue;
      AtMaxInternal := FALSE;
      AtMinInternal := FALSE;
   ELSE
      IF CountUp THEN
         CurrentValueInternal := CurrentValueInternal + StepSize;
      ELSE
         CurrentValueInternal := CurrentValueInternal - StepSize;
      END_IF;

      // Handle overflow and underflow
      IF CurrentValueInternal >= MaxValue THEN
         CurrentValueInternal := MaxValue;
         AtMaxInternal := TRUE;
      ELSIF CurrentValueInternal <= MinValue THEN
         CurrentValueInternal :=

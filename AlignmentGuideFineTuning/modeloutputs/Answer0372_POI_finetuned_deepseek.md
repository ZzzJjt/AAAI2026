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
FUNCTION_BLOCK FB_Counter
VAR_INPUT
    Enable : BOOL; // Enable/disable counter
    Reset : BOOL; // Reset counter to initial value
    CountUp : BOOL; // Set counter to increasing mode
    StepSize : INT; // Increment/decrement value
    MaxValue : INT; // Max limit
    MinValue : INT; // Min limit
END_VAR

VAR_OUTPUT
    CurrentValue : INT; // Current count value
    AtMax : BOOL; // Flag when at max limit
    AtMin : BOOL; // Flag when at min limit
END_VAR

VAR
    PrevValue : INT; // Previous value for underflow/overflow detection
END_VAR

// Initialize outputs
CurrentValue := 0;
AtMax := FALSE;
AtMin := FALSE;

// Internal logic
IF Enable THEN
    IF Reset THEN
        CurrentValue := InitValue;
        PrevValue := CurrentValue;
    ELSIF CountUp THEN
        CurrentValue := CurrentValue + StepSize;
        PrevValue := CurrentValue;
    ELSE
        CurrentValue := CurrentValue - StepSize;
        PrevValue := CurrentValue;
    END_IF;

    // Check for overflow and underflow
    IF CurrentValue >= MaxValue THEN
        CurrentValue := MaxValue;
        AtMax := TRUE;
    ELSIF CurrentValue <= MinValue THEN
        CurrentValue := MinValue;
        AtMin := TRUE;
    END_IF;

    // Check for underflow and overflow
    IF CurrentValue < MinValue AND PrevValue >= MinValue THEN
        CurrentValue := MinValue;
        AtMin := TRUE;
    ELSIF CurrentValue > MaxValue AND PrevValue <= MaxValue THEN
        CurrentValue := MaxValue;
        AtMax := TRUE;
    END_IF;
END_IF;
END_FUNCTION_BLOCK
(* IEC 61131-3 Structured Text: FB_Counter Function Block *)
(* Purpose: Implements a configurable digital counter with up/down modes, step size, and limits *)
(* Features: Configurable initial value, step size, max/min limits, reset, and overflow/underflow handling *)

FUNCTION_BLOCK FB_Counter
VAR_INPUT
    Enable : BOOL; // Enable/disable counter
    Reset

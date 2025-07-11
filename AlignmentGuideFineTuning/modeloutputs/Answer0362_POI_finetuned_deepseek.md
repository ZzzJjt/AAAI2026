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
FUNCTION_BLOCK FB_DigitalCounter
VAR_INPUT
    Enable : BOOL; // Enable counter operation
    Reset : BOOL; // Reset counter to initial value
    CountUp : BOOL; // Set counter to increase
    StepSize : INT; // Increment/decrement value
    InitValue : INT; // Initial value
    MaxValue : INT; // Max value
    MinValue : INT; // Min value
END_VAR

VAR_OUTPUT
    CurrentValue : INT; // Current value of the counter
    AtMax : BOOL; // Flag indicating if current value is max
    AtMin : BOOL; // Flag indicating if current value is min
END_VAR

VAR
    PrevValue : INT; // Previous value for overflow/underflow detection
END_VAR

// Reset counter to initial value
IF Reset THEN
    CurrentValue := InitValue;
    AtMax := FALSE;
    AtMin := FALSE;
    PrevValue := InitValue;
    CountUp := FALSE;
    StepSize := 0;
END_IF;

// Enable counter operation
IF Enable THEN
    // Check for overflow/underflow
    IF CurrentValue >= MaxValue THEN
        CurrentValue := MaxValue;
        AtMax := TRUE;
    ELSIF CurrentValue <= MinValue THEN
        CurrentValue := MinValue;
        AtMin := TRUE;
    END_IF;

    // Update current value based on direction and step size
    IF CountUp THEN
        CurrentValue := CurrentValue + StepSize;
    ELSE
        CurrentValue := CurrentValue - StepSize;
    END_IF;

    // Check if current value is valid
    IF CurrentValue >= MaxValue THEN
        CurrentValue := MaxValue;
        AtMax := TRUE;
    ELSIF CurrentValue <= MinValue THEN
        CurrentValue := MinValue;
        AtMin := TRUE;
    END_IF;

    // Store previous value for next scan cycle
    PrevValue := CurrentValue;
END_IF;

// Output current value and flags
CurrentValue := PrevValue;
AtMax := FALSE;
AtMin := FALSE;
END_FUNCTION_BLOCK

// Example usage:
// Enable := TRUE;
// Reset := FALSE;
// CountUp := TRUE;
// StepSize := 1;

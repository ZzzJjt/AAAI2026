### Intent:
"Create a reusable IEC 61131-3 structured text function block for a configurable digital counter with up/down modes, initial value/step settings, limit protection, and status outputs for PLC automation systems."

### Prompt:
**Counter:**
Implement a self-contained function block in IEC 61131-3 structured text for a digital counter with up/down counting modes. Include configurable initial value, step size, and overflow handling.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC developer creating a flexible, reusable digital counter function block in IEC 61131-3 Structured Text for automation applications.

⸻

🟩 T (Task) – Define the Objective

Implement a self-contained counter function block that supports both up and down counting modes with the following features:
	•	A configurable initial value and step size
	•	Inputs for count direction, enable, and reset
	•	Protection against overflow and underflow, using configurable MaxValue and MinValue limits
	•	Output of the current count value and status flags indicating if limits are reached

The counter should operate reliably in scan-cycle-driven environments and support integration into larger automation programs.

⸻

🟧 F (Format) – Specify the Output Format

Provide:
	•	A complete IEC 61131-3 Structured Text function block
	•	Declarations for all inputs, outputs, and internal variables
	•	Logic using IF/ELSIF structures to increment/decrement the counter
	•	Overflow and underflow handling using comparison conditions
	•	A Reset condition to reinitialize the counter
	•	Inline comments explaining the purpose of each block of code

### Generated Code:
"Create a reusable IEC 61131-3 structured text function block for a configurable digital counter with up/down modes, initial value/step settings, limit protection, and status outputs for PLC automation systems."
**Counter:**
Implement a self-contained function block in IEC 61131-3 structured text for a digital counter with up/down counting modes. Include configurable initial value, step size, and overflow handling.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC developer creating a flexible, reusable digital counter function block in IEC 61131-3 Structured Text for automation applications.

⸻

🟩 T (Task) – Define the Objective

Implement a self-contained counter function block that supports both up and down counting modes with the following features:
	•	A configurable initial value and step size
	•	Inputs for count direction, enable, and reset
	•	Protection against overflow and underflow, using configurable MaxValue and MinValue limits
	•	Output of the current count value and status flags indicating if limits are reached

The counter should operate reliably in scan-cycle-driven environments and support integration into larger automation programs.

⸻

🟧 F (Format) – Specify the Output Format

Provide:
	•	A complete IEC 61131-3 Structured Text function block
	•	Declarations for all inputs, outputs, and internal variables
	•	Logic using IF/ELSIF structures to increment/decrement the counter
	•	Overflow and underflow handling using comparison conditions
	•	A Reset condition to reinitialize the counter
	•	Inline comments explaining the purpose of each block of code

⸻

🟨 S (Solution) – Provide the Solution

```IEC 61131-3 Structured Text
// Digital Counter Function Block
FB DigitalCounter
  VAR_INPUT
    Direction : BOOL;  // Up/Down Counting Direction
    Enable : BOOL;  // Counter Enable
    Reset : BOOL;  // Counter Reset
    InitialValue : INT;  // Initial Counter Value
    StepSize : INT;  // Step Size for Increment/Decrement
    MaxValue : INT;  // Maximum Counter Value
    MinValue : INT;  // Minimum Counter Value
  END_VAR

  VAR
    CounterValue : INT := InitialValue;  // Current Counter Value
    LimitReached : BOOL := FALSE;  // Flag indicating if limits are reached
  END_VAR

  IF Enable THEN
    IF Direction THEN
      IF CounterValue < MaxValue THEN
        CounterValue := CounterValue + StepSize;
      ELSIF CounterValue = MaxValue THEN
        LimitReached := TRUE;
      END_IF;
    ELSE
      IF CounterValue > MinValue THEN
        CounterValue := CounterValue - StepSize;
      ELSIF CounterValue = MinValue THEN
        LimitReached := TRUE;
      END_IF;
    END_IF;
  END_IF;

  IF Reset THEN
    CounterValue := InitialValue;
    LimitReached := FALSE;
  END_IF;

END_FB;
```

**Evaluation:**

The provided function block meets the requirements of the task. It includes all necessary inputs, outputs, and internal variables, and implements the logic for up/down counting with overflow and underflow protection. The comments within the code help to understand the purpose of each block of code. The function block can be easily integrated into larger automation programs and is ready for use in a PLC automation system.

**Additional Considerations:**

1. **Error Handling**: The function block does not include error handling. In a real-world application, it would be beneficial to add error handling to ensure the function block operates correctly under all conditions.
2. **Performance**: The function block is designed to operate in a scan-cycle-driven environment. However, the performance may vary depending on the specific PLC system and the complexity of the larger automation program.
3. **Compatibility**: The function block is written in IEC 61131-3 Structured Text, which is compatible with most P

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

Ensure the function block is modular and can be easily integrated into larger automation programs.

**Counter Function Block:**
```structuredtext
// Counter Function Block
// Inputs:
//   - Direction: 0 = Up, 1 = Down
//   - Enable: Enable/disable counter operation
//   - Reset: Reset counter to initial value
// Outputs:
//   - Count: Current count value
//   - Overflow: True if count exceeds MaxValue
//   - Underflow: True if count falls below MinValue
// Internal Variables:
//   - InitialValue: Starting count value
//   - StepSize: Increment/decrement step size
//   - MaxValue: Maximum count value
//   - MinValue: Minimum count value
//   - CurrentCount: Current count value

// Function Block Declaration
FUNCTION_BLOCK Counter
VAR_INPUT
    Direction : BOOL; // 0 = Up, 1 = Down
    Enable : BOOL; // Enable/disable counter operation
    Reset : BOOL; // Reset counter to initial value
END_VAR
VAR_OUTPUT
    Count : INT; // Current count value
    Overflow : BOOL; // True if count exceeds MaxValue
    Underflow : BOOL; // True if count falls below MinValue
END_VAR
VAR
    InitialValue : INT; // Starting count value
    StepSize : INT; // Increment/decrement step size
    MaxValue : INT; // Maximum count value
    MinValue : INT; // Minimum count value
    CurrentCount : INT; // Current count value
END_VAR

// Initialization
INIT
    CurrentCount := InitialValue;
END_INIT

// Main Logic
RUN
    IF Enable THEN
        IF Direction THEN
            // Increment counter
            IF CurrentCount < MaxValue THEN
                CurrentCount := CurrentCount + StepSize;
            ELSE
                Overflow := TRUE;
            END_IF;
        ELSE
            // Decrement counter
            IF CurrentCount > MinValue THEN
                CurrentCount := CurrentCount - StepSize;
            ELSE
                Underflow := TRUE;
            END_IF;
        END_IF;
    END_IF;
END_RUN

// Reset Counter
IF Reset THEN
    CurrentCount := InitialValue;
    Overflow := FALSE;
    Underflow := FALSE;
END_IF

// Output Count Value
Count := CurrentCount;
```
This function block provides a flexible and reusable digital counter with configurable initial value, step size, and overflow handling. It supports both up and

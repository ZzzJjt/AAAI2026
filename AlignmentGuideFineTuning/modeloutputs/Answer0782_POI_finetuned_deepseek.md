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

For example:

// Inputs
Up := TRUE; // TRUE = up direction
Down := FALSE; // FALSE = down direction
Reset := FALSE; // Reset the counter to 0

// Outputs
CurrentCount := 0; // Current count value
Overflow := FALSE; // TRUE if count > MaxValue
Underflow := FALSE; // TRUE if count < MinValue

// Internal Variables
CurrentCount := 0; // Current count value
MaxValue := 100; // Max value for the counter
MinValue := 0; // Min value for the counter

// Logic
IF Up THEN
    CurrentCount := CurrentCount + 1;
ELSIF Down THEN
    CurrentCount := CurrentCount - 1;
ELSIF Reset THEN
    CurrentCount := 0;
END_IF;

// Check for overflow and underflow
IF CurrentCount > MaxValue THEN
    Overflow := TRUE;
ELSIF CurrentCount < MinValue THEN
    Underflow := TRUE;
END_IF;
FUNCTION_BLOCK FB_Counter
VAR_INPUT
    Enable : BOOL; // Enable the counter
    Reset : BOOL; // Reset the counter to 0
    Up : BOOL; // TRUE = up direction
    Down : BOOL; // FALSE = down direction
END_VAR

VAR_OUTPUT
    CurrentCount : INT; // Current count value
    Overflow : BOOL; // TRUE if count > MaxValue
    Underflow : BOOL; // TRUE if count < MinValue
    Done : BOOL; // TRUE when the counter is finished
END_VAR

VAR
    CurrentCount : INT := 0; // Current count value
    MaxValue : INT := 100; // Max value for the counter
    MinValue : INT := 0; // Min value for the counter
END_VAR

// Reset the counter to 0
IF Reset THEN
    CurrentCount := 0;
    Overflow := FALSE;
    Underflow := FALSE;
    Done := FALSE;
    Up := FALSE;
    Down := FALSE;
END_IF;

// Enable the counter
IF Enable THEN
    // Check for up direction
    IF Up THEN
        CurrentCount := CurrentCount + 1;
        IF CurrentCount > MaxValue THEN
            Overflow := TRUE;
        END_IF;

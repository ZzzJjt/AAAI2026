### Intent:
The task is to create a reusable IEC 61131-3 structured text function block for a configurable digital counter with up/down counting, overflow protection, and reset capabilities for industrial PLC applications.

### Prompt:
**Counter:**
Implement a self-contained function block in IEC 61131-3 structured text for a digital counter with up/down counting modes. Include configurable initial value, step size, and overflow handling.


**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC programmer developing reusable function blocks in IEC 61131-3 Structured Text for use in industrial automation systems.

⸻

🟩 I (Input) – Information Provided

You need to implement a digital counter function block that:
	•	Supports both up and down counting modes
	•	Accepts a configurable initial value and step size
	•	Handles overflow and underflow conditions using MaxValue and MinValue limits
	•	Includes a reset input to reinitialize the counter
	•	Works efficiently in a scan-cycle PLC environment

⸻

🟧 S (Steps) – Steps to Perform
	1.	Define the function block interface with inputs:
	•	Enable : BOOL
	•	CountUp : BOOL
	•	StepSize : INT
	•	InitValue : INT
	•	Reset : BOOL
	•	MaxValue : INT
	•	MinValue : INT
	2.	Use internal logic to:
	•	Reset the counter when Reset = TRUE
	•	Increase or decrease the counter based on CountUp and Enable
	•	Clamp the value within MinValue and MaxValue to prevent overflows
	3.	Define outputs:
	•	CurrentValue : INT
	•	AtMax : BOOL
	•	AtMin : BOOL
	4.	Add inline comments to explain each control mechanism and safeguard.

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a robust, modular, and easy-to-use function block that enables configurable and safe digital counting in industrial environments. The block should be reusable, scan-cycle stable, and clear enough for other developers to maintain and integrate into larger control applications.

### Generated Code:
The task is to create a reusable IEC 61131-3 structured text function block for a configurable digital counter with up/down counting, overflow protection, and reset capabilities for industrial PLC applications.
**Counter:**
Implement a self-contained function block in IEC 61131-3 structured text for a digital counter with up/down counting modes. Include configurable initial value, step size, and overflow handling.


**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a PLC programmer developing reusable function blocks in IEC 61131-3 Structured Text for use in industrial automation systems.

⸻

🟩 I (Input) – Information Provided

You need to implement a digital counter function block that:
	•	Supports both up and down counting modes
	•	Accepts a configurable initial value and step size
	•	Handles overflow and underflow conditions using MaxValue and MinValue limits
	•	Includes a reset input to reinitialize the counter
	•	Works efficiently in a scan-cycle PLC environment

⸻

🟧 S (Steps) – Steps to Perform
	1.	Define the function block interface with inputs:
	•	Enable : BOOL
	•	CountUp : BOOL
	•	StepSize : INT
	•	InitValue : INT
	•	Reset : BOOL
	•	MaxValue : INT
	•	MinValue : INT
	2.	Use internal logic to:
	•	Reset the counter when Reset = TRUE
	•	Increase or decrease the counter based on CountUp and Enable
	•	Clamp the value within MinValue and MaxValue to prevent overflows
	3.	Define outputs:
	•	CurrentValue : INT
	•	AtMax : BOOL
	•	AtMin : BOOL
	4.	Add inline comments to explain each control mechanism and safeguard.

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a robust, modular, and easy-to-use function block that enables configurable and safe digital counting in industrial environments. The block should be reusable, scan-cycle stable, and clear enough for other developers to maintain and integrate into larger control applications.
FUNCTION_BLOCK FB_DigitalCounter
VAR_INPUT
    Enable : BOOL; // Enable the counter
    CountUp : BOOL; // TRUE for up counting, FALSE for down counting
    StepSize : INT; // Increment or decrement value
    InitValue : INT; // Initial value
    Reset : BOOL; // Reset the counter
    MaxValue : INT; // Maximum value
    MinValue : INT; // Minimum value
END_VAR

VAR_OUTPUT
    CurrentValue : INT; // Current value of the counter
    AtMax : BOOL; // TRUE if the counter has reached MaxValue
    AtMin : BOOL; // TRUE if the counter has reached MinValue
END_VAR

VAR
    // Internal state variables
    CurrentValue_ : INT;
    AtMax_ : BOOL;
    AtMin_ : BOOL;
END_VAR

METHOD Execute : BOOL
BEGIN
    // Reset the counter if Reset = TRUE
    IF Reset THEN
        CurrentValue := InitValue;
        AtMax := FALSE;
        AtMin := FALSE;
        RETURN TRUE;
    END_IF;

    // Check for overflow or underflow
    IF CurrentValue > MaxValue THEN
        AtMax := TRUE;
        CurrentValue := MaxValue;
    ELSIF CurrentValue < MinValue THEN
        AtMin := TRUE;
        CurrentValue := MinValue;
    END_IF;

    // Update the counter based on the input
    IF Enable THEN
        IF CountUp THEN
            CurrentValue := CurrentValue + StepSize;
        ELSIF CountUp THEN
            CurrentValue := CurrentValue - StepSize;
        END_IF;
    END_IF;

    // Clamp the value within MinValue and MaxValue
    IF CurrentValue > MaxValue THEN
        CurrentValue := MaxValue;
    ELSIF CurrentValue < MinValue THEN
        CurrentValue := MinValue;
    END_IF;

    // Store the current value
    CurrentValue_ := CurrentValue;
    AtMax_ := AtMax;
    AtMin_ := AtMin;

    RETURN TRUE;
END_METHOD

METHOD Reset : BOOL
BEGIN
    CurrentValue := InitValue;
    AtMax := FALSE;
    AtMin := FALSE;
    RETURN TRUE;
END

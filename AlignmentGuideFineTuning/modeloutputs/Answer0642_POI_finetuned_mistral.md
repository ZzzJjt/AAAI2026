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
FUNCTION_BLOCK FB_Counter
VAR_INPUT
    Enable : BOOL; // Enables counting
    CountUp : BOOL; // TRUE for up counting, FALSE for down counting
    StepSize : INT := 1; // Step size for counting
    InitValue : INT := 0; // Initial value of the counter
    Reset : BOOL; // Resets the counter to InitValue
    MaxValue : INT := 100; // Maximum value allowed
    MinValue : INT := 0; // Minimum value allowed
END_VAR

VAR_OUTPUT
    CurrentValue : INT; // Current value of the counter
    AtMax : BOOL; // TRUE when the counter reaches MaxValue
    AtMin : BOOL; // TRUE when the counter reaches MinValue
END_VAR

VAR
    PrevEnable : BOOL; // Previous state of Enable for edge detection
    PrevReset : BOOL; // Previous state of Reset for edge detection
    PrevCountUp : BOOL; // Previous state of CountUp for edge detection
END_VAR

METHOD Execute : BOOL
BEGIN
    // Edge detection for Enable, Reset, and CountUp
    PrevEnable := Enable;
    PrevReset := Reset;
    PrevCountUp := CountUp;

    IF Enable AND NOT PrevEnable THEN
        // Reset the counter if Reset is TRUE
        IF Reset THEN
            CurrentValue := InitValue;
            AtMax := FALSE;
            AtMin := FALSE;
        END_IF;
    END_IF;

    IF NOT Enable AND Enable = PrevEnable THEN
        // Store the current value as the new init value
        IF NOT Reset THEN
            InitValue := CurrentValue;
        END_IF;
    END_IF;

    IF CountUp AND Enable THEN
        // Increment or decrement the counter
        IF CurrentValue + StepSize <= MaxValue THEN
            CurrentValue := CurrentValue + StepSize;
        ELSE
            CurrentValue := MaxValue;
            AtMax := TRUE;
        END_IF;
    ELSIF NOT CountUp AND Enable THEN
        IF CurrentValue - StepSize >= MinValue THEN
            CurrentValue := CurrentValue - StepSize;

### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block for a configurable digital counter with up/down modes, initial value/step settings, and overflow protection, suitable for industrial PLC applications.  

*(Focus: Configurable counting logic with safety limits for automation systems.)*

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
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block for a configurable digital counter with up/down modes, initial value/step settings, and overflow protection, suitable for industrial PLC applications.  

*(Focus: Configurable counting logic with safety limits for automation systems.)*
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
    CountUp : BOOL; // TRUE to increment, FALSE to decrement
    StepSize : INT; // Increment/decrement value
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

    // Enable the counter
    IF Enable THEN
        // Count up if CountUp = TRUE
        IF CountUp THEN
            // Clamp the value within MinValue and MaxValue
            IF CurrentValue + StepSize > MaxValue THEN
                CurrentValue := MaxValue;
                AtMax := TRUE;
            ELSIF CurrentValue + StepSize < MinValue THEN
                CurrentValue := MinValue;
                AtMin := TRUE;
            ELSE
                CurrentValue := CurrentValue + StepSize;
            END_IF;
        // Count down if CountUp = FALSE
        ELSE
            IF CurrentValue - StepSize < MinValue THEN
                CurrentValue := MinValue;
                AtMin := TRUE;
            ELSIF CurrentValue - StepSize > MaxValue THEN
                CurrentValue := MaxValue;
                AtMax := TRUE;
            ELSE
                CurrentValue := CurrentValue - StepSize;
            END_IF;
        END_IF;
    END_IF;

    // Return TRUE if the counter is enabled and valid
    RETURN Enable AND NOT Reset;
END_METHOD

METHOD Reset : BOOL
BEGIN
    CurrentValue := InitValue;
    AtMax := FALSE;
    At

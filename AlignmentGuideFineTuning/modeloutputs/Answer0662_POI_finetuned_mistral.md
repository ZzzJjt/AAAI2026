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
FUNCTION_BLOCK FB_Counter
VAR_INPUT
    Enable : BOOL; // Enables counting
    CountUp : BOOL; // TRUE for up, FALSE for down
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
END_VAR

METHOD Execute : BOOL
BEGIN
    // Edge detection for Enable and Reset
    PrevEnable := Enable;
    PrevReset := Reset;
    IF Enable AND NOT PrevEnable THEN
        // Reset the counter when Enable goes high
        CurrentValue := InitValue;
        AtMax := FALSE;
        AtMin := FALSE;
    END_IF;

    IF Reset AND NOT PrevReset THEN
        // Reset the counter when Reset goes high
        CurrentValue := InitValue;
        AtMax := FALSE;
        AtMin := FALSE;
    END_IF;

    IF Enable AND NOT Reset THEN
        // Count up or down based on CountUp
        IF CountUp THEN
            // Increment the counter
            IF CurrentValue < MaxValue THEN
                CurrentValue := CurrentValue + StepSize;
            ELSE
                AtMax := TRUE; // Reach the maximum value
            END_IF;
        ELSE
            // Decrement the counter
            IF CurrentValue > MinValue THEN
                CurrentValue := CurrentValue - StepSize;
            ELSE
                AtMin := TRUE; // Reach the minimum value
            END_IF;
        END_IF;
    END_IF;

    RETURN TRUE; //

### Intent:
The task is to implement a reusable IEC 61131-3 structured text function block for a configurable digital counter with up/down counting modes, overflow protection, and reset capability for industrial PLC applications.

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
The task is to implement a reusable IEC 61131-3 structured text function block for a configurable digital counter with up/down counting modes, overflow protection, and reset capability for industrial PLC applications.
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
    StepSize : INT; // Step size for counting
    InitValue : INT; // Initial value of the counter
    Reset : BOOL; // Resets the counter to InitValue
    MaxValue : INT; // Maximum value for the counter
    MinValue : INT; // Minimum value for the counter
END_VAR

VAR_OUTPUT
    CurrentValue : INT; // Current value of the counter
    AtMax : BOOL; // TRUE when the counter reaches MaxValue
    AtMin : BOOL; // TRUE when the counter reaches MinValue
END_VAR

VAR
    PrevEnable : BOOL; // Previous state of Enable for debouncing
    Counter : INT; // Internal counter variable
END_VAR

// Reset the counter when Reset is TRUE
IF Reset THEN
    Counter := InitValue;
    AtMax := FALSE;
    AtMin := FALSE;
    RETURN;
END_IF;

// Debounce Enable input
PrevEnable := Enable;
Enable := NOT Enable; // Invert Enable to debounce
IF Enable AND NOT PrevEnable THEN
    // Rising edge detected
    // Initialize counter if Enable is TRUE and Reset is FALSE
    IF NOT Reset THEN
        Counter := InitValue;
        AtMax := FALSE;
        AtMin := FALSE;
    END_IF;
END_IF;

// Check if Enable is TRUE and Reset is FALSE
IF Enable AND NOT Reset THEN
    // Update counter based on CountUp and StepSize
    IF CountUp THEN
        IF Counter < MaxValue THEN
            Counter := Counter + StepSize;
        ELSE
            AtMax := TRUE;
        END_IF;
    ELSE
        IF Counter > MinValue THEN
            Counter := Counter - StepSize;
        ELSE
            AtMin := TRUE;
        END_IF;
    END_IF;
ELSE
    // Reset to initial value if Reset is TRUE
    Counter := InitValue;
    AtMax := FALSE;
    AtMin := FALSE;
END_IF;

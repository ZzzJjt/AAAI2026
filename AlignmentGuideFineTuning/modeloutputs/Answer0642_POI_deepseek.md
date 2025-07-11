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

⸻

🟪 S (Solution) – Solution

```
FUNCTION BLOCK Counter
    // Inputs
    ENABLE : BOOL
    COUNTUP : BOOL
    STEPSIZE : INT
    INITVALUE : INT
    RESET : BOOL
    MAXVALUE : INT
    MINVALUE : INT

    // Internal Variables
    CURRENTVALUE : INT
    ATMAX : BOOL
    ATMIN : BOOL

    // Initialize Counter
    IF RESET = TRUE THEN
        CURRENTVALUE = INITVALUE
    ELSE
        IF ENABLE = TRUE AND COUNTUP = TRUE THEN
            CURRENTVALUE = CURRENTVALUE + STEPSIZE
        ENDIF
    ENDIF

    // Overflow and Underflow Handling
    IF CURRENTVALUE > MAXVALUE THEN
        ATMAX = TRUE
        CURRENTVALUE = MAXVALUE
    ELSEIF CURRENTVALUE < MINVALUE THEN
        ATMIN = TRUE
        CURRENTVALUE = MINVALUE
    ENDIF

    // Outputs
    CURRENTVALUE : INT
    ATMAX : BOOL
    ATMIN : BOOL
END FUNCTION BLOCK
```

This solution provides a self-contained function block in IEC 61131-3 structured text for a digital counter with configurable initial value, step size, and overflow handling. The function block can be easily integrated into other control applications and is designed to work efficiently in a scan-cycle PLC environment.

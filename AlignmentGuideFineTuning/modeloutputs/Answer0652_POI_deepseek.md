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

⸻

🟪 S (Solution) – Solution

```
FUNCTION Block Counter
	VAR
		CurrentValue : INT
		AtMax : BOOL
		AtMin : BOOL
	END_VAR

	INPUT Enable : BOOL
	INPUT CountUp : BOOL
	INPUT StepSize : INT
	INPUT InitValue : INT
	INPUT Reset : BOOL
	INPUT MaxValue : INT
	INPUT MinValue : INT
	OUTPUT CurrentValue : INT
	OUTPUT AtMax : BOOL
	OUTPUT AtMin : BOOL

	IF Reset = TRUE THEN
		CurrentValue = InitValue
		AtMax = FALSE
		AtMin = FALSE
	END_IF

	IF Enable = TRUE THEN
		IF CurrentValue = MinValue THEN
			CurrentValue = MinValue + StepSize
			AtMin = FALSE
		END_IF

		IF CurrentValue = MaxValue THEN
			CurrentValue = MaxValue - StepSize
			AtMax = TRUE
		END_IF

		IF CurrentValue + StepSize > MaxValue THEN
			CurrentValue = MaxValue
			AtMax = TRUE
		ELSEIF CurrentValue - StepSize < MinValue THEN
			CurrentValue = MinValue
			AtMin = TRUE
		END_IF

		CurrentValue = CurrentValue + (CountUp AND StepSize) - (NOT CountUp AND StepSize)
	END_IF
END_FUNCTION
```

This function block provides a configurable digital counter with up/down counting modes, overflow protection, and reset capability. The function block can be easily integrated into other control applications and is scan-cycle stable.

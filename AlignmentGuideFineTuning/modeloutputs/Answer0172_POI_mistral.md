### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block for an iterative quicksort algorithm that sorts integer arrays in PLC environments, featuring stack-based emulation, input validation, and state-machine-driven execution for safe, efficient sorting within industrial automation systems.

### Prompt:
**Counter:**
Implement a self-contained function block in IEC 61131-3 structured text for a digital counter with up/down counting modes. Include configurable initial value, step size, and overflow handling.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

Digital counters are essential in industrial automation for tracking events, cycles, or product quantities. However, basic counters often lack flexibility—such as configurable counting direction, custom step sizes, and overflow protection. Without a robust and reusable function block, engineers may struggle to maintain or scale these functions in complex control systems.

⸻

🟩 A (After) – The Desired Outcome

Design and implement a self-contained IEC 61131-3 Structured Text function block that performs as a flexible digital counter, supporting:
	•	Up/down counting modes
	•	A configurable initial value
	•	A customizable step size
	•	Overflow and underflow handling
This function block should be modular, reusable, and safe for use in scan-cycle-driven PLC environments.

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block with inputs:
	•	Enable : BOOL
	•	CountUp : BOOL
	•	StepSize : INT
	•	InitValue : INT
	•	Reset : BOOL
	•	MaxValue : INT
	•	MinValue : INT
	2.	Use internal variables to store the current count and handle direction logic:
	•	Increment or decrement based on CountUp and Enable
	•	Reset counter when Reset = TRUE
	•	Clamp the value between MinValue and MaxValue to prevent overflow/underflow
	3.	Output the result as CurrentValue : INT and status flags like AtMax, AtMin.
	4.	Comment each section to make the block readable and easy to reuse across projects.

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block for an iterative quicksort algorithm that sorts integer arrays in PLC environments, featuring stack-based emulation, input validation, and state-machine-driven execution for safe, efficient sorting within industrial automation systems.
**Counter:**
Implement a self-contained function block in IEC 61131-3 structured text for a digital counter with up/down counting modes. Include configurable initial value, step size, and overflow handling.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

Digital counters are essential in industrial automation for tracking events, cycles, or product quantities. However, basic counters often lack flexibility—such as configurable counting direction, custom step sizes, and overflow protection. Without a robust and reusable function block, engineers may struggle to maintain or scale these functions in complex control systems.

⸻

🟩 A (After) – The Desired Outcome

Design and implement a self-contained IEC 61131-3 Structured Text function block that performs as a flexible digital counter, supporting:
	•	Up/down counting modes
	•	A configurable initial value
	•	A customizable step size
	•	Overflow and underflow handling
This function block should be modular, reusable, and safe for use in scan-cycle-driven PLC environments.

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block with inputs:
	•	Enable : BOOL
	•	CountUp : BOOL
	•	StepSize : INT
	•	InitValue : INT
	•	Reset : BOOL
	•	MaxValue : INT
	•	MinValue : INT
	2.	Use internal variables to store the current count and handle direction logic:
	•	Increment or decrement based on CountUp and Enable
	•	Reset counter when Reset = TRUE
	•	Clamp the value between MinValue and MaxValue to prevent overflow/underflow
	3.	Output the result as CurrentValue : INT and status flags like AtMax, AtMin.
	4.	Comment each section to make the block readable and easy to reuse across projects.

**Code Example:**

```
PROGRAM DigitalCounter;

VAR
	CurrentValue : INT;
	LastValue : INT;
	Direction : BOOL;
	Overflow : BOOL;
	Underflow : BOOL;

FUNCTION_BLOCK DigitalCounterFB
	Input
		Enable : BOOL;
		CountUp : BOOL;
		StepSize : INT;
		InitValue : INT;
		Reset : BOOL;
		MaxValue : INT;
		MinValue : INT;
	Output
		CurrentValue : INT;
		AtMax : BOOL;
		AtMin : BOOL;
	END_FUNCTION_BLOCK

BEGIN
	Direction := CountUp;
	CurrentValue := InitValue;
	LastValue := InitValue;
	Overflow := FALSE;
	Underflow := FALSE;

	IF Reset THEN
		CurrentValue := InitValue;
	END_IF;

	IF Enable THEN
		IF Direction THEN
			IF CurrentValue < MaxValue THEN
				CurrentValue := CurrentValue + StepSize;
			ELSE
				CurrentValue := MaxValue;
				Overflow := TRUE;
			END_IF;
		ELSE
			IF CurrentValue > MinValue THEN
				CurrentValue := CurrentValue - StepSize;
			ELSE
				CurrentValue := MinValue;
				Underflow := TRUE;
			END_IF;
		END_IF;

		IF CurrentValue <> LastValue THEN
			LastValue := CurrentValue;
		END_IF;

		IF CurrentValue = MaxValue THEN
			AtMax := TRUE;
		ELSE
			AtMax := FALSE;
		END_IF;

		IF CurrentValue = MinValue THEN
			AtMin := TRUE;
		ELSE
			AtMin := FALSE;
		END_IF;
	END_IF;
END_PROGRAM
```

**Testing:**

1.	Create a test

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
	5.	Test the function block with various input combinations to ensure correct behavior.

**Example Usage:**

```ST
VAR_INPUT
  Enable : BOOL;
  CountUp : BOOL;
  StepSize : INT;
  InitValue : INT;
  Reset : BOOL;
  MaxValue : INT;
  MinValue : INT;
END_VAR

VAR
  CurrentValue : INT;
  AtMax : BOOL;
  AtMin : BOOL;
BEGIN
  IF Enable THEN
    IF CountUp THEN
      CurrentValue := CurrentValue + StepSize;
    ELSE
      CurrentValue := CurrentValue - StepSize;
    END_IF;
  END_IF;
  
  IF Reset THEN
    CurrentValue := InitValue;
  END_IF;
  
  IF CurrentValue > MaxValue THEN
    CurrentValue := MaxValue;
    AtMax := TRUE;
  ELSE
    AtMax := FALSE;
  END_IF;
  
  IF CurrentValue < MinValue THEN
    CurrentValue := MinValue;
    AtMin := TRUE;
  ELSE
    AtMin := FALSE;
  END_IF;
  
END_VAR
```

**Expected Output:**

The function block should return the current value of the counter and status flags indicating if the counter has reached its maximum or minimum value. The output can be used to trigger actions or display the counter value in a HMI.

**Additional Considerations:**

-	Consider edge cases, such as when the step size is zero or the initial value is outside the valid range.
-	Ensure the function block is efficient and does not cause excessive scan time or memory usage.
-	Document the function block thoroughly, including input and output descriptions, parameter settings, and any potential limitations or caveats.
-	Test the function block under various conditions to ensure its robustness and reliability in real-world scenarios.

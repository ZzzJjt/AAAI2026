### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block for a binary search algorithm that efficiently locates a target value in a sorted 100-element array, with input validation, bounds safety, and real-time PLC compatibility.  

*(Focus: Modularity, performance (O(log n)), and industrial robustness.)*

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
Create a reusable IEC 61131-3 Structured Text function block for a binary search algorithm that efficiently locates a target value in a sorted 100-element array, with input validation, bounds safety, and real-time PLC compatibility.  

*(Focus: Modularity, performance (O(log n)), and industrial robustness.)*
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
	4.	Comment each section to make the block readable and easy to reuse across projects. **IEC 61131-3 Structured Text Function Block for Digital Counter**

```structuredtext
// Function Block: DigitalCounter
// Inputs:
//   Enable: BOOL - Enable/disable counter
//   CountUp: BOOL - Count up or down
//   StepSize: INT - Step size for each increment/decrement
//   InitValue: INT - Initial value of the counter
//   Reset: BOOL - Reset counter to initial value
//   MaxValue: INT - Maximum value before overflow
//   MinValue: INT - Minimum value before underflow
// Outputs:
//   CurrentValue: INT - Current value of the counter
//   AtMax: BOOL - True if counter is at maximum value
//   AtMin: BOOL - True if counter is at minimum value

VAR
  CurrentValue: INT := InitValue; // Initialize counter with initial value
  AtMax: BOOL := FALSE; // Flag for maximum value
  AtMin: BOOL := FALSE; // Flag for minimum value
  Direction: BOOL := CountUp; // Direction of counting (TRUE = up, FALSE = down)
  Step: INT := StepSize; // Step size for each increment/decrement
  Max: INT := MaxValue; // Maximum value before overflow
  Min: INT := MinValue; // Minimum value before underflow
END_VAR

// Main logic
IF Enable THEN
  IF Reset THEN
    CurrentValue := InitValue; // Reset counter to initial value
  ELSE
    IF Direction THEN
      CurrentValue := CurrentValue + Step; // Increment counter
    ELSE
      CurrentValue := CurrentValue - Step; // Decrement counter
    END_IF
  END_IF
END_IF

// Clamp counter value within bounds
IF CurrentValue > Max THEN
  CurrentValue := Max; // Prevent overflow
  AtMax := TRUE; // Set flag for maximum value
ELSE
  AtMax := FALSE; // Clear flag for maximum value
END_IF

IF CurrentValue < Min THEN
  CurrentValue := Min; // Prevent underflow
  AtMin := TRUE; // Set flag for minimum value
ELSE
  AtMin := FALSE; // Clear flag for minimum value
END_IF

// Output current value and status flags
OUTPUT CurrentValue;
OUTPUT AtMax;
OUTPUT AtMin;
```

This function block provides a flexible and reusable solution for implementing a digital counter in IEC 61131-3 Structured

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

	**T-A-G:**

	•	Implement a self-contained function block in IEC 61131-3 Structured Text for a digital counter with configurable counting direction, initial value, and overflow protection.
	•	Provide detailed comments explaining the logic and usage of the function block.
	•	Ensure the function block is scan-cycle-safe and modular for use in industrial automation systems.

	**R-I-S-E:**

	•	Role: Your Role is to develop a PLC function block for a digital counter that supports flexible counting modes, configurable initial values, and safe overflow handling.
	•	Issue: The Challenge is to create a reusable and scan-cycle-safe function block that can be integrated into industrial automation systems without requiring additional context or external logic.
	•	Steps: The Process involves defining the function block inputs, implementing the counting logic with overflow protection, and ensuring scan-cycle safety through structured text programming.
	•	Example: A self-contained function block that allows up/down counting, configurable initial values, and overflow handling, with detailed comments for clarity and reusability.

	**B-A-B:**

	⸻

	**B (Before) – The Problem or Challenge:**

	Implement a self-contained function block in IEC 61131-3 Structured Text for a digital counter that supports up/down counting modes, configurable initial values, and overflow protection. Without a flexible and scan-cycle-safe counter function block, engineers face difficulties in scaling and maintaining automation logic in industrial systems.

	⸻

	**A (After) – The Desired Outcome:**

Develop a self-contained function block that:
	•	Accepts inputs for up/down counting modes, initial value, and overflow limits
	•	Performs counting operations with configurable step sizes
	•	Handles overflow and underflow conditions
	•	Includes detailed comments for clarity and reusability
	•	Ensures scan-cycle safety and modularity for industrial automation systems

	⸻

	**B (Bridge) – How to Get There:**

	1.	Define the function block inputs:
	•	Enable : BOOL — activates the counter
	•	CountUp : BOOL — selects up/down counting direction
	•	StepSize : INT — sets the increment/decrement amount
	•	InitValue : INT — sets the initial value of the counter
	•	Reset : BOOL — resets the counter to the initial value
	•	MaxValue : INT — sets

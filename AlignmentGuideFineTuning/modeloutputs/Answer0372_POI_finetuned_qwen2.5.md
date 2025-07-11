### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block for a configurable digital counter with up/down modes, step size, limits, and overflow/underflow protection.  

*(Focus: Modular, safe, and flexible counting logic for PLCs.)*

### Prompt:
**Counter:**
Implement a self-contained function block in IEC 61131-3 structured text for a digital counter with up/down counting modes. Include configurable initial value, step size, and overflow handling.

**C-A-R-E:**

🟥 C (Context) – Background Situation

Digital counters are commonly used in industrial control systems to track quantities such as parts, pulses, or process cycles. However, many basic implementations lack configurable options like up/down mode, step size control, and overflow protection. In a PLC environment governed by scan cycles, a flexible, reusable counter function block can improve both functionality and system safety.

⸻

🟩 A (Action) – Task to Perform

Implement a self-contained function block in IEC 61131-3 Structured Text that performs as a versatile digital counter, supporting:
	•	Up and down counting modes based on a direction input
	•	A configurable initial value and custom step size
	•	Handling of overflow and underflow conditions using max and min limits
	•	An optional reset function to reinitialize the counter
	•	Clearly defined input/output variables and readable internal logic

⸻

🟨 R (Result) – Expected Outcome

The result should be a modular, reliable function block that can be easily reused across projects requiring counting logic. It should integrate seamlessly into existing PLC programs, provide accurate state tracking, and protect against boundary violations. The implementation should enhance maintainability, safety, and clarity in industrial automation systems.

⸻

🟦 E (Example) – Concrete Illustration

Example functionality:

IF Enable THEN
   IF Reset THEN
      CurrentValue := InitValue;
   ELSIF CountUp THEN
      CurrentValue := CurrentValue + StepSize;
   ELSE
      CurrentValue := CurrentValue - StepSize;
   END_IF;

   // Handle overflow and underflow
   IF CurrentValue >= MaxValue THEN
      CurrentValue := MaxValue;
      AtMax := TRUE;
   ELSIF CurrentValue <= MinValue THEN
      CurrentValue := MinValue;
      AtMin := TRUE;
   END_IF;
END_IF;

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block for a configurable digital counter with up/down modes, step size, limits, and overflow/underflow protection.  

*(Focus: Modular, safe, and flexible counting logic for PLCs.)*
**Counter:**
Implement a self-contained function block in IEC 61131-3 structured text for a digital counter with up/down counting modes. Include configurable initial value, step size, and overflow handling.

**C-A-R-E:**

🟥 C (Context) – Background Situation

Digital counters are commonly used in industrial control systems to track quantities such as parts, pulses, or process cycles. However, many basic implementations lack configurable options like up/down mode, step size control, and overflow protection. In a PLC environment governed by scan cycles, a flexible, reusable counter function block can improve both functionality and system safety.

⸻

🟩 A (Action) – Task to Perform

Implement a self-contained function block in IEC 61131-3 Structured Text that performs as a versatile digital counter, supporting:
	•	Up and down counting modes based on a direction input
	•	A configurable initial value and custom step size
	•	Handling of overflow and underflow conditions using max and min limits
	•	An optional reset function to reinitialize the counter
	•	Clearly defined input/output variables and readable internal logic

⸻

🟨 R (Result) – Expected Outcome

The result should be a modular, reliable function block that can be easily reused across projects requiring counting logic. It should integrate seamlessly into existing PLC programs, provide accurate state tracking, and protect against boundary violations. The implementation should enhance maintainability, safety, and clarity in industrial automation systems.

⸻

🟦 E (Example) – Concrete Illustration

Example functionality:

IF Enable THEN
   IF Reset THEN
      CurrentValue := InitValue;
   ELSIF CountUp THEN
      CurrentValue := CurrentValue + StepSize;
   ELSE
      CurrentValue := CurrentValue - StepSize;
   END_IF;

   // Handle overflow and underflow
   IF CurrentValue >= MaxValue THEN
      CurrentValue := MaxValue;
      AtMax := TRUE;
   ELSIF CurrentValue <= MinValue THEN
      CurrentValue := MinValue;
      AtMin := TRUE;
   END_IF;
END_IF;  

This example shows how to create a self-contained function block that manages both up and down counting modes, with configurable step sizes and limits, while ensuring proper handling of edge cases like overflow and underflow. It also includes a reset capability to clear the counter to its initial value.

⸻

Incorporate this function block into your PLC program to manage quantities such as product counters, sensor pulses, or process cycles with greater flexibility and safety.**Counter:**
Implement a self-contained function block in IEC 61131-3 Structured Text for a digital counter with configurable up/down modes, initial value, and overflow protection.

**C-A-R-E:**

🟥 C (Context) – Background Situation

Digital counters are essential in industrial automation for tracking quantities such as product units, sensor pulses, or process cycles. However, many basic implementations lack configurable options like up/down counting modes, custom step sizes, and overflow protection. In a PLC environment governed by scan cycles, a flexible, reusable counter function block can improve both functionality and system safety.

⸻

🟩 A (Action) – Task to Perform

Create a self-contained function block in IEC 61131-3 Structured Text that performs as a versatile digital counter, supporting:
	•	Up and down counting modes based on a direction input
	•	A configurable initial value and custom step size
	•	Handling of overflow and underflow conditions using configurable limits
	•	An optional reset function to reinitialize the counter
	•	Clearly defined input/output variables and readable internal logic

⸻

🟨 R (Result) – Expected Outcome

The result should be a modular, reliable function block that can be easily reused across projects requiring counting logic. It should integrate seamlessly into existing PLC programs, provide accurate state tracking, and protect against boundary violations. The implementation should enhance maintainability, safety, and clarity in industrial automation systems.

⸻

🟦 E (Example) – Concrete Illustration

Implement the following function block in IEC 61131-3 Structured Text:

	// Function Block: COUNTER
	// Inputs:
	//	Enable		: BOOL		//	Enable counter operation
	//	Reset		: BOOL		//	Reset counter to initial value
	//	CountUp		: BOOL		//	Count up or down
	//	StepSize	: INT		//	Step size for each increment/decrement

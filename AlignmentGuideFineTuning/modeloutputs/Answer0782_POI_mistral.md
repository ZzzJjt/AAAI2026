### Intent:
"Create a reusable IEC 61131-3 structured text function block for a configurable digital counter with up/down modes, initial value/step settings, limit protection, and status outputs for PLC automation systems."

### Prompt:
**Counter:**
Implement a self-contained function block in IEC 61131-3 structured text for a digital counter with up/down counting modes. Include configurable initial value, step size, and overflow handling.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC developer creating a flexible, reusable digital counter function block in IEC 61131-3 Structured Text for automation applications.

⸻

🟩 T (Task) – Define the Objective

Implement a self-contained counter function block that supports both up and down counting modes with the following features:
	•	A configurable initial value and step size
	•	Inputs for count direction, enable, and reset
	•	Protection against overflow and underflow, using configurable MaxValue and MinValue limits
	•	Output of the current count value and status flags indicating if limits are reached

The counter should operate reliably in scan-cycle-driven environments and support integration into larger automation programs.

⸻

🟧 F (Format) – Specify the Output Format

Provide:
	•	A complete IEC 61131-3 Structured Text function block
	•	Declarations for all inputs, outputs, and internal variables
	•	Logic using IF/ELSIF structures to increment/decrement the counter
	•	Overflow and underflow handling using comparison conditions
	•	A Reset condition to reinitialize the counter
	•	Inline comments explaining the purpose of each block of code

### Generated Code:
"Create a reusable IEC 61131-3 structured text function block for a configurable digital counter with up/down modes, initial value/step settings, limit protection, and status outputs for PLC automation systems."
**Counter:**
Implement a self-contained function block in IEC 61131-3 structured text for a digital counter with up/down counting modes. Include configurable initial value, step size, and overflow handling.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a PLC developer creating a flexible, reusable digital counter function block in IEC 61131-3 Structured Text for automation applications.

⸻

🟩 T (Task) – Define the Objective

Implement a self-contained counter function block that supports both up and down counting modes with the following features:
	•	A configurable initial value and step size
	•	Inputs for count direction, enable, and reset
	•	Protection against overflow and underflow, using configurable MaxValue and MinValue limits
	•	Output of the current count value and status flags indicating if limits are reached

The counter should operate reliably in scan-cycle-driven environments and support integration into larger automation programs.

⸻

🟧 F (Format) – Specify the Output Format

Provide:
	•	A complete IEC 61131-3 Structured Text function block
	•	Declarations for all inputs, outputs, and internal variables
	•	Logic using IF/ELSIF structures to increment/decrement the counter
	•	Overflow and underflow handling using comparison conditions
	•	A Reset condition to reinitialize the counter
	•	Inline comments explaining the purpose of each block of code

⸻

🟦 E (Example) – Provide an Example Implementation

```
PROGRAM DigitalCounter;

VAR_INPUT
	i_Direction : BOOL;		// Count direction (Up: True, Down: False)
	i_Enable : BOOL;		// Enable counting (True) or stop (False)
	i_Reset : BOOL;		// Reset counter (True) or maintain current value (False)
	i_InitialValue : DINT;	// Initial counter value
	i_StepSize : DINT;		// Step size for counting
	i_MaxValue : DINT;		// Maximum counter value
	i_MinValue : DINT;		// Minimum counter value
END_VAR

VAR_OUTPUT
	o_Count : DINT;		// Current counter value
	o_Overflow : BOOL;		// Overflow status flag
	o_Underflow : BOOL;		// Underflow status flag
END_VAR

VAR
	v_Counter : DINT;		// Internal counter variable
END_VAR

IF i_Enable THEN
	IF i_Reset THEN
		v_Counter := i_InitialValue;
	END_IF

	IF i_Direction THEN
		IF v_Counter < i_MaxValue THEN
			v_Counter := v_Counter + i_StepSize;
		ELSIF v_Counter >= i_MaxValue THEN
			v_Counter := i_MinValue;
			o_Overflow := TRUE;
		END_IF
	ELSE
		IF v_Counter > i_MinValue THEN
			v_Counter := v_Counter - i_StepSize;
		ELSIF v_Counter <= i_MinValue THEN
			v_Counter := i_MaxValue;
			o_Underflow := TRUE;
		END_IF
	END_IF

	o_Count := v_Counter;
END_IF

END_PROGRAM
```

This example provides a basic implementation of the digital counter function block with the specified features. The user can adjust the input parameters to
